# AoT 普查 v2 · S1「决策与判断」集群穷尽性文献扫描

> 范围：9 个指定候选方向 + 扫描中发现的补充方向。对照 v1 = 12 家族 175 构念（`census/constructs_index.md`）逐条标注「增量 / 已有→v1 id」。
> 证据分级：【已查证】= 本轮检索到期刊/出版社/PMC/作者官网页面核验标题·作者·年份·卷期一致；【一方称·教科书经典】= 学界公认但本轮未逐页翻原文。
> 可计算性：A=现成词表/量表题面可直接转文本判定；B=LLM 从理论自举；C=基本不可从自由文本测量（需行为任务）。
> 中文适用性：✅ 有中文版量表/词表；🟡 需自建校准；❌ 无文本侧入口。

---

## 0. 集群级结论（先给判断）

| # | 候选方向 | 一句话结论 | 可计算性 |
|---|---|---|---|
| 1 | 决策风格 GDMS（含 Bass 前身） | **独立成族**（F-DM 决策风格与风险偏好）：理性/直觉两维与 v1 重叠，但依赖/回避/自发三维是真增量 | B |
| 2 | 自然决策 NDM / RPD | **不独立**：过程理论非个体差异构念，无量表；拆 1–2 个构念并入决策族 | C |
| 3 | 概率与统计思维 / 风险素养 | **并入 F10 认知能力**（能力侧增量）；基础率忽视偏差侧已在 heur-005 | B |
| 4 | 风险感知与风险偏好（Slovic / DOSPERT） | **并入决策族**：领域特异风险偏好是真增量；风险感知维度偏情境 | B |
| 5 | 框架与语境效应 | **重复**：heur-010 已覆盖，仅补 risky/attribute/goal 三型细分 | C（测人易感性）/ B（测文本框架语言） |
| 6 | 反事实与假设思维 | **独立成族**（F-CF 反事实与后悔）：文本标记极强，v1 完全空白 | A |
| 7 | 未来思维 / 情景预见 EFT | **并入时间视角族**：与 ZTPI 未来维、nar-012 future-script 合并 | B |
| 8 | 时间视角 ZTPI | **独立成族**（F-TP 时间取向）：5 维自陈成熟、中文有修订版、文本可测 | B |
| 9 | 延迟折扣 / 跨期选择 | **并入时间视角族**（现在偏差构念），方法上是行为选择任务 | C/B |

**集群建议产出 3 个 v2 新家族**：
- **F-DM 决策风格与风险偏好**（GDMS 5 风格 + DOSPERT 领域风险 + NDM 专家直觉 1 构念 + 补充：决策回避/最优化-满意化）
- **F-TP 时间取向**（ZTPI 5 维 + EFT 情景未来思维 + 延迟折扣/现在偏差）
- **F-CF 反事实与后悔**（向上/向下反事实 + 后悔 + 假设思维）

并入现有：概率统计素养→F10；框架效应→heur-010 细分；NDM→F-DM/F2。

---

