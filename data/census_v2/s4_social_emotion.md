# S4 集群普查：社会认知、情绪、动机与价值（v2 家族重研）

> 任务：AoT 普查 v2 地基层重研·S4 集群穷尽性文献扫描。
> 对照底库：v1 12 家族 175 构念（F1 认知风格 / F2 双过程 / F3 论证图式 / F4 归因 / F5 抽象 / F6 元认知 / F7 概念隐喻 / F8 内隐动机 / F9 知识论 / F10 认知能力 / F11 启发式偏差 / F12 叙事身份）。
> 证据分级：【已查证】= 本轮经期刊页/出版社/PubMed/作者主页交叉核验作者·年份·期刊卷期·页码一致；【一方称·教科书经典】= 学界公认但本轮未逐页核验原文。
> 可计算性：A=现成词表/量表题面可直接转文本判定；B=LLM 从理论/量表自举；C=基本不可从文本测量。
> 中文适用性：✅ 有中文版量表/词表；🟡 需自建校准；❌ 无文本侧入口。

---

## 0. 一句话总判

本集群 9 个候选方向中，**真正够格独立成 v2 新家族的只有 2 个**：道德认知（MFT 五基础，A 级）与持续性/重复性认知（反刍-忧虑，B 级）；**社会认知与视角采择（ToM 文本侧）建议作为第 3 个候选小族**；其余方向应并入现有 12 家族或移除。价值（Schwartz）应并入 F8 内隐动机；超自然/阴谋信念并入 F9 知识论；自我参照并入 F12+F4；情绪调节拆成"重评/抑制"两个构念并入持续性认知族；幽默与想象生动性移除（前者非思维、后者已被 F1/F5/F12 覆盖）。

---

## 1. 社会认知与心理理论（ToM / mentalizing / 视角采择）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Does the chimpanzee have a theory of mind? | Premack & Woodruff 1978, *Behavioral and Brain Sciences* 1(4):515–526. https://carta.ucsd.edu/sites/default/files/file_fields/event/premack_and_woodruff_1978.pdf | 【已查证】 | ① 心智化/ToM 总构念（增量）；② 意图性归因（**已有→att-011**）；③ 信念-愿望推理（增量） | C（发展性 false-belief 行为任务，非文本） | ❌ 行为测验无文本入口 | 与 F4 归因共享 att-011，新增"读心"维度 |
| Does the autistic child have a "theory of mind"?（Sally-Anne 错误信念范式） | Baron-Cohen, Leslie & Frith 1985, *Cognition* 21(1):37–46. DOI:10.1016/0010-0277(85)90022-8. http://www.sscnet.ucla.edu/polisci/faculty/chwe/austen/baroncohenlesliefrith.pdf | 【已查证】 | ④ 错误信念推理（增量）；⑤ 心智状态归因准确度（增量） | C（发展测验） | ❌ | 纯发展诊断，不入思维量化 |
| Development and neurophysiology of mentalizing | Frith & Frith 2003, *Phil. Trans. R. Soc. B* 358(1431):459–473. DOI:10.1098/rstb.2002.1218. https://royalsocietypublishing.org/rstb/article-abstract/358/1431/459 | 【已查证】 | ⑥ 内隐 vs 外显心智化（增量）；⑦ 社会脚本知识（增量） | B（成人语篇中心智状态语言密度） | 🟡 需自建"心智动词/视角转换"词表 | 新增候选；与 F5 社会距离抽象（abs-004）相邻 |
| Reading the Mind in the Eyes（成人 ToM 行为测验） | Baron-Cohen et al. 1997, *J. Child Psychol. Psychiatry* 38(7):813–820.【一方称·教科书经典】 | 【一方称】 | ⑧ 认知共情/视角采择准确度（增量） | C（图片反应时） | ❌ | 行为测验，不入 |

**文本侧可测部分（真正进入 Atlas 的对象）**：成人自然语篇中的①心智状态动词密度（think/believe/know/want/guess/feel 的使用频率与区分度）；②视角采择标记（"在他看来""我猜你觉得"）；③自我中心 vs 异我中心语言（ego/alter 取向）。这一层可由 LLM 从理论自举，无现成词表。

