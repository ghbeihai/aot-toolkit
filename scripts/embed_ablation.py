"""AoT —— 因子链拼接策略消融（对照实验）。

诊断：五层词元全拼的"定义串"共词过多（认知/思维/判断/倾向…），轮廓系数仅 0.036。
对照三种拼接策略，比较 BGE-M3 嵌入后的轮廓系数与簇纯度，选最优方案进入正式聚类。

变体：
  A = 全五层拼接（现状基线）
  B = factor + name + synonyms + verbs（去掉 adjectives/nouns 中高共词）
  C = factor + name + synonyms + nouns（去掉动词/形容词）
  D = 只拼 synonyms + verbs + nouns（语义负载最重）
"""
from __future__ import annotations

import glob
import re
from pathlib import Path

import numpy as np
import yaml

AOT_ROOT = Path(__file__).resolve().parent.parent
CENSUS_DIR = AOT_ROOT / "data" / "census"
MODEL_DIR = AOT_ROOT / "assets" / "bge-m3"

# 高频共词（出现在大量构念定义里的词，压低区分度）
STOP = {"认知", "思维", "判断", "倾向", "性", "能力", "风格", "过程", "模式", "程度", "水平", "层面", "方式", "的", "与", "和"}


def load_census():
    constructs = []
    for f in sorted(glob.glob(str(CENSUS_DIR / "*.yaml"))):
        d = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
        fam = d.get("family_id", Path(f).stem)
        for c in d.get("constructs", []):
            c["family_id"] = fam
            constructs.append(c)
    return constructs


def clean(words):
    out = []
    for w in words:
        w = w.strip()
        if not w or w in STOP or len(w) < 2:
            continue
        out.append(w)
    return out


def variant(c, mode):
    name = c.get("name", "")
    factor = c.get("factor", "")
    syn = c.get("synonyms", [])
    adj = c.get("adjectives", [])
    vrb = c.get("verbs", [])
    nou = c.get("nouns", [])
    if mode == "A":
        return "；".join(clean([factor, name] + adj + syn + vrb + nou))
    if mode == "B":
        return "；".join(clean([factor, name] + syn + vrb))
    if mode == "C":
        return "；".join(clean([factor, name] + syn + nou))
    if mode == "D":
        return "；".join(clean(syn + vrb + nou))
    raise ValueError(mode)


def main():
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sentence_transformers import SentenceTransformer

    constructs = load_census()
    print(f"[census] {len(constructs)} 构念，加载 BGE-M3 ...")
    model = SentenceTransformer(str(MODEL_DIR), device="cpu")

    for mode in "ABCD":
        texts = [variant(c, mode) for c in constructs]
        vecs = model.encode(texts, batch_size=16, normalize_embeddings=True)
        vecs = np.asarray(vecs)
        best = (-1, None, None)
        for k in (12, 15, 18, 20):
            km = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = km.fit_predict(vecs)
            sil = silhouette_score(vecs, labels)
            if sil > best[0]:
                best = (sil, k, labels)
        sil, k, labels = best
        print(f"[{mode}] 最佳 k={k} 轮廓系数={sil:.4f}")
        # 平均每簇家族纯度（最大家族占比的均值）
        from collections import Counter
        purities = []
        for ci in range(k):
            fams = Counter(constructs[i]["family_id"] for i in range(len(constructs)) if labels[i] == ci)
            purities.append(max(fams.values()) / sum(fams.values()))
        print(f"[{mode}] 平均簇纯度={np.mean(purities):.3f}")


if __name__ == "__main__":
    main()
