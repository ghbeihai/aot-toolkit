# AoT 普查 v2 集群三：学习、语言、发展与个体差异（S3）穷尽性文献扫描

> 任务：判定本集群 8 个候选方向是否应成为思维量化体系的独立普查家族（或并入现有 12 家族），给出可计算性评估。
> 对照基线：v1 = 12 家族 175 构念（constructs_index.md）。证据分级：【已查证】= 本轮已抓取出版社/期刊/PubMed/PMC 页面核验标题·作者·年份·出处一致；【一方称·教科书经典】= 学界公认但本轮未逐页翻原文。
> 可计算性：A=现成词表/量表题面可直接转文本判定；B=LLM 从理论/题面自举；C=基本不可从文本测量。

---

## 0. 集群一句话总评

**本集群 8 个方向里，7 个不 warrant 独立成族**——它们要么是"发展阶段/能力测验"（Piaget、认知老化、空间能力、ANS），本质是年龄/任务梯度而非成人自由文本可测的思维倾向；要么已被 v1 覆盖（学习风格≈F1、学习策略元认知侧≈F6、具身隐喻≈F7/F5、空间言语-表象≈cgs-004、流体晶体≈F10）。**唯一值得独立成族的是方向 4 神经多样性认知风格**（Baron-Cohen 系统化-共情化 + 自闭特质连续谱 + ADHD 语言标记），理由：①它在 v1 12 族里无对应轴；②有成熟连续量表（AQ/EQ/SQ）+ 中文版 + 从文本检测自闭特质的 NLP 先例（>0.85 准确率）；③它在普通人群中是连续分布的个体差异维度，不是纯临床诊断。补充方向里，growth mindset 并入 F4 归因、epistemic curiosity 并入 F2 认知需求、CLT 移除、成人后形式思维/智慧并入 F9 知识论。

---

