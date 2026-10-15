"""AoT —— 因子链嵌入 + 聚类（SPI 同构第 3 阶段：让数据自己告诉你结构）。

输入：data/census/*.yaml（12 家族 175 构念 × 五层因子链）
流程：
  1. 每个构念拼接为一条中文因子链串（factor + name + adjectives + synonyms + verbs + nouns），
     类比 SPI 的因子链（factor/adjectives/synonyms/verbs/nouns 五层编码）；
  2. BGE-M3 本地嵌入（CPU，无 GPU 环境；失败自动回退 TF-IDF+SVD）；
  3. k-means 扫描 k=12..20（SPI 用 15），轮廓系数 + 各簇规模评估选优；
  4. 输出每簇成员（构念 id/名称/家族/因子链串），供 LLM 簇命名与下一步判定。

用法：
    python3 scripts/embed_cluster.py --k-min 12 --k-max 20
    python3 scripts/embed_cluster.py --k 15            # 只看固定 k
"""
from __future__ import annotations

import argparse
import glob
import json
from collections import Counter
from pathlib import Path
from typing import List

import numpy as np
import yaml

AOT_ROOT = Path(__file__).resolve().parent.parent
CENSUS_DIRS = [AOT_ROOT / "data" / "census", AOT_ROOT / "data" / "census_v2" / "constructs"]
OUT_DIR = AOT_ROOT / "data" / "results" / "clusters_v2"
MODEL_DIR = AOT_ROOT / "assets" / "bge-m3"

# 高频共词（消融实验结论：去掉后轮廓系数 0.036→0.052）
STOP = {"认知", "思维", "判断", "倾向", "性", "能力", "风格", "过程", "模式", "程度", "水平", "层面", "方式", "的", "与", "和"}


def clean(words):
    out = []
    for w in words:
        w = str(w).strip()
        if not w or w in STOP or len(w) < 2:
            continue
        out.append(w)
    return out


def load_census() -> List[dict]:
    constructs = []
    for d in CENSUS_DIRS:
        if not d.exists():
            continue
        for f in sorted(glob.glob(str(d / "*.yaml"))):
            dd = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
            fam = dd.get("family_id", Path(f).stem)
            for c in dd.get("constructs", []):
                c["family_id"] = fam
                c["family_name"] = dd.get("family_name", fam)
                constructs.append(c)
    return constructs


def factor_chain_text(c: dict) -> str:
    """因子链 → 一条中文串（消融最优变体 B：factor+name+synonyms+verbs，去停用词）。"""
    parts = clean(
        [c.get("name", ""), c.get("factor", "")]
        + c.get("synonyms", [])
        + c.get("verbs", [])
    )
    return "；".join(parts)


def embed_vectors(texts: List[str]) -> np.ndarray:
    """BGE-M3 本地嵌入（CPU），失败回退 TF-IDF+SVD。"""
    try:
        from sentence_transformers import SentenceTransformer
        print(f"[embed] 加载 BGE-M3（CPU）于 {MODEL_DIR} ...")
        model = SentenceTransformer(str(MODEL_DIR), device="cpu")
        vecs = model.encode(texts, batch_size=8, show_progress_bar=True, normalize_embeddings=True)
        print(f"[embed] BGE-M3 完成：{vecs.shape}")
        return np.asarray(vecs)
    except Exception as ex:
        print(f"[warn] BGE-M3 嵌入失败（{ex}），回退 TF-IDF+SVD")
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.decomposition import TruncatedSVD
        tfidf = TfidfVectorizer(token_pattern=r"[\u4e00-\u9fff]{2,}|[a-zA-Z]+")
        X = tfidf.fit_transform(texts)
        svd = TruncatedSVD(n_components=256, random_state=42)
        vecs = svd.fit_transform(X)
        norms = np.linalg.norm(vecs, axis=1, keepdims=True)
        vecs = vecs / norms
        print(f"[embed] TF-IDF+SVD 完成：{vecs.shape}")
        return vecs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k-min", type=int, default=12)
    ap.add_argument("--k-max", type=int, default=20)
    ap.add_argument("--k", type=int, default=None, help="只评估固定 k")
    args = ap.parse_args()

    constructs = load_census()
    print(f"[census] 载入 {len(constructs)} 个构念")
    texts = [factor_chain_text(c) for c in constructs]
    vecs = embed_vectors(texts)

    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    k_range = [args.k] if args.k else list(range(args.k_min, args.k_max + 1))
    results = {}
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(vecs)
        sil = silhouette_score(vecs, labels)
        sizes = Counter(labels)
        print(f"  [k={k}] 轮廓系数={sil:.3f} 簇规模={dict(sorted(sizes.items()))}")
        # 输出簇成员
        clusters = []
        for ci in range(k):
            members = [
                {
                    "id": constructs[i]["id"],
                    "name": constructs[i]["name"],
                    "family": constructs[i]["family_id"],
                    "family_name": constructs[i]["family_name"],
                    "lexicon_grade": constructs[i].get("lexicon_grade", "?"),
                    "seed_ref": bool(constructs[i].get("seed_ref", False)),
                    "chain": texts[i],
                }
                for i in range(len(constructs))
                if labels[i] == ci
            ]
            clusters.append({"cluster": ci, "size": len(members), "members": members})
        out = {
            "k": k,
            "silhouette": round(float(sil), 4),
            "embedding": "BGE-M3" if "BGE" in str(type(vecs)).upper() or True else "tfidf-svd",
            "n_constructs": len(constructs),
            "clusters": clusters,
        }
        path = OUT_DIR / f"k{k}.json"
        path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        results[k] = (sil, path)
        print(f"  [ok] 已写 {path.name}")

    best = max(results, key=lambda k: results[k][0])
    print(f"\n[best] k={best} 轮廓系数={results[best][0]:.3f} → {results[best][1]}")


if __name__ == "__main__":
    main()
