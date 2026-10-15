# AoT 思维普查（Census）总览 — SPI 同构管线第 1-2 阶段交付

> 管线定位：SPI 价值链「44 模型 → 358 因子 → 6694 因子链（五层编码）→ 嵌入 → k-means → 15 语义簇」在思维侧的普查重建。本目录 = 模型普查 + 因子链编码成果，**维度结构不由手选，由后续嵌入+聚类阶段从数据聚出**。
> 编码日期：2026-10-11。Schema 对齐 `AoT/config/thinking_constructs.yaml`（必填字段：id/name/en/dimension/question/factor/adjectives/synonyms/verbs/nouns/anchors(positive,negative)/source/lexicon_grade；可选：seed_ref/tags/iso_group）。

## 一、12 家族 × 统计总览

| 家族 | 文件 | 构念数 | iso 去重组 | A 级（现成资产） | B 级（LLM 自举） | seed_ref 代表构念（仅参考） |
|---|---|---|---|---|---|---|
| F1 认知风格 | cogstyle.yaml | 14 | 2 | 6 | 8 | 分析-整体、直觉-分析(CSI) |
| F2 双过程/理性 | dualprocess.yaml | 14 | 2 | 5 | 9 | 认知反思 |
| F3 论证图式 | argument.yaml | 16 | 2 | 9 | 7 | 专家意见论证、实践推理、类比论证 |
| F4 归因风格 | attribution.yaml | 15 | 3 | 7 | 8 | 内归因、悲观解释风格 |
| F5 解释水平/抽象 | abstraction.yaml | 13 | 2 | 9 | 4 | 抽象语言倾向、形容词特质化层(LCM 高层) |
| F6 元认知 | metacognition.yaml | 14 | 3 | 11 | 3 | 陈述性元认知知识、理解监控 |
| F7 概念隐喻 | metaphor.yaml | 16 | 3 | 10 | 6 | 旅程隐喻、战争隐喻 |
| F8 内隐动机与防御 | motive.yaml | 14 | 2 | 7 | 7 | 成就动机、权力动机 |
| F9 知识论认知/批判性思维 | epistemic.yaml | 16 | 2 | 5 | 11 | 反思判断、批判性思维倾向 |
| F10 认知能力 | ability.yaml | 14 | 2 | 9 | 5 | 晶体智力/词汇广度(Gc)、分析(Bloom) |
| F11 启发式与偏差 | heuristic.yaml | 15 | 3 | 1 | 14 | 代表性启发、认知反思 |
| F12 叙事身份 | narrative.yaml | 14 | 3 | 8 | 6 | agency 能动性、communion 交流/归属 |
| **合计** | **12 文件** | **175** | **29** | **87** | **88** | **24 个 seed_ref** |

**总量 175 构念，落在 100-200 验收区间；A/B 级接近对半（87/88），可直接进入嵌入管线。**

## 二、iso 异名同构去重（29 组，含跨族）

典型同构组（族内）：
- 认知风格：分析-整体 ≈ Riding 整体-分析 ≈ 系统化-直觉（iso-f1-analytic-holistic）
- 论证图式：诉诸权威 ⊂ 专家意见；claim=结论=论点
- 归因：内归因族=能力/努力；外归因族=运气/结构
- 抽象：形容词特质化 ≈ 高层行为识别 ≈ 抽象语言；动作动词层 ≈ 低层行为识别 ≈ 具体语言
- 启发式：损失厌恶 ≈ 沉没成本 ≈ 现状偏差；过度自信 ≈ 校准偏差 ≈ 元认知过度自信（跨族 F11↔F6）

跨族同构（已互指，聚类阶段避免重复计簇）：
- 因果论证（F3）↔ 因果归因（F4）
- 形容词特质化（F5）↔ 基本归因错误（F4）
- 认知反思（F2 CRT）≈ 分析型（F1）≈ LIWC analytic（F10）
- 评价（F10 Bloom）↔ 元认知评价（F6）
- agency/communion：F7 met-015/016 ↔ F12 nar-001/002/009/010（iso-agency / iso-communion）
- 权力动机（F8 mot-002）↔ 叙事权力主题（F12 nar-014）