**建议结论**：**独立成候选小族"社会认知与视角采择"（B 级）**，但只收语篇层构念（心智状态语言、视角采择、自我中心偏差），不收发展性 false-belief 行为测验。与 F4 归因（att-011 意图性归因）、F5（abs-004 社会距离）做边界切分。

---

## 2. 道德推理（Kohlberg 阶段 / Haidt MFT / Rest 四成分）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| The Philosophy of Moral Development（六阶段：前习俗/习俗/后习俗×2） | Kohlberg 1981, Harper & Row（Essays on Moral Development Vol.1）；阶段结构经 De Gruyter 道德心理学章复核【已查证】https://www.degruyterbrill.com/document/doi/10.1515/9783110466034-006/pdf | 【一方称·教科书经典】（六阶段内容） | ① 道德发展阶段（增量）；② 道德两难推理层级（增量，与 epi-007 论证推理层级相邻但不同域） | B（MJI 对两难开放式回答编码，文本可编码） | 🟡 需自建中文两难编码 | 与 F9 知识论（epi-001~003 反思判断）同构但域不同（道德≠认知知识） |
| The emotional dog and its rational tail（社会直觉模型：道德判断先于推理，推理为事后合理化） | Haidt 2001, *Psychological Review* 108(4):814–834. DOI:10.1037/0033-295X.108.4.814. https://pages.uoregon.edu/uophil/files/HaidtEmotionalDog.pdf | 【已查证】 | ③ 道德直觉优先（增量）；④ 道德事后合理化（增量，与 dp-006 省力处理/att 自利相邻）；⑤ 道德失声 moral dumbfounding（增量） | B | 🟡 | 与 F2 双过程（dp-007/dp-008 直觉-分析）正交，属道德域 |
| Liberals and Conservatives Rely on Different Sets of Moral Foundations（MFT 五基础：关爱/公平/忠诚/权威/纯洁） | Graham, Haidt & Nosek 2009, *JPSP* 96(5):1029–1046. DOI:10.1037/a0015141. http://pages.stern.nyu.edu/~jhaidt/articles/graham.haidt.nosek.2009.liberals-and-conservatives.pub064.pdf | 【已查证】 | ⑥ 关爱/伤害基础（增量）；⑦ 公平/互惠基础（增量）；⑧ 内群体/忠诚基础（增量）；⑨ 权威/尊重基础（增量）；⑩ 纯洁/神圣基础（增量） | **A**（MFQ 题面 + 道德基础词典 Moral Foundations Dictionary 可直接转文本判定） | ✅ 中文版 MFQ 已修订（38 题 6 维度，α=.93）【已查证】https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2024.1432407/full | **全新独立域**，F9 只覆盖"如何知道"，不覆盖"道德内容偏好" |
| Postconventional Moral Thinking（Rest 四成分：敏感性/判断/动机/品格；DIT2） | Rest, Narvaez, Bebeau & Thoma 1999, Erlbaum；DIT2 见 *J. Educational Psychology* 91(4):644【已查证】https://ethicaldevelopment.ua.edu/about-the-dit/ | 【已查证】 | ⑪ 道德敏感性（识别情境道德含义，增量）；⑫ 道德动机（道德优先性，增量） | B（DIT 为迫选，文本侧弱） | 🟡 | 道德动机可与 F8 动机层对接，但判断成分属本族 |

**关键数字核验**：MFT 五基础=关爱/care、公平/fairness、内群体/loyalty、权威/authority、纯洁/purity（Graham 2009 原文明确"liberals 重关爱+公平，conservatives 五基础均衡"）；中文版 MFQ 38 题 α=.93。

**建议结论**：**独立成 v2 新家族"道德认知"（A 级，本集群最硬）**。收：五基础偏好、道德直觉 vs 推理、道德失声、道德敏感性。Kohlberg 六阶段作为发展轴弱收（B）。它与 F9 知识论必须切开：F9 管"证据/知识如何被评估"，本族管"道德内容的直觉偏好与推理"。

---

