"""AoT —— LLM 零样本思维打分器（DeepSeek，OpenAI 兼容接口）。

复用 SPI 已验证协议（<SPI_ROOT>/src/spi_quant/scorer_llm.py）：
- 单构念独立调用，避免跨构念污染与顺序效应；
- 结构化输出 JSON {score: 1-7, evidence: [...], confidence: 0-1}；
- 双轮平均：temperature 0.3 / 0.7 两轮取均值，压低评分抖动；
- 每轮打乱构念顺序；
- 断点续跑：已完成的 (person, chunk, construct) 跳过；
- 无 API key 时进入模拟模式（确定性启发式，结果带 simulated 标记）。

用法：
    python3 scripts/score_thinking.py                 # 全量 49 块 × 12 构念 × 双轮
    python3 scripts/score_thinking.py --pilot 2 12    # 试点：第 1 人前 2 块 × 12 构念
"""
from __future__ import annotations

import json
import os
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional

import yaml

AOT_ROOT = Path(__file__).resolve().parent.parent
CONSTRUCTS_PATH = AOT_ROOT / "config" / "thinking_constructs.yaml"
LLM_PATH = AOT_ROOT / "config" / "llm.yaml"
CORPUS_DIR = AOT_ROOT / "data" / "corpus"
OUT_DIR = AOT_ROOT / "data" / "results" / "scores"
ENV_PATH = AOT_ROOT / ".env"

MAX_TEXT_CHARS = 6000  # 控制单次输入 token，超长截断

SYSTEM_PROMPT = """你是一位严谨的思维测量编码器（thinking-pattern encoder）。

你会收到两部分输入：
1. 【思维构念定义】——某思维构念的五层编码：定义设问、特质形容词、同义词、行为动词、相关名词/情境、正反锚句；
2. 【待分析文本】——一段自然语言文本。

你的任务：仅根据这段文本的实际内容，判断【文本作者】在多大程度上表现出该思维构念的思维模式，
并输出严格 JSON（不要输出任何其他文字或解释）：
{"score": 1到7的整数, "evidence": ["原文片段1", ...最多3条], "confidence": 0到1之间的小数}

评分标尺：
- 7 = 文本强烈且一致地体现该思维构念（存在多处明确证据）
- 5~6 = 明显体现
- 3~4 = 部分或含糊体现
- 1~2 = 几乎不体现，或体现的是相反特征（构念若定义了两极，按定义文本中写明的方向打分）

规则：
- 评分必须基于文本本身，不得臆测作者未表达的信息；
- evidence 必须逐字引用原文片段（保留原文语言，不做改写）；
- confidence 表示你对评分的把握程度（0=完全没把握，1=非常有把握）。"""


def render_definition(c: dict) -> str:
    lines = [
        f"构念名称：{c['name']}（{c.get('en', '')}）",
        f"所属维度：{c.get('dimension', '')}",
        f"设问：{c.get('question', '')}",
        f"核心词：{c.get('factor', '')}",
        f"特质形容词：{'、'.join(c.get('adjectives', []))}",
        f"同义词：{'、'.join(c.get('synonyms', []))}",
        f"行为动词：{'、'.join(c.get('verbs', []))}",
        f"相关名词/情境：{'、'.join(c.get('nouns', []))}",
    ]
    anchors = c.get('anchors', {})
    for side, label in (('positive', '正面锚句（典型体现）'), ('negative', '反面锚句（相反体现）')):
        v = anchors.get(side)
        if isinstance(v, str):
            lines.append(f"{label}：{v}")
        elif isinstance(v, list) and v:
            lines.append(f"{label}：{'；'.join(v)}")
    return "\n".join(lines)


def load_key() -> Optional[str]:
    k = os.environ.get("DEEPSEEK_API_KEY")
    if k:
        return k
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


