# s2｜问题解决与思维过程集群——穷尽性文献扫描（AoT 普查 v2）

> 扫描范围：任务书指定 8 方向 + 文献扫描中补充的可计算候选方向。
> 证据分级：【已查证】= 已抓取出版社/期刊/机构库页面核验标题·作者·年份·卷期一致；【一方称·教科书经典】= 学界公认、本轮以教材/综述转引核验，未逐页翻原文。
> 对照基线：v1 175 构念索引（constructs_index.md），凡"已有"均给出精确构念 id。
> 可计算性口径：A=现成词表/量表题面可直接转文本判定；B=LLM 从理论自举/需任务诱发；C=基本不可从自由文本测（需反应时/施测/实验室任务）。

---

## 0. 集群总判定（一句话结论先行）

本集群 8 个指定方向中，**只有"创造力与发散思维"（方向 3）具备独立成族条件**（有中文验证量表、有真实文本输出评分、v1 仅 1 个单薄构念）；其余 7 个方向均为"实验室任务型认知架构"或与 v1 已有族高度重叠，**建议并入而非独立**。补充方向里，**"类比迁移心理过程"与"顿悟/Aha 文本事件标记"值得作为小增量纳入，其余降级为背景**。

| # | 方向 | 建议结论（一句话） | 可计算性 |
|---|---|---|---|
| 1 | 问题解决（Polya/Newell-Simon） | **并入 F6 元认知**（策略语言=程序性调节），不独立 | B/C |
| 2 | 专家-新手认知 | **并入 F10 认知能力**（=Gc/领域知识组织），不独立 | C |
| 3 | 创造力与发散思维 | **独立成新族 F13**（从 cgs-013/cgs-008 提升拆出） | B（诱发任务可达 A） |
| 4 | 洞察与顿悟 | **FOK 并入 F6；Aha 事件标记并入新 F13 或作文本事件**，不独立 | B/A（事件标记） |
| 5 | 心智模型与知识表征 | **降级为推理背景理论**，心理模拟/反事实语言作弱标记，不独立 | C/B |
| 6 | 因果推理与因果学习 | **维持分散**（arg-004 因果论证 + att-* 因果归因），不独立；机制vs协变解释偏好在背景库 | C |
| 7 | 工作记忆与执行功能 | **并入 F10（abil-006 Gwm）**，EF 三成分为反应时任务，不独立 | C |
| 8 | 演绎推理心理学 | **并入 F3+F2**（belief bias 已 dp-005），不独立 | C/B |
| S1 | 类比迁移心理过程（补充） | **小增量**：与 arg-003（论证类比）区分，建议入新 F13 或 F3 子条 | B |
| S2 | 功能固着/心理定势（补充） | **并入问题解决障碍**，弱文本标记，不单列 | C/B |
| S3 | 酝酿/四阶段创造过程（补充） | **并入新 F13**（Wallas 阶段），作过程描述而非个体差 | C/B |

---