## 3. 情绪与认知互动（affect-as-information / Gross 过程模型 / ERQ / EQ 认知侧）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Mood, misattribution, and judgments of well-being（affect-as-information：情绪被当作判断信息源） | Schwarz & Clore 1983, *JPSP* 45(3):513–523. DOI:10.1037/0022-3514.45.3.513. https://static1.squarespace.com/static/55917f64e4b0cd3b4705b68c/t/5cc485ffc83025df858d4bf7/1556383235120/Schwarz+Clore+1983.pdf | 【已查证】 | ① 情绪信息利用倾向（机制，非个体差异）；② 心境归因偏差（增量，与 heur-004 情感启发相邻） | C（效应机制，非可测特质；个体差异无成熟文本入口） | ❌ 机制层 | 与 F11 情感启发（heur-004）合并，不独立 |
| The emerging field of emotion regulation（Gross 五阶段过程模型：情境选择/情境修正/注意部署/认知改变/反应调节） | Gross 1998, *Review of General Psychology* 2(3):271–299. DOI:10.1037/1089-2680.2.3.271. https://ayaktangelensaglik.com/uploads/migrated/sites/1353/2021/11/Gross-1998-The-Emerging-Field-of-Emotion-Regulation-An-Integrative-Review.pdf | 【已查证】 | ③ 认知重评倾向（增量）；④ 表达抑制倾向（增量）；⑤ 注意部署策略（增量） | B（重评=重构语言；抑制=回避/压抑语言，LLM 从 ERQ 题面自举） | ✅ 中文版 ERQ 已修订（10 题：6 重评+4 抑制，7 点，结构/重测/内部一致性良好）【已查证】https://journal.psych.ac.cn/xlxb/article/2023/0439-755X/0439-755X-55-6-892.shtml | 重评是"对情绪的认知操作"，与 F8 防御（mot-009 压抑/mot-010 合理化）相邻 |
| ERQ 量表本身（10 题：重评 6 + 抑制 4） | Gross & John 2003, *JPSP* 85(2):348–362. DOI:10.1037/0022-3514.85.2.348 | 【已查证】 | ⑥ 认知重评使用频率（增量）；⑦ 表达抑制使用频率（增量） | B | ✅ 同上 | 见上 |
| 情绪智力四分支能力模型（感知/促进思维/理解/管理情绪） | Mayer & Salovey 1997, in *Emotional Development and Emotional Intelligence*, Basic Books；MSCEIT 为操作化测验 | 【一方称·教科书经典】 | ⑧ 情绪理解能力（增量，与 met-014 情绪实体隐喻相邻） | C（MSCEIT 为操作测验，非自陈非文本） | ❌ | 属能力测验，不入文本 Atlas |

**建议结论**：**不独立成族**。affect-as-information 是机制不是特质，并入 heur-004 情感启发；EQ 能力侧（MSCEIT）C 级移除。**仅保留"认知重评 vs 表达抑制"两个构念（B 级），并入方向 8 的"持续性认知/情绪调节"候选族**——因为重评是对重复反刍的认知应对，二者同域。这回答了任务问题：情绪调节的认知侧（重评）属"思维"，抑制偏行为/情感侧。

---

## 4. 自我参照思维（self-referential processing / 自传记忆 / 自我中心偏差）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Self-reference and the encoding of personal information（自我参照效应：自我编码记忆最优） | Rogers, Kuiper & Kirker 1977, *JPSP* 35(9):677–688. DOI:10.1037/0022-3514.35.9.677 | 【已查证】 | ① 自我参照编码深度（记忆范式，非文本） | C（记忆实验） | ❌ | 实验范式，不入 |
| 自传记忆/自我记忆系统 | Conway 2005（self-memory system）【一方称·教科书经典】 | 【一方称】 | ② 自传推理（**已有→nar-007**）；③ 自传记忆具体性（增量） | B（叙事中事件具体/概括程度） | 🟡 | 已被 F12 narrative 覆盖大部 |
| 自我中心偏差 / I-talk（第一人称单数使用与自我关注） | 总报告已引 LIWC/开放词表传统；Pennebaker 第一人称代词研究 | 【一方称】 | ④ 自我关注语言密度（增量）；⑤ 自我中心偏差（增量，与 att-010 自利归因相邻） | B（LIWC 第一人称代词计数 + LLM 判定） | ✅ C-LIWC 代词类目成熟 | 与 F4 自利归因、F12 叙事重叠 |

