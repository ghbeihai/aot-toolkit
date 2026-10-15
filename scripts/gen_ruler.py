"""AoT —— 尺子固化：为 25 个数据聚出的维度生成【维度特化评分锚点】。

输入：data/results/clusters_v2/k25_named.json（维度名/设问/本质/关键词 + 成员构念）
过程：DeepSeek 逐维生成 low(1-2分)/mid(3-5分)/high(6-7分) 行为描述 + 正反对照示例
输出：data/results/ruler/AoT尺子_v1.0.json（机器冻结版）+ AoT尺子_v1.0.md（人读版）

用法：python3 scripts/gen_ruler.py
"""
from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
NAMED_PATH = AOT_ROOT / "data" / "results" / "clusters_v2" / "k25_named.json"
OUT_DIR = AOT_ROOT / "data" / "results" / "ruler"
ENV_PATH = AOT_ROOT / ".env"

SYSTEM_PROMPT = """你是一位严谨的心理学测量量表开发专家（psychometric scale developer），为思维画像系统编写【维度特化评分锚点】（behavioral anchors）。

你会收到一个思维维度的定义（名称/判定设问/本质/判定锚点词/组成构念）。

任务：为这个维度设计可操作的行为评分锚点，输出严格 JSON（无其他文字）：
{
  "anchor_low": "1-2分的行为与文本特征描述，约50-90字，具体到可见的语言行为；",
  "anchor_mid": "3-5分的行为与文本特征描述（部分、含糊、偶发、混合）约50-90字；",
  "anchor_high": "6-7分的行为与文本特征描述（强烈、一致、贯穿性）约50-90字；",
  "polar_note": "该维度的对立极是什么（如直觉vs审慎），低分端在文本中如何体现；若维度本身无极差对立只体现强度，则写\"强度差\"并说明低分端如何区分于无表现；",
  "example_low": ["1条低分端示例句（2-4句，中文，虚构但不脱离该维度语义）"],
  "example_mid": ["1条中分端示例句"],
  "example_high": ["1条高分端示例句"]
}

要求：
1. 锚点必须可判（描述可观察的语言行为，而不是抽象人格标签）；
2. 三档之间边界清晰、不重叠；
3. 贴合该维度的判定设问与本质，不要泛化为通用思维质量；
4. 示例句服务于人类审阅理解，不进入判定提示词。"""


def load_key() -> str | None:
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def render_dimension(cl) -> str:
    dim = cl["dimension"]
    members = [m["name"] for m in cl["members"]]
    return "\n".join([
        f"维度名称：{dim.get('name', '')}（{dim.get('name_en', '')}）",
        f"判定设问：{dim.get('question', '')}",
        f"本质：{dim.get('essence', '')}",
        f"判定锚点词：{'、'.join(dim.get('keywords', []))}",
        f"组成构念：{'、'.join(members[:10])}{'…' if len(members) > 10 else ''}",
    ])