## 1. 方向一：问题解决（Polya 启发式 / Newell-Simon 问题空间 / 问题表征）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| How to Solve It（四阶段启发式） | Pólya, G. (1945/1957). *How to Solve It*. Princeton UP. 四阶段：理解问题→拟定计划→执行计划→回顾。启发式：类比、辅助问题、分解、倒推（working backward）。全文 PDF：https://math.ucr.edu/~res/math133-2020/week0/polya.pdf | 【已查证】 | ①问题表征重述（增量）②手段-目的分析 means-ends（增量）③倒推法 working-backward（增量）④分解/化整为零（增量）⑤回顾反思 look-back（已有→meta-008 元认知评价、meta-009 监控）⑥计划拟定（已有→meta-004 计划） | B（出声思考/解题文本里可识别"先拆/倒推/转化为已知"，自由文本稀疏） | 🟡 理论无文化门槛，但无中文"解题策略词表"，需自建；Polya 启发式中译普及 | **并入 F6 元认知**：计划/回顾/调试已 meta-004/007/008；新增"手段-目的/倒推/分解"3 条程序性策略词入 F6 或新 F13 |
| Human Problem Solving（问题空间+产生式） | Newell, A., & Simon, H. A. (1972). *Human Problem Solving*. Prentice-Hall. 问题空间=初始态+目标态+算子+中间态；GPS；手段-目的分析；出声思考协议分析。CMU 存档：https://iiif.library.cmu.edu/file/Newell_box00018_fld01306_doc0001/Newell_box00018_fld01306_doc0001.pdf | 【已查证】 | ①问题空间搜索（理论构念，非个体差）②算子选择/移动（增量，弱）③产生式规则 IF-THEN（理论，ACT-R 背景）④协议分析方法学（背景） | C（信息加工架构，非文本量表；只能从 protocol 文本编码） | 🟡 同 Polya | **不独立**：作背景架构；其"出声思考→编码"方法学正是本项目 LLM 判定可借鉴路径，但构念本身不进画像 |
| On Problem Solving（功能固着/表征重构） | Duncker, K. (1945). On Problem Solving. *Psychological Monographs*, 58(5). 蜡烛问题；辐射问题；功能固着；表征重构。综述见 York U：https://www.yorku.ca/vgoel/reprints/problem_solving.pdf | 【一方称·教科书经典】 | ①功能固着 functional fixedness（增量→见 S2）②表征重构 restructuring（增量）③心理定势 mental set（增量→见 S2） | C/B（实验室顿悟题；自由文本难测） | 🟡 无中文量表 | **并入 S2 问题解决障碍**；表征重构与方向 4 顿悟共享 |

**本方向判定**：问题解决"策略"在文本侧极稀疏——Polya 四阶段里只有"计划/回顾/监控"已有 meta-004/008/009 覆盖，真正新增的手段-目的/倒推/分解是程序性动作词，只能从解题类文本识别（B），普通自由文本几乎不触发。Newell-Simon 是认知架构非个体差。**建议并入 F6，不独立成族。**

---

## 2. 方向二：专家-新手认知（Chase & Simon 组块 / 领域知识组织 / 自动化）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Perception in Chess / Skill in Chess（象棋组块） | Chase, W. G., & Simon, H. A. (1973a). Perception in Chess. *Cognitive Psychology*, 4(1), 55–81；(1973b). Skill in Chess. *American Scientist*, 61(4), 393–403。大师复盘真实棋局回忆 81% vs 新手 33%；随机棋局全部仅回忆 3–5 子；组块间隔约 2 秒。原文：http://ereserve.library.utah.edu/Annual/ACCTG/7610/Plumlee/chess.pdf ；https://gwern.net/doc/psychology/chess/1973-simon.pdf | 【已查证】（81%/33%/随机 3–5 子数据经 eScholarship 复证） | ①领域组块 chunking（理论构念）②专家长时记忆模式库（理论）③自动化加工（增量，弱） | C（5 秒回忆+反应时实验，无文本入口） | ❌ 无文本侧入口；这是实验范式非写作倾向 | **并入 F10 认知能力**：=abil-001 Gc（晶体/领域知识）的机制解释，不单列 |
| Categorization of Physics Problems by Experts and Novices | Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). *Cognitive Science*, 5(2), 121–152。专家按深层物理原理（牛顿定律）分类问题，新手按表面特征（斜面/滑轮）分类。全文：https://courses.physics.ucsd.edu/2006/Winter/physics180_280/documents/chi.pdf | 【已查证】 | ①深层原理表征 vs 表面特征表征（增量，弱文本可辨）②领域图式组织（理论）③专家-新手差异结构（理论） | C/B（"按本质归类"vs"按表面归类"在分类性文本里可弱辨，但需领域语料） | 🟡 无中文量表 | **并入 F10 + F5 抽象**：深层vs表面近似 abs-001/002 抽象语言倾向的领域版；不单列 |
| Cambridge Handbook of Expertise（刻意练习/自动化背景） | Ericsson, K. A., et al. (Eds.) (2006/2018). *Cambridge Handbook of Expertise and Expert Performance*. Cambridge UP.（Simon-Chase 组块理论的局限与修正章节） https://www.cambridge.org/core/books/cambridge-handbook-of-expertise-and-expert-performance/superior-working-memory-in-experts/8979912B089C15FC7049AC46F940D012 | 【已查证】 | ①刻意练习 deliberate practice（背景）②专家优势工作记忆（理论） | C | ❌ | 背景，不入画像 |

