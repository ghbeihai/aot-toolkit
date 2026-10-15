"""AoT —— 维度级 LLM 打分（SPI 同构第 4 阶段：LLM 判定）。

与 score_thinking.py（12 种子构念）不同：本脚本用【数据聚出的 25 个思维维度】+ AoT 尺子 v1.0 锚点对文本打分。

维度定义来源（按顺序取第一个存在的）：
  --named 指定文件 → data/results/clusters_v2/k25_named.json（本地聚类产物，gitignore）
  → data/results/ruler/AoT尺子_v1.0.json（仓库内冻结尺子，含同样 25 维定义，开箱即用）
v1 的 k18_named.json 已废弃；--v2 保留为兼容参数（现在默认就是 v2）。

语料：--corpus-dir（默认 data/corpus/，每人一个 {person, name, items:[{id,title,text}]} JSON，
     可用 scripts/prepare_corpus.py 从 txt 目录生成）；--full 等价于 --corpus-dir data/corpus_full --out-dir scores_full。

用法：
    python3 scripts/prepare_corpus.py ./原文 --person zhanglinjun --name 张林军   # → data/corpus/zhanglinjun.json
    python3 scripts/score_dimensions.py --dry-run                 # 只估算调用次数
    python3 scripts/score_dimensions.py --pilot 1 2               # 试点：第 1 人前 2 块
    python3 scripts/score_dimensions.py --person zhanglinjun      # 只评一个人
    python3 scripts/aggregate_profiles.py data/results/scores_dim_v2 --names zhanglinjun=张林军 --out people_profiles.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import llm_common

AOT_ROOT = Path(__file__).resolve().parent.parent
NAMED_V2 = AOT_ROOT / "data" / "results" / "clusters_v2" / "k25_named.json"
CORPUS_DIR = AOT_ROOT / "data" / "corpus"
OUT_DIR = AOT_ROOT / "data" / "results" / "scores_dim_v2"
RULER_PATH = AOT_ROOT / "data" / "results" / "ruler" / "AoT尺子_v1.0.json"
LLM_PATH = AOT_ROOT / "config" / "llm.yaml"

SYSTEM_PROMPT = """你是一位严谨的思维测量编码器（thinking-pattern encoder）。

你会收到：
1. 【思维维度定义】——某思维维度的名称、判定设问、本质概括、判定锚点词，以及组成它的学术构念名；
2. 【待分析文本】——一段自然语言文本。

任务：仅根据文本实际内容，判断【文本作者】在多大程度上表现出该思维维度，输出严格 JSON（无其他文字）：
{"score": 1到7的整数, "evidence": ["原文片段", ...最多3条], "confidence": 0到1之间的小数}