## 1. 决策风格（GDMS；Bass 前身）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **General Decision-Making Style Inventory (GDMS)**，25 题 5 风格各 5 题，5 点 Likert | Scott, S. G., & Bruce, R. A. (1995). *Educational and Psychological Measurement*, 55(5), 818–831. DOI:10.1177/0013164495055005017 | 【已查证】（卷期/25 题/5 因子经多语复核一致） | ①理性风格 rational → 部分已有 cgs-009 直觉-分析、dp-008 分析加工；②直觉风格 intuitive → 部分已有 cgs-009、dp-007 直觉加工；③**依赖风格 dependent（遇事先征询他人）=增量**；④**回避风格 avoidant（拖延/能躲则躲）=增量**；⑤**自发风格 spontaneous（求快、即时决断）=增量**（与 cgs-012 冲动-反思部分重叠但决策域不同） | B（自陈习惯句，LLM 可从"我总问别人/我一直拖着/我拍脑袋定"判定；无现成中文思维词表） | 🟡→✅（已有中文修订：驾驶员群体 11 题 3 维分半信度 .868/.887/.897/.859、α .878–.912；通用版中文期刊多篇修订） | **独立成族 F-DM 主干**；理性/直觉维与 F1/F2 去重后只留依赖/回避/自发 3 增量 |
| 子量表信度（再验证样本） | BMC Psychology 2020（结直肠癌筛查样本）报 rational α=.68 / intuitive α=.82 / dependent α=.81 / avoidant α=.85；MDPI 2024 复核五因子 α=.83–.92 | 【已查证】（rational 偏低 .68 是反复出现的弱点） | —（信度锚点，供尺子固化外部效标） | — | — | 原 Scott&Bruce 报告 α≈.77–.88【一方称·教科书经典】 |
| **Bass 决策风格（前身脉络）** | Bass, B. M. (1981). *Stogdill's Handbook of Leadership* (Rev. ed.). Free Press；Henderson & Nutt (1980) 分析型/启发型决策风格 | 【一方称·教科书经典】 | Scott&Bruce 明确说 GDMS 是整合前人（含 Bass、Mintzberg、Driver）的产物；Bass 式分类无独立存活量表 | — | — | **不独立**，作为 F-DM 的理论前史注脚，不单列构念 |
| 补充：Melbourne 决策问卷 MDMQ（vigilance / buck-passing / procrastination / hypervigilance） | Mann, L., et al. (1997). *MDMQ*；源出 Janis & Mann (1977) *Decision Making*（冲突理论） | 【已查证】（葡/波多黎各修订见 JDM 2023） | 警觉 vigilance（≈理性）、推诿 buck-passing（≈依赖）、拖延 procrastination（≈回避）、过度警觉 hypervigilance（≈自发/焦虑性匆忙） | B | 🟡 | 与 GDMS 高度重合，**作为 F-DM 的并行效标**，不新增家族 |

---

## 2. 自然决策 NDM / 识别启动决策 RPD

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **RPD 模型**（情境识别匹配 + 诊断 + 行动心理模拟三分支） | Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press；原始 Klein, Calderwood & Clinton-Cirocco (1986/1989) 消防指挥官现场研究 | 【已查证】（gary-klein.com/rpd、WSU Patterson 2009 系统动力学建模 PDF 一致） | ①**经验式模式识别即选第一可行方案（非逐方案比较）=增量**；②**行动 course-of-action 心理模拟 =增量**（与 EFT 有邻接） | C（描述专家过程，无自陈量表；"靠经验一眼认出"从自由文本难判定，需领域专长上下文） | ❌（无文本侧入口，是过程理论非特质） | **不独立成族**。2 个构念并入 F-DM（标注为"专家直觉型决策"，与 heur-013 快速节俭启发、dp-007 直觉加工三角互证） |
| NDM 学科纲领 | Zsambok, C. E., & Klein, G. (Eds.) (1997). *Naturalistic Decision Making*. Erlbaum | 【一方称·教科书经典】 | 非实验室、时间压力、高风险、线索动态的决策生态 | — | — | 作为 F-DM 的适用边界说明（NDM 构念只在高 stakes 语境有效） |

---

## 3. 概率与统计思维 / 风险素养

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **自然频率改善贝叶斯推理** | Gigerenzer, G., & Hoffrage, U. (1995). *Psychological Review*, 102(4), 684–704 | 【已查证】（PMC6530428、PLOS 复证一致） | ①**频率格式推理能力（把概率转频次即顿悟）=增量（能力侧）**；②条件概率盲点（偏差侧） | B（LLM 可判文本中是否用"每 100 人里 X 个"而非"X%"；但真正测量要做题） | 🟡 | **并入 F10 认知能力**（与 abil-003 流体推理、abil-014 分析性思维倾向同列）；偏差侧已 heur-005 基础率忽视 |
| 元分析效应量 | McDowell, M., & Jacobs, A. M. (2017). *Behavior Research Methods*（自然频率把正确率从 4% 抬到 24%） | 【已查证】（Frontiers 2018 转引一致） | —（效应锚点） | — | — | 作为"统计素养"构念的效度锚 |
| **Berlin Numeracy Test（数值素养 4 题）** | Cokely, E. T., et al. (2012). *Judgment and Decision Making*, 7(1), 25–47 | 【一方称·教科书经典】 | **统计/数值能力（numeracy）=增量** | C（是纸笔/施测题，非自由文本；文本侧只能 LLM 间接推断） | 🟡（中文 numeracy 修订版存在） | F10 认知能力的窄域能力增量 |
| **Quick Risk Test（极简医学统计素养 6 题）** | Jenny, M. A., Keller, N., & Gigerenzer, G. (2018). *BMJ Open*, 8, e020847 | 【已查证】（PMC6112405） | 同上（短版效标） | C | 🟡 | 同上 |

