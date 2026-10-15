"""AoT —— 维度级 LLM 打分（SPI 同构第 4 阶段：LLM 判定）。

与 score_thinking.py（12 种子构念）不同：本脚本用【数据聚出的思维维度】
（k25_named.json 的 dimension 字段 + AoT 尺子 v1.0 锚点）对文本打分。

用法：
    python3 scripts/score_dimensions.py --v2 --pilot 1 2   # 试点：第 1 人前 2 块
    python3 scripts/score_dimensions.py --v2                # 抽样 49 块 × 25 维 × 双轮
    python3 scripts/score_dimensions.py --v2 --full         # 全量语料 × 25 维 × 双轮（冻结尺子）
"""
from __future__ import annotations

import argparse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
NAMED_PATH = AOT_ROOT / "data" / "results" / "clusters" / "k18_named.json"
CORPUS_DIR = AOT_ROOT / "data" / "corpus"
OUT_DIR = AOT_ROOT / "data" / "results" / "scores_dim"
RULER_PATH = AOT_ROOT / "data" / "results" / "ruler" / "AoT尺子_v1.0.json"
ENV_PATH = AOT_ROOT / ".env"

MAX_TEXT_CHARS = 6000

SYSTEM_PROMPT = """你是一位严谨的思维测量编码器（thinking-pattern encoder）。

你会收到：
1. 【思维维度定义】——某思维维度的名称、判定设问、本质概括、判定锚点词，以及组成它的学术构念名；
2. 【待分析文本】——一段自然语言文本。

任务：仅根据文本实际内容，判断【文本作者】在多大程度上表现出该思维维度，输出严格 JSON（无其他文字）：
{"score": 1到7的整数, "evidence": ["原文片段", ...最多3条], "confidence": 0到1之间的小数}

标尺：7=强烈且一致体现；5~6=明显体现；3~4=部分或含糊；1~2=几乎不体现或相反（维度定义写了两极时，按定义方向打分）。
规则：评分基于文本本身；evidence 逐字引用原文；confidence 表示把握程度。"""


def load_key() -> str | None:
    # 优先读环境变量（开源推荐方式，同事用自己的 key）
    env_key = os.environ.get("DEEPSEEK_API_KEY")
    if env_key:
        return env_key.strip()
    # 回退到本地 .env 文件
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def render_dimension(cl, anchors: dict | None = None) -> str:
    dim = cl["dimension"]
    members = [m["name"] for m in cl["members"]]
    lines = [
        f"维度名称：{dim.get('name', '')}（{dim.get('name_en', '')}）",
        f"判定设问：{dim.get('question', '')}",
        f"本质：{dim.get('essence', '')}",
        f"判定锚点词：{'、'.join(dim.get('keywords', []))}",
        f"组成构念：{'、'.join(members[:8])}{'…' if len(members) > 8 else ''}",
    ]
    if anchors:
        lines.append(
            "维度特化评分锚点："
            f"低分(1-2)：{anchors.get('anchor_low', '')}；"
            f"中分(3-5)：{anchors.get('anchor_mid', '')}；"
            f"高分(6-7)：{anchors.get('anchor_high', '')}；"
            f"对立极说明：{anchors.get('polar_note', '')}"
        )
    return "\n".join(lines)