## 三、lexicon_grade 词元来源分级（A=87 / B=88）

- **A 级（现成资产，source 给出处）**：CRT/AOT/NFC/NFCS 题面、CSI/CoSI/KAI 题面、CCTDI 七子倾向、MAI 8 子成分、Bloom 19 动词、CHC 广域名、Walton 图式名+批判性问题、Toulmin 六组件、CAVE 三维、LCM 词性梯度、BIF、CLT 四维、MML 条目（#LIFE IS A JOURNEY 等）、McAdams 编码手册类目、Winter 动机词表（nAch/nPow/nAff）、Cramer TAT 类目、LIWC 认知机制词类（C-LIWC/SCLIWC 中文可复用）、中文具体性常模（Yao 2017/ANCW 2023/谢志鹏&毕冉 2022）。
- **B 级（LLM 从理论原典自举，标 bootstrap，待人工抽审）**：启发式偏差族（F11，行为实验构念无现成中文词表，14/15 为 B）、反思判断/Perry 立场（原为访谈编码）、认知风格中文词表（中文无公开风格词表）、防御机制（反向形成等标【一方称】）。

## 四、中文适用性要点

- ✅ 直接可用：LIWC 认知机制词类（C-LIWC 黄金兰 2012 / SCLIWC Gao 2013）、中文具体性常模（Yao 2017/ANCW 2023/Chan & Tse 2024/谢志鹏&毕冉 2022）、中文隐喻 NLP（Song 2021 知识图谱/MultiCMET 2023）。
- 🟡 需自建/校准：Bloom 动词中文同义词集、叙事 agency/communion 与内隐动机中文词典（无验证版，建议编码规则 prompt 化 + LLM 多模型零样本 + 小样本人工校准，外部效度锚 OMT r≈.85 与 McAdams 人工编码）。
- 所有词元以中文为主（可直接嵌入），en/factor 字段保留英文对照（可做跨语言嵌入对齐）。

## 五、用户 8 维草图覆盖对应（种子仅参考，构念不丢失）

| 草图维度 | 落点 | 说明 |
|---|---|---|
| 元认知 | F6（14 构念） | MAI 8 子成分全编码 |
| 推理习惯 | F2（双过程）+ F3（论证图式） | 反思-直觉 + 图式使用 |
| 抽象层级 | F5（13 构念） | CLT 四维 + LCM 四级梯度 |
| 归因结构 | F4（15 构念） | Weiner 三维 + CAVE + actor-observer |
| 论证图式 | F3（16 构念） | Walton 核心图式 + Toulmin |
| 根隐喻/agency-communion | F7（16 构念）+ F12（14 构念） | CMT 源域 + 叙事主题，iso 互指 |
| 无意识 | F8（14 构念） | 内隐动机 + 防御机制 |
| 注意力 | **未预编码，留待聚类涌现** | 文献无统一文本框架（见总报告 7.4），符合"维度由数据聚出"原则 |

## 六、下一步（嵌入+聚类阶段输入就绪说明）

- 12 个 YAML 词元层全部为中文词项，可直接喂嵌入模型（建议：中文 Sentence-BERT/BGE-M3 或与 SPI 同族的 1536/3072 维 API 嵌入）。
- 嵌入对象建议 = 每构念的 factor 名 + 五层词元拼接（类比 SPI 因子链）；聚类 k 从 12-20 起步（SPI 用 15），轮廓系数 + 外部效标（CRT/归因问卷/OMT 人工编码）反推最优 k。
- iso 组已互指：聚类后可把同构成员并入同一簇或降权，避免重复计簇。
- 文献出处：全部复用此前已核验调研（总报告 95+31 条），未做新全网检索；新增未核验条目已在各文件 models 表标 `verified: claimed`（如 CoSI/KAI/NFC/NFCS/Perry/CCTDI/Bakan/Pasupathi）。