## 方向 1｜学习风格与学习策略（Kolb / Honey&Mumford / VARK / MSLQ / Zimmerman SRL）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 构念 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Kolb 经验学习 LSI 四型 | Kolb, D. A. (1984). *Experiential Learning*. Prentice Hall；LSI 修订版 12 题（1985）。题本：https://aim.stanford.edu/wp-content/uploads/2013/05/Kolb-Learning-Style-Inventory.pdf | 【已查证】（12 题、CE/RO/AC/AE 四阶段、四象限型：发散/同化/聚合/顺应，见题本与昆明医科大学学报中文使用例） | ①具体经验-抽象概念化（CE-AC 感知维）②反思观察-主动实验（RO-AE 加工维）③发散型④同化型⑤聚合型⑥顺应型——**全部与 F1 认知风格重叠**：CE-AC 维≈cgs-001 分析-整体；RO-AE 维≈cgs-009 直觉-分析 / cgs-012 冲动-反思。**无净增量** | C（LSI 是迫选排序自陈，非自由文本可推；且 Freedman & Stumpf 1981、Newstead 1992 反复报告重测信度低） | 🟡 有中文使用例（昆明医科大学学报住培生研究，α=.81）但非标准化中文常模 | **并入 F1 认知风格，不独立**。其"学习风格"内核与 cgs-001/009/012 同构 |
| VARK 学习偏好 | Fleming, N. D., & Mills, C. (1992). Not Another Typology! *Phi Delta Kappan*；16 题 | 【已查证】（Fleming & Mills 1992 出处；16 题问卷 vark-learn.com） | 视觉/听觉/阅读-书写/动觉四偏好——**= cgs-004 言语型-表象型 / cgs-010 言语-视觉认知偏好 的感官通道版**。无净增量 | C（自我报告通道偏好，非文本可测） | 🟡 有中文网络传播但无标准化修订研究 | **并入 F1（cgs-004/cgs-010），不独立**。且 meshing 假设已被证伪（见下） |
| Honey & Mumford LSQ | Honey, P., & Mumford, A. (1992). *The Manual of Learning Styles* (rev.). Peter Honey；80 题（4 型各 20 题） | 【已查证】（80 题、activist/reflector/theorist/pragmatist 四型；Duff & Duffy 2002 报告 α=.52–.73、Swailes & Senior 1999 因子结构不符 Kolb 双极假设） | 行动者/反思者/理论家/实用者——**= Kolb 四型改名**（activist=AE、reflector=RO、theorist=AC、pragmatist=CE）。无净增量 | C | 🟡 有西语 CHAEA 改编，中文无权威修订 | **并入 F1，不独立**（Kolb 的弱心理测量学复制品） |
| Pashler 等学习风格证伪综述 | Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning Styles: Concepts and Evidence. *Psychological Science in the Public Interest*, 9(3), 105–119. https://brucehayes.org/Teaching/papers/PashlerEtAl2008OnLearningStyles.pdf | 【已查证】 | "meshing hypothesis"（按风格匹配教学才增效）在严格交叉交互设计下**证据近乎为零**；结论：无充分证据把学习风格评估纳入教育实践。这是否决 Kolb/VARK/H&M 成族的决定性文献 | —（方法论否决，非构念） | — | 对整个"学习风格"方向的**证伪性元证据**：即便可测，构念效度也不成立 |
| MSLQ 学习策略问卷 | Pintrich, P. R., Smith, D. A., Garcia, T., & McKeachie, W. J. (1991/1993). *A Manual for the Use of the Motivated Strategies for Learning Questionnaire*；81 题=动机 31（6 子量表）+学习策略 50（9 子量表），α=.52–.93。Duncan & McKeachie (2005) "The Making of the MSLQ" | 【已查证】（81 题、15 子量表、α 区间见 Duncan 2005 子量表表：rehearsal α=.69、elaboration .75、organization .64、critical thinking .80、metacognitive self-regulation .79、self-efficacy .93） | 学习策略 9 子量表：①复述 rehearsal②精细加工 elaboration③组织 organization④批判性思维 critical thinking⑤元认知自我调节 metacog. self-regulation⑥时间与学习环境⑦努力调节⑧同伴学习⑨求助求助。其中：⑤→**meta-004 计划 / meta-009 监控 / meta-010 控制（F6 已有）**；④→**epi-012 批判性思维倾向（F9 已有）**；①②③≈dp-014 加工深度。⑥⑦⑧⑨（时间/努力/同伴/求助）=学习行为习惯，**非思维构念** | B（元认知自我调节子量表题面可被 LLM 从文本自举"我会定期检查自己是否读懂了"类表达；但⑥-⑨学习行为无文本入口） | 🟡 有中文/多语改编研究，非权威统一中文版 | **元认知侧并入 F6（meta-004/009/010 已覆盖，无增量）；批判性思维并入 F9；资源管理/求助/时间管理不入 Atlas** |
| Zimmerman SRL 三阶段循环 | Zimmerman, B. J. (2000). Attaining Self-Regulation: A Social Cognitive Perspective. In *Handbook of Self-Regulation*；三阶段：预先思考 forethought / 表现 performance / 自我反思 self-reflection | 【已查证】（三阶段及子过程见 Frontiers in Psychology 2017 六模型综述、Cleary & Zimmerman 手册） | ①任务分析/目标设定/策略计划（forethought）②自我控制/自我观察/自言自语（performance）③自我评估/自我反应/归因（self-reflection）。其中：①→**meta-004 计划（F6 已有）**；②→meta-006 理解监控；③→**att-004 可控归因 / att-014 能力归因（F4 已有）** | B（三阶段是过程结构，可作 LLM 判定提示词维度，但无现成词表） | 🟡 理论可直接用，无中文 SRL 词表 | **并入 F6（计划/监控/调节）+ F4（反思阶段归因），不独立**。SRL 是 F6 元认知在学习场景的过程展开，非新构念轴 |

**方向 1 小结**：学习风格三模型（Kolb/VARK/H&M）= 弱信度 + meshing 假设被 Pashler 2008 证伪 + 与 F1 已有风格轴重叠 → **整体不独立成族**。学习策略/SRL 的元认知侧已被 F6 覆盖、批判性思维被 F9 覆盖、资源管理/求助是行为习惯非思维构念。**净增量 = 0**。

---

