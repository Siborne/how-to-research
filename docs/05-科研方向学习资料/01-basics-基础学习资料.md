# 🧱 基础学习资料

> 🧭 [首页](../../README.md) › [科研方向学习资料](README.md) › **基础学习资料**

> 以下资料仅作为学习参考，不需要完全读完；按「能理解 + 能写代码」的标准推进即可。

## 1. 神经网络与深度学习基础

**学习目标**

- 掌握神经网络的基本原理，能理解前向传播与反向传播的数学推导与代码实现。
- 掌握 CNN / ResNet、RNN 等机器学习基础模型架构。
- 掌握 PyTorch 核心组件的使用，例如 DataLoader、损失函数、模型搭建、优化器等。

**参考资料**

- [动手学深度学习](https://zh.d2l.ai/)
- [Neural Networks: Zero to Hero（Andrej Karpathy）](https://karpathy.ai/zero-to-hero.html)
- [PyTorch Tutorial](https://pytorch.org/tutorials/)

## 2. 大语言模型（LLMs）

**学习目标**

- 掌握 Transformer 的核心机制（Self-Attention、Positional Encoding、Decoder-only vs Encoder-Decoder 等）。
- 了解 GPT 系列、LLaMA 系列等典型大语言模型。

**参考资料**

- [Happy-LLM（Datawhale）](https://datawhalechina.github.io/happy-llm/)

## 3. 视觉与多模态大模型

**学习目标**

- 了解 Vision Transformer（ViT）的基本原理。
- 了解 LLaVA、Qwen-VL 系列等前沿多模态大模型。

**参考资料**

- 多模态大模型论文串讲：[上](https://www.bilibili.com/video/BV1Vd4y1v77v/?spm_id_from=333.337.search-card.all.click&vd_source=4deb09ae020d1de21482612e7102fb83)、[下](https://www.bilibili.com/video/BV1fA411Z772/?share_source=copy_web&vd_source=b19e968ea4fbdf0cb9dfd7fbc468280e)
- [ViT 论文](https://arxiv.org/abs/2010.11929) ｜ [代码库](https://github.com/lucidrains/vit-pytorch)
- [LLaVA 论文](https://arxiv.org/abs/2304.08485)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)

## 4. 大模型 / 多模态推理（LLM / MLLM Reasoning）

**学习目标**

- 掌握基础的 Prompt Engineering（Zero-shot、Few-shot 等）及 API 调用方式。
- 掌握 Chain-of-Thought 等大模型推理机制。
- 掌握 SFT、PPO、DPO、GRPO 等提升基座模型推理能力的后训练方式。
- 了解 GSM8K、MATH 等常用 benchmark。

**参考资料**

- [Prompt Engineering Guide](https://www.promptingguide.ai/zh)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models](https://arxiv.org/pdf/2504.11468)
- [SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training](https://arxiv.org/abs/2501.17161)

## 5. 智能体（Agent）

**学习目标**

- 理解大模型 Agent 的基本概念与核心架构，能区分 Agent 与普通对话型 LLM 的差异。
- 掌握 ReAct 等基础 Agent 框架的原理与实现。
- 了解 Agent 的记忆机制与规划方法。
- 了解大模型 Agent 背景下 Multi-Agent 系统的基本概念。

**参考资料**

- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)（经典必读）
- [《从零开始构建智能体》](https://github.com/datawhalechina/hello-agents/tree/main)（偏工程视角）

---

⬅️ 上一篇：[科研方向学习资料（总览）](README.md) ｜ ➡️ 下一篇：[方向选题与代码实践](02-directions-方向选题与代码实践.md)