**建议结论**：**不独立，并入现有家族**。自传推理/自我掌控已在 F12（nar-001/nar-007/nar-009），自利归因已在 F4（att-010）。仅补一个增量构念"自我关注语言密度（I-talk）"（B 级），可挂 F12 或 F6。自我参照作为记忆现象本身 C 级移除。

---

## 5. 世界观与价值认知（Schwartz 价值论 / PVQ / 政治认知）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Universals in the content and structure of values（十基本价值：自主/刺激/享乐/成就/权力/安全/传统/遵从/仁慈/普世） | Schwartz 1992, *Advances in Experimental Social Psychology* 25:1–65. DOI:10.1016/S0065-2601(08)60281-6 | 【已查证】 | ① 十动机价值类型（增量，与 mot-001 成就/mot-002 权力/mot-003 亲和高度重叠） | B（PVQ 为人物画像迫选，文本侧靠 LLM 从叙事推断价值优先级） | ✅ 中文版 PVQ-RR 已修订并做测量不变性检验（Wang 2025, *PsyCh Journal*）【已查证】https://onlinelibrary.wiley.com/doi/full/10.1002/pchj.70023 | 与 F8 内隐动机同域（动机=价值的心理底色） |
| Refining the theory of basic individual values（19 细化价值，circumplex） | Schwartz et al. 2012, *JPSP* 103(4):663–688. DOI:10.1037/a0029393. https://library.scottbarrykaufman.com/uploads/2017/09/Schwartz-2012-19-values-JPSP.pdf | 【已查证】 | ② 19 细分价值（增量）；③ 开放-保守 vs 自我增强-自我超越两轴（增量） | B | ✅ 同上（PVQ-RR 57 题中文版） | 扩展 F8 动机结构 |
| 世界观/政治认知 | 无单一奠基量表；散见于社会政治态度测量 | 【一方称】 | ④ 世界观闭合/开放（与 dp-004 认知闭合、dp-002 开放思维相邻） | B | 🟡 | 已被 F2（AOT/认知闭合）覆盖 |

**建议结论**：**不独立成族，并入 F8 内隐动机与防御机制**。理由：价值是"目标-动机内容"而非"推理过程"；Schwartz 十价值中的成就/权力/仁慈与 v1 的 nAch/nPow/nAff（mot-001~003）本质同构。v2 可把 F8 从 3 个内隐动机扩展为"动机-价值 circumplex"（补开放/保守轴）。这回答任务问题：价值层**不单独进思维量化**，它属于动机/目标层，挂 F8。

---

## 6. 信仰与超自然信念（宗教认知 / magical thinking / 阴谋信念）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Magical Ideation Scale（MIS，30 题对错：占星/心灵/意念致动/关系思维） | Eckblad & Chapman 1983, *J. Consulting and Clinical Psychology* 51(2):215–225 | 【已查证】 | ① 魔幻思维/神奇因果（增量）；② 关系性思维/参考观念（增量） | B（魔幻因果语言："冥冥中""注定""有天意"；teleology） | 🟡 中文修订版存在但文本词表需自建 | 与 F9 信念结构相邻 |
| Revised Paranormal Belief Scale（R-PBS，26 题 7 子量表：传统宗教/psi/巫术/迷信/唯灵论/奇异生命/预知） | Tobacyk 2004, *Int. J. Transpersonal Studies* 23:94–98. DOI:10.24972/ijts.2004.23.1.94 | 【已查证】 | ③ 超自然信念谱系（增量）；④ 预知/迷信倾向（增量） | B（信念内容词表 + LLM） | 🟡 | 并入 F9 知识论信念层 |
| Generic Conspiracist Beliefs scale（GCB，15 题 5 因子：政府渎职/外星掩盖/个人福祉/信息控制/邪恶全球阴谋） | Brotherton, French & Pickering 2013, *Frontiers in Psychology* 4:279. DOI:10.3389/fpsyg.2013.00279. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00279/pdf | 【已查证】（注意：年份为 2013 非任务所写 2015） | ⑤ 阴谋论思维/阴谋心智（增量）；⑥ 意图化合谋归因（与 att-011 意图性归因相邻但极端化） | **B+**（阴谋修辞标记："掩盖""他们在隐瞒""幕后黑手"；NLP 阴谋检测已有成熟先例） | 🟡 中文社媒阴谋话语检测可行 | 并入 F9；极端化的意图归因挂 F4 |