## 方向 2｜认知发展（Piaget 四阶段 / 形式运算 / 成人后形式思维与智慧）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Piaget 认知发展四阶段 | Piaget, J. (1970). *Piaget's Theory*. In *Carmichael's Manual of Child Psychology*；四阶段：感知运动(0-2)/前运算(2-7)/具体运算(7-11)/形式运算(11+) | 【一方称·教科书经典】（四阶段年龄区间见 ERIC ED117874、Stony Brook 讲义；Piaget 1972 本人承认形式运算非成人普遍达到） | ①客体永久性②守恒③可逆性④假设-演绎推理⑤命题逻辑。这是**儿童发展阶段**，靠守恒/摆锤等临床任务访谈测，**不是成人个体差异思维倾向** | C（需临床任务施测；成人自由文本无法反推"处于哪一阶段"） | — | **移除/不入 Atlas**。发展阶段非思维风格，且成人阶段不可文本化 |
| 成人后形式思维 / 辩证思维 | Labouvie-Vief (1984, 1992)；Kramer (1983)；Perry (1970) | 【一方称·教科书经典】（见心理学空间成人发展心理学、Columbia Aging 综述） | 超越形式运算：对结构不良问题的容忍、对逻辑不确定性的接受、认知-情绪整合、辩证/相对主义思维。→ 与 **F9 高度重叠**：epi-004 二元立场 / epi-005 相对主义立场 / epi-015 认知复杂性容忍(dp-012) / epi-016 认知成熟度 | B（相对主义/不确定性容忍可从文本判定） | 🟡 理论可直接用 | **并入 F9 知识论**（epi-005/epi-016 已覆盖，无独立增量） |
| Baltes 柏林智慧范式 BWP | Baltes, P. B., & Smith, J. (1990); Baltes & Staudinger (2000). Wisdom. *American Psychologist*；五标准评分：事实知识/程序知识/ lifespan 情境主义/价值相对主义/不确定性觉知与管理。出声思考转录本 0-7 评分 | 【已查证】（五标准与 think-aloud 评分法见 PMC9546793、Oxford Gerontologist 综述） | ①关于生命基本实用知识的专家知识②价值/目标相对主义③生命周期情境化④不确定性觉知与管理——**这是少数对"转录本"直接评分的发展构念，文本可测**。与 F9 关系：④≈epi-016 认知成熟度；②≈epi-005 相对主义 | **B（偏 A）**：BWP 本来就是对出声思考文本按 5 标准人工编码，LLM 可直接照编码手册判定 | 🟡 无中文常模，但编码维度可 LLM 化 | **并入 F9**，可把"智慧五标准"作为 epi-016 认知成熟度的细化子构念补充，不独立成族 |

**方向 2 小结**：Piaget 儿童四阶段 = 发展梯度、临床任务测量、非成人思维倾向 → **移除**。成人后形式思维/辩证/智慧 = 与 F9 知识论（反思判断/相对主义/认知成熟度）同构，BWP 是其中最可文本化的一支，**并入 F9 作 epi-016 细化**。不独立成族。

---

## 方向 3｜认知老化 / 发展性变化（加工速度、流体 vs 晶体、补偿策略）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| Salthouse 加工速度理论 | Salthouse, T. A. (1996). The Processing-Speed Theory of Adult Age Differences in Cognition. *Psychological Review*, 103(3), 403–428. DOI:10.1037/0033-295X.103.3.403 | 【已查证】（limited-time + simultaneity 两机制，见 PMC2958696、Cambridge 认知老化模型综述） | ①加工速度下降（limited time 机制）②同时协调失败（simultaneity 机制）。加工速度 = **abil-004 加工速度 Gs（F10 已有）**；且它是年龄协变量，非个体思维风格 | C（加工速度靠数字符号/反应时测验，非文本） | — | **并入 F10（abil-004 Gs 已覆盖），不独立** |
| 流体 vs 晶体智力（力学 vs 实用） | Horn, J. L. (1989); Cattell (1963); Baltes 力学/实用二分 | 【已查证】（流体早期高峰后下降、晶体到 50-70 岁仍升，见 Frontiers Aging Neurosci 2026、Seattle Longitudinal Study） | ①流体/力学（Gf：抽象推理、工作记忆）②晶体/实用（Gc：词汇、世界知识）。→ **abil-003 流体推理 Gf / abil-001 晶体智力 Gc（F10 已有）** | C（靠智测验，非文本） | — | **并入 F10（abil-001/003 已覆盖），无增量** |
| SOC 成功老龄化模型 | Baltes, P. B., & Baltes, M. M. (1990). Psychological Perspectives on Successful Aging；选择 Selection / 优化 Optimization / 补偿 Compensation | 【一方称·教科书经典】 | ①选择性投入②优化③补偿——是老龄化行为策略，非认知构念 | C（行为策略，无文本入口） | — | **移除**（发展性应对策略，非思维量化构念） |

