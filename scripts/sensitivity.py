"""AoT —— 普查 v2 敏感性分析（sensitivity analysis）

比较 v1 175 构念在「仅 v1 语料」与「v1+新增构念」两种因子链语料下的 k-means 簇归属变化率。
判定：变化率 <20% → 保留 v1 画像 + 新增维度；≥20% → 全量重跑。

复用 scripts/embed_cluster.py 的 clean / factor_chain_text / embed 逻辑（importlib 加载，避免重复代码）。

用法：
    python3 scripts/sensitivity.py --with-new 0 --k-min 15 --k-max 25   # baseline（仅 v1 175 构念）
    python3 scripts/sensitivity.py --with-new 1 --k-min 15 --k-max 25   # v1 + census_v2/constructs 新增
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import yaml

AOT_ROOT = Path(__file__).resolve().parent.parent
CENSUS_DIR = AOT_ROOT / "data" / "census"
NEW_DIR = AOT_ROOT / "data" / "census_v2" / "constructs"
OUT_DIR = AOT_ROOT / "data" / "results" / "sensitivity"

# 加载 embed_cluster 模块并复用 clean / factor_chain_text
spec = importlib.util.spec_from_file_location("embed_cluster", AOT_ROOT / "scripts" / "embed_cluster.py")
ec = importlib.util.module_from_spec(spec)
sys.modules["embed_cluster"] = ec
spec.loader.exec_module(ec)


def load_constructs(dir_path: Path, tag: str) -> list:
    """加载指定目录下所有 YAML 的构念，返回 [(id, family_id, name, chain_text)]"""
    out = []
    for f in sorted(glob.glob(str(dir_path / "*.yaml"))):
        try:
            d = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
        except Exception as ex:
            print(f"[warn] 无法解析 {f.name}: {ex}")
            continue
        fam = d.get("family_id", Path(f).stem)
        for c in d.get("constructs", []):
            if not isinstance(c, dict) or "id" not in c:
                print(f"[warn] {f.name} 中跳过非标准构念: {str(c)[:60]}")
                continue
            out.append({
                "id": c["id"],
                "family_id": fam,
                "name": c.get("name", ""),
                "text": ec.factor_chain_text(c),
            })
    return out


def align_labels(base_labels: np.ndarray, new_labels: np.ndarray) -> np.ndarray:
    """用最大重叠（贪心，按重叠量降序）把 new 的簇标签对齐到 base 的簇标签空间。"""
    k_base = int(base_labels.max()) + 1
    k_new = int(new_labels.max()) + 1
    mapping = {}
    # 重叠计数矩阵
    counts = np.zeros((k_base, k_new), dtype=int)
    for b, n in zip(base_labels, new_labels):
        counts[b, n] += 1
    used_new = set()
    for b in range(k_base):
        # 找与 base 簇 b 重叠最大的 new 簇（未用）
        best = -1
        best_cnt = -1
        for n in range(k_new):
            if n in used_new:
                continue
            if counts[b, n] > best_cnt:
                best_cnt = counts[b, n]
                best = n
        if best >= 0:
            mapping[best] = b
            used_new.add(best)
    # 未映射的 new 簇给新标签（>= k_base）
    next_id = k_base
    aligned = np.zeros_like(new_labels, dtype=int)
    for i, n in enumerate(new_labels):
        if n in mapping:
            aligned[i] = mapping[n]
        else:
            aligned[i] = next_id
            next_id += 1
    return aligned


def run(with_new: bool, k_min: int, k_max: int):
    v1 = load_constructs(CENSUS_DIR, "v1")
    print(f"[load] v1 构念: {len(v1)}")
    v1_ids = [c["id"] for c in v1]

    texts_v1 = [c["text"] for c in v1]
    vecs_v1 = ec.embed_vectors(texts_v1)

    if with_new:
        new = load_constructs(NEW_DIR, "new")
        print(f"[load] 新增构念: {len(new)}")
        texts_all = texts_v1 + [c["text"] for c in new]
        vecs_all = ec.embed_vectors(texts_all)
        tag = "v1plusnew"
    else:
        new = []
        vecs_all = vecs_v1
        tag = "baseline"

    from sklearn.cluster import KMeans
    summary = {}
    for k in range(k_min, k_max + 1):
        # 新语料的聚类
        km_all = KMeans(n_clusters=k, n_init=10, random_state=42).fit(vecs_all)
        labels_all = km_all.labels_
        labels_v1_new = labels_all[:len(v1)]
        # 保存新语料聚类（构念 id → 簇）
        rec_all = {c["id"]: int(l) for c, l in zip(v1 + new, labels_all)}
        (OUT_DIR / f"{tag}_k{k}.json").write_text(
            json.dumps(rec_all, ensure_ascii=False, indent=0), encoding="utf-8")

        if with_new:
            # baseline 对应 k 的簇归属（v1-only 语料、相同 k、相同 random_state）
            km_base = KMeans(n_clusters=k, n_init=10, random_state=42).fit(vecs_v1)
            labels_base = km_base.labels_
            aligned = align_labels(labels_base, labels_v1_new)
            changed = int((aligned != labels_base).sum())
            rate = changed / len(v1)
            summary[k] = {"changed": changed, "total": len(v1), "change_rate": round(rate, 4)}
            print(f"[k={k}] 簇归属变化: {changed}/{len(v1)} = {rate:.1%}")
        else:
            summary[k] = {"note": "baseline only"}

    # 一致性：同一构念在不同 k 下的稳定性（供参考）
    stability = {}
    if not with_new:
        base_maps = {}
        for k in range(k_min, k_max + 1):
            m = json.loads((OUT_DIR / f"baseline_k{k}.json").read_text(encoding="utf-8"))
            base_maps[k] = m
        for cid in v1_ids:
            labs = [base_maps[k][cid] for k in range(k_min, k_max + 1)]
            stability[cid] = int(Counter(labs).most_common(1)[0][1])
        print(f"[稳定] 175 构念中，{sum(1 for v in stability.values() if v >= 3)} 个在 ≥3 个 k 下落到同一簇")

    (OUT_DIR / f"sensitivity_summary_{tag}.json").write_text(
        json.dumps({"tag": tag, "k_min": k_min, "k_max": k_max,
                    "v1_count": len(v1), "new_count": len(new),
                    "per_k": summary}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] 结果写入 {OUT_DIR / f'sensitivity_summary_{tag}.json'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-new", type=int, default=0)
    ap.add_argument("--k-min", type=int, default=15)
    ap.add_argument("--k-max", type=int, default=25)
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)  # 原在模块级：--help/import 也会建目录
    run(bool(args.with_new), args.k_min, args.k_max)