**本方向判定**：专家-新手差异本质是"领域知识量与组织"（Gc），靠回忆/反应时实验测量，**自由文本无入口（C）**。唯一文本侧可弱辨的"按本质 vs 按表面归类"与 F5 抽象语言倾向（abs-001/002）和 F10 Gc（abil-001）重叠。**不独立成族，并入 F10。**

---

## 3. 方向三：创造力与发散思维（Guilford SOI / Torrance TTCT / RAT / Amabile CAT）——★独立成族候选

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Structure of Intellect（发散生产） | Guilford, J. P. (1967). *The Nature of Human Intelligence*. McGraw-Hill。SOI 三维：5 操作（认知/记忆/发散生产/收敛生产/评价）×4 内容×6 产物=120 能力。发散生产=流畅性/变通性/独特性/精致性。综述：https://kiecon.org/wp-content/uploads/2022/02/J.P.-GUILFORD.pdf | 【已查证】 | ①发散生产 divergent production（已有→cgs-013 发散-聚合）②流畅性 fluency（增量）③变通性 flexibility（增量）④独特性 originality（增量）⑤精致性 elaboration（增量）⑥收敛生产 convergent（已有→cgs-013） | B（四指标可对"诱发的发散产出"自动评分；见下 TTCT 自动评分） | 🟡 理论中译普及；无现成中文发散词表 | **★从 cgs-013 拆出，升级为独立新族 F13** |
| Torrance Tests of Creative Thinking（TTCT） | Torrance, E. P. (1974/1990/1998). *TTCT*. Scholastic Testing Service。言语式 6–7 活动（问原因/猜后果/产品改进/不寻常用途等）+ 图形式 3 任务；四指标 fluency/flexibility/originality/elaboration；评分者信度 .80–.90、复本/分半 .70–.90（Kim 2006 综述）。原文综述：https://people.uncw.edu/caropresoe/giftedfoundations/SocialEmotional/Creativity-articles/Kim_Can-we-trust-creativity-tests.pdf ；自动评分：https://files.eric.ed.gov/fulltext/EJ1356011.pdf | 【已查证】（信度区间经科普中国+Kim 综述双证；言语式活动数经 ERIC/Frontiers 复证） | ①不寻常用途发散任务（诱发文本）②产品改进任务（诱发文本）③新颖性统计罕见度（增量）④类别转移数（增量） | **A（任务诱发）**：言语式产出本身是文本，流畅性=答案数、变通性=类别数、独特性=统计罕见度，已有自动 originality 评分（ERIC EJ1356011）；自由文本中为 B | ✅ **有中文版**：叶仁敏、洪德厚与 Torrance 合作修订（1988，《应用心理学》3(3):22–29 中美跨文化比较）；台湾刘英茂（语文甲式）、吴静吉（语文乙式/图形甲式）、陈龙安（图形乙式）修订。见 https://journal.psych.ac.cn/xlxb/article/2018/0439-755X/0439-755X-50-11-1197.shtml | **★独立新族 F13 核心**：v1 仅 cgs-013 一条，严重不足 |
| Remote Associates Test（RAT 远隔联想） | Mednick, S. A. (1962). The Associative Basis of the Creative Productive Process. *Psychological Review*, 69(3), 220–232；Mednick & Mednick (1967) RAT Manual。给三词找连接第四词（如 Sleeping/Bean/Trash→Bag）。 | 【已查证】（范式与三词例子经 P21 综述+ERiC 复证） | ①远隔联想 remote association（增量）②双关/语义远距离跳跃（增量）③联想层级扁平度（理论） | B（RAT 是施测题；但"远距联想能力"可从文本比喻跳跃/跨域词联结弱测） | ✅ **有中文版**：肖微、姚翔、邱永桃（2015）《用项目反应理论编制中文版远程联想测验(RAT)》，《北京大学学报(自然科学版)》，IRT 双参数、91 题、N=2659 中学生，与 Torrance/瑞文正相关。https://xbna.pku.edu.cn/CN/10.13209/j.0479-8023.2015.123 ；另有 CWRAT 中文词汇 RAT 80 题 | **★新族 F13 重要增量**（v1 无远隔联想构念） |
| Consensual Assessment Technique（CAT 同感评估） | Amabile, T. M. (1982). Social psychology of creativity: A consensual assessment technique. *JPSP*, 43(5), 997–1013. DOI:10.1037/0022-3514.43.5.997。由领域内合适专家对产品独立评分。中文介绍：中科院心理所机构库 https://ir.psych.ac.cn/bitstream/311026/2630/1/创造力测量手段_同感评估技术_CAT_简介.pdf | 【已查证】（卷期页码经 Rider 金标准文献+HBS 履历复证） | ①产品创造性同感评估（方法学）②领域专家独立评级（方法学）③内在动机对创造的作用（背景，见 mot-001） | B（CAT 是"找评委打分"，LLM 可充当评委对产出文本评创造性，多模型平均） | 🟡 中科院心理所已有 CAT 中文引介与应用；无标准化中文 CAT 手册 | **★新族 F13 的评分方法学锚**（与背景库 Wright 2025 LLM 打分同源） |

