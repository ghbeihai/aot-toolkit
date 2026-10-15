"""AoT —— 簇命名（SPI 同构第 3 阶段收尾：让 LLM 给数据聚出的维度命名）。

输入：data/results/clusters/k{k}.json（每簇 = 一组语义相近的思维构念）
流程：对每簇，把成员构念的因子链串交给 DeepSeek，归纳为一条可判定的"思维维度"：
      名称 + 英文名 + 设问（判定时问什么）+ 本质（一句话）+ 关键词（判定锚点）
输出：data/results/clusters/k{k}_named.json

用法：python3 scripts/name_clusters.py --k 18
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
CLUSTERS_DIR = AOT_ROOT / "data" / "results" / "clusters"
ENV_PATH = AOT_ROOT / ".env"

SYSTEM_PROMPT = """你是一位认知科学方法学专家。我给你一个"思维构念簇"——它是由 270 个学术思维构念（来自认知风格、双过程、论证图式、归因、解释水平、元认知、概念隐喻、内隐动机、知识论、认知能力、启发式偏差、叙事身份、决策风格、时间取向、反事实、创造力、神经多样性、道德认知、持续性认知、社会认知等 20 大模型家族）经高维语义嵌入聚类得到的、语义相近的一组构念。

你的任务：为这个簇归纳出一条**可测量的思维维度**。输出严格 JSON（无其他文字）：
{"name": "中文维度名（4-8字，名词性短语）", "name_en": "英文名", "question": "判定设问：用『他是否/他如何…』提问，用于 LLM 从文本判断", "essence": "该维度本质的一句话概括（写清两极或核心特征）", "keywords": ["3-6个判定锚点词"]}

要求：
- 维度名必须能概括簇内大多数构念的共同内核，而不是某个单一构念；
- 如果簇内构念跨多个家族，找出它们的共同底层机制（如"自我监控""证据校准""结构归因"）；
- 如果簇内构念本身两极对立（如抽象↔具体），essence 里写清两极方向；
- question 要能被 LLM 直接用于 1-7 打分。"""


def load_key() -> str | None:
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=18)
    ap.add_argument("--v2", action="store_true", help="使用 v2 全量聚类结果目录 clusters_v2")
    args = ap.parse_args()

    clusters_dir = CLUSTERS_DIR if not args.v2 else AOT_ROOT / "data" / "results" / "clusters_v2"

    key = load_key()
    if not key:
        print("[!] 无 API key，无法命名")
        return
    from openai import OpenAI
    client = OpenAI(api_key=key, base_url="https://api.deepseek.com", timeout=120)

    src = clusters_dir / f"k{args.k}.json"
    data = json.loads(src.read_text(encoding="utf-8"))

    for cl in data["clusters"]:
        members = cl["members"]
        lines = []
        for m in members:
            lines.append(f"- {m['name']}（家族 {m['family_name']}）· {m['chain'][:60]}")
        user = (
            "【思维构念簇成员】\n"
            + "\n".join(lines)
            + "\n\n请归纳这条思维维度并输出 JSON。"
        )
        try:
            resp = client.chat.completions.create(
                model="deepseek-chat",
                temperature=0.4,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user},
                ],
            )
            named = json.loads(resp.choices[0].message.content or "{}")
        except Exception as ex:
            print(f"[err] 簇{cl['cluster']} 命名失败: {ex}")
            named = {"name": "命名失败", "name_en": "", "question": "", "essence": str(ex)[:50], "keywords": []}
        cl["dimension"] = named
        print(f"[ok] 簇{cl['cluster']:>2} (n={cl['size']:>2}) → {named.get('name','?')} | {named.get('essence','')[:40]}")

    out = clusters_dir / f"k{args.k}_named.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[ok] 已写 {out.name}")


if __name__ == "__main__":
    main()
