#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一个人的原文（txt/md 目录，或 SPI 篇章 dict JSON）整理成 AoT 语料 JSON。

输出：<out-dir>/<person>.json = {"person", "name", "n_total", "n_sampled", "items": [{"id", "title", "text"}]}
  - id = 文件 stem（与 wenbi-replica / WFP 的 doc_id 一致）
  - 长文按段落切成 ≤ --chunk-chars 的块（id 加 #k 后缀），--chunk-chars 0 表示不切
  - --sample N + --seed 可复现抽样；空文本跳过并告警

用法：
  python3 scripts/prepare_corpus.py ./原文 --person zhanglinjun --name 张林军
  python3 scripts/prepare_corpus.py articles_clean.json --person kyh --name 康玉华 --out-dir data/corpus_full
"""
import argparse
import json
import random
import sys
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent


def load_docs(src: Path):
    if src.is_file() and src.suffix.lower() == ".json":
        d = json.loads(src.read_text(encoding="utf-8"))
        if isinstance(d, dict) and "items" in d:
            return [(str(it.get("id")), it.get("title", ""), it.get("text", "")) for it in d["items"]]
        return [(str(k), str(k), " ".join(v) if isinstance(v, list) else str(v)) for k, v in d.items()]
    files = [src] if src.is_file() else sorted(f for f in src.iterdir() if f.suffix.lower() in (".txt", ".md"))
    return [(f.stem, f.stem, f.read_text(encoding="utf-8")) for f in files]


def chunk(text: str, n: int):
    if not n or len(text) <= n:
        return [text]
    out, cur = [], ""
    for p in (x.strip() for x in text.split("\n")):
        if not p:
            continue
        while len(p) > n:
            if cur:
                out.append(cur)
                cur = ""
            out.append(p[:n])
            p = p[n:]
        if cur and len(cur) + len(p) + 1 > n:
            out.append(cur)
            cur = p
        else:
            cur = f"{cur}\n{p}" if cur else p
    if cur:
        out.append(cur)
    return out


def main():
    ap = argparse.ArgumentParser(description="整理 AoT 语料 JSON（data/corpus/<person>.json）")
    ap.add_argument("src", help="原文目录（.txt/.md）、单文件，或 SPI 篇章 dict / items JSON")
    ap.add_argument("--person", required=True, help="pid（英文/拼音，作文件名）")
    ap.add_argument("--name", default=None, help="人读名（默认同 pid）")
    ap.add_argument("--out-dir", default=str(AOT_ROOT / "data" / "corpus"))
    ap.add_argument("--chunk-chars", type=int, default=3000, help="长文切块阈值（默认 3000；0=不切）")
    ap.add_argument("--sample", type=int, default=0, help="随机抽 N 块（0=全部）")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    src = Path(args.src)
    if not src.exists():
        sys.exit(f"错误：{src} 不存在")
    items, n_empty = [], 0
    for doc_id, title, text in load_docs(src):
        if not text.strip():
            n_empty += 1
            continue
        parts = chunk(text.strip(), args.chunk_chars)
        for k, part in enumerate(parts):
            items.append({"id": doc_id if len(parts) == 1 else f"{doc_id}#{k}", "title": title, "text": part})
    if n_empty:
        print(f"[warn] 跳过 {n_empty} 篇空文本", file=sys.stderr)
    if not items:
        sys.exit("错误：没有可用文本")
    n_total = len(items)
    if args.sample and args.sample < n_total:
        items = random.Random(args.seed).sample(items, args.sample)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{args.person}.json"
    path.write_text(json.dumps({"person": args.person, "name": args.name or args.person, "n_total": n_total,
                                "n_sampled": len(items), "items": items}, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    print(f"[ok] {path}：{len(items)}/{n_total} 块")


if __name__ == "__main__":
    main()