标尺：7=强烈且一致体现；5~6=明显体现；3~4=部分或含糊；1~2=几乎不体现或相反（维度定义写了两极时，按定义方向打分）。
规则：评分基于文本本身；evidence 逐字引用原文；confidence 表示把握程度。"""


def render_dimension(cl, anchors: dict | None = None) -> str:
    dim = cl["dimension"]
    members = [m["name"] if isinstance(m, dict) else str(m) for m in cl.get("members", [])]
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
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.client = llm_common.make_client(llm_common.require_key(AOT_ROOT), cfg)  # 无 key → 退出 1
        self.temperatures = list(cfg.get("temperatures") or [0.3, 0.7])

    def score(self, definition: str, name: str, text: str) -> dict:
        text, truncated = llm_common.truncate(text, self.cfg)
        user = f"【思维维度定义】\n{definition}\n\n【待分析文本】\n{text}\n\n请按系统要求输出 JSON。"
        msgs = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}]
        scores, confs, evs = [], [], []
        for temp in self.temperatures:
            try:  # 429/5xx/截断/JSON 失败在 chat_json 内指数退避重试
                data = llm_common.chat_json(self.client, self.cfg, msgs, temperature=temp,
                                            log_prefix=f"{name} t={temp} ")
                s = int(data["score"])
                if not 1 <= s <= 7:
                    raise ValueError(f"score 越界: {s}")
            except Exception as ex:  # noqa: BLE001
                print(f"    [warn] {name} t={temp} 失败: {ex}", file=sys.stderr)
                continue
            scores.append(s)
            confs.append(float(data.get("confidence", 0.5)))
            for e in data.get("evidence", []) or []:
                e = str(e).strip()
                if e and e not in evs and len(evs) < 3:
                    evs.append(e)
        if not scores:
            return {"score": None, "raw_scores": [], "evidence": [], "confidence": 0.0,
                    "simulated": False, "failed": True, "truncated": truncated}  # 不伪装成 0 分
        return {
            "score": round(sum(scores) / len(scores), 2),
            "raw_scores": scores,
            "evidence": evs,
            "confidence": round(sum(confs) / len(confs), 2),
            "simulated": False,
            "truncated": truncated,
            "model": self.cfg.get("model"),
        }


def load_dimensions(named_arg: str | None):
    for p in ([Path(named_arg)] if named_arg else [NAMED_V2, RULER_PATH]):
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            clusters = d.get("clusters") or d.get("dimensions") or []
            clusters = [c for c in clusters if c.get("dimension")]
            if clusters:
                return clusters, p
    sys.exit(f"错误：找不到维度定义（试过 {named_arg or NAMED_V2}、{RULER_PATH}）")


def main():
    ap = argparse.ArgumentParser(description="AoT 25 维思维维度 LLM 打分（需 DEEPSEEK_API_KEY）")
    ap.add_argument("--pilot", nargs="*", default=None, help="试点：'人数 块数'，如 --pilot 1 2")
    ap.add_argument("--v2", action="store_true", help="兼容参数：现在默认即 v2 25 维（k18 v1 已废弃）")
    ap.add_argument("--named", help="维度定义 JSON（默认 clusters_v2/k25_named.json，缺失时用冻结尺子）")
    ap.add_argument("--corpus-dir", help=f"语料目录（默认 {CORPUS_DIR}）")
    ap.add_argument("--out-dir", help=f"输出目录（默认 {OUT_DIR}）")
    ap.add_argument("--full", action="store_true",
                    help="等价于 --corpus-dir data/corpus_full --out-dir data/results/scores_full（需先准备全量语料）")
    ap.add_argument("--person", action="append", help="只评这些 pid（可多次）")
    ap.add_argument("--no-ruler", action="store_true", help="不注入 AoT 尺子 v1.0 锚点（默认注入）")
    ap.add_argument("--workers", type=int, default=None, help="并发数（默认 config/llm.yaml concurrency）")
    ap.add_argument("--dry-run", action="store_true", help="只打印任务数与调用次数，不调用 LLM")
    ap.add_argument("--max-runtime", type=int, default=0, help="主动限时退出（秒）；到点停止接收新任务并保存退出，便于断点续跑 + 守护重启")
    args = ap.parse_args()

    cfg = llm_common.load_llm_cfg(LLM_PATH, section="llm")
    out_dir = Path(args.out_dir) if args.out_dir else (
        AOT_ROOT / "data" / "results" / "scores_full" if args.full else OUT_DIR)
    corpus_dir = Path(args.corpus_dir) if args.corpus_dir else (
        AOT_ROOT / "data" / "corpus_full" if args.full else CORPUS_DIR)
    if not corpus_dir.is_dir() or not any(corpus_dir.glob("*.json")):
        sys.exit(f"错误：语料目录 {corpus_dir} 不存在或没有 *.json。\n"
                 f"  用 scripts/prepare_corpus.py <txt目录> --person <pid> --name <姓名> [--out-dir {corpus_dir}] 生成")
    clusters, src = load_dimensions(args.named)
    print(f"[dims] 载入 {len(clusters)} 个思维维度（{src.name}）")

    anchors_by_cluster = {}
    if not args.no_ruler and RULER_PATH.exists():
        ruler = json.loads(RULER_PATH.read_text(encoding="utf-8"))
        anchors_by_cluster = {c["cluster"]: c.get("anchors") or {} for c in ruler["dimensions"]}
        print(f"[ruler] 注入 AoT 尺子 v1.0 锚点 {len(anchors_by_cluster)} 个维度")

    people = []
    for p in sorted(corpus_dir.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        if args.person and d["person"] not in args.person:
            continue
        items = [it for it in d["items"] if (it.get("text") or "").strip()]
        if len(items) < len(d["items"]):
            print(f"[warn] {d['person']}: 跳过 {len(d['items']) - len(items)} 个空文本块", file=sys.stderr)
        people.append({"pid": d["person"], "items": items})
    if args.pilot is not None:
        vals = args.pilot if args.pilot else ["1", "2"]
        n_p, n_c = int(vals[0]), int(vals[1])
        people = [dict(p, items=p["items"][:n_c]) for p in people[:n_p]]
    if not people:
        sys.exit("错误：没有可评分的人物/文本")

    tasks = []
    for p in people:
        out_path = out_dir / f"{p['pid']}.json"
        existing = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else {}
        for item in p["items"]:
            for cl in clusters:
                key_t = f"{item['id']}::dim{cl['cluster']}"
                e = existing.get(key_t) or {}
                if (e.get("score") or 0) > 0 and not e.get("simulated") and not e.get("failed"):
                    continue
                tasks.append((p, out_path, existing, key_t, cl, item["text"]))

    n_temp = len(cfg.get("temperatures") or [0.3, 0.7])
    print(f"[info] 待打分任务 {len(tasks)} 条 × {n_temp} 轮 = {len(tasks) * n_temp} 次调用"
          f"（model={cfg.get('model')}）→ {out_dir}")
    if args.dry_run:
        return
    scorer = DimScorer(cfg)
    out_dir.mkdir(parents=True, exist_ok=True)
    done, n_failed = 0, 0
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

    with ThreadPoolExecutor(max_workers=args.workers or int(cfg.get("concurrency", 8))) as ex:
        futs = {ex.submit(run, t): t for t in tasks}
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                p, out_path, existing, key_t, res = fut.result()
                existing[key_t] = res
                out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
                done += 1
                n_failed += bool(res.get("failed"))
                if done % 20 == 0 or done == len(tasks):
                    print(f"  [prog] {done}/{len(tasks)}（失败 {n_failed}）", flush=True)
            except Exception as e:  # noqa: BLE001
                n_failed += 1
                print(f"  [err] {t[3]} 失败: {e}", file=sys.stderr)
            if args.max_runtime and time.time() - t0 > args.max_runtime:
                print(f"  [timeout] 已运行 {int(time.time()-t0)}s，主动退出（已完成条目已落盘，重启断点续跑）", flush=True)
                ex.shutdown(wait=False, cancel_futures=True)
                break

    print(f"[ok] 维度打分（本批）完成，结果在 {out_dir}（失败 {n_failed}）")
    if n_failed:
        sys.exit(3)


if __name__ == "__main__":
    main()