class ThinkingScorer:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or load_key()
        self.simulated = not self.api_key
        self.client = None
        if not self.simulated:
            try:
                from openai import OpenAI
            except ImportError:
                print("[warn] openai 未安装，尝试 pip install openai ...")
                os.system(f"{os.sys.executable} -m pip install -q openai")
                from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com", timeout=120)

    def _call_once(self, definition: str, name: str, text: str, temperature: float) -> dict:
        user = (
            f"【思维构念定义】\n{definition}\n\n"
            f"【待分析文本】\n{text}\n\n请按系统要求输出 JSON。"
        )
        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            temperature=temperature,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
        )
        content = resp.choices[0].message.content or ""
        return json.loads(content)

    def _simulate(self, name: str, definition: str, text: str) -> dict:
        tokens = set(re.findall(r"[\u4e00-\u9fff]{2,}", text))
        hits = 0
        total = 0
        for w in re.findall(r"[\u4e00-\u9fff]{2,}", definition):
            total += 1
            if w in tokens:
                hits += 1
        score = 1 if total == 0 else max(1, min(7, round(hits / max(total, 1) * 50)))
        return {
            "score": score,
            "evidence": [text[:60] + ("…" if len(text) > 60 else "")],
            "confidence": 0.1,
            "simulated": True,
        }

    def score_once(self, definition: str, name: str, text: str) -> dict:
        """双轮评分（0.3/0.7 各一次，取平均），返回结构化结果。"""
        raw_scores: List[int] = []
        evidence: List[str] = []
        confidences: List[float] = []
        simulated = False
        for t in (0.3, 0.7):
            for attempt in range(2):
                try:
                    data = self._call_once(definition, name, text, t) if not self.simulated else self._simulate(name, definition, text)
                    simulated = simulated or self.simulated or data.get("simulated", False)
                    score = int(data["score"])
                    if 1 <= score <= 7:
                        raw_scores.append(score)
                        ev = data.get("evidence", [])
                        for e in ev:
                            e = str(e).strip()
                            if e and e not in evidence and len(evidence) < 3:
                                evidence.append(e)
                        confidences.append(float(data.get("confidence", 0.5)))
                        break
                except Exception as ex:
                    if attempt == 1:
                        print(f"    [warn] {name} t={t} 失败: {ex}")
                    time.sleep(1.5)
        if not raw_scores:
            return {"score": 0.0, "raw_scores": [], "evidence": [], "confidence": 0.0, "simulated": True}
        return {
            "score": round(sum(raw_scores) / len(raw_scores), 2),
            "raw_scores": raw_scores,
            "evidence": evidence,
            "confidence": round(sum(confidences) / len(confidences), 2) if confidences else 0.0,
            "simulated": simulated,
        }


def load_corpus() -> List[dict]:
    people = []
    for p in sorted(CORPUS_DIR.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        people.append({"pid": d["person"], "name": d.get("name", d["person"]), "items": d["items"]})
    return people


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", nargs="*", default=None,
                    help="试点模式：'人数 块数'，如 --pilot 1 2（第 1 人前 2 块）")
    ap.add_argument("--constructs", type=int, default=None, help="只用前 N 个构念")
    args = ap.parse_args()

    constructs = yaml.safe_load(CONSTRUCTS_PATH.read_text(encoding="utf-8"))["constructs"]
    if args.constructs:
        constructs = constructs[: args.constructs]
    llm_cfg = yaml.safe_load(LLM_PATH.read_text(encoding="utf-8"))["llm"]

    scorer = ThinkingScorer()
    if scorer.simulated:
        print("[!] 未找到 DEEPSEEK_API_KEY，进入模拟模式（结果带 simulated 标记）")

    people = load_corpus()
    if args.pilot is not None:
        vals = args.pilot if args.pilot else ["1", "2"]
        n_p, n_c = int(vals[0]), int(vals[1])
        people = [dict(p, items=p["items"][:n_c]) for p in people[:n_p]]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_calls = sum(len(p["items"]) * len(constructs) * 2 for p in people)
    done_calls = 0

    def build_tasks():
        for p in people:
            out_path = OUT_DIR / f"{p['pid']}.json"
            existing = {}
            if out_path.exists():
                existing = json.loads(out_path.read_text(encoding="utf-8"))
            for item in p["items"]:
                text = item["text"][:MAX_TEXT_CHARS]
                cid = item["id"]
                for c in constructs:
                    key = f"{cid}::{c['id']}"
                    if key in existing and existing[key].get("score", 0) > 0 and not existing[key].get("simulated", False):
                        continue  # 断点续跑
                    yield p, out_path, existing, key, c, text

    tasks = list(build_tasks())
    print(f"[info] 任务总量：{len(people)} 人 × {len(constructs)} 构念 × 双轮，预计 {len(tasks)*2} 次调用（含续跑跳过）")

    def run_task(t):
        p, out_path, existing, key, c, text = t
        definition = render_definition(c)
        res = scorer.score_once(definition, c["name"], text)
        res["construct"] = c["id"]
        res["construct_name"] = c["name"]
        res["person"] = p["pid"]
        res["chunk"] = key.split("::")[0]
        return p, out_path, existing, key, res

    with ThreadPoolExecutor(max_workers=llm_cfg.get("concurrency", 12)) as ex:
        futs = {ex.submit(run_task, t): t for t in tasks}
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                p, out_path, existing, key, res = fut.result()
                existing[key] = res
                out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
                done_calls += 2
                if done_calls % 20 == 0 or done_calls == len(tasks) * 2:
                    print(f"  [prog] {done_calls}/{len(tasks)*2} 次调用完成", flush=True)
            except Exception as ex:
                print(f"  [err] {t[3]} 失败: {ex}")

    print(f"[ok] 打分完成，结果在 {OUT_DIR}")


if __name__ == "__main__":
    main()