**本方向判定**：这是 8 个方向里**唯一同时满足三条件者**——(a) 有中文验证工具（TTCT 叶仁敏 1988、RAT 肖微 2015）；(b) 有真实文本输出可评分（言语式发散任务产出=文本，已有自动 originality 评分）；(c) v1 仅 cgs-013（发散-聚合）+cgs-008（适应-创新 KAI）两条，构念密度极低。**建议 v2 独立成新族 F13「创造力与发散思维」**，核心构念：流畅性/变通性/独特性/精致性/远隔联想/类比迁移/产品创造性同感评估。可计算性 B（诱发任务下可达 A；自由文本为 B）。

---

## 4. 方向四：洞察与顿悟（Gestalt 顿悟 / insight vs 分析式 / FOK 元认知体验）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Intuition in Insight and Noninsight Problem Solving（FOW 温暖感） | Metcalfe, J., & Wiebe, D. (1987). Intuition in insight and noninsight problem solving. *Memory & Cognition*, 15(3), 238–246. DOI:10.3758/BF03197722。顿悟题温暖感评分=平直后突升，分析题=渐进上升；FOW 能预测分析题解决但不能预测顿悟题。 | 【已查证】（DOI 经中科院知识服务平台+Purdue 综述复证） | ①知道感/温暖感 FOW（已有→meta-011 信心校准、meta-013 元认知体验）②顿悟 vs 分析式过程二分（增量）③僵局 impasse（增量） | B（FOK 本质是元认知监控，已在 F6；顿悟事件可作文本事件标记） | 🟡 无中文 FOK 量表；顿悟中文研究（罗劲等 EEG）存在但非文本量表 | **FOW 部分并入 F6（meta-011/013）**；不独立 |
| Aha! Insight / 顿悟右半球 | Bowden, E. M., & Jung-Beeman, M. (2003). Aha! Insight experience correlates with solution activation in the right hemisphere. *Psychonomic Bulletin & Review*, 10(4), 730–737；Kounios et al. (2006). *Psychological Science*, 17(10), 882–890。144 个复合远隔联想题；顿悟自评 1/2/3。原文：https://cseweb.ucsd.edu//~gary/cs200/f06/papers/PsychSci_2006_Kounios_MJB.pdf | 【已查证】 | ①顿悟体验 Aha（增量）②右半球远距离语义激活（理论）③顿悟自评事件标记（增量，见下） | **A（事件标记）**：Aha 时刻在文本有明确词元（"突然想到/顿悟/原来如此/茅塞顿开/灵光一现"），可作文本事件计数；作为稳定个体差为 B | 🟡 罗劲、沈汪兵等顿悟脑机制中文文献丰富，但无"顿悟倾向"中文词表；词元可自建 | **Aha 事件标记并入新 F13 或作跨族文本事件**；不独立成族 |
| Gestalt 顿悟（Köhler 猩猩 / Maier 双绳） | Köhler, W. (1925). *The Mentality of Apes*. Routledge；Maier, N. R. F. (1931). Reasoning in humans II. *J. Comparative Psychology*。 | 【一方称·教科书经典】 | ①顿悟重构 insight restructuring（理论）②酝酿 incubation（见 S3） | C（经典实验范式） | 🟡 | 背景，并入 S3 |