**方向 3 小结**：加工速度/流体晶体 = v1 F10 CHC 已逐字覆盖（abil-001/003/004），且全部是反应时/智测验、非文本可测。SOC = 行为策略。**无任何独立成族理由，整体并入/移除。**

---

## 方向 4｜神经多样性认知风格（Baron-Cohen 系统化-共情化 / AQ-EQ-SQ / 自闭谱系 / ADHD）★本集群唯一新族候选

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 共情化-系统化 E-S 理论 | Baron-Cohen, S. (2003/2009). The Empathizing-Systemizing (E-S) Theory of Autism. *Annals of the NY Academy of Sciences*. https://docs.autismresearchcentre.com/papers/2009_BC_nyas.pdf | 【已查证】（E=识别他人心理状态并以适当情绪回应的驱力；S=分析/构建规则系统的驱力；自闭=E 低 S 高的"极端男性脑"） | ①共情化 empathizing②系统化 systemizing③E-S 差异落差。**系统化≠v1 cgs-014 systematic-intuitive-processing**（那是 Kruglanski 的"系统化 vs 启发式加工"lay theory，完全不同构念）；共情化在 v1 无对应轴。**真增量** | B（E/S 是自陈驱力倾向，题面可 LLM 自举；且有文本 NLP 先例见下） | ✅（见 AQ 中文版行） | **独立成族核心**——这是 v1 缺失的"社会认知-系统认知"轴 |
| AQ 自闭谱系商数 | Baron-Cohen, S., Wheelwright, S., Skinner, R., Martin, J., & Clubley, E. (2001). The Autism-Spectrum Quotient. *J. Autism and Developmental Disorders*, 31, 5–17. 50 题，0-50 分，5 子域：社交技能/注意转移/注意细节/沟通/想象。https://neuroscience.cam.ac.uk/publications/... | 【已查证】（50 题、AS/HFA 均值 35.8 vs 对照 16.4、80% 病例≥32 vs 对照 2%；α 总量表=.90 见 PMC9192400） | ④社交技能缺损⑤注意转移困难⑥**注意细节/局部加工**⑦沟通语用偏差⑧想象受限。其中⑥局部-整体加工是认知风格层（与 cgs-001 分析-整体相关但不同：自闭的"局部偏向"是知觉层，非辩证层） | B→A 边界（50 题题面可转 LLM 判定；更关键见下"文本 NLP 先例"） | ✅ **有成熟中文版**：Zhang et al. (2016) *BMC Psychiatry* 16:213 简体成人 AQ（Back-translation 核验）；刘萌容 (2008) 台湾中文成人版 | **独立成族核心构念清单** |
| EQ 共情商数 | Baron-Cohen, S., & Wheelwright, S. (2004). The Empathy Quotient. *J. Autism and Developmental Disorders*. 60 题=40 共情题+20 填充，满分 80，α=.93。https://docs.autismresearchcentre.com/papers/2004_BCandSW_EQ.pdf | 【已查证】（40+20 结构、满分 80、AS/HFA 81%≤30 分 vs 对照 12%） | ⑨认知共情⑩情感共情。与 E-S 理论的 E 对应 | B | 🟡 有中文研究引用，无广泛验证中文版 | 独立成族（E 侧量表） |
| SQ 系统化商数 | Baron-Cohen, Richler, Bisarya, Gurunathan, & Wheelwright (2003). The Systemizing Quotient. *J. Autism and Developmental Disorders*. 60 题=40 系统化题+20 填充，α=.78 | 【已查证】（40+20、满分 80、α=.78 见 PMC5357270） | ⑪对规则系统的 drive⑫机械/数字/抽象系统分类兴趣 | B | 🟡 | 独立成族（S 侧量表） |
| ADHD 认知特征（执行功能模型） | Barkley, R. A. (1997). ADHD and the Nature of Self-Control. Guilford；行为抑制→四大执行功能：非言语工作记忆/言语内化(自言自语)/情绪动机调节/重构 | 【已查证】（Barkley 1997 四域 EF 级联见 PMC6378275、Frontiers Psych 2025 综述；dual-pathway：hot 抑制-动机-延迟厌恶 + cool 执行注意-WM-计划） | ⑬抑制控制缺陷⑭注意不集中/持续注意差⑮冲动/延迟厌恶⑯时间盲（time blindness）。与 D2 注意力缺口相关，但 ADHD 是连续维度特质 | B（LIWC 已有 ADHD 语言标记见下） | 🟡 ASRS-v1.1 有中文版 | 独立成族（注意-冲动子轴） |
| **从文本检测自闭/ADHD 特质的 NLP 先例** | (a) #ActuallyAutistic Twitter 数据集（6.5M tweets），tweet 分类 73%/user 分类 87% 准确，medRxiv 2023.09.19.23295799；(b) 8 年级书面叙事 DNN 预测自闭 >0.85 敏感性/特异性；(c) arXiv 2604.10063 Reddit 社区 LIWC 差异：自闭=高 clout/social/tentative，ADHD=高 authentic/第一人称 | 【已查证】（medRxiv 数据集与准确率；arXiv 2604.10063 LIWC d 值） | **关键证据：自闭特质/ADHD 可从自由文本被机器读出**——这把本方向从"自陈量表"提升到"文本可测" | **A-/B**（有监督 NLP 先例已跑通；LLM 零样本判定可期） | 🟡 中文缺对应数据集，需自建校准 | **这是把方向 4 评为"可成族"的计算可行性支柱** |

