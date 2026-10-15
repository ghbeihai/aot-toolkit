"""AoT —— 思维画像报告生成（v1.0，270 构念全量重跑版）。

从 clusters_v2/k25_named.json + profiles_v2/*.json 生成 Markdown 报告：
25 维体系、8 维对照、7×25 矩阵、每人画像、方法论、下一步。

用法：python3 scripts/report_md.py --v2
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
NAMED_V1 = AOT_ROOT / "data" / "results" / "clusters" / "k18_named.json"
NAMED_V2 = AOT_ROOT / "data" / "results" / "clusters_v2" / "k25_named.json"
PROFILES_V1 = AOT_ROOT / "data" / "results" / "profiles" / "people_profiles.json"
PROFILES_V2 = AOT_ROOT / "data" / "results" / "profiles_v2" / "people_profiles.json"
MATRIX_V1 = AOT_ROOT / "data" / "results" / "profiles" / "dimension_matrix.json"
MATRIX_V2 = AOT_ROOT / "data" / "results" / "profiles_v2" / "dimension_matrix.json"

# 8 维草图 → 数据聚出的维度 对照（人工判定，来自簇成员构成与命名；25 维 v2）
SKETCH_MAP = {
    "D1 元认知": ["元认知调控力（簇8）"],
    "D2 注意力": ["自我聚焦持续度（簇7，反刍/沉浸式注意聚焦的子集）——注意力本身仍为文献缺口，未聚出独立簇"],
    "D3 推理习惯": ["直觉速断倾向（簇4）", "反思审慎倾向（簇21）", "认知加工深度（簇12）", "分析性结构加工（簇22）"],
    "D4 抽象层级": ["抽象-具体转换（簇20）", "心理距离抽象度（簇14）"],
    "D5 归因结构": ["归因解释倾向（簇10）", "动机归因取向（簇2）", "能动掌控取向（簇17）"],
    "D6 论证图式": ["认知加工深度（簇12，论证主族 F3 落位，含证据-结论结构加工）", "反事实反驳倾向（簇16，证伪性思维的子类）"],
    "D7 根隐喻/叙事": ["隐喻根域偏好（簇6）", "关系联结取向（簇13，communion）", "能动掌控取向（簇17，agency）"],
    "D8 无意识/内隐": ["抑制回避倾向（簇19，防御机制）", "动机归因取向（簇2，内隐动机）——部分覆盖，防御机制无成熟 NLP 基线"],
}
NEW_DIMS = [
    "认知开放性（簇0）", "即时偏向（簇1）", "系统化-创造加工倾向（簇3）",
    "知识建构取向（簇5）", "道德直觉与践行（簇9）", "概率校准偏差（簇11）",
    "顿悟通达性（簇15）", "未来时间导向（簇18）", "道德情感评价取向（簇23）",
    "创造性阶段推进（簇24）",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v2", action="store_true", help="兼容参数：现在默认即 v2（v1 的 k18_named.json 已废弃）")
    ap.add_argument("--v1", action="store_true", help="旧 v1 结果（需本地仍有 clusters/k18_named.json）")
    ap.add_argument("--full", action="store_true", help="使用全量评分（scores_full → profiles_full），输出报告 v2.0")
    args = ap.parse_args()

    v2 = not args.v1
    full = args.full
    named_path = NAMED_V2 if (v2 or full) else NAMED_V1
    prof_path = PROFILES_V2 if (v2 or full) else PROFILES_V1
    mat_path = MATRIX_V2 if (v2 or full) else MATRIX_V1
    if full:
        prof_path = AOT_ROOT / "data" / "results" / "profiles_full" / "people_profiles.json"
        mat_path = AOT_ROOT / "data" / "results" / "profiles_full" / "dimension_matrix.json"
        version = "v2.0"
    else:
        version = "v1.0" if v2 else "v0.2"

    for p, hint in ((named_path, "name_clusters.py --v2 --k 25"),
                    (prof_path, "score_dimensions.py + aggregate_profiles.py --out " + str(prof_path))):
        if not p.exists():
            raise SystemExit(f"错误：缺少 {p}（先跑 {hint}）")
    named = json.loads(named_path.read_text(encoding="utf-8"))
    profiles = json.loads(prof_path.read_text(encoding="utf-8"))
    matrix = json.loads(mat_path.read_text(encoding="utf-8"))
    dims = {d["dim"]: d["name"] for d in matrix["dims"]}
    people = matrix["people"]
    # 人物顺序：矩阵中出现且有画像的人（原代码引用了未定义的 order → NameError）
    order = [p for p in people if p in profiles]
    names = {p: profiles[p].get("name", p) for p in order}

    L = []
    L.append(f"# AoT 思维图谱 {version} —— 7 人思维画像报告（270 构念全量重跑）\n")
    L.append("> 方法论：与 SPI（人格量化 Atlas）同构的六步链 —— 模型普查 → 因子链五层编码 → 高维语义嵌入 → 无监督聚类 → LLM 维度命名 → LLM 文本判定。维度由数据聚出，不是手写。\n")
    L.append("> 本版相对 v0.2（175 构念 / 18 维）的变更：普查 v2 新增 8 家族 95 构念 → 敏感性分析判定全量重跑 → 270 构念 / 25 维（k=25，轮廓系数 0.038）。\n")

    n_dim = len(named["clusters"])
    L.append(f"## 一、{n_dim} 个数据聚出的思维维度\n")
    L.append("| # | 维度 | 判定设问 | 来源家族（成员数） | 种子构念落位 |")
    L.append("|---|------|----------|--------------------|--------------|")
    for cl in named["clusters"]:
        dim = cl["dimension"]
        fams = {}
        for m in cl["members"]:
            fam = m.get("family_name") or m.get("family_id", "?")
            fams[fam] = fams.get(fam, 0) + 1
        fam_str = "、".join(f"{f}×{n}" for f, n in sorted(fams.items(), key=lambda x: -x[1])[:3])
        seeds = "、".join(m["name"] for m in cl["members"] if m.get("seed_ref")) or "—"
        q = dim.get("question", "")[:42] + ("…" if len(dim.get("question", "")) > 42 else "")
        L.append(f"| {cl['cluster']} | **{dim.get('name','')}** | {q} | {fam_str} | {seeds} |")
    L.append("")

    L.append("## 二、与用户 8 维草图的对照\n")
    L.append("| 8 维草图 | 数据聚出的对应维度 |")
    L.append("|----------|--------------------|")
    for k, v in SKETCH_MAP.items():
        L.append(f"| {k} | {'；'.join(v)} |")
    L.append(f"\n**数据新增维度（超出 8 维草图）**：{'、'.join(NEW_DIMS)}")
    L.append("\n**注意力维度**：文献中无统一文本测量框架（调研结论），本次未聚出独立簇——符合『维度由数据聚出』原则，留待更大语料观察。\n")

    L.append(f"## 三、7 人 × {n_dim} 维 平均分矩阵\n")
    L.append("（每人格 N 块文本上双轮 LLM 打分的块均值，1-7 分）\n")
    header = "| 维度 | " + " | ".join(names[p] for p in order) + " |"
    L.append(header)
    L.append("|------|" + "|".join(["---"] * len(order)) + "|")
    for d in sorted(dims):
        cells = []
        for p in order:
            v = people[p].get(str(d), people[p].get(d, "—"))
            if isinstance(v, (int, float)):
                cells.append(f"{v:.2f}")
            else:
                cells.append("—")
        L.append(f"| {dims[d]} | " + " | ".join(cells) + " |")
    L.append("")

    L.append("## 四、每人思维画像（Top5 维度 + 证据句）\n")
    for p in order:
        prof = profiles[p]
        L.append(f"### {prof['name']}\n")
        for r in prof["top5"]:
            ev = (r["evidence"][0][:50] + "…") if r["evidence"] else ""
            L.append(f"- **{r['dim_name']}** {r['mean']}（块间 σ={r.get('std', '—')}）—— {ev}")
        L.append("")

    if full:
        L.append("## 五、本次执行的数据链（全部可复现）\n")
        L.append("| 阶段 | 输入 → 输出 | 结果 |")
        L.append("|------|-------------|------|")
        L.append("| ① 模型普查 v2 | 4 领域集群穷尽扫描 + 资产复证 | 20 家族 × 270 构念（A 116 / B 151 / C 2） |")
        L.append("| ② 因子链编码 | 每构念 → 五层词元 | factor+name+synonyms+verbs（消融最优变体 B） |")
        L.append("| ③ 嵌入 | 270 条因子链 → BGE-M3 1024 维 | 本地 CPU，0 成本 |")
        L.append("| ④ 聚类 | k-means k=12-25 扫描 | k=25（轮廓系数 0.038） |")
        L.append("| ⑤ 维度命名 | DeepSeek 归纳每簇 | 25 条可判定维度 |")
        L.append("| ⑥ 尺子固化 | 25 维 → 维度特化评分锚点（低/中/高 + 对立极） | AoT 尺子 v1.0 冻结 |")
        L.append("| ⑦ 文本判定（抽样） | 7 人 49 块 × 25 维 × 双轮 | 2,450 次调用 |")
        L.append("| ⑧ 文本判定（全量） | 7 人 1001 块 × 25 维 × 双轮 | 50,050 次调用（25,025 条全部完成） |")
        L.append("| ⑨ 效标反标定（抽样） | 49 块 × 6 工具 × 双轮 | 588 次调用，收敛效度 0.52-0.88 |")
        L.append("| ⑩ 效标反标定（全量） | 1001 块 × 6 工具 × 双轮 | 12,012 次调用（随报告更新） |")
        L.append("")
        L.append("## 六、下一步\n")
        L.append("1. **外部效标反标定（全量）**：全量效标评分完成后出全量效标报告（CRT/NFC/ASQ/MFQ/MAI/ABS 收敛与判别效度）；")
        L.append("2. **人物级聚类（自下而上）**：1001 块文本嵌入 → 块级聚类 → 每簇命名，与自上而下 25 维交叉验证；")
        L.append("3. **F20 观察**：社会认知候选族在 25 维中的渗透（簇1/簇7 等）——是否转正由聚类涌现决定；")
        L.append("4. **最终目标**：思维画像与人格画像（SPI 六件套 32 因子）双图对照，支持『模仿其思考方式与文风』。")
    elif v2:
        L.append("## 五、本次执行的数据链（全部可复现）\n")
        L.append("| 阶段 | 输入 → 输出 | 结果 |")
        L.append("|------|-------------|------|")
        L.append("| ① 模型普查 v1 | 12 大思维模型家族 → 175 构念 | 12 家族 × 175 构念（A 级 87 / B 级 88） |")
        L.append("| ② 模型普查 v2 | 4 领域集群穷尽扫描 + 资产复证 → +95 构念 | 20 家族 × 270 构念（A 116 / B 151 / C 2，iso ~48 组） |")
        L.append("| ③ 敏感性分析 | 新增 95 构念追加后簇归属变化率 | k=15-25 全部 ≥52%（k=18 为 63.4%）→ 判定全量重跑 |")
        L.append("| ④ 因子链编码 | 每构念 → 五层词元 | factor+name+synonyms+verbs（消融最优变体 B） |")
        L.append("| ⑤ 嵌入 | 270 条因子链 → BGE-M3 1024 维 | 本地 CPU，0 成本 |")
        L.append("| ⑥ 聚类 | k-means k=12-25 扫描 | k=25（轮廓系数 0.038，簇规模 2-27 均匀） |")
        L.append("| ⑦ 维度命名 | DeepSeek 归纳每簇 | 25 条可判定维度（名称/设问/本质/关键词） |")
        L.append("| ⑧ 文本判定 | 7 人 49 块 × 25 维 × 双轮 | 2,450 次调用，证据句逐字引用 |")
        L.append("")
        L.append("## 六、下一步\n")
        L.append("1. **尺子固化**：25 维判定提示词定稿为 AoT 尺子 v1.0（冻结），建立『维度→阈值→描述』映射；")
        L.append("2. **外部效标反标定**：用 CRT/NFC（推理维）、归因风格问卷（归因维）、MFQ（道德维）、OMT 人工编码（动机维）反标定维度分数，达不到效度的维度回退重修词元；")
        L.append("3. **人物级聚类（自下而上）**：49 块文本嵌入 → 块级聚类 → 每簇命名，与自上而下 25 维交叉验证；")
        L.append("4. **全量语料**：从抽样扩展到全量语料，重跑判定；")
        L.append("5. **F20 观察**：社会认知候选族在 25 维中的渗透（簇1/簇7 等）——是否转正由聚类涌现决定；")
        L.append("6. **最终目标**：思维画像与人格画像（SPI 六件套 32 因子）双图对照，支持『模仿其思考方式与文风』。")
    else:
        L.append("## 五、方法论与数据链（v0.2，已被 v1.0 取代）\n")
        L.append("请以 --v2 重新生成 v1.0 报告。")

    out = AOT_ROOT / "data" / "results" / f"AoT思维画像报告_{version}.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] 报告已生成：{out}")


if __name__ == "__main__":
    main()