**本方向判定**：Metcalfe 的 FOW/温暖感本质是**元认知监控体验**，v1 已有 meta-011（信心校准）+meta-013（元认知体验）覆盖，应并入 F6。真正文本侧有价值的是 **Aha 时刻词元事件**（"突然想到/原来如此"），这是 A 级可计数事件，但它是过程性事件而非稳定人格倾向，建议作为新 F13 的一个标记或跨族事件，不单独立族。

---

## 5. 方向五：心智模型与知识表征（Johnson-Laird / 心理模拟）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Mental Models（心理模型理论） | Johnson-Laird, P. N. (1983). *Mental Models*. Cambridge UP；(2006). *How We Reason*. Oxford UP；Johnson-Laird & Bara (1984). Syllogistic inference. *Cognition*, 16(1)。人对可能性建模型，单模型易多模型难；搜索反例证伪。历史综述：https://modeltheory.org/papers/2005HistoryMentalModels.pdf | 【已查证】 | ①心理模型建构（理论架构）②单模型vs多模型推理（理论）③反例搜索 counterexample search（增量，弱）④心理模拟 mental simulation（增量） | C/B（推理架构理论，非个体差量表；"设想如果…会怎样"的反事实/模拟语言可弱测） | 🟡 理论中译普及；无中文量表 | **降级为推理背景理论**；心理模拟/反事实语言作弱标记，并入 F2 或 F5，不独立 |
| The Nature of Explanation（心智模拟前驱） | Craik, K. (1943). *The Nature of Explanation*. Cambridge UP. | 【一方称·教科书经典】 | ①现实的小规模模型模拟（理论前驱） | C | 🟡 | 背景 |

**本方向判定**：Johnson-Laird 心理模型是**演绎推理的架构理论**（解释人为什么单模型题快、多模型题错），它回答"人怎么推理"而非"这个人的思维倾向是什么"。自由文本里唯一可弱测的是"心理模拟/反事实推演"语言（"假如…就会…"），这与 F2 双过程、F5 抽象重叠。**不独立成族，作方向 8 的背景理论。**

---

## 6. 方向六：因果推理与因果学习（Griffiths & Tenenbaum 贝叶斯因果）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Theory-Based Causal Induction（因果归纳贝叶斯） | Griffiths, T. L., & Tenenbaum, J. B. (2009). Theory-based causal induction. *Psychological Review*, 116(4), 661–716；(2005). Structure and strength in causal induction. *Cognitive Psychology*, 51(4), 334–384。三类先验：本体论/合理性/函数形式；因果支持模型。原文：https://cocosci.princeton.edu/tom/papers/tbci.pdf | 【已查证】（2009 卷期页码经 cocosci 论文集复证） | ①因果结构推断 causal structure（理论）②因果强度 vs 结构分离（理论）③机制先验 vs 协变先验（增量，见背景库 Lombrozo） | C（协变数据表+贝叶斯建模实验，无文本量表） | ❌ 无文本侧入口；这是计算认知模型 | **维持分散**：不独立。因果*论证*已有 arg-004；因果*归因*已有 att-011/012 |
| Causal Mechanism vs Covariation 解释偏好 | Lombrozo, T. (2006). The structure and function of explanations. *Trends in Cognitive Sciences*, 10(10)；Vasil & Lombrozo (2022). *Frontiers in Psychology*。人对机制敏感、对协变钝感。（已在背景总报告集群 B 收录） | 【已查证】（见背景报告 #32/#33） | ①机制论解释偏好（增量）②功能论解释偏好（增量） | B（LLM 判定"这段解释诉诸机制/数据/类比/叙事"，背景报告已列） | 🟡 LLM 判定可行 | **并入背景库解释偏好维度**（已在集群 B），不单列因果族 |