---

## 4. 风险感知与风险偏好

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **心理测量范式（dread risk × unknown risk 两主维）** | Slovic, P. (1987). *Science*, 236(4799), 280–285；Fischhoff, Slovic, Lichtenstein, Read & Combs (1978) | 【已查证】（informationr 转引一致；dread=失控/灾难性/致命，unknown=不可观察/未知/新发/迟发） | ①**dread 风险敏感 =增量**；②**unknown 风险敏感 =增量**（偏情境/ hazard 评级，非稳定特质） | C（让人对各类 hazard 打分，是情境量表；自由文本里只能捕到"我最怕/我不敢碰"类情绪语言） | 🟡 | 情境维度，**弱并入 F-DM 作为风险感知子轴**，不独立 |
| **DOSPERT 领域特异风险寻求-规避**（5 域：财务/健康安全/娱乐/职业/社会） | Weber, E. U., Blais, A.-R., & Betz, N. E. (2002)；Blais, A.-R., & Weber, E. U. (2006). *Judgment and Decision Making*, 1(2), 233–239（修订短版） | 【已查证】（Cambridge/JDM、Columbia 商院页面一致） | ①**领域特异风险寻求 =增量**；②**风险感知-风险回报双因子 =增量**（v1 只有 heur-007 损失厌恶这一个风险构念） | B（DOSPERT 是自陈行为倾向；LLM 可从"我愿意尝试高风险投资/我从不冒险"判定） | ✅（中文 DOSPERT 修订版多篇） | **并入 F-DM 决策族**，与 GDMS 同族；损失厌恶 heur-007 去重 |
| 跨期风险 / 风险寻求-规避连续谱 | （与 #9 延迟折扣交叠；Loewenstein, Weber, Hsee & Welch 2001 风险即情绪） | 【一方称·教科书经典】 | 情感性风险直觉 | B | 🟡 | F-DM 子轴，不另立 |

---

## 5. 框架与语境效应

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **亚洲疾病问题（risky choice framing）** | Tversky, A., & Kahneman, D. (1981). *Science*, 211(4481), 453–458 | 【已查证】（UCSD SHERMCKENZIE 综述 PDF、多源一致；gain 框架 72% 选确定项，loss 框架反转） | 框架效应 → **已有 heur-010（重复）** | C（测"一个人是否易被框架翻转"要做被试间实验；自由文本只能测"他用了什么框架语言"） | 🟡 | **重复，并入 heur-010**；不新增家族 |
| **框架三型细分（risky choice / attribute / goal framing）** | Levin, I. P., Schneider, S. L., & Gaeth, G. J. (1998). *Organizational Behavior and Human Decision Processes*, 76(2), 141–188 | 【已查证】（多源转引一致；attribute=存活率 90% vs 死亡率 10%；goal=不节能损失 vs 节能收益） | ①属性框架（正向/负向描述）= heur-010 细分；②目标框架（损失框 vs 收益框说服）= heur-010 细分 | B（文本侧：LLM 可判一段论述用了收益框还是损失框） | 🟡 | **作为 heur-010 的二级子类编码**，不单列家族 |

---

