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
config/thinking_constructs.yaml   思维构念词元库（单一配置源，尺子 v0.1）
config/llm.yaml                   LLM 打分协议
data/corpus/                      每人抽样语料（prepare_corpus.py 产出）
data/results/scores/              每人 × 每构念分数（断点续跑）
data/results/clusters.json        自下而上聚类结果
data/results/cluster_names.json   LLM 簇命名
scripts/prepare_corpus.py         从 SPI 清洗语料抽样
scripts/score_thinking.py         LLM 零样本打分（主入口）
scripts/cluster_thinking.py       文本嵌入→聚类→每人簇分布
scripts/name_clusters.py          LLM 给簇命名
scripts/build_report.py           汇总画像报告
```

## 运行

```bash
cd AoT
python3 scripts/prepare_corpus.py
python3 scripts/score_thinking.py       # 断点续跑：重复运行只补未完成项
python3 scripts/cluster_thinking.py
python3 scripts/name_clusters.py
python3 scripts/build_report.py
```

API key：放在 `.env`（DEEPSEEK_API_KEY=sk-...），脚本自动读取；无 key 时进入模拟模式（结果带 simulated 标记）。

## 12 个思维构念（v0.1）

因果机制推理 / 类比迁移推理 / 数据证据校准 / 反例证伪意识 / 外因结构归因（两极）/ 抽象层级（两极）/
演绎必然推理 / 归纳概括推理 / 试探确定性（两极）/ 概念隐喻密度 / 元认知监控 / 内隐动机意象

## 尺子基线（v0.1 探索期）

- 尚未冻结；进入 v1.0 前须补：判别效度（构念间区分度）、重测稳定（同文双跑）、外部效标反标定。