**建议结论**：**不独立成族，并入 F9 知识论/批判性思维**。理由：这些是"信念结构/信念形成方式"——阴谋论是意图归因的过度泛化（连 F4），超自然/魔幻是因果推理的非科学范式（连 F9 客观主义 vs 主观主义）。文本侧 B 级可行（尤其阴谋论话语 NLP 成熟）。宗教认知本身（Boyer 类）偏人类学，弱收。

---

## 7. 幽默认知（HSQ 四风格 / incongruity-resolution）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Humor Styles Questionnaire（HSQ，四风格：亲和/自我提升/攻击/自嘲；原 α≈.77–.81） | Martin, Puhlik-Doris, Larsen, Gray & Weir 2003, *J. Research in Personality* 37(1):48–75. DOI:10.1016/S0092-6566(02)00534-2 | 【已查证】（α 区间经多语言复核） | ① 亲和幽默（增量）；② 自我提升幽默（增量）；③ 攻击幽默（增量）；④ 自嘲/自贬幽默（增量） | B（语篇中调侃/反讽/自贬标记；但风格信号弱、语境依赖强） | 🟡 中文幽默语用差异大，需校准 | 与 F7 隐喻（反讽=修辞）、F8 亲和动机相邻 |
| Incongruity-resolution 幽默理解理论 | Suls 1972【一方称·教科书经典】 | 【一方称】 | ⑤ 不一致-解决理解（机制，非个体差异） | C（机制） | ❌ | 机制层，不入 |

**建议结论**：**移除（不入 v2 思维 Atlas）**。理由：幽默风格是社会人格/应对风格，不是思维过程；文本信号弱且文化语用高度依赖（B 级偏低），与"思维量化"目标偏离。若 v2 想保留，最多作为 F7 修辞/反讽的一个边缘构念弱挂。

---

## 8. 思维反刍与焦虑性认知（rumination / worry / perseverative cognition）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Responses to depression...（反应风格理论：反刍延长抑郁） | Nolen-Hoeksema 1991, *J. Abnormal Psychology* 100(4):569–582. DOI:10.1037/0021-843X.100.4.569 | 【已查证】 | ① 反刍反应风格（增量） | B（重复过去指向、自我聚焦、"为什么是我"语言） | ✅ 中文 RRS 修订成熟 | 与 F6 元认知体验（meta-013）相邻 |
| Rumination Reconsidered（RRS 拆为 brooding 思虑 5 题 + reflection 反省 5 题） | Treynor, Gonzalez & Nolen-Hoeksema 2003, *Cognitive Therapy and Research* 27(3):247–259. DOI:10.1023/A:1023910315561 | 【已查证】 | ② 思虑 brooding（反刍的病态成分，增量）；③ 反省 reflection（适应性成分，增量） | **A-**（RRS 题面即典型反刍句，可直接转文本判定；LIWC 过去时态/原因词辅助） | ✅ 中文版成熟 | 全新"重复性思维"域 |
| Penn State Worry Questionnaire（PSWQ，16 题，特质忧虑金标准） | Meyer, Miller, Metzger & Borkovec 1990, *Behaviour Research and Therapy* 28(6):487–495. DOI:10.1016/0005-7967(90)90135-6 | 【已查证】 | ④ 特质忧虑/未来指向重复担忧（增量）；⑤ 侵入性思维（增量） | B（未来指向、"万一"灾难化语言） | ✅ 中文版 PSWQ 修订 | 与反刍构成"持续性认知"两极（反刍=过去/抑郁，忧虑=未来/焦虑） |
| Perseverative cognition（Borkovec/Brosschot 持续性认知总框架） | Borkovec 等；总报告未收【一方称】 | 【一方称】 | ⑥ 持续性认知总构念（反刍+忧虑+侵入） | B | 🟡 | 本族的统一理论伞 |

