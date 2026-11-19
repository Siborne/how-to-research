<div align="center">
  <img src="assets/how-to-research-logo.png" width="180" alt="科研入门指南" />
  <h1>科研入门指南：从 0 开始，掌握做科研、写论文的基本流程</h1>
  <p>面向刚进入课题组参与科研工作的同学，帮助大家快速建立对科研的基本认识，了解如何做科研、如何写论文。<br/>本仓库是相关文档的 Markdown 版本，便于本地阅读、检索与版本管理。</p>
  <p>
    <a href="http://siborne.top/how-to-research/">🌐 网站</a> ·
    <a href="https://github.com/Siborne/how-to-research/releases/latest/download/how-to-research.pdf">📕 PDF 手册</a> ·
    <a href="#acknowledgements">📚 参考文献</a>
  </p>
  <p>
    <img src="https://img.shields.io/badge/status-building-brightgreen" alt="status: building" />
    <img src="https://img.shields.io/badge/audience-research%20beginners-blue" alt="audience: research beginners" />
    <img src="https://img.shields.io/badge/docs-markdown%20%2B%20PDF-orange" alt="docs: markdown + PDF" />
  </p>
</div>

## 🖥️ 网页版

仓库自带一个无构建依赖的 landing page，入口为 [`index.html`](index.html)。

```bash
# 本地预览
python -m http.server 8080
# 打开 http://localhost:8080
```

网页版通过 [`.github/workflows/pages.yml`](.github/workflows/pages.yml) 自动发布。工作流只上传 landing page 所需文件，不经过 Jekyll，因此不会误解析 Markdown 内容。

## 📥 离线 PDF 下载

仓库会在每次推送到 `main` 后，自动把全部 Markdown 文档合并渲染成一份 PDF 并发布到 Releases，方便离线阅读：