## 6. 反事实与假设思维

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **反事实思维综述（functional theory；upward/downward）** | Roese, N. J. (1997). *Psychological Bulletin*, 121(1), 133–148；Roese & Olson (1995) | 【已查证】（PMC2408534、PhilPapers 章节一致） | ①**向上反事实（要是当时再好一点=更好结果）=增量（v1 空白）**；②**向下反事实（至少没更糟=安慰）=增量**；③反事实→因果推断→行为准备功能 =增量 | A（语言标记极强：英文 "if only / would have / at least"；中文"要是…就好了/早知道/至少还没…"可直接词表+嵌入判定） | ✅（中文反事实标记丰富，C-LIWC 有相应语法探测；人工编码协议可移植） | **独立成族 F-CF**。v1 完全没有反事实构念，文本可计算性最高的一支 |
| **后悔理论（regret = 实际结果 vs 反事实结果之差）** | Loomes, G., & Sugden, R. (1982). *Economic Journal*, 92(368), 805–824；Bell, D. E. (1982) | 【已查证】（Coricelli 2009 转引一致） | **决策后后悔 / 预期后悔 =增量** | A/B（"后悔/早知道/当初就不该"直接可测；预期后悔需 LLM 自举） | ✅ | **并入 F-CF**（后悔是反事实的情绪面） |
| **假设思维（hypothetical thinking / 可能性表征）** | Evans, J. St. B. T., & Over, D. E. (2004). *If*. Oxford UP | 【一方称·教科书经典】 | 条件句/可能性思维 → 与 abs-005 假设性距离抽象部分重叠 | B | 🟡 | 部分已有 abs-005；剩余并入 F-CF |

---

## 7. 未来思维 / 情景预见 EFT

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **Episodic Future Thinking（情景未来思维）** | Atance, C. M., & O'Neill, D. K. (2001). *Trends in Cognitive Sciences*, 5(12), 533–539. DOI:10.1016/S1364-6613(00)01804-0 | 【已查证】（PMC2429996、Frontiers 2015 转引一致） | **情景式预演未来事件的细节/生动性 =增量**（与 nar-012 future-script 部分重叠：后者是叙事脚本，EFT 是感知细节） | B（EFT 范式让人想象未来事件并编码细节数——这恰恰是可对文本做的事：LLM 数"未来叙事里感官/场景细节密度"） | 🟡 | **并入 F-TP 时间视角族**；与 nar-012 去重，留"细节密度"这一增量 |
| **心理时间旅行 / 建构性情景模拟** | Suddendorf, T., & Corballis, M. C. (2007). *Behavioral and Brain Sciences*, 30(3), 299–351；Schacter & Addis (2007) 建构性情景模拟假说 | 【已查证】（UCSD PDF、Harvard Schacter 站点一致） | ①前瞻 prospection（自传记忆→未来投射）=增量；②场景建构 =邻接 EFT | B | 🟡 | F-TP 子轴，不独立 |

---

## 8. 时间视角 ZTPI

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **Zimbardo Time Perspective Inventory (ZTPI)**，56 题 5 维 | Zimbardo, P. G., & Boyd, J. N. (1999). *Journal of Personality and Social Psychology*, 77(6), 1271–1288 | 【已查证】（Redalyc、PMC10482053 一致：56 题、5 点 Likert、5 维） | ①**过去消极（aversive past）=增量**；②**过去积极（怀旧/温暖过去）=增量**；③**现在享乐（present hedonistic）=增量**；④**现在宿命（present fatalistic）=增量**；⑤**未来导向（future）=增量**（与 nar-012 future-script、#7 EFT 三角邻接） | B（LLM 从叙事语言判时间取向：怀旧词、及时行乐词、"听天由命"、"按计划推进"；无现成中文思维词表需自建） | ✅（中文修订版存在：西南大学 ZTPI 聚类分析、Lyu 中文简版见 Frontiers 2021） | **独立成族 F-TP 主干**。信度 α=.619–.770（2021 系统综述 ZTPI-56）【已查证】 |
| 平衡时间视角 BTP / DBTP | Stolarski et al. (2011)；Boniwell et al. (2010) 聚类 | 【已查证】（PMC11169753） | **平衡时间视角（五维配比而非单维）=增量** | B | 🟡 | F-TP 的整合指标 |

---