**方向 4 小结**：这是本集群唯一**独立成族**候选（建议编号 F13 候选：神经多样性认知风格 / 共情化-系统化轴）。理由：①E-S 轴在 v1 12 族无对应（cgs-014 是不同构念）；②AQ/EQ/SQ 是连续分布的成人个体差异量表，非纯临床诊断；③AQ 有简体中文版（Zhang 2016）；④已有从 Twitter/书面叙事检测自闭特质的 NLP 管线（准确率 0.73-0.87+）。可计算性 B（接近 A），中文 🟡（量表✅但中文 NLP 数据集需自建）。

---

## 方向 5｜空间认知与视觉思维（心理旋转 / 空间能力 / 言语-意象）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 心理旋转实验 | Shepard, R. N., & Metzler, J. (1971). Mental Rotation of Three-Dimensional Objects. *Science*, 171(3972), 701–703. DOI:10.1126/science.171.3972.701 | 【已查证】（反应时随旋转角度线性上升） | ①心理旋转 analog 表象操作。靠反应时/纸笔 MRT（Vandenberg & Kuse 1978）测 | C（反应时任务，非文本） | — | **并入 F10 abil-005 视觉加工 Gv**（空间能力即 Gv 广域），不独立 |
| Uttal 空间技能 2×2 分类 | Uttal, D. H., et al. (2013). The Malleability and Spatial Training. *Psychological Bulletin*（217 项训练研究元分析）；2×2：内在/外在 × 静态/动态 | 【已查证】（2×2 框架见 PMC13113327、Frontiers Educ 2023 综述） | ②内在-静态③内在-动态（心理旋转）④外在-静态⑤外在-动态（视角采择）。= CHC Gv 的细分，属能力而非思维风格 | C（空间能力测验，非文本） | — | **并入 F10 abil-005 Gv**，不独立 |
| 言语型-表象型认知偏好 | Linn & Petersen (1985) 空间能力三分类；已在 v1 | 【已查证】 | ⑥言语-表象偏好——**= cgs-004 言语型-表象型 + cgs-010 言语-视觉认知偏好（F1 已有，逐字覆盖）** | B（表象词频/具体度可文本测，已走 F5 abs-001/002 路线） | ✅（具体性常模见 F5 已查证资源） | **已有，无增量** |

