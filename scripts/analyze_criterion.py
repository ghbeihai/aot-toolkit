"""AoT —— 效标相关分析：25 维分数 × 6 效标工具 的 Spearman 相关。

输入：
  - 25 维：data/results/scores_dim_v2/{person}.json（或 --full 时 scores_full）
  - 效标：data/results/criterion/{person}.json（或 criterion_full）
按 人×块 对齐，计算相关矩阵，输出收敛/判别效度表。

用法：python3 scripts/analyze_criterion.py [--full]
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
DIM_DIR = AOT_ROOT / "data" / "results" / "scores_dim_v2"
CRIT_DIR = AOT_ROOT / "data" / "results" / "criterion"
NAMED_PATH = AOT_ROOT / "data" / "results" / "clusters_v2" / "k25_named.json"
OUT_DIR = AOT_ROOT / "data" / "results" / "criterion"


def spearman(xs: list[float], ys: list[float]) -> float:
    """Spearman 秩相关（scipy 不可用时的手写实现）。"""
    n = len(xs)
    if n < 3:
        return 0.0

    def rank(vals):
        order = sorted(range(n), key=lambda i: vals[i])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks

    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    dy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def load_scores(pid: str, d: dict, dim_names: dict) -> dict[str, dict]:
    """返回 {chunk: {dim: score}}"""
    by_chunk: dict[str, dict] = defaultdict(dict)
    for key, v in d.items():
        if (v.get("score") or 0) <= 0 or v.get("simulated"):
            continue
        if "::dim" not in key:
            continue
        chunk, _, dim = key.partition("::dim")
        by_chunk[chunk][int(dim)] = v["score"]
    return {c: s for c, s in by_chunk.items() if len(s) >= 10}


def load_crit(pid: str, d: dict) -> dict[str, dict]:
    by_chunk: dict[str, dict] = defaultdict(dict)
    for key, v in d.items():
        if (v.get("score") or 0) <= 0 or v.get("simulated"):
            continue
        if "::" not in key:
            continue
        chunk, _, tool = key.partition("::")
        by_chunk[chunk][tool] = v["score"]
    return {c: s for c, s in by_chunk.items() if len(s) >= 4}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="使用全量结果（scores_full + criterion_full）")
    args = ap.parse_args()

    dim_dir = DIM_DIR
    crit_dir = CRIT_DIR
    tag = "抽样49块"
    if args.full:
        dim_dir = AOT_ROOT / "data" / "results" / "scores_full"
        crit_dir = AOT_ROOT / "data" / "results" / "criterion_full"
        tag = "全量1001块"

    named = json.loads(NAMED_PATH.read_text(encoding="utf-8"))
    dim_names = {cl["cluster"]: cl["dimension"]["name"] for cl in named["clusters"]}

    people = sorted(dim_dir.glob("*.json"))
    rows = []  # {dim: score, tool: score}
    for pf in people:
        pid = pf.stem
        dims = load_scores(pid, json.loads(pf.read_text(encoding="utf-8")), dim_names)
        critf = crit_dir / f"{pid}.json"
        if not critf.exists():
            continue
        crits = load_crit(pid, json.loads(critf.read_text(encoding="utf-8")))
        for chunk, dvals in dims.items():
            if chunk not in crits:
                continue
            rows.append({"dim": dvals, "tool": crits[chunk]})
    print(f"[info] 对齐样本：{len(rows)} 块（{tag}）")
    if len(rows) < 5:
        print("[!] 样本过少，无法计算相关")
        return

    tools = ["CRT", "NFC", "ASQ", "MFQ", "MAI", "ABS"]
    dims = sorted(dim_names.keys())
    mat = {}
    for t in tools:
        mat[t] = {}
        for d in dims:
            pairs = [(r["tool"][t], r["dim"][d]) for r in rows if t in r["tool"] and d in r["dim"]]
            if len(pairs) >= 3:
                mat[t][d] = spearman([a for a, _ in pairs], [b for _, b in pairs])
            else:
                mat[t][d] = 0.0

    # 输出 Markdown 报告
    L = []
    L.append(f"# AoT 效标反标定报告（{tag}）\n")
    L.append(f"> 样本：{len(rows)} 个 人×块 配对；Spearman 秩相关；收敛=预期维度相关，判别=非预期维度相关。\n")
    L.append("| 效标 | " + " | ".join(dim_names[d] for d in dims) + " |")
    L.append("|------|" + "|".join(["---"] * len(dims)) + "|")
    for t in tools:
        cells = []
        for d in dims:
            r = mat[t][d]
            cells.append(f"{r:+.2f}")
        L.append(f"| **{t}** | " + " | ".join(cells) + " |")
    L.append("")

    L.append("## 收敛效度（预期相关）与判别效度（非预期相关均值）\n")
    L.append("| 效标 | 预期+维度（实际 r） | 预期−维度（实际 r） | 非预期维度均值 | 判别比(收敛/判别) |")
    L.append("|------|---------------------|---------------------|----------------|--------------------|")
    for t in tools:
        pos = [mat[t][d] for d in dims if dim_names[d] in TOOL_EXPECT[t]["pos"]]
        neg = [mat[t][d] for d in dims if dim_names[d] in TOOL_EXPECT[t]["neg"]]
        other = [mat[t][d] for d in dims if dim_names[d] not in TOOL_EXPECT[t]["pos"] and dim_names[d] not in TOOL_EXPECT[t]["neg"]]
        pos_mean = sum(pos) / len(pos) if pos else 0
        neg_mean = sum(neg) / len(neg) if neg else 0
        other_mean = sum(other) / len(other) if other else 0
        disc = (abs(pos_mean) + abs(neg_mean)) / (abs(other_mean) + 1e-9)
        L.append(f"| {t} | {pos_mean:+.2f}（{len(pos)} 维） | {neg_mean:+.2f}（{len(neg)} 维） | {other_mean:+.2f} | {disc:.1f} |")
    L.append("")

    L.append("## 结论与回退建议\n")
    L.append("- 收敛方向正确：对应维度相关为正（或预期负向为负）且 |r| 明显高于非预期维度 → 维度有效；")
    L.append("- 收敛但判别弱：相关方向对但区分度不足 → 维度命名/锚点需细化；")
    L.append("- 方向错误或接近 0：维度判定与该工具构念无对应 → 列为**回退重修候选**。\n")
    out = OUT_DIR / f"AoT效标反标定报告_{'full' if args.full else 'sample'}.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] 报告：{out}")
    # 控制台摘要
    print("\n=== 收敛/判别摘要 ===")
    for t in tools:
        pos = [mat[t][d] for d in dims if dim_names[d] in TOOL_EXPECT[t]["pos"]]
        neg = [mat[t][d] for d in dims if dim_names[d] in TOOL_EXPECT[t]["neg"]]
        other = [mat[t][d] for d in dims if dim_names[d] not in TOOL_EXPECT[t]["pos"] and dim_names[d] not in TOOL_EXPECT[t]["neg"]]
        pos_mean = sum(pos) / len(pos) if pos else 0
        neg_mean = sum(neg) / len(neg) if neg else 0
        other_mean = sum(other) / len(other) if other else 0
        print(f"  {t}: 收敛+ {pos_mean:+.2f} | 收敛− {neg_mean:+.2f} | 判别 {other_mean:+.2f}")


TOOL_EXPECT = {
    "CRT": {"pos": ["反思审慎倾向", "认知加工深度", "分析性结构加工"], "neg": ["直觉速断倾向", "即时偏向"]},
    "NFC": {"pos": ["认知加工深度", "认知开放性", "知识建构取向"], "neg": ["直觉速断倾向", "即时偏向"]},
    "ASQ": {"pos": ["归因解释倾向", "动机归因取向", "能动掌控取向"], "neg": ["概率校准偏差", "抑制回避倾向"]},
    "MFQ": {"pos": ["道德情感评价取向", "道德直觉与践行"], "neg": ["概率校准偏差", "反事实反驳倾向"]},
    "MAI": {"pos": ["元认知调控力"], "neg": ["直觉速断倾向", "即时偏向"]},
    "ABS": {"pos": ["抽象-具体转换", "心理距离抽象度"], "neg": ["直觉速断倾向"]},
}


if __name__ == "__main__":
    main()