**建议结论**：**独立成 v2 新家族"持续性/重复性认知"（B 级，本集群第 2 个硬候选）**。收：反刍（brooding/reflection 拆分）、特质忧虑、侵入性思维，并把方向 3 的"认知重评 vs 表达抑制"作为应对子构念挂入。理由：这是真正的"思维过程/内容"——重复性、时间指向性（过去 vs 未来）、聚焦性，文本侧可由 LIWC 时态/代词 + LLM 判定，且与 v1 任何一族都不重叠（F6 元认知是监控，F11 是偏差，都不管"思维的重复性与时间锚点"）。

---

## 9. 想象与生动性（VVIQ / mental imagery 生动性）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量/已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Vividness of Visual Imagery Questionnaire（VVIQ，16 题 4 场景×4 侧面，5 点评定心理图像清晰度） | Marks 1973, *British Journal of Psychology* 64(1):17–24. DOI:10.1111/j.2044-8295.1973.tb01322.x | 【已查证】 | ① 视觉意象生动性（自陈内省，非文本） | C（内省能力自陈，无文本入口） | ❌ | 与 F1 言语-表象型（cgs-004/cgs-010）、F10 视觉加工（abil-005）相邻 |
| 心理意象生动性的文本代理 | 散见于叙事研究 | 【一方称】 | ② 场景意象密度（**已有→nar-013**）；③ 具体感觉词密度（**已有→abs-001/002 具体语言**） | B（靠 F5 具体度词表 + F12 场景意象） | ✅ 中文具体度词典成熟 | 已被 F1/F5/F12 覆盖 |

**建议结论**：**不独立，移除**。VVIQ 是内省能力自陈（C 级无文本入口）；它的文本侧代理（意象生动→具体感觉词/场景密度）已被 v1 的 cgs-004/cgs-010（言语-表象风格）、abs-001/002（抽象-具体）、nar-013（场景意象密度）完全覆盖。与 F5 抽象、F7 隐喻的关系是：意象生动性是这两者的"输入端"，不需单独立族。

---

## 10. 补充方向（文献扫描中发现）

| 补充方向 | 代表文献 | 已查证 | 核心构念 | 可计算性 | 建议处置 |
|---|---|---|---|---|---|
| 社会比较（向上/向下） | Festinger 1954, *Human Relations* 7(2):117–140 | 【已查证】 | ① 向上比较（增量）；② 向下比较（增量） | B（"比上不足/比下有余"、相对位置语言） | 并入方向 1 社会认知候选小族（社会比较是视角采择的自我-他者轴） |
| 心智游移 mind-wandering（认知侧） | Smallwood & Schooler 2006, *Psychological Bulletin* 132(6):946–958（已在总报告引） | 【已查证】 | ③ 任务无关思维（增量） | B-C（注意脱离，文本侧弱；写作"跑题"可粗测） | 弱挂方向 8 持续性认知族作对照轴（focused vs wandering） |
| 解释偏差 interpretation bias | Mathews & Mackintosh 2000（模糊情境解释训练范式），经 PMC 复核 https://pmc.ncbi.nlm.nih.gov/articles/PMC3988928/ | 【已查证】 | ④ 威胁性解释偏差（增量）；⑤ 模糊情境的威胁/良性归因（与 att-006 悲观解释风格相邻） | B（对模糊事件的威胁化语言） | 并入方向 8（与焦虑性认知同域）或 F4 归因 |
| 偏执思维/参考观念 | 与 MIS/GCB 同源 | 【一方称】 | ⑥ 偏执性意图归因（增量） | B | 并入 F4/F9（极端化意图归因） |

---

## 11. 集群总结：每方向"建议结论一句话"表