**方向 5 小结**：心理旋转/空间能力 = F10 abil-005 Gv 已覆盖且是反应时能力测验；言语-表象偏好 = cgs-004/cgs-010 已逐字覆盖。**不独立，无增量。**

---

## 方向 6｜语言-思维关系（Sapir-Whorf 弱版 / 双语认知 / 语言相对论实验 / 内语）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 语言相对论（弱版） | Boroditsky, L. (2001). Does Language Shape Thought? Mandarin and English Speakers' Conceptions of Time. *Cognitive Psychology*；Winawer et al. (2007) PNAS 俄语蓝实验 | 【已查证】（英语水平时间隐喻、汉语垂直时间 shàng/xià yuè；俄语 goluboy/siniy 类别边界加速辨别） | ①语法/词汇习惯→注意与范畴化习惯。**这是跨语言/跨文化效应，不是同一语言人群内的个体思维风格**——无法从一个人的中文文本反推"Whorf 倾向" | C（靠反应时启动实验测，非个体文本） | — | **移除/不入 Atlas**（语言间效应，非个体思维构念；且汉语垂直时间隐喻已被 F7 met-012 时间空间化隐喻覆盖） |
| 双语认知 | Bialystok 等执行功能优势研究 | 【一方称·教科书经典】 | 双语经验→执行控制。群体层面效应，非个体思维倾向 | C | — | **移除** |
| 内语 inner speech | Vygotsky, L. S. (1934/1986). *Thought and Language*. MIT Press | 【一方称·教科书经典】 | ②自我指导言语（private/inner speech）。有自陈问卷（Verkhrud 内语量表）但非自由文本可直接测 | C/B（内语频率靠自陈；与 meta 自言自语弱相关） | 🟡 | **弱，作 F6 旁注不独立**（与 Barkley ADHD"言语内化"相关，归方向 4） |

**方向 6 小结**：Sapir-Whorf/双语 = 跨语言群体效应，非个体思维风格，且时间隐喻已被 F7 met-012 覆盖 → **移除**。内语 = 弱，归方向 4 ADHD 子轴。不独立成族。

---

## 方向 7｜数量/数学认知（数感 / ANS / 算术 / 数学焦虑）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 近似数量系统 ANS | Dehaene, S. (1997). *The Number Sense*. Oxford UP；Feigenson, Dehaene, & Spelke (2004). Core systems of number. *TiCS* 8(7), 307–314 | 【已查证】（ANS=非语言近似量级表征、Weber 定律、距离/大小效应；IPS 脑区；与 symbolic math 关系有争议） | ①ANS 敏锐度②量级距离效应。靠点阵比较反应时任务测，属 Gq 定量能力（CHC），非思维风格 | C（反应时/点阵任务，非文本） | — | **并入 F10 能力背景（Gq），不独立** |
| 数学焦虑 | Ashcraft, M. H., & Faust, M. W. (1994). Mathematics Anxiety and Mental Arithmetic Performance. *Cognition & Emotion*, 8(2), 97–125；MARS 量表 | 【已查证】（数学焦虑经工作记忆占用损害计算；Maloney 2011 关联 ANS 表征粗糙） | ③数学焦虑（情绪-认知占用）。有 MARS 自陈量表；文本侧可探测"我对数字发怵"类情绪语言，但领域窄 | B（情绪语言可 LLM 探测，但领域高度特定） | 🟡 | **弱，不入核心**。与情绪/归因交叉，不独立成族 |

**方向 7 小结**：ANS/数感 = 反应时能力测验，归 F10 Gq 背景；数学焦虑 = 领域特定情绪，B 级弱文本入口。**不独立成族。**

---