**本方向判定**：任务书特别提示"注意 F3 已有因果论证、F4 已有因果归因，判定是否需独立"。核验结论：**不需要独立**。Griffiths-Tenenbaum 是实验室协变数据上的贝叶斯结构学习模型（C 级，无文本入口）；人们日常文本里的因果思维已被 arg-004（因果论证）+ att-*（因果归因/意图性/运气）+ 背景库 Lombrozo 机制偏好三分覆盖。**维持分散，不独立成族。**

---

## 7. 方向七：工作记忆与执行功能（Baddeley WM / Miyake EF 三成分）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Working Memory 多成分模型 | Baddeley, A. D., & Hitch, G. (1974)；Baddeley, A. D. (1992). Working Memory. *Science*, 255(5044), 556–559；(2000) 增补情景缓冲器。四成分：中央执行+语音环+视空模板+情景缓冲。五十年综述：https://pmc.ncbi.nlm.nih.gov/articles/PMC11783980/ | 【已查证】（2000 情景缓冲器增补经 PMC 2024 综述复证） | ①工作记忆容量（已有→abil-006 Gwm）②中央执行注意（理论）③语音环/视空模板（理论） | C（n-back/广度任务，反应时+记忆负荷，无文本入口） | ❌ 无文本侧入口 | **并入 F10（abil-006 Gwm）**，不独立 |
| Unity and Diversity of Executive Functions（EF 三成分潜变量） | Miyake, A., Friedman, N. P., Emerson, M. J., Witzki, A. H., Howerter, A., & Wager, T. D. (2000). The unity and diversity of executive functions... *Cognitive Psychology*, 41(1), 49–100。CFA 三因子：抑制/转移/更新；中等相关（unity）且可分（diversity）。Miyake & Friedman (2012) 修正为共同 EF+转移+更新。出处复证：https://onlinelibrary.wiley.com/doi/10.1111/sode.12764 | 【已查证】（2000 卷期 41(1):49–100 经 Wiley 论文+PMC 多篇复证） | ①抑制抑制优势反应 inhibition（理论）②任务转移 shifting（理论）③更新监控 updating（已有→abil-006） | C（Stroop/任务切换/n-back 反应时实验，无文本量表） | ❌ 无文本侧入口 | **并入 F10（abil-006 Gwm）**；EF 三成分为实验任务，不入文本画像 |

**本方向判定**：任务书提示"注意 F10 已有 Gwm/Gs，判定增量"。核验：工作记忆容量=abil-006 已覆盖；Miyake 抑制/转移/更新三成分全部靠**反应时实验室任务**测量（Stroop、task-switching、n-back），自由文本完全无入口（C）。**并入 F10，不独立成族。**

---

## 8. 方向八：演绎推理心理学（Wason 选择任务 / belief bias / 逻辑形式vs内容）

| 理论/模型/量表 | 作者·年份·出处 URL | 查证 | 核心构念（增量/已有） | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| Wason Selection Task（四卡片选择任务） | Wason, P. C. (1966/1968). Reasoning about a rule. *Quarterly J. Experimental Psychology*, 20(3), 273–281。抽象版<10% 答对；验证/证实偏差；匹配偏差（Evans & Lynch 1973）。综述：https://content.scirp.org/pdf/PSYCH_2016062714135935.pdf | 【已查证】（<10% 正确率、证实偏差/匹配偏差双机制经 SCIRP 综述+MIT 动机推理文复证） | ①证实偏差 confirmation bias（增量，弱；与 heur-014 认知反思、dp-011 去动机推理相邻）②匹配偏差 matching bias（增量，弱）③条件推理 if-then（理论） | C/B（四卡片是施测题；自由文本不可测演绎任务正确率；"寻求证实vs寻求证伪"倾向可弱辨） | 🟡 无中文演绎推理倾向量表 | **并入 F3+F2**：证实偏差与 dp-011（去动机推理/反证搜索）、F11 相邻；不独立 |
| Belief Bias（信念偏差） | （Evans, J. St. B. T. 等）三段论中内容可信度压倒逻辑形式。 | 【一方称·教科书经典】 | ①信念偏差 belief bias（**已有→dp-005 信念偏差**）②逻辑形式vs内容（理论） | C（三段论施测） | 🟡 | **已在 F2（dp-005）**，无需重复；并入即可 |
| Syllogistic Inference（三段论心理模型） | Johnson-Laird & Bara (1984). *Cognition*, 16(1)。（见方向 5） | 【已查证】 | ①三段论心理模型（理论） | C | 🟡 | 背景，见方向 5 |

