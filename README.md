# AoT —— 思维图谱 Atlas of Thinking

把「人类是怎么想问题的」（思维过程/思维方式）从文本中量化出来：多维、有刻度、可比较、可复现，
最终目标：模仿一个人的思考方式与写作风格。它是「人格量化 SPI」的思维层孪生项目，同一套方法论，
对象从「他是谁」换成「他怎么想」。

## 版本状态

- v0.1（探索版，未冻结）：12 个思维构念降级为「种子构念」；SPI 同构管线重建中——思维构念普查（12 模型家族）→ 因子链编码 → 嵌入聚类，维度结构由数据聚出（详见 `data/census/`）
- 下一步 v1.0：外部效标反标定（D3↔CRT/NFC、D5↔归因问卷、D8↔OMT 人工编码）后冻结

## 架构（三层混合 Atlas）

1. **概念骨架层**：构念定义表（config/thinking_constructs.yaml，每个构念有设问/两极方向/词元/锚句/文献出处）
2. **词元资产层**：12 构念词元库，文献底座 = Walton 论证图式、LIWC 思维词类、CMT/MetaNet 隐喻、
   归因 CAVE、LCM 抽象层级、元认知 MAI、OMT 内隐动机（详见 config 内 source 字段）
3. **计算层**：DeepSeek 零样本判定（双轮平均 + 证据句 + 置信度）→ 思维画像；自下而上路线 = 文本嵌入聚类 → LLM 簇命名

## 嵌入方案（2026-10 定）

- 因子链嵌入（构念层，自上而下主路径）：**Qwen3-Embedding-8B（4096 维）**，BGE-M3 / TF-IDF+SVD 做对照——中文词元质量优先；
- 人物文本嵌入（个人层，自下而上补充路径）：**Qwen3-Embedding-8B / BGE-M3**（本地跑）；
- SPI 的 OpenAI 3072 维 HF 资产（<SPI_ROOT>/assets/hf-3072，879M）**仅作可选对照**：只有未来做「人格×思维跨图谱映射」时才需要同空间嵌入，当前不绑定；
- 嵌入全部本地、免费；DeepSeek 只用于词元自举 / 簇命名 / 文本打分。

## 目录

```
config/thinking_constructs.yaml   12 种子构念词元库（score_thinking 用）
config/llm.yaml                   LLM 协议：model / temperatures / 并发 / 退避重试 / 截断阈值
data/results/ruler/AoT尺子_v1.0.json  冻结尺子：25 维定义 + 锚点（仓库内，开箱即用）
data/corpus/<pid>.json            每人语料 {person, name, n_total, n_sampled, items:[{id,title,text}]}（gitignore，prepare_corpus.py 生成）
data/corpus_full/                 全量语料（可选，--full 用；同格式，gitignore）
data/results/clusters_v2/         embed_cluster + name_clusters 产物（k25.json / k25_named.json，gitignore）
data/results/scores_dim_v2/       25 维块级分数（score_dimensions 输出，断点续跑）

scripts/prepare_corpus.py         txt/md 目录或 SPI JSON → data/corpus/<pid>.json
scripts/score_dimensions.py       25 维打分（主入口；无 k25_named 时自动用冻结尺子定义）
scripts/aggregate_profiles.py     块级分数 → people_profiles.json（--names pid=人读名）
scripts/score_criterion.py        6 个效标工具代理打分（CRT/NFC/ASQ/MFQ/MAI/ABS）
scripts/score_thinking.py         12 种子构念打分
scripts/analyze_criterion.py      25 维 × 效标相关分析
scripts/embed_cluster.py / name_clusters.py / gen_ruler.py   构建尺子（研究用，需嵌入模型）
scripts/report_md.py              画像报告（默认 v2；--full 读 profiles_full）
scripts/llm_common.py             LLM 公共模块（与 WFP/SPI 同一实现）
```

## 运行（复刻流水线用到的部分）

```bash
cd $AOT_ROOT
python3 scripts/prepare_corpus.py ./原文 --person zhanglinjun --name 张林军     # → data/corpus/zhanglinjun.json
python3 scripts/score_dimensions.py --person zhanglinjun --dry-run              # 先看调用次数
python3 scripts/score_dimensions.py --person zhanglinjun                        # 断点续跑：重复运行只补未完成/失败项
python3 scripts/aggregate_profiles.py data/results/scores_dim_v2 --names zhanglinjun=张林军 --out people_profiles.json
# 可选：
python3 scripts/score_criterion.py   # 效标代理（data/results/criterion/）
python3 scripts/score_thinking.py    # 12 种子构念（data/results/scores/）
```

`--full` 只是把语料/输出目录切到 `data/corpus_full` / `scores_full`（或 `criterion_full`）；该目录不随仓库提供，需自己用
`prepare_corpus.py --out-dir data/corpus_full` 生成，否则脚本会直接报错说明。

API key：`DEEPSEEK_API_KEY` 环境变量 → `$WENBI_ENV_FILE` → 本仓 `.env` → `$SPI_ROOT/$WFP_ROOT` 的 `.env`；
**无 key 报错退出 1**（模拟模式已移除）。429/5xx/截断自动指数退避；`WENBI_MOCK_LLM=1` 为离线假客户端（测试用）。
退出码：0 成功；1 参数/输入/key 错误；3 有打分项失败（重跑即续跑）。

## 12 个思维构念（v0.1）

因果机制推理 / 类比迁移推理 / 数据证据校准 / 反例证伪意识 / 外因结构归因（两极）/ 抽象层级（两极）/
演绎必然推理 / 归纳概括推理 / 试探确定性（两极）/ 概念隐喻密度 / 元认知监控 / 内隐动机意象

## 尺子基线（v0.1 探索期）

- 尚未冻结；进入 v1.0 前须补：判别效度（构念间区分度）、重测稳定（同文双跑）、外部效标反标定。