- **最新版直达**：[`how-to-research.pdf`](https://github.com/Siborne/how-to-research/releases/latest/download/how-to-research.pdf)
- **查看历史版本**：[Releases 页面](https://github.com/Siborne/how-to-research/releases)

PDF 由 [`.github/workflows/release-pdf.yml`](.github/workflows/release-pdf.yml) 自动生成；如需手动触发，可到 Actions 页面运行 `Release PDF` 工作流。本地也可自行生成：先 `pip install markdown` 并安装 WeasyPrint，然后运行 `python scripts/build_pdf.py`，再执行 `weasyprint build/how-to-research.html build/how-to-research.pdf`。

## 🗂️ 目录结构

```text
.
├── README.md                    # 你在这里，总入口
├── index.html                   # 网页版 landing page
├── styles.css                   # 页面样式
├── script.js                    # 导航、动效与复制交互
├── assets/                      # favicon 与社交分享封面
├── .github/workflows/pages.yml  # GitHub Pages 自动发布
├── .github/workflows/release-pdf.yml  # 离线 PDF 自动发布
├── scripts/build_pdf.py         # 合并 Markdown 并生成 PDF 源文件
└── docs/
    ├── 01-做科研/               # 找论文 → 读论文 → 想 Idea → 汇报 / Meeting / 习惯
    │   ├── README.md            # 本章总览（如何做科研？）
    │   ├── 01-find-papers-如何找论文.md
    │   ├── 02-read-papers-如何读论文.md
    │   ├── 03-idea-如何想Idea.md
    │   ├── 04-presentation-如何进行学术汇报.md
    │   ├── 05-meeting-如何高效Meeting.md
    │   ├── 06-good-habits-一些好的习惯.md
    │   └── img/
    ├── 02-写论文/               # 画图 → Abstract → Introduction → … → Rebuttal
    │   ├── README.md            # 本章总览（如何写论文？）
    │   ├── 01-figure-guide-论文画图指南.md
    │   ├── 02-abstract-如何写论文-Abstract.md
    │   ├── 03-introduction-如何写论文-Introduction.md
    │   ├── 04-related-works-如何写论文-RelatedWorks.md
    │   ├── 05-methods-如何写论文-Methods.md
    │   ├── 06-experiments-如何写论文-Experiments.md
    │   ├── 07-reference-如何写论文-Reference.md
    │   ├── 08-rebuttal-如何Rebuttal.md
    │   └── img/
    ├── 03-杂项/                 # 参会指南、奖学金、AI 辅助科研 tips
    │   ├── README.md
    │   ├── 01-conference-学术会议参会指南.md
    │   ├── 02-scholarship-有哪些能申请的奖学金.md
    │   ├── 03-ai-tips-AI辅助科研tips.md
    │   └── img/
    ├── 04-本科论文写作/          # 本科毕业设计：开题报告 → 初稿 → 查重避坑
        ├── README.md
        ├── 01-开题报告/          # Markdown 正文（9 篇）
        ├── 02-初稿与写作/        # Markdown 正文（8 篇）
        └── 原件/                 # 原始 .docx / .doc / .pdf（保留排版与图片）
    └── 05-科研方向学习资料/      # AI 方向入门：基础 → 选题实践 → 汇报
        ├── README.md            # 本章总览与学习路线
        ├── 01-basics-基础学习资料.md
        ├── 02-directions-方向选题与代码实践.md
        └── 03-notes-观后感与想法记录.md
```

## 🚀 推荐阅读顺序

### 第一步 · 如何做科研

从「怎么找到并读懂一篇论文」开始，再到「怎么提出问题、怎么做实验汇报」。

| 顺序 | 文档 | 内容 |
| :--: | --- | --- |
| — | [🧪 如何做科研？（章节总览）](docs/01-做科研/README.md) | 什么是研究、研究生的任务、TPIC 流程 |
| 1 | [☁️ 如何找论文？](docs/01-做科研/01-find-papers-如何找论文.md) | 会议 / 种子论文 / 引文网络 / 作者与生态 |
| 2 | [📄 如何读论文？](docs/01-做科研/02-read-papers-如何读论文.md) | 读论文七步法 |
| 3 | [💡 如何想 Idea？](docs/01-做科研/03-idea-如何想Idea.md) | 问题驱动 vs 方法驱动、如何找问题、如何解决问题 |
| 4 | [🎙️ 如何进行学术汇报](docs/01-做科研/04-presentation-如何进行学术汇报.md) | PPT 形式与汇报内容 |
| 5 | [🧭 如何高效 Meeting](docs/01-做科研/05-meeting-如何高效Meeting.md) | Meeting 的目的、组织形式与模板 |
| 6 | [📝 一些好的习惯](docs/01-做科研/06-good-habits-一些好的习惯.md) | 学术输入、实验日志、记录与交流习惯 |

### 第二步 · 如何写论文

按真实论文的写作顺序展开，从配图到 Rebuttal。

| 顺序 | 文档 | 内容 |
| :--: | --- | --- |
| — | [📄 如何写论文？（章节总览）](docs/02-写论文/README.md) | 署名、投稿目标、论文大纲 |
| 1 | [🎨 论文画图指南](docs/02-写论文/01-figure-guide-论文画图指南.md) | 动机图 / 方法流程图 / 结果图表 |
| 2 | [🧾 如何写论文-Abstract](docs/02-写论文/02-abstract-如何写论文-Abstract.md) | 贡献说明书与「五句话原则」 |
| 3 | [🚪 如何写论文-Introduction](docs/02-写论文/03-introduction-如何写论文-Introduction.md) | 四段式结构与可复用骨架 |
| 4 | [🗺️ 如何写论文-Related Works](docs/02-写论文/04-related-works-如何写论文-RelatedWorks.md) | 分类、定位与常用表达 |
| 5 | [⚙️ 如何写论文-Methods](docs/02-写论文/05-methods-如何写论文-Methods.md) | 总分结构、公式与模块写法 |
| 6 | [📊 如何写论文-Experiments](docs/02-写论文/06-experiments-如何写论文-Experiments.md) | Setup / 主结果 / 消融 / 分析 |
| 7 | [📚 如何写论文-Reference](docs/02-写论文/07-reference-如何写论文-Reference.md) | bib 整理规范与投稿前自检 |
| 8 | [⚔️ 如何 Rebuttal](docs/02-写论文/08-rebuttal-如何Rebuttal.md) | 原则、常见问题回答技巧与常用句式 |

### 第三步 · 杂项

可以按需查阅，不必按顺序。

| 文档 | 内容 |
| --- | --- |
| [🧳 学术会议参会指南](docs/03-杂项/01-conference-学术会议参会指南.md) | 会前准备、会中交流、会后整理 |
| [💰 有哪些能申请的奖学金？](docs/03-杂项/02-scholarship-有哪些能申请的奖学金.md) | 本科生 / 研究生奖学金汇总 |
| [🤖 AI 辅助科研的一些 Tips](docs/03-杂项/03-ai-tips-AI辅助科研tips.md) | 常用快捷键与使用建议 |

### 第四步 · 本科论文写作

面向本科毕业设计（提前进组的本科生同样适用）：开题报告怎么写、初稿怎么起步、查重怎么避坑。

| 分组 | 内容 |
| --- | --- |
| [🎓 本科论文写作（章节总览）](docs/04-本科论文写作/README.md) | 全部资料的索引与来源说明 |
| [📋 开题报告](docs/04-本科论文写作/01-开题报告/) | 9 份开题报告模板、大纲与写作指南 |
| [✍️ 初稿与写作](docs/04-本科论文写作/02-初稿与写作/) | 初稿模板、查重避坑、文献综述与写作笔记 |

### 第五步 · 科研方向学习资料

面向已有一定基础、想进一步入门 LLM / MLLM Reasoning、Agent、Neuro-Symbolic Learning 等 AI 科研方向的同学，按「基础 → 选题实践 → 汇报」推进。

| 顺序 | 文档 | 内容 |
| :--: | --- | --- |
| — | [🎯 科研方向学习资料（章节总览）](docs/05-科研方向学习资料/README.md) | 学习目标、自测标准与路线图 |
| 1 | [🧱 基础学习资料](docs/05-科研方向学习资料/01-basics-基础学习资料.md) | 深度学习、LLM、多模态、推理与 Agent 基础 |
| 2 | [🧭 方向选题与代码实践](docs/05-科研方向学习资料/02-directions-方向选题与代码实践.md) | 7 个可选题方向 + 论文与复现任务 |
| 3 | [📝 观后感与想法记录](docs/05-科研方向学习资料/03-notes-观后感与想法记录.md) | 读完论文、跑完代码后的沉淀方法 |

## 🧩 说明

- 文档按 **目录分组 + 数字前缀** 组织，文件名形如 `01-find-papers-如何找论文.md`，既保证文件管理器中的顺序，也便于检索。
- 每篇文档顶部有面包屑导航，底部有「上一篇 / 下一篇」，可以顺着读下来。
- 图片统一放在各章节的 `img/` 目录下，相对路径引用。
- `docs/04-本科论文写作/` 把 **Markdown 正文**与**原始文档**分开存放：正文放在各章节目录，`.docx` / `.doc` / `.pdf` 原件统一放在 `原件/` 下，便于阅读与检索。

## 📄 许可协议

Copyright © 2026 Siborne。本作品采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) 许可协议：署名后可自由共享、改编，但不得用于商业目的。仓库中的 [LICENSE](LICENSE) 为官方协议全文。

## 📌 TODO

- [ ] 补充更多配套资料（进行中）

<a id="acknowledgements"></a>

## 📚 参考文献

本仓库在目录组织、写作思路与学习资料方面参考了以下项目与资料，特此致谢并标注来源。

### 项目与指南

1. LAMDA-NeSy. Research-Starter-Kit. <https://github.com/LAMDA-NeSy/Research-Starter-Kit> —— 目录组织与分章方式参考。
2. LAMDA-NeSy. Lab-RoadMap（本科生科研入门学习指南）. <https://github.com/LAMDA-NeSy/Lab-RoadMap> —— 第 5 章《科研方向学习资料》整理改写来源。
3. 周志华. 做研究与写论文. <https://zhuanlan.zhihu.com/p/98747105> —— 做科研、写论文思路参考。
4. 彭思达. 我的科研经验（learning_research）. <https://github.com/pengsida/learning_research> —— 科研经验参考。
5. 魏秀参. 浅谈学术 Rebuttal. <https://zhuanlan.zhihu.com/p/104298923> —— Rebuttal 内容参考。
6. MLNLP-World. Paper-Rebuttal-Tips. <https://github.com/MLNLP-World/Paper-Rebuttal-Tips> —— Rebuttal 内容参考。
7. Datawhale. 科研论文配图绘制指南（paper-chart-tutorial）. <https://github.com/datawhalechina/paper-chart-tutorial> —— 论文画图指南参考。
8. 斯坦福大学. 如何做好学术报告（公开讲座）. <https://www.bilibili.com/video/BV1WF411Y73C/> —— 学术汇报章节参考。

### 学习资料与教程

9. Zhang A., Lipton Z. C., Li M., et al. 动手学深度学习（Dive into Deep Learning）. <https://zh.d2l.ai/> —— 深度学习基础。
10. Karpathy A. Neural Networks: Zero to Hero. <https://karpathy.ai/zero-to-hero.html> —— 深度学习基础。
11. PyTorch. PyTorch Tutorials. <https://pytorch.org/tutorials/> —— 深度学习框架实践。
12. Datawhale. Happy-LLM. <https://datawhalechina.github.io/happy-llm/> —— 大语言模型基础。
13. Datawhale. 从零开始构建智能体（hello-agents）. <https://github.com/datawhalechina/hello-agents> —— Agent 工程实践。
14. Prompt Engineering Guide. <https://www.promptingguide.ai/zh> —— Prompt 与推理基础。
15. Weng L. LLM Powered Autonomous Agents. <https://lilianweng.github.io/posts/2023-06-23-agent/> —— Agent 经典必读。
16. lucidrains. vit-pytorch. <https://github.com/lucidrains/vit-pytorch> —— Vision Transformer 代码参考。
17. 多模态大模型论文串讲（B 站视频）. <https://www.bilibili.com/video/BV1Vd4y1v77v/> 与 <https://www.bilibili.com/video/BV1fA411Z772/> —— 多模态大模型入门。
18. Symbolic Regression Tutorial. <https://symbolicregression2025.github.io/> —— 符号回归入门。

### 其他说明

- `docs/04-本科论文写作/` 中的开题报告与写作材料为网络收集整理，非原创，仅供学习参考；引用、转载或公开展示前请自行确认版权与授权。
- `docs/05-科研方向学习资料/` 中涉及的具体综述与论文，均已在对应文档内逐条标注链接，此处不重复列出。
