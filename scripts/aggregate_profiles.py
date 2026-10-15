#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AoT 人物画像汇总：把每人一个 {pid}.json 合并成 people_profiles.json。

用法：
  python3 aggregate_profiles.py <scores_dir> --out people_profiles.json

输入：score_dimensions.py 产出的 scores/ 目录，每人一个 {pid}.json
输出：people_profiles.json，结构 {pid: {name, top5: [{dim, dim_name, mean, evidence}]}}
"""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="AoT 人物画像汇总")
    ap.add_argument("scores_dir", help="score_dimensions.py 产出的 scores/ 目录")
    ap.add_argument("--out", default="people_profiles.json", help="输出文件名")
    args = ap.parse_args()

    scores_dir = Path(args.scores_dir)
    if not scores_dir.exists():
        print(f"错误：目录不存在 {scores_dir}", file=__import__("sys").stderr)
        raise SystemExit(1)

    profiles = {}
    for f in sorted(scores_dir.glob("*.json")):
        pid = f.stem
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[warn] 跳过 {f.name}: {e}", file=__import__("sys").stderr)
            continue

        dims = data.get("dimensions", {})
        sorted_dims = sorted(dims.items(), key=lambda x: -x[1].get("mean", 0))
        top5 = [
            {
                "dim": k,
                "dim_name": v.get("dim_name", k),
                "mean": round(v.get("mean", 0), 2),
                "evidence": (v.get("evidence") or [])[:2],
            }
            for k, v in sorted_dims[:5]
        ]

        profiles[pid] = {
            "name": data.get("name", pid),
            "n_dims": len(dims),
            "top5": top5,
        }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"汇总完成：{len(profiles)} 人 → {out_path}")


if __name__ == "__main__":
    main()