def main():
    import argparse
    argparse.ArgumentParser(description=f"生成 AoT 尺子锚点（需 DEEPSEEK_API_KEY）→ {OUT_DIR}").parse_args()
    from openai import OpenAI

    key = load_key()
    if not key:
        print("[!] 无 API key，无法生成尺子锚点")
        return
    client = OpenAI(api_key=key, base_url="https://api.deepseek.com", timeout=120)

    named = json.loads(NAMED_PATH.read_text(encoding="utf-8"))
    clusters = named["clusters"]
    print(f"[dims] 载入 {len(clusters)} 个维度")

    out_dir = OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "AoT尺子_v1.0.json"

    existing = {}
    if out_path.exists():
        existing = {c["cluster"]: c for c in json.loads(out_path.read_text(encoding="utf-8"))["dimensions"]}

    def gen(cl):
        cid = cl["cluster"]
        if cid in existing and existing[cid].get("anchors"):
            return cid, existing[cid], True
        definition = render_dimension(cl)
        user = f"【思维维度定义】\n{definition}\n\n请为该维度设计评分锚点并输出 JSON。"
        for attempt in range(2):
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
                data = json.loads(resp.choices[0].message.content or "{}")
                rec = {
                    "cluster": cid,
                    "dimension": cl["dimension"],
                    "members": [m["name"] for m in cl["members"]],
                    "anchors": {
                        "anchor_low": str(data.get("anchor_low", "")).strip(),
                        "anchor_mid": str(data.get("anchor_mid", "")).strip(),
                        "anchor_high": str(data.get("anchor_high", "")).strip(),
                        "polar_note": data.get("polar_note") or "",
                    },
                    "examples": {
                        "example_low": list(data.get("example_low", []))[:3],
                        "example_mid": list(data.get("example_mid", []))[:3],
                        "example_high": list(data.get("example_high", []))[:3],
                    },
                }
                ok = all(len(v) > 20 for v in (rec["anchors"]["anchor_low"], rec["anchors"]["anchor_mid"], rec["anchors"]["anchor_high"]))
                if ok:
                    return cid, rec, False
                print(f"  [warn] dim{cid} 锚点过短，重试")
            except Exception as ex:
                print(f"  [err] dim{cid} 失败: {ex}")
                time.sleep(2)
        return cid, {"cluster": cid, "dimension": cl["dimension"], "anchors": {}, "error": "generation_failed"}, False

    results = {}
    todo = [cl for cl in clusters if cl["cluster"] not in existing or not existing[cl["cluster"]].get("anchors")]
    if not todo:
        print("[ok] 全部维度已有锚点，跳过生成")
    else:
        print(f"[info] 待生成锚点维度 {len(todo)} 个")
        with ThreadPoolExecutor(max_workers=8) as ex:
            futs = {ex.submit(gen, cl): cl for cl in todo}
            for fut in as_completed(futs):
                cid, rec, skipped = fut.result()
                results[cid] = rec
                if not skipped:
                    print(f"  [ok] dim{cid} 锚点生成完成", flush=True)

    dims = [existing.get(c["cluster"]) or results.get(c["cluster"]) for c in clusters]
    ruler = {
        "meta": {
            "name": "AoT 尺子 v1.0",
            "version": "1.0",
            "generated": "2026-10-11",
            "base": "k25_named.json（270 构念 → k=25 聚类命名）",
            "scoring_protocol": "双轮 LLM 判定（temperature 0.3/0.7），score 1-7 整数，evidence ≤3 条逐字引用，confidence 0-1；块级均值聚合为人均分",
            "scale": "7=强烈且一致体现；5~6=明显体现；3~4=部分或含糊；1~2=几乎不体现（或按维度定义的对立极方向）",
            "thresholds": {
                "low": [1, 2.49],
                "mid": [2.5, 4.49],
                "high": [4.5, 7],
            },
        },
        "dimensions": [d for d in dims if d],
    }
    out_path.write_text(json.dumps(ruler, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] 尺子冻结版：{out_path}")

    # —— 人读版 Markdown ——
    L = []
    L.append("# AoT 尺子 v1.0 —— 25 维思维判定协议（冻结版）\n")
    L.append("> 用途：对任意自然语言文本判定其作者在 25 个数据聚出思维维度上的得分（1-7）。本文件是 AoT 全量评分与后续画像的唯一判定依据，修改须升版。\n")
    L.append("## 判定协议\n")
    L.append("- 评分制：**1-7 分整数**，双轮（temperature 0.3/0.7）取均值；证据 `evidence` 逐字引用原文，≤3 条；confidence 0-1。")
    L.append("- 通用标尺：7=强烈且一致体现；5~6=明显体现；3~4=部分或含糊；1~2=几乎不体现或按定义对立极方向。")
    L.append("- 阈值映射：**低 1.0-2.49 / 中 2.5-4.49 / 高 4.5-7.0**。")
    L.append("- 来源：270 构念因子链 → BGE-M3 嵌入 → k=25 聚类 → DeepSeek 命名（k25_named.json），本尺子仅补充【维度特化锚点】，不改变维度定义。\n")
    for d in ruler["dimensions"]:
        dim = d["dimension"]
        a = d.get("anchors") or {}
        L.append(f"## 维度 {d['cluster']}：{dim.get('name','')}（{dim.get('name_en','')}）\n")
        L.append(f"- **判定设问**：{dim.get('question','')}")
        L.append(f"- **本质**：{dim.get('essence','')}")
        L.append(f"- **判定锚点词**：{'、'.join(dim.get('keywords',[]))}")
        L.append(f"- **组成构念**：{'、'.join(d['members'][:12])}{'…' if len(d['members'])>12 else ''}")
        if a:
            L.append(f"- **低分锚点（1-2）**：{a.get('anchor_low','')}")
            L.append(f"- **中分锚点（3-5）**：{a.get('anchor_mid','')}")
            L.append(f"- **高分锚点（6-7）**：{a.get('anchor_high','')}")
            if a.get('polar_note'):
                L.append(f"- **对立极说明**：{a.get('polar_note','')}")
            exs = d.get("examples") or {}
            if exs.get("example_low"):
                L.append(f"  - 低分示例：{exs['example_low'][0]}")
            if exs.get("example_mid"):
                L.append(f"  - 中分示例：{exs['example_mid'][0]}")
            if exs.get("example_high"):
                L.append(f"  - 高分示例：{exs['example_high'][0]}")
        else:
            L.append("- ⚠ 锚点生成失败（见 JSON 中 error 字段）")
        L.append("")
    md = out_dir / "AoT尺子_v1.0.md"
    md.write_text("\n".join(L), encoding="utf-8")
    print(f"[ok] 尺子人读版：{md}")


if __name__ == "__main__":
    main()