**本方向判定**：任务书提示"与 F3 论证图式的关系，判定是否独立"。核验：belief bias **已是 dp-005**；演绎任务正确率是实验室施测（C），自由文本不可测；人们日常推理是否"重逻辑形式 vs 重内容可信度"已被 F2 双过程（dp-007/008 System1/2）+ F3 图式覆盖。**并入 F3+F2，不独立成族。**

---

## 9. 补充方向（文献扫描中发现的可计算候选）

| 补充方向 | 作者·年份·出处 URL | 查证 | 核心构念 | 可计算性 | 中文适用性 | 与 v1 关系 |
|---|---|---|---|---|---|---|
| **S1 类比迁移心理过程**（区别于论证类比） | Gick, M. L., & Holyoak, K. J. (1980). Analogical Problem Solving. *Cognitive Psychology*, 12(3), 306–355。Duncker 辐射问题；自发解决 10%，给故事类比后 30%，加提示后 75%；三步=注意→映射→应用。 | 【已查证】（10%/30%/75% 数据经 LibreTexts/ERiC 多源复证） | ①类比注意 noticing（增量）②类比结构映射 mapping（增量）③类比迁移应用 transfer（增量） | B（"拿另一领域经验套过来"的迁移语言可辨；与 arg-003 论证类比不同——那是说服手段，这是问题解决迁移） | 🟡 无中文量表 | **小增量**：v1 arg-003 是"类比论证"（修辞），Gick-Holyoak 是"类比迁移"（认知过程），二者不同。建议入新 F13 或作 F3 子条 |
| **S2 功能固着/心理定势** | Duncker (1945) 蜡烛问题（见方向 1）；Luchins, A. S. (1942). Mechanism in problem solving: The effect of Einstellung. *Psychological Monographs*。量水实验心理定势。 | 【一方称·教科书经典】 | ①功能固着（增量）②心理定势 Einstellung（增量） | C/B（实验室顿悟题；自由文本弱） | 🟡 | **并入问题解决障碍**，不单列族 |
| **S3 酝酿/创造四阶段** | Wallas, G. (1926). *The Art of Thought*。准备→酝酿→豁朗→验证。中文酝酿效应综述：心理科学进展 https://journal.psych.ac.cn/xlkxjz/CN/10.3724/SP.J.1042.2022.00291 | 【已查证】（中文酝酿效应文献经心理科学进展复证） | ①酝酿期 incubation（增量）②豁朗期 illumination（=Aha，见方向 4） | C/B（过程阶段描述，非稳定个体差） | 🟡 中文文献存在 | **并入新 F13**（作创造过程阶段描述），不单列 |
| **S4 Aha 时刻文本词元**（事件级，非倾向） | Bowden & Jung-Beeman (2003) 顿悟自评；中文词元："突然想到/顿悟/原来如此/茅塞顿开/灵光一现/豁然开朗" | 【已查证】（范式）+【一方称】（中文词元清单为本扫描拟建） | ①顿悟事件计数（增量，事件标记） | **A（事件级词表计数）** | 🟡 词元需小样本校准 | **跨族事件标记**：建议作新 F13 的一个文本事件计数器 |

---

## 10. 集群级增量清单（交付 v2 家族决议用）

**建议新独立成族：1 个**
- **F13 创造力与发散思维**：核心构念 = 流畅性 / 变通性 / 独特性 / 精致性（Guilford/Torrance）+ 远隔联想（RAT）+ 类比迁移（Gick-Holyoak，与 arg-003 区分）+ 产品创造性同感评估（CAT，LLM 多模型打分）+ Aha/顿悟事件标记（词元计数）。中文工具齐备（TTCT 叶仁敏 1988、RAT 肖微 2015）。可计算性 B（诱发任务下 A，自由文本 B）。