class DimScorer:
    def __init__(self, key: str | None):
        if not key:
            print("错误：未检测到 DEEPSEEK_API_KEY。\n"
                  "请先 export DEEPSEEK_API_KEY=sk-... 或在 .env 文件中配置。",
                  file=sys.stderr)
            sys.exit(1)
        self.key = key
        self.simulated = False
        from openai import OpenAI
        self.client = OpenAI(api_key=key, base_url="https://api.deepseek.com", timeout=120)

    def _call(self, definition: str, name: str, text: str, temp: float) -> dict:
        user = f"【思维维度定义】\n{definition}\n\n【待分析文本】\n{text}\n\n请按系统要求输出 JSON。"
        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            temperature=temp,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
        )
        return json.loads(resp.choices[0].message.content or "{}")

    def score(self, definition: str, name: str, text: str) -> dict:
        scores, confs, evs, simulated = [], [], [], False
        for temp in (0.3, 0.7):
            for attempt in range(2):
                try:
                    data = self._call(definition, name, text, temp)
                    simulated = simulated or data.get("simulated", False)
                    s = int(data["score"])
                    if 1 <= s <= 7:
                        scores.append(s)
                        confs.append(float(data.get("confidence", 0.5)))
                        for e in data.get("evidence", []):
                            e = str(e).strip()
                            if e and e not in evs and len(evs) < 3:
                                evs.append(e)
                        break
                except Exception as ex:
                    if attempt == 1:
                        print(f"    [warn] {name} t={temp} 失败: {ex}")
                    time.sleep(1.5)
        if not scores:
            return {"score": 0.0, "raw_scores": [], "evidence": [], "confidence": 0.0, "simulated": True}
        return {
            "score": round(sum(scores) / len(scores), 2),
            "raw_scores": scores,
            "evidence": evs,
            "confidence": round(sum(confs) / len(confs), 2) if confs else 0.0,
            "simulated": simulated,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", nargs="*", default=None, help="试点：'人数 块数'，如 --pilot 1 2")
    ap.add_argument("--v2", action="store_true", help="使用 v2 全量聚类命名结果（clusters_v2/k25_named.json），输出到 scores_dim_v2")
    ap.add_argument("--full", action="store_true", help="使用全量语料（data/corpus_full/），输出到 scores_full")
    ap.add_argument("--no-ruler", action="store_true", help="不注入 AoT 尺子 v1.0 锚点（默认注入）")
    ap.add_argument("--workers", type=int, default=12, help="并发数（默认 12）")
    ap.add_argument("--max-runtime", type=int, default=0, help="主动限时退出（秒）；到点停止接收新任务并保存退出，便于断点续跑 + 守护重启")
    args = ap.parse_args()

    named_path = NAMED_PATH
    out_dir = OUT_DIR
    corpus_dir = CORPUS_DIR
    if args.v2:
        named_path = AOT_ROOT / "data" / "results" / "clusters_v2" / "k25_named.json"
        out_dir = AOT_ROOT / "data" / "results" / "scores_dim_v2"
    if args.full:
        corpus_dir = AOT_ROOT / "data" / "corpus_full"
        out_dir = AOT_ROOT / "data" / "results" / "scores_full"
    named = json.loads(named_path.read_text(encoding="utf-8"))
    clusters = named["clusters"]
    print(f"[dims] 载入 {len(clusters)} 个数据聚出的思维维度")

    # 冻结尺子锚点（默认注入）
    anchors_by_cluster = {}
    if not args.no_ruler and RULER_PATH.exists():
        ruler = json.loads(RULER_PATH.read_text(encoding="utf-8"))
        anchors_by_cluster = {c["cluster"]: c.get("anchors") or {} for c in ruler["dimensions"]}
        print(f"[ruler] 注入 AoT 尺子 v1.0 锚点 {len(anchors_by_cluster)} 个维度")

    people = []
    for p in sorted(corpus_dir.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        people.append({"pid": d["person"], "items": d["items"]})
    if args.pilot is not None:
        vals = args.pilot if args.pilot else ["1", "2"]
        n_p, n_c = int(vals[0]), int(vals[1])
        people = [dict(p, items=p["items"][:n_c]) for p in people[:n_p]]

    key = load_key()
    scorer = DimScorer(key)
    if scorer.simulated:
        print("[!] 无 API key，进入模拟模式")

    out_dir.mkdir(parents=True, exist_ok=True)
    tasks = []
    for p in people:
        out_path = out_dir / f"{p['pid']}.json"
        existing = {}
        if out_path.exists():
            existing = json.loads(out_path.read_text(encoding="utf-8"))
        for item in p["items"]:
            text = item["text"][:MAX_TEXT_CHARS]
            for cl in clusters:
                key_t = f"{item['id']}::dim{cl['cluster']}"
                if key_t in existing and existing[key_t].get("score", 0) > 0 and not existing[key_t].get("simulated", False):
                    continue
                tasks.append((p, out_path, existing, key_t, cl, text))

    print(f"[info] 待打分任务 {len(tasks)} 条 × 双轮 = {len(tasks)*2} 次调用")
    done = 0
    t0 = time.time()

    def run(t):
        p, out_path, existing, key_t, cl, text = t
        definition = render_dimension(cl, anchors_by_cluster.get(cl["cluster"]))
        res = scorer.score(definition, cl["dimension"]["name"], text)
        res["dim"] = cl["cluster"]
        res["dim_name"] = cl["dimension"]["name"]
        res["person"] = p["pid"]
        res["chunk"] = key_t.split("::")[0]
        return p, out_path, existing, key_t, res

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run, t): t for t in tasks}
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                p, out_path, existing, key_t, res = fut.result()
                existing[key_t] = res
                out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
                done += 2
                if done % 40 == 0 or done == len(tasks) * 2:
                    print(f"  [prog] {done}/{len(tasks)*2}", flush=True)
            except Exception as ex:
                print(f"  [err] {t[3]} 失败: {ex}")
            if args.max_runtime and time.time() - t0 > args.max_runtime:
                print(f"  [timeout] 已运行 {int(time.time()-t0)}s，主动退出（已完成条目已落盘，重启断点续跑）", flush=True)
                ex.shutdown(wait=False, cancel_futures=True)
                break

    print(f"[ok] 维度打分（本批）完成，结果在 {out_dir}")


if __name__ == "__main__":
    main()
