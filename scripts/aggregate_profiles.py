#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AoT 人物画像汇总：把 score_dimensions.py 产出的扁平结果汇总成 people_profiles.json。

输入结构（score_dimensions.py 产出）：
  {"chunk_id::dimN": {"score": 1-7, "dim": "dimN", "dim_name": "...", "person": "pid", ...}, ...}

输出结构：
  {"pid": {"name": "...", "n_dims": 25, "top5": [{"dim", "dim_name", "mean", "evidence"}]}}

用法：
  python3 aggregate_profiles.py <scores_dir> --out people_profiles.json
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="AoT 人物画像汇总")
    ap.add_argument("scores_dir", help="score_dimensions.py 产出的 scores/ 目录")
    ap.add_argument("--out", default="people_profiles.json", help="输出文件名")
    args = ap.parse_args()

    scores_dir = Path(args.scores_dir)
    if not scores_dir.exists():
        print(f"错误：目录不存在 {scores_dir}", file=sys.stderr)
        sys.exit(1)

    # 按 pid → dim → scores[] 分组
    by_person = defaultdict(lambda: defaultdict(list))
    person_names = {}

    for f in sorted(scores_dir.glob("*.json")):
        pid = f.stem
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[warn] 跳过 {f.name}: {e}", file=sys.stderr)
            continue

        for key, entry in data.items():
            if not isinstance(entry, dict):
                continue
            dim = entry.get("dim", "")
            dim_name = entry.get("dim_name", dim)
            score = entry.get("score", 0)
            if score <= 0:
                continue
            by_person[pid][dim].append({"score": score, "dim_name": dim_name})
            if "person" in entry and pid not in person_names:
                person_names[pid] = entry["person"]

    profiles = {}
    for pid, dims in by_person.items():
        # 算每维均值
        dim_means = []
        for dim, entries in dims.items():
            scores = [e["score"] for e in entries]
            dim_name = entries[0]["dim_name"] if entries else dim
            mean = sum(scores) / len(scores)
            dim_means.append({
                "dim": dim,
                "dim_name": dim_name,
                "mean": round(mean, 2),
                "n_chunks": len(scores),
            })

        # 按均值排序取 top5
        dim_means.sort(key=lambda x: -x["mean"])
        top5 = dim_means[:5]

        profiles[pid] = {
            "name": person_names.get(pid, pid),
            "n_dims": len(dim_means),
            "top5": top5,
        }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"汇总完成：{len(profiles)} 人 → {out_path}")
    for pid, p in profiles.items():
        print(f"  {pid}: {p['n_dims']} 维, top1={p['top5'][0]['dim_name']} ({p['top5'][0]['mean']})")


if __name__ == "__main__":
    main()
