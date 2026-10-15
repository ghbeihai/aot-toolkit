#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AoT 人物画像汇总：把 score_dimensions.py 产出的扁平结果汇总成 people_profiles.json。

输出结构：
  {"pid": {"name": "...", "n_dims": 25, "top5": [{"dim", "dim_name", "mean", "evidence": [...]}]}}
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
    ap.add_argument("--names", default="",
                    help="pid→人读名映射：'zhanglinjun=张林军,kangyuhua=康玉华' 或 JSON 文件路径")
    args = ap.parse_args()
    name_map = {}
    if args.names:
        if Path(args.names).is_file():
            name_map = json.loads(Path(args.names).read_text(encoding="utf-8"))
        else:
            for kv in args.names.split(","):
                if "=" in kv:
                    k, v = kv.split("=", 1)
                    name_map[k.strip()] = v.strip()

    scores_dir = Path(args.scores_dir)
    if not scores_dir.exists():
        print(f"错误：目录不存在 {scores_dir}", file=sys.stderr)
        sys.exit(1)

    # 按 pid → dim → scores[] + evidence[] 分组
    by_person = defaultdict(lambda: defaultdict(lambda: {"scores": [], "evidences": []}))
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
            score = entry.get("score")
            if not isinstance(score, (int, float)) or score <= 0 or entry.get("failed"):
                continue  # 失败分（None/failed）不进画像
            by_person[pid][dim]["scores"].append(score)
            if "dim_name" not in by_person[pid][dim]:
                by_person[pid][dim]["dim_name"] = dim_name
            # 收集 evidence
            evs = entry.get("evidence", [])
            if evs:
                by_person[pid][dim]["evidences"].extend(evs[:2])  # 每维最多存 2 条
            for nk in ("display_name", "person_name", "name"):
                if entry.get(nk) and pid not in person_names:
                    person_names[pid] = entry[nk]

    profiles = {}
    for pid, dims in by_person.items():
        dim_means = []
        for dim, data in dims.items():
            scores = data["scores"]
            if not scores:
                continue
            dim_name = data.get("dim_name", dim)
            mean = sum(scores) / len(scores)
            # 取该维前 2 条 evidence
            evidence = data["evidences"][:2] if data["evidences"] else []
            dim_means.append({
                "dim": dim,
                "dim_name": dim_name,
                "mean": round(mean, 2),
                "n_chunks": len(scores),
                "evidence": evidence,
            })

        dim_means.sort(key=lambda x: -x["mean"])
        top5 = dim_means[:5]

        profiles[pid] = {
            "pid": pid,
            # 优先 --names 映射，其次评分里带的人读名；都没有才退回 pid
            "name": name_map.get(pid) or person_names.get(pid, pid),
            "n_dims": len(dim_means),
            "top5": top5,
        }

    out_path = Path(args.out)
    out_path.write_text(json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"汇总完成：{len(profiles)} 人 → {out_path}")
    for pid, p in profiles.items():
        top1 = p["top5"][0] if p["top5"] else {}
        print(f"  {pid}: {p['n_dims']} 维, top1={top1.get('dim_name','?')} ({top1.get('mean',0)})")


if __name__ == "__main__":
    main()