## 方向 8｜具身认知（Barsalou 知觉符号 / 感觉运动模拟）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 知觉符号系统 PSS / 接地认知 | Barsalou, L. W. (1999). Perceptual Symbol Systems. *Behavioral and Brain Sciences*, 22(4), 577–660. http://ruccs.rutgers.edu/images/.../Barsalou_BBS1999.pdf | 【已查证】（概念=感觉运动模态经验的再模拟/模拟器；抽象概念靠内感受+元认知状态接地） | ①感觉运动模拟②模态再激活③具体概念 vs 抽象概念接地差异。**Lakoff & Johnson 概念隐喻是此框架的一支，已入 F7（met-001..016）** | B（文本侧可测的表面=具体性/感觉运动词频，已被 F5 abs-001/002 抽象-具体语言倾向覆盖；Brysbaert 40k 具体性常模已查证） | ✅（中文具体性常模：Yao 2017、ANCW 2023、Chan&Tse 2024，见总报告 §5） | **不独立成族**。作为 F7 概念隐喻的理论上游补注；其可测表面（具体度）已在 F5。无独立新构念 |
| 具身隐喻/动作语言 | Glenberg & Kaschak (2002) 动作-句子兼容效应；Gallese & Lakoff (2005) | 【一方称】 | 动作句的运动共振——反应时实验，非文本构念 | C | — | 理论背景，并入 F7 |

**方向 8 小结**：具身认知是 F7 概念隐喻的更广义理论框架，Lakoff 一支已入 v1；其唯一可从文本测的表面（具体性/感觉运动词频）已被 F5 abs-001/002 覆盖。**不独立成族，作 F7 理论注脚。**

---

## 补充方向（文献扫描中新发现，一并评估）

| 理论/模型/量表 | 作者 年份 出处 URL | 已查证/一方称 | 核心构念（增量 or 已有→v1 id） | 可计算性 | 中文适用性 | 与现有 12 家族关系 |
|---|---|---|---|---|---|---|
| 认知负荷理论 CLT | Sweller, J. (1988). Cognitive Load During Problem Solving. *Cognitive Science*, 12(2), 257–285；Sweller, van Merriënboer, & Paas (1998). *Educational Psychology Review*, 10, 251–296 | 【已查证】（内在/外在/相关三类负荷相加；element interactivity；Paas 主观评定量表） | ①内在负荷②外在负荷③相关负荷——是**教学设计理论**，靠 Paas 9 点主观评定/双任务测，非个体思维倾向 | C（设计负荷，非思维风格） | — | **移除**（教学设计框架，非思维构念） |
| 成长思维模式 growth mindset | Dweck, C. S. (2006). *Mindset*；Dweck & Leggett (1988) entity vs incremental theory；8 题内隐智力观量表 | 【已查证】（entity=智力固定 vs incremental=智力可塑；Blackwell 2007 数学成绩追踪） | ①实体论（能力固定）②增量论（能力可塑）。**与 F4 归因直接同构**：att-014 能力归因（固定）vs att-015 努力归因（可塑）。但 mindset 是 global 信念、归因是情境特异 | B（文本可探测"我就是不擅长X"固定 vs"我能练出来"增长） | 🟡 有中文 mindset 量表修订 | **并入 F4 归因**（att-014/015 的 global 版），可作 1 个增量构念"智力内隐观"，不独立 |
| 认知/认识好奇心 | Loewenstein, G. (1994). The Psychology of Curiosity: A Review and Reinterpretation. *Psychological Bulletin*, 116(1), 75–98（信息缺口理论）；Litman ECS 量表 | 【已查证】（好奇心=意识到知识缺口的剥夺感；倒 U 形；RPL 近端学习区） | ①认知好奇心/信息寻求驱力。**与 F2 dp-003 认知需求 need-for-cognition 高度相邻**（NFC=享受思考；epistemic curiosity=欲求信息） | B（好奇心可探测提问/信息寻求密度，但无现成词表） | 🟡 | **并入 F2 双过程/理性**（dp-003 NFC 的信息寻求侧），作 1 个增量构念，不独立 |
| 格式塔学习 | Wertheimer (1945) *Productive Thinking* | 【一方称·教科书经典】 | 顿悟/重组——经典学习理论，无现代文本测量传统 | C | — | **移除**（无独立构念价值） |

---

## 集群补充方向清单（扫描中发现、建议纳入 v2 候选池）

