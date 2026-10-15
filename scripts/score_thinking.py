"""AoT —— LLM 零样本思维打分器（DeepSeek，OpenAI 兼容接口）。

复用 SPI 已验证协议（<SPI_ROOT>/src/spi_quant/scorer_llm.py）：
- 单构念独立调用，避免跨构念污染与顺序效应；
- 结构化输出 JSON {score: 1-7, evidence: [...], confidence: 0-1}；
- 双轮平均：temperature 0.3 / 0.7 两轮取均值，压低评分抖动；
- 每轮打乱构念顺序；
- 断点续跑：已完成的 (person, chunk, construct) 跳过；
- 无 API key 直接报错退出 1（模拟模式已移除）；429/5xx/截断指数退避（llm_common）；温度/模型来自 config/llm.yaml。

用法：
    python3 scripts/score_thinking.py                 # 全量 49 块 × 12 构念 × 双轮
    python3 scripts/score_thinking.py --pilot 2 12    # 试点：第 1 人前 2 块 × 12 构念
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import List

import yaml

import llm_common

AOT_ROOT = Path(__file__).resolve().parent.parent
CONSTRUCTS_PATH = AOT_ROOT / "config" / "thinking_constructs.yaml"
LLM_PATH = AOT_ROOT / "config" / "llm.yaml"
CORPUS_DIR = AOT_ROOT / "data" / "corpus"
OUT_DIR = AOT_ROOT / "data" / "results" / "scores"


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


class ThinkingScorer:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.client = llm_common.make_client(llm_common.require_key(AOT_ROOT), cfg)  # 无 key → 退出 1

    def score_once(self, definition: str, name: str, text: str) -> dict:
        """多温度（config temperatures，默认 0.3/0.7）各一次取均值。"""
        text, truncated = llm_common.truncate(text, self.cfg)
        user = f"【思维构念定义】\n{definition}\n\n【待分析文本】\n{text}\n\n请按系统要求输出 JSON。"
        return llm_common.score_1to7(
            self.client, self.cfg,
            [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}],
            label=name, truncated=truncated)


def load_corpus(corpus_dir: Path = CORPUS_DIR) -> List[dict]:
    if not corpus_dir.is_dir() or not any(corpus_dir.glob("*.json")):
        sys.exit(f"错误：语料目录 {corpus_dir} 不存在或没有 *.json；先用 scripts/prepare_corpus.py 生成")
    people = []
    for p in sorted(corpus_dir.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        people.append({"pid": d["person"], "name": d.get("name", d["person"]), "items": d["items"]})
    return people


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", nargs="*", default=None,
                    help="试点模式：'人数 块数'，如 --pilot 1 2（第 1 人前 2 块）")
    ap.add_argument("--constructs", type=int, default=None, help="只用前 N 个构念")
    ap.add_argument("--corpus-dir", default=str(CORPUS_DIR), help="语料目录（默认 data/corpus）")
    ap.add_argument("--out-dir", default=str(OUT_DIR), help="输出目录")
    ap.add_argument("--dry-run", action="store_true", help="只打印调用次数，不调用 LLM")
    args = ap.parse_args()

    constructs = yaml.safe_load(CONSTRUCTS_PATH.read_text(encoding="utf-8"))["constructs"]
    if args.constructs:
        constructs = constructs[: args.constructs]
    llm_cfg = llm_common.load_llm_cfg(LLM_PATH, section="llm")
    out_dir = Path(args.out_dir)
    people = load_corpus(Path(args.corpus_dir))
    if args.pilot is not None:
        vals = args.pilot if args.pilot else ["1", "2"]
        n_p, n_c = int(vals[0]), int(vals[1])
        people = [dict(p, items=p["items"][:n_c]) for p in people[:n_p]]

    done_calls, n_failed = 0, 0

    def build_tasks():
        for p in people:
            out_path = out_dir / f"{p['pid']}.json"
            existing = {}
            if out_path.exists():
                existing = json.loads(out_path.read_text(encoding="utf-8"))
            for item in p["items"]:
                text = item["text"]
                if not text.strip():
                    continue
                cid = item["id"]
                for c in constructs:
                    key = f"{cid}::{c['id']}"
                    e = existing.get(key) or {}
                    if (e.get("score") or 0) > 0 and not e.get("simulated") and not e.get("failed"):
                        continue  # 断点续跑
                    yield p, out_path, existing, key, c, text

    tasks = list(build_tasks())
    print(f"[info] 任务总量：{len(people)} 人 × {len(constructs)} 构念 × {len(llm_cfg['temperatures'])} 轮，预计 {len(tasks)*len(llm_cfg['temperatures'])} 次调用（已跳过续跑项）")
    if args.dry_run:
        return
    scorer = ThinkingScorer(llm_cfg)
    out_dir.mkdir(parents=True, exist_ok=True)

    def run_task(t):
        p, out_path, existing, key, c, text = t
        definition = render_definition(c)
        res = scorer.score_once(definition, c["name"], text)
        res["construct"] = c["id"]
        res["construct_name"] = c["name"]
        res["person"] = p["pid"]
        res["chunk"] = key.split("::")[0]
        return p, out_path, existing, key, res

    with ThreadPoolExecutor(max_workers=int(llm_cfg.get("concurrency", 8))) as ex:
        futs = {ex.submit(run_task, t): t for t in tasks}
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                p, out_path, existing, key, res = fut.result()
                existing[key] = res
                out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
                done_calls += 1
                n_failed += bool(res.get("failed"))
                if done_calls % 20 == 0 or done_calls == len(tasks):
                    print(f"  [prog] {done_calls}/{len(tasks)} 项完成（失败 {n_failed}）", flush=True)
            except Exception as e:  # noqa: BLE001
                n_failed += 1
                print(f"  [err] {t[3]} 失败: {e}", file=sys.stderr)

    print(f"[ok] 打分完成，结果在 {out_dir}（失败 {n_failed}）")
    if n_failed:
        sys.exit(3)


if __name__ == "__main__":
    main()