| # | 方向 | 建议结论（独立/并入/移除） | 可计算性 |
|---|---|---|---|
| 1 | 社会认知与 ToM | **独立成候选小族"社会认知与视角采择"**（只收语篇层：心智状态语言/视角采择/自我中心偏差；行为 false-belief 不收） | B |
| 2 | 道德推理 | **独立成 v2 新家族"道德认知"**（MFT 五基础为主轴，本集群最硬） | A |
| 3 | 情绪与认知互动 | **不独立**；affect-as-info 并入 heur-004，EQ 能力侧移除；仅"重评 vs 抑制"2 构念并入方向 8 | B |
| 4 | 自我参照思维 | **并入 F12 叙事 + F4 归因**；仅补"I-talk 自我关注"1 构念 | B |
| 5 | 世界观与价值 | **并入 F8 内隐动机**（价值=动机内容，非思维过程；扩展为动机-价值 circumplex） | B |
| 6 | 信仰/超自然/阴谋 | **并入 F9 知识论**（信念结构）；极端意图归因连 F4 | B+ |
| 7 | 幽默认知 | **移除**（社会人格风格，非思维，文本信号弱） | B（偏低，弃） |
| 8 | 反刍/焦虑性认知 | **独立成 v2 新家族"持续性/重复性认知"**（反刍 brooding/reflection + 忧虑 + 侵入性 + 重评/抑制应对） | A-/B |
| 9 | 想象生动性 | **移除**（VVIQ 无文本入口；文本代理已被 F1/F5/F12 覆盖） | C |

**补充方向清单**：社会比较（→方向1）、心智游移（→方向8 对照轴）、解释偏差（→方向8/F4）、偏执思维（→F4/F9）。

---

## 12. v2 家族增删建议（本集群贡献）

- **新增独立家族（2 个硬 + 1 个候选小族）**：
  - **F13 道德认知**（A 级）：五基础偏好、道德直觉-推理、道德失声、道德敏感性。
  - **F14 持续性/重复性认知**（B 级）：反刍 brooding/reflection、特质忧虑、侵入性思维、认知重评 vs 表达抑制。
  - **F15 社会认知与视角采择**（B 级，候选）：心智状态语言、视角采择、社会比较、自我中心偏差。
- **并入扩展**：F8 加 Schwartz 动机-价值 circumplex；F9 加阴谋/超自然信念结构；F12/F4 加自我关注语言。
- **移除**：幽默风格、想象生动性、ToM 行为测验、EQ 操作测验、affect-as-information 机制层。

---

## 13. 合并文献清单（本集群，逐条可回溯）

