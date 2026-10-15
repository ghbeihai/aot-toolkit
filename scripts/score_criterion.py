"""AoT —— 效标代理评分（criterion-proxy scoring）。

对文本按【心理学测量工具的核心构念】打分（1-7），作为 25 维判定的第二把尺子。
工具：CRT（认知反思）/ NFC（认知需求）/ ASQ（归因风格）/ MFQ（道德基础）/ MAI（元认知意识）/ ABS（具体性-抽象性）。

用法：
    python3 scripts/score_criterion.py --pilot 1 2    # 试点：第 1 人前 2 块
    python3 scripts/score_criterion.py                # 抽样 49 块 × 6 工具 × 双轮
    python3 scripts/score_criterion.py --full         # 全量 1001 块 × 6 工具 × 双轮
"""
from __future__ import annotations

import argparse
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

AOT_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = AOT_ROOT / "data" / "corpus"
OUT_DIR = AOT_ROOT / "data" / "results" / "criterion"
ENV_PATH = AOT_ROOT / ".env"
MAX_TEXT_CHARS = 6000

TOOLS = [
    {
        "tool": "CRT",
        "name": "认知反思（Cognitive Reflection）",
        "desc": (
            "依据 CRT（Frederick 2005，认知反思测验）的构念：人在判断时抑制直觉/第一反应、"
            "进行审慎慢思考的程度。高分者面对看似显然的答案会停下来重新计算、检验；低分者直接给出直觉答案。"
            "判定文本作者：他/她在思考与表达中，多大程度上展现『抑制直觉冲动、主动复核、慢思考』？"
        ),
        "expected_pos": ["反思审慎倾向", "认知加工深度", "分析性结构加工"],
        "expected_neg": ["直觉速断倾向", "即时偏向"],
    },
    {
        "tool": "NFC",
        "name": "认知需求（Need for Cognition）",
        "desc": (
            "依据 NFC（Cacioppo & Petty 1984，认知需求量表）的构念：人是否享受并主动寻求复杂、"
            "费力的思考活动，而非回避认知负担。高分者喜欢深挖问题、比较观点、解构原理；低分者偏好简单直接、"
            "回避脑力消耗。判定文本作者：他/她在文本中多大程度上展现『主动追求复杂思考、享受认知挑战』？"
        ),
        "expected_pos": ["认知加工深度", "认知开放性", "知识建构取向"],
        "expected_neg": ["直觉速断倾向", "即时偏向"],
    },
    {
        "tool": "ASQ",
        "name": "归因风格（Attributional Style）",
        "desc": (
            "依据 ASQ/CAVE（Seligman 1979；Schulman 1989）的构念：人对事件（尤其是负面事件）原因的"
            "解释倾向，三维度：内部-外部、稳定-不稳定、可控-不可控。高分=惯于做稳定、内在、可控的因果归因"
            "并形成解释体系；低分=少做归因、归因于外部偶然情境。判定文本作者：他/她在解释事情原因时，"
            "多大程度上展现『稳定的内在归因与因果解释建构』？"
        ),
        "expected_pos": ["归因解释倾向", "动机归因取向", "能动掌控取向"],
        "expected_neg": ["概率校准偏差", "抑制回避倾向"],
    },
    {
        "tool": "MFQ",
        "name": "道德基础（Moral Foundations）",
        "desc": (
            "依据 MFQ（Haidt 2007，道德基础问卷）的构念：道德判断依赖的直觉基础——关怀/伤害、"
            "公平/欺骗、忠诚/背叛、权威/颠覆、圣洁/堕落。高分者频繁用道德词汇评价人、事、制度，"
            "并以道德情感驱动表达；低分者少做道德评价、就事论事。判定文本作者：他/她在文本中"
            "多大程度上展现『道德基础的直觉评价与道德情感表达』？"
        ),
        "expected_pos": ["道德情感评价取向", "道德直觉与践行"],
        "expected_neg": ["概率校准偏差", "反事实反驳倾向"],
    },
    {
        "tool": "MAI",
        "name": "元认知意识（Metacognitive Awareness）",
        "desc": (
            "依据 MAI（Schraw & Dennison 1994，元认知意识量表）的构念：人对自身认知过程的觉察与调节"
            "（陈述性知识、程序性知识、条件性知识；计划、监控、评价）。高分者在思考中明确追踪理解状态、"
            "评估策略、纠正错误；低分者缺乏自我监控语言。判定文本作者：他/她在文本中多大程度上展现"
            "『对自身思考的觉察、监控与调节』？"
        ),
        "expected_pos": ["元认知调控力"],
        "expected_neg": ["直觉速断倾向", "即时偏向"],
    },
    {
        "tool": "ABS",
        "name": "语言抽象层级（Linguistic Abstraction）",
        "desc": (
            "依据 Brysbaert 2014 具体性常模与 LCM（Semin & Fiedler 1989）的构念：语言在具体（动作、场景、"
            "实体细节）与抽象（概括、本质、类别、关系）之间的层级位置。高分=惯用抽象概括、去情境化、"
            "类别性语言；低分=惯用具体细节、动作、场景语言。判定文本作者：他/她的语言多大程度上"
            "偏向抽象层级（而非具体层级）？"
        ),
        "expected_pos": ["抽象-具体转换", "心理距离抽象度"],
        "expected_neg": ["直觉速断倾向"],
    },
]