## 9. 延迟折扣 / 跨期选择

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念 | 可计算性 | 中文适用性 | 与 12 家族关系 |
|---|---|---|---|---|---|---|
| **Monetary Choice Questionnaire（27 题 SS/LL 选择）** | Kirby, K. N., Petry, N. M., & Bickel, W. K. (1999). *Journal of Experimental Psychology: General*, 128(1), 78–87 | 【已查证】（心理学报转引、PhenX、PMC8818853 一致：27 题、即时小额 vs 延迟大额） | **延迟折扣率（ impatience / 现在偏差）=增量** | C（是二择一行为选择任务，靠算 k 值；自由文本无直接入口，只能捕"及时行乐/等不及"语言代理） | 🟡（中文跨期决策实验范式成熟，无文本词表） | **并入 F-TP 时间视角族**（现在宿命/现在享乐维的经济行为面），不独立 |
| **Picoeconomics / 双曲折扣** | Ainslie, G. (1975/1992/2001)；Laibson (1997) present bias | 【已查证】（picoeconomics.org、PMC10489299） | ①双曲折扣偏好反转 =理论；②现在偏差 present bias =增量 | C | 🟡 | F-TP 理论注脚 |
| 神经机制（PDC 主观价值） | Kable, J. W., & Glimcher, P. W. (2007/2009). *Nature Neuroscience* / *J Neurophysiol* | 【已查证】（J Neurophysiol 2009 "ASAP effect"） | 非文本构念（神经相关物） | C | — | 不进文本 Atlas，仅背景 |

---

## 10. 扫描中发现的补充方向（集群内）

| 补充构念 | 出处 | 证据 | 建议落点 |
|---|---|---|---|
| **决策回避 / 不行动心理学**（deferring / delegating / ignoring；omission bias） | Anderson, C. J. (2003). *Psychological Bulletin*, 129(1), 139–167. DOI:10.1037/0033-2909.129.1.139 | 【已查证】（SE Oklahoma 全文 PDF） | 并入 F-DM（与 GDMS 回避风格、MDMQ procrastination 同族） |
| **最优化 vs 满意化（maximizing vs satisficing）** | Schwartz, B., et al. (2002). *JPSP*, 83(5), 1178–1197 | 【已查证】（ECNU 心理科学期刊转引一致；最优化与后悔/完美主义正相关） | 并入 F-DM（决策搜索策略轴）；上海华东师大学报已有中文中介研究 |
| **过度自信的元认知面 / 信心校准** | v1 已有 heur-009 过度自信、meta-011 信心与校准 | 对照索引已确认 | **不新增**，避免与 v1 重复 |
| **意图性决策 / 实施意向（implementation intentions）** | Gollwitzer (1999). *American Psychologist* | 【一方称·教科书经典】 | 邻接 F-TP（未来导向→行动执行），可作 F-TP 边缘构念 B 级 |
| **预测误差 / 信念更新** | 邻接 dp-010 信念修正倾向 | 对照索引已确认 dp-010 | **不新增** |

---

## 11. 与 v1 175 构念的精确去重对照（关键 id 回指）

- heur-005 基础率忽视 ↔ #3 概率统计思维（偏差侧已有，能力侧才增量）
- heur-007 损失厌恶 ↔ #4 风险偏好（部分重叠）
- heur-010 框架效应 ↔ #5 全部（重复，仅细分三型）
- heur-012 现状偏差 ↔ #10 决策回避/omission bias（邻接）
- heur-013 快速节俭启发 ↔ #2 NDM RPD（理论邻接）
- dp-007 直觉加工 / dp-008 分析加工 / cgs-009 直觉-分析 CSI ↔ #1 理性/直觉风格（重叠，去重）
- cgs-012 冲动-反思 ↔ #1 spontaneous 风格（部分重叠）
- abs-003 时间距离抽象 / abs-005 假设性距离 / abs-011 心理距离 ↔ #7 EFT、#6 假设思维（邻接）
- nar-012 未来脚本 future-script ↔ #8 ZTPI 未来维、#7 EFT（邻接，需明确切分：nar-012=叙事脚本内容，F-TP=时间取向情感态度）

---

*扫描完成。9 个指定方向全部评估；建议 v2 新增 F-DM / F-TP / F-CF 三族，概率统计素养并入 F10，框架效应并入 heur-010 细分，NDM 不独立。*