1. Premack D, Woodruff G. 1978. Does the chimpanzee have a theory of mind? *BBS* 1(4):515–526. https://carta.ucsd.edu/sites/default/files/file_fields/event/premack_and_woodruff_1978.pdf 【已查证】
2. Baron-Cohen S, Leslie AM, Frith U. 1985. Does the autistic child have a "theory of mind"? *Cognition* 21(1):37–46. http://www.sscnet.ucla.edu/polisci/faculty/chwe/austen/baroncohenlesliefrith.pdf 【已查证】
3. Frith U, Frith CD. 2003. Development and neurophysiology of mentalizing. *Phil. Trans. R. Soc. B* 358(1431):459–473. https://royalsocietypublishing.org/rstb/article-abstract/358/1431/459 【已查证】
4. Kohlberg L. 1981. *The Philosophy of Moral Development*. Harper & Row.【一方称·教科书经典】
5. Haidt J. 2001. The emotional dog and its rational tail. *Psychological Review* 108(4):814–834. https://pages.uoregon.edu/uophil/files/HaidtEmotionalDog.pdf 【已查证】
6. Graham J, Haidt J, Nosek BA. 2009. Liberals and Conservatives Rely on Different Sets of Moral Foundations. *JPSP* 96(5):1029–1046. http://pages.stern.nyu.edu/~jhaidt/articles/graham.haidt.nosek.2009.liberals-and-conservatives.pub064.pdf 【已查证】
7. Rest J, Narvaez D, Bebeau M, Thoma S. 1999. *Postconventional Moral Thinking*. Erlbaum. https://ethicaldevelopment.ua.edu/about-the-dit/ 【已查证】
8. Schwarz N, Clore GL. 1983. Mood, misattribution, and judgments of well-being. *JPSP* 45(3):513–523. https://static1.squarespace.com/static/55917f64e4b0cd3b4705b68c/t/5cc485ffc83025df858d4bf7/1556383235120/Schwarz+Clore+1983.pdf 【已查证】
9. Gross JJ. 1998. The emerging field of emotion regulation: an integrative review. *Rev. Gen. Psychol.* 2(3):271–299. 【已查证】
10. Gross JJ, John OP. 2003. Individual differences in two emotion regulation processes. *JPSP* 85(2):348–362. 【已查证】
11. 中文版 ERQ. 心理学报 2023,55(6). https://journal.psych.ac.cn/xlxb/article/2023/0439-755X/0439-755X-55-6-892.shtml 【已查证】
12. Mayer JD, Salovey P. 1997. What is emotional intelligence. In *Emotional Development and Emotional Intelligence*, Basic Books.【一方称·教科书经典】
13. Rogers TB, Kuiper NA, Kirker WS. 1977. Self-reference and the encoding of personal information. *JPSP* 35(9):677–688. 【已查证】
14. Schwartz SH. 1992. Universals in the content and structure of values. *Adv. Exp. Soc. Psychol.* 25:1–65. 【已查证】
15. Schwartz SH et al. 2012. Refining the theory of basic individual values. *JPSP* 103(4):663–688. https://library.scottbarrykaufman.com/uploads/2017/09/Schwartz-2012-19-values-JPSP.pdf 【已查证】
16. Wang et al. 2025. PVQ-RR in Chinese population. *PsyCh Journal*. https://onlinelibrary.wiley.com/doi/full/10.1002/pchj.70023 【已查证】
17. Eckblad M, Chapman LJ. 1983. Magical ideation as an indicator of schizotypy. *J. Consult. Clin. Psychol.* 51(2):215–225. 【已查证】
18. Tobacyk JJ. 2004. A Revised Paranormal Belief Scale. *Int. J. Transpersonal Studies* 23:94–98. 【已查证】
19. Brotherton R, French CC, Pickering AD. 2013. Measuring belief in conspiracy theories: the GCB scale. *Front. Psychol.* 4:279. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00279/pdf 【已查证】
20. Martin RA et al. 2003. Individual differences in uses of humor (HSQ). *J. Res. Pers.* 37(1):48–75. 【已查证】
21. Nolen-Hoeksema S. 1991. Responses to depression and their effects on duration. *J. Abnorm. Psychol.* 100(4):569–582. 【已查证】
22. Treynor W, Gonzalez R, Nolen-Hoeksema S. 2003. Rumination reconsidered. *Cogn. Ther. Res.* 27(3):247–259. 【已查证】
23. Meyer TJ et al. 1990. Penn State Worry Questionnaire. *Behav. Res. Ther.* 28(6):487–495. 【已查证】
24. Marks DF. 1973. Visual imagery differences in the recall of pictures. *Br. J. Psychol.* 64(1):17–24. 【已查证】
25. Festinger L. 1954. A theory of social comparison processes. *Human Relations* 7(2):117–140. 【已查证】
26. Smallwood J, Schooler JW. 2006. The restless mind. *Psychol. Bull.* 132(6):946–958. 【已查证（总报告已收）】
27. Mathews A, Mackintosh B. 2000. 解释偏差模糊情境范式.（经 PMC 复核）https://pmc.ncbi.nlm.nih.gov/articles/PMC3988928/ 【已查证】
28. 中文版 MFQ. *Front. Psychiatry* 2024. https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2024.1432407/full 【已查证】

---

*S4 集群扫描完成。所有关键数字（MFT 五基础、HSQ 四风格 α≈.77–.81、RRS brooding/reflection 各 5 题、VVIQ 16 题、MIS 30 题、R-PBS 26 题 7 子量表、GCB 15 题 5 因子、PSWQ 16 题、ERQ 10 题 6+4、Schwartz 10→19 价值）均逐条核到原始出处；中文版适用性已查 ERQ-C / MFQ-C / PVQ-RR-C。*