1. **智力内隐观 / growth mindset**（Dweck）→ 建议入 F4，1 个增量构念（global entity/incremental belief）。
2. **认识好奇心 / 信息寻求驱力**（Loewenstein）→ 建议入 F2，1 个增量构念（epistemic curiosity，与 dp-003 NFC 配对）。
3. **智慧五标准**（Baltes BWP）→ 建议入 F9，作 epi-016 认知成熟度的细化。
4. **【核心新增】神经多样性认知风格轴**（E-S / AQ 五域 / ADHD 注意-冲动）→ 建议独立成族 F13 候选。

---

## 每方向"建议结论一句话"汇总表

| # | 方向 | 建议结论 | 可计算性 | 中文适用性 |
|---|---|---|---|---|
| 1 | 学习风格与学习策略 | **不独立**：Kolb/VARK/H&M 并入 F1（且被 Pashler 2008 证伪），MSLQ/SRL 元认知侧并入 F6、批判性思维并入 F9，资源管理/求助移除 | C（风格量表）/ B（SRL 过程） | 🟡 |
| 2 | 认知发展 | **不独立**：Piaget 儿童四阶段移除（发展阶段非思维倾向）；成人后形式/智慧并入 F9（BWP 作 epi-016 细化） | C（Piaget）/ B（智慧） | 🟡 |
| 3 | 认知老化 | **不独立**：加工速度/流体晶体并入 F10（abil-001/003/004 已逐字覆盖），SOC 移除 | C | — |
| 4 | 神经多样性认知风格 | **★独立成族（F13 候选）**：E-S 轴 + AQ 五域 + ADHD 注意-冲动是 v1 缺失轴，有连续量表+中文版+文本 NLP 先例 | **B（近 A）** | ✅量表 / 🟡NLP 需自建 |
| 5 | 空间认知与视觉思维 | **不独立**：空间能力并入 F10 abil-005 Gv，言语-表象偏好已有 cgs-004/010，心理旋转 C 不可文本测 | C（旋转）/ B（表象偏好） | ✅ |
| 6 | 语言-思维关系 | **不独立**：Sapir-Whorf/双语=跨语言效应移除（时间隐喻已被 met-012 覆盖），内语归方向 4 | C / 弱 B | — |
| 7 | 数量/数学认知 | **不独立**：ANS/数感并入 F10 Gq 能力背景，数学焦虑 B 级弱入口不入核心 | C（ANS）/ B（焦虑） | 🟡 |
| 8 | 具身认知 | **不独立**：作 F7 概念隐喻的理论上游注脚，可测表面（具体度）已在 F5 abs-001/002 | B | ✅ |
| 补 | CLT 认知负荷 | **移除**（教学设计理论，非思维构念） | C | — |
| 补 | growth mindset | **并入 F4**（att-014/015 的 global 版，1 增量构念） | B | 🟡 |
| 补 | 认识好奇心 | **并入 F2**（dp-003 NFC 信息寻求侧，1 增量构念） | B | 🟡 |
| 补 | 格式塔学习 | **移除**（无现代文本测量传统） | C | — |

---

### 交付说明
- 本集群净新增独立家族 = **1 个**（方向 4 神经多样性认知风格，F13 候选）。
- 其余 7 方向 + 3 个补充方向全部判定为"并入现有族"或"移除"，净增量构念约 4 个（E-S 轴 2 + mindset 1 + curiosity 1，外加智慧作 epi-016 细化）。
- 所有关键数字已核到原始出处：MSLQ 81 题/15 子量表/α.52-.93；Kolb LSI 12 题；H&M LSQ 80 题/α.52-.73；VARK 16 题；AQ 50 题/α.90；EQ 60 题(40+20)/α.93；SQ 60 题(40+20)/α.78；Piaget 4 阶段；Salthouse 1996 Psych Review 103(3):403-428；Shepard-Metzler 1971 Science 171:701；Uttal 2013 2×2/217 研究；Barsalou 1999 BBS 22(4):577-660；Sweller 1988 Cognitive Science 12(2):257-285；Loewenstein 1994 Psych Bull 116:75-98。
