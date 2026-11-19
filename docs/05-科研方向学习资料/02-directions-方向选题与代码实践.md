# 🧭 方向选题与代码实践

> 🧭 [首页](../../README.md) › [科研方向学习资料](README.md) › **方向选题与代码实践**

本阶段的重点是论文调研、阅读、复现与思考，而不是追求「背答案」。核心流程如下：

1. **了解方向**：了解 Neuro-Symbolic Learning、LLM Reasoning、Agent 等主要研究方向。
2. **选择题目**：结合自己的兴趣，选择一个方向。
3. **实践汇报**：完成相应的论文阅读与代码实践，并形成 PPT 汇报。

> 这个过程帮助你判断：你是否真正享受分析问题、阅读论文、调试代码和反思实验的过程。如果你对「研究问题本身」感到兴奋，那就值得继续深入。

## 研究方向初步认知

建议先浏览以下综述或教程，建立对各方向的整体认识。

- **神经符号学习（Neuro-Symbolic Learning）**
  - [Neuro-Symbolic Learning in the era of Large Models](https://www.lamda.nju.edu.cn/guolz/paper/AAAI_Logic_AI_Keynote.pdf)
  - [Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models](https://arxiv.org/abs/2508.13678)
- **大模型推理与规划（LLM / MLLM Reasoning & Planning）**
  - [Towards Reasoning Era: A Survey of Long Chain-of-Thought for Reasoning Large Language Models](https://arxiv.org/abs/2503.09567)
  - [Perception, Reason, Think, and Plan: A Survey on Large Multi-Modal Reasoning Models](https://arxiv.org/pdf/2505.04921)
- **智能体（Agent）**
  - [Agent AI: Surveying the Horizons of Multi-Modal Interaction](https://arxiv.org/pdf/2401.03568)
  - [A Survey on Agentic Multi-Modal Large Language Models](https://arxiv.org/pdf/2510.10991)
  - [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538)
- **符号回归（Symbolic Regression）**
  - Tutorial: [https://symbolicregression2025.github.io/](https://symbolicregression2025.github.io/)

## 选题实战

请结合个人兴趣选择一个方向，检索并阅读相关论文，完成代码实践。

**⚠️ 注意事项**

- 不要求完整复现论文全部实验，但需要在至少 1 个数据集上跑通完整算法流程并得到结果。
- 尽量复用开源框架（如 `LLaMA-Factory`、`TRL`、`LangChain` 等），重点在于掌握算法流程与分析实验结果，而非重复造轮子。
- 若算力受限，优先使用 PEFT（LoRA / QLoRA）或小参数量模型（如 Qwen-2.5-1.5B / 3B）。
- 如果未能复现论文中的性能结果，并不视为失败；请尝试定位问题来源、分析原因并给出合理解释。
- 如果复现自行查找的论文，优先选择近两年（2025 年后）在顶会（ICML / NeurIPS / ICLR）上发表、或具有较高影响力（Citation > 100）的文章。

### 方向 1：大模型逻辑推理

LLM 很擅长「看起来有道理但实际错误的回答」，在需要严格逻辑推导的任务上容易出错。本方向的主要目标是提升大模型严谨的逻辑推理能力。如果你对数理逻辑、形式化方法感兴趣，或者喜欢一步步推导结论的严谨感，可以关注这个方向。

- [Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning](https://arxiv.org/abs/2305.12295)
- [Faithful Logical Reasoning via Symbolic Chain-of-Thought](https://arxiv.org/pdf/2405.18357)
- [VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks](https://arxiv.org/abs/2511.04662)

> **🎯 实践任务**：基于上述论文，调研「结合 Formal Language 与 Symbolic Solver 提升 LLM 逻辑推理能力」的工作，在至少 1 个逻辑推理 benchmark 中完成 1 篇论文复现。
>
> 目标：体会结合形式化语言与求解器提升 LLM 逻辑推理能力的思想。

### 方向 2：数学、几何推理

数学推理是检验 LLM 推理能力的经典战场，从小学应用题到 IMO 竞赛题，模型的表现差异巨大。本方向主要目标是提升大模型的数学推理能力，相关算法思路也可以迁移到司法、医疗等垂直领域。如果你对数学或垂域大模型训练感兴趣，可以关注这个方向。

- [Neuro-Symbolic Data Generation for Math Reasoning](https://arxiv.org/abs/2412.04857)
- [NeSyGeo: A Neuro-Symbolic Framework for Multimodal Geometric Reasoning Data Generation](https://arxiv.org/abs/2505.17121)

> **🎯 实践任务**：复现上述论文中数据合成的方法，并基于 SFT 或 GRPO 微调一个开源大语言模型 / 多模态大模型，在数学推理数据集（如 GSM8K、MATH、MathVista、WeMath 等）上评测，分析合成数据与训练算法对推理性能的影响。
>
> 目标：体会 SFT 与 RL 作为两种常用 post-training 范式的区别，并学会用两种方式提升 base model 推理能力。SFT 为必选任务；GRPO 如果跑不起来，可以先只掌握原理 / 代码实现。

### 方向 3：视觉图像推理

给定一幅图像和对应的问题，如何完成推理任务？人类处理图像推理时会在脑海中「画辅助线」「放大局部」，但现有 MLLM 大多只能被动地看一眼图片再回答。本方向探索如何让模型在推理过程中主动生成、修改和利用中间图像，实现「边想边看」。

- [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://arxiv.org/abs/2505.14362)
- [Thyme: Think Beyond Images](https://arxiv.org/abs/2508.11630)
- [TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning](https://arxiv.org/abs/2511.01833)
- [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/abs/2508.05748)
- [Thinking with Images for Multi-Modal Reasoning: Foundations, Methods, and Future Frontiers](https://arxiv.org/pdf/2506.23918)

> **🎯 实践任务**：调研 "Think with Images" 方向的论文，尝试在一个视觉推理数据集上复现一种方法，并做结果分析。
>
> 目标：体会该方向的主要研究问题与常见范式；算力不允许时可优先选择 Training-Free 的方法。

### 方向 4：抽象视觉推理

ARC-AGI-Challenge 是专门设计来测试 AI 泛化能力的视觉谜题：每道题给出若干输入输出图案样例，需要归纳背后的抽象规则并预测新输入。这是一个难度很高的挑战，被认为是实现 AGI 的重要基准，每年相关比赛奖金超过 100 万美元。

- [ARC Challenge](https://arcprize.org/)
- [NSA: Neuro-symbolic ARC Challenge](https://arxiv.org/abs/2501.04424)

> **🎯 实践任务**：了解什么是 ARC Challenge，调研相关论文与解决方案，尝试实现至少一种方法，分析其结果和瓶颈。
>
> 目标：熟悉 ARC Challenge 这一任务及已有方法范式。

### 方向 5：Travel Agent（Tool-Use & Planning）

给定一个复杂的用户旅行需求，例如「预算 5000 元，从南京出发，三天游云南，满足若干偏好」，如何让 Agent 自动调用工具、查询信息并生成一个满足约束的合理方案？这个方向的核心挑战是让 LLM 可靠地完成复杂的约束满足与规划任务，比较贴近实际应用。

- [TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622)
- [ChinaTravel: An Open-Ended Benchmark for Language Agents in Chinese Travel Planning](https://arxiv.org/pdf/2412.13682)
- [Mind the Gap to Trustworthy LLM Agents: A Systematic Evaluation on Constraint Satisfaction for Real-World Travel Planning](https://openreview.net/pdf?id=SXKIaWTe4N)

> **🎯 实践任务**：基于 ReAct 框架构建一个简单 Agent，分析其在上述两个数据集中的性能表现。
>
> 目标：体会 Travel Planning 任务的关键挑战（约束可满足的复杂规划能力）及潜在解决方案。

### 方向 6：Game / Embodied Agent

本方向探索让 Agent 在模拟或真实环境中行动，例如在 Minecraft 中自主探索、采矿、建造，或在家居场景中让机器人完成具身任务。挑战在于环境动态、反馈稀疏、任务长程，Agent 需要记忆、技能积累与自我反思能力。如果你对游戏智能体、具身智能体感兴趣，会比较合适。

- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
- [WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents](https://arxiv.org/pdf/2504.15785)
- [InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning](https://openreview.net/pdf?id=nzwjvpCO4F)
- [Agent Workflow Memory](https://arxiv.org/pdf/2409.07429)
- [Inducing Programmatic Skills for Agentic Tasks](https://arxiv.org/abs/2504.06821)
- [Training-Free Group Relative Policy Optimization](https://arxiv.org/pdf/2510.08191)
- [Re2 Agent: Reflection and Re-execution Agent for Embodied Decision Making](https://openreview.net/pdf?id=nHhOvYrPMf)

> **🎯 实践任务**：参考上述论文，在 Minecraft 环境、具身数据集 ALFWorld 或 Web Agent 环境 WebShop 中进行实验，并汇报性能结果。Minecraft 环境更复杂、对模型能力要求更高，请根据自身工程能力选择。
>
> 目标：了解 Agent Skill、Agent Memory 等相关内容，熟悉相关 benchmark。

### 方向 7：Symbolic Regression

给你一批科学观测数据，能否发现背后隐藏的科学规律？例如从物理实验数据中自动发现牛顿定律，这就是符号回归的目标。传统方法依赖演化计算等搜索策略，近年来 LLM 的引入带来了新思路。如果你对 AI4Science 感兴趣，这个方向值得关注。

- Tutorial: [https://symbolicregression2025.github.io/](https://symbolicregression2025.github.io/)

> **🎯 实践任务**：基于上述 Tutorial 阅读相关论文，尝试复现 [LLM-SR: Scientific Equation Discovery via Programming with Large Language Models](https://openreview.net/forum?id=m2nmp8P5in)，根据论文给出的 GitHub 仓库跑通代码，并对比原文结果。
>
> 目标：了解 Symbolic Regression 任务、常见 benchmark 以及 LLM 时代的主流方法。

## 自定义方向

如果你对其他隶属于 Neuro-Symbolic Learning、Agent、LLM Reasoning 领域的方向感兴趣（比如多模态医学推理、遥感图像推理、Chart QA、智慧司法，或 Minecraft 之外的其他游戏场景等），也可以自选方向查阅文献，按同等要求完成：**至少复现 1 篇论文算法在 1 个数据集上的实验结果**。

---

⬅️ 上一篇：[基础学习资料](01-basics-基础学习资料.md) ｜ ➡️ 下一篇：[观后感与想法记录](03-notes-观后感与想法记录.md)