SYSTEM_PROMPT = """你是一位严谨的心理学测量编码器（psychometric coder）。

你会收到：
1. 【效标工具构念】——某个心理学测量工具测量的核心构念及其行为表现；
2. 【待分析文本】——一段自然语言文本。

任务：仅根据文本实际内容，判断【文本作者】在该效标构念上的水平，输出严格 JSON（无其他文字）：
{"score": 1到7的整数, "evidence": ["原文片段", ...最多3条], "confidence": 0到1之间的小数}

标尺：7=强烈且一致体现；5~6=明显体现；3~4=部分或含糊；1~2=几乎不体现或相反。
规则：评分基于文本本身；evidence 逐字引用原文；confidence 表示把握程度。"""


def load_key() -> str | None:
    # 优先读环境变量
    env_key = os.environ.get("DEEPSEEK_API_KEY")
    if env_key:
        return env_key.strip()
    # 回退读 .env 文件
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DEEPSEEK_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def render_tool(t) -> str:
    return f"工具名称：{t['name']}\n构念说明：{t['desc']}"


class ToolScorer:
    def __init__(self, key: str | None):
        if not key:
            print("错误：未检测到 DEEPSEEK_API_KEY。\n"
                  "请先 export DEEPSEEK_API_KEY=sk-... 或在 .env 文件中配置。",
                  file=sys.stderr)
            sys.exit(1)
        self.key = key
        self.simulated = False
        from openai import OpenAI
        self.client = OpenAI(api_key=key, base_url="https://api.deepseek.com", timeout=120)

    def _call(self, desc: str, text: str, temp: float) -> dict:
        user = f"【效标工具构念】\n{desc}\n\n【待分析文本】\n{text}\n\n请按系统要求输出 JSON。"
        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            temperature=temp,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user},
            ],
        )
        return json.loads(resp.choices[0].message.content or "{}")

    def score(self, desc: str, text: str) -> dict:
        scores, confs, evs = [], [], []
        for temp in (0.3, 0.7):
            for attempt in range(2):
                try:
                    data = self._call(desc, text, temp)
                    s = int(data["score"])
                    if 1 <= s <= 7:
                        scores.append(s)
                        confs.append(float(data.get("confidence", 0.5)))
                        for e in data.get("evidence", []):
                            e = str(e).strip()
                            if e and e not in evs and len(evs) < 3:
                                evs.append(e)
                        break
                except Exception as ex:
                    if attempt == 1:
                        print(f"    [warn] t={temp} 失败: {ex}")
                    time.sleep(1.5)
        if not scores:
            return {"score": 0.0, "raw_scores": [], "evidence": [], "confidence": 0.0, "simulated": True}
        return {
            "score": round(sum(scores) / len(scores), 2),
            "raw_scores": scores,
            "evidence": evs,
            "confidence": round(sum(confs) / len(confs), 2) if confs else 0.0,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", nargs="*", default=None, help="试点：'人数 块数'，如 --pilot 1 2")
    ap.add_argument("--full", action="store_true", help="使用全量语料 data/corpus_full，输出到 criterion_full")
    ap.add_argument("--workers", type=int, default=12, help="并发数（默认 12）")
    ap.add_argument("--max-runtime", type=int, default=0, help="主动限时退出（秒）")
    args = ap.parse_args()

    corpus_dir = CORPUS_DIR
    out_dir = OUT_DIR
    if args.full:
        corpus_dir = AOT_ROOT / "data" / "corpus_full"
        out_dir = AOT_ROOT / "data" / "results" / "criterion_full"

    people = []
    for p in sorted(corpus_dir.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        people.append({"pid": d["person"], "items": d["items"]})
    if args.pilot is not None:
        vals = args.pilot if args.pilot else ["1", "2"]
        n_p, n_c = int(vals[0]), int(vals[1])
        people = [dict(p, items=p["items"][:n_c]) for p in people[:n_p]]

    key = load_key()
    scorer = ToolScorer(key)
    if scorer.simulated:
        print("[!] 无 API key，进入模拟模式")

    out_dir.mkdir(parents=True, exist_ok=True)
    tasks = []
    for p in people:
        out_path = out_dir / f"{p['pid']}.json"
        existing = {}
        if out_path.exists():
            existing = json.loads(out_path.read_text(encoding="utf-8"))
        for item in p["items"]:
            text = item["text"][:MAX_TEXT_CHARS]
            for t in TOOLS:
                key_t = f"{item['id']}::{t['tool']}"
                if key_t in existing and existing[key_t].get("score", 0) > 0 and not existing[key_t].get("simulated", False):
                    continue
                tasks.append((p, out_path, existing, key_t, t, text))

    print(f"[info] 效标代理：{len(people)} 人 × {len(TOOLS)} 工具，待打分 {len(tasks)} 条 × 双轮 = {len(tasks)*2} 次调用")
    done = 0
    t0 = time.time()

    def run(t):
        p, out_path, existing, key_t, tool, text = t
        res = scorer.score(render_tool(tool), text)
        res["tool"] = tool["tool"]
        res["tool_name"] = tool["name"]
        res["person"] = p["pid"]
        res["chunk"] = key_t.split("::")[0]
        return p, out_path, existing, key_t, res

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run, t): t for t in tasks}
        for fut in as_completed(futs):
            t = futs[fut]
            try:
                p, out_path, existing, key_t, res = fut.result()
                existing[key_t] = res
                out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
                done += 2
                if done % 40 == 0 or done == len(tasks) * 2:
                    print(f"  [prog] {done}/{len(tasks)*2}", flush=True)
            except Exception as ex:
                print(f"  [err] {t[3]} 失败: {ex}")
            if args.max_runtime and time.time() - t0 > args.max_runtime:
                print(f"  [timeout] 已运行 {int(time.time()-t0)}s，主动退出", flush=True)
                ex.shutdown(wait=False, cancel_futures=True)
                break

    print(f"[ok] 效标代理评分（本批）完成，结果在 {out_dir}")


if __name__ == "__main__":
    main()