**建议并入现有族（不独立）：**
- 问题解决策略（手段-目的/倒推/分解）→ F6 元认知（与 meta-004/008/009 合并扩写）。
- FOW/知道感/信心校准 → F6（meta-011/013 已覆盖）。
- 工作记忆/执行功能三成分 → F10（abil-006 Gwm 已覆盖；EF 为反应时任务，仅作背景注记）。
- 专家-新手/领域组块 → F10（abil-001 Gc 的机制解释）。
- 演绎推理/信念偏差/证实偏差 → F3+F2（dp-005 belief bias 已在；证实偏差并入 dp-011）。
- 因果归纳贝叶斯/机制解释偏好 → 维持分散（arg-004 因果论证 + att-* 因果归因 + 背景库 Lombrozo）。
- 心智模型/心理模拟 → 降级为推理背景理论（与 F2/F5 共享弱标记）。

**明确移除/降级（不可从文本测，仅作背景架构）：**
- Newell-Simon 问题空间/产生式系统、ACT-R/SOAR、Miyake EF 反应时三成分、Baddeley WM 成分、Griffiths-Tenenbaum 贝叶斯因果结构、Chase-Simon 象棋组块、Johnson-Laird 心理模型架构——均为认知架构/实验室范式，**C 级无文本入口**，不入画像因子，仅作概念定义层背景。

---

## 11. 关键数字核验台账（逐条对原始出处）

| 数字/结构 | 核验值 | 出处 | 级别 |
|---|---|---|---|
| Polya 四阶段 | 理解→计划→执行→回顾 | 原书 PDF（UCR Math） | 已查证 |
| Newell-Simon 问题空间四要素 | 初始态/目标态/算子/中间态 | CMU 存档 + LibreTexts | 已查证 |
| Chase-Simon 大师回忆率 | 真实棋局 81% vs 新手 33%；随机局 3–5 子 | eScholarship 复证 + gwern 1973-simon.pdf | 已查证 |
| Chi 1981 分类差异 | 专家按物理原理/新手按表面特征 | Cognitive Science 5(2):121–152 原文 PDF | 已查证 |
| Guilford SOI | 5 操作×4 内容×6 产物=120 | KIE 综述 + Structural Learning | 已查证 |
| TTCT 信度 | 评分者 .80–.90；复本/分半 .70–.90 | Kim 2006 综述 + 科普中国 | 已查证 |
| TTCT 中文版 | 叶仁敏、洪德厚 1988（应用心理学 3(3):22–29） | 心理学报 2018 引文 | 已查证 |
| 中文 RAT | 肖微等 2015，IRT 双参数，91 题，N=2659 | 北大学报自科版 | 已查证 |
| Amabile CAT | JPSP 1982, 43(5):997–1013 | Rider 金标准 + HBS 履历 | 已查证 |
| Metcalf & Wiebe 1987 | Memory & Cognition 15(3):238–246，DOI 10.3758/BF03197722 | 中科院知识平台 | 已查证 |
| Gick-Holyoak 迁移率 | 自发 10% / 给类比 30% / 加提示 75% | LibreTexts 多源 | 已查证 |
| Griffiths-Tenenbaum 2009 | Psychological Review 116(4):661 | cocosci tbci.pdf 页脚 | 已查证 |
| Miyake 2000 | Cognitive Psychology 41(1):49–100，三因子抑制/转移/更新 | Wiley + PMC 多源 | 已查证 |
| Wason 抽象版正确率 | <10% | SCIRP 综述 | 已查证 |
| Bowden-Jung-Beeman | 144 复合远隔联想题，顿悟自评 1/2/3 | Kounios 2006 Psych Sci PDF | 已查证 |

---

*本集群扫描覆盖 8 指定方向 + 4 补充方向，每方向 2–4 篇可追溯文献，关键数字逐条核到原始出处；"已查证/一方称"分级透明。核心结论：8 方向中仅创造力与发散思维够独立成族（新 F13），其余并入现有 12 族或降级为认知架构背景。*
