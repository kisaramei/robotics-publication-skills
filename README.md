# Robotics Publication Skills

面向机器人、具身智能、VLA、计算机视觉与机器学习研究者的 Codex 学术投稿工作流，覆盖论文写作、投稿前模拟审稿、期刊返修和会议 rebuttal。

本项目基于 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) 进行领域适配，重点补充机器人与学习系统论文中的公平比较、数据泄漏、实验独立性、消融、泛化、sim-to-real、实时性、安全和复现检查。

> [!IMPORTANT]
> 这是独立维护的派生项目，并非 `nature-skills` 上游项目的官方发行版。

## 包含的 Skills

| Skill | 用途 | 来源 |
|---|---|---|
| `robotics-writing` | 论文规划、章节写作、结构重建与首次投稿材料 | 由 `nature-writing` 适配 |
| `robotics-reviewer` | 投稿前模拟审稿、实验有效性与拒稿风险检查 | 由 `nature-reviewer` 适配 |
| `robotics-response` | 期刊返修、逐点回复与会议 rebuttal | 由 `nature-response` 适配 |
| `nature-polishing` | 学术英语润色、压缩与中英转换 | 保留上游版本 |
| `nature-ref-verifier` | 参考文献、DOI 与书目信息核验 | 保留上游版本 |
| `nature-statistics` | 统计设计和论文统计报告审查 | 保留上游版本 |
| `nature-shared` | 共享写作规则和运行依赖，不作为主要入口 | 保留上游版本 |

最小领域套装为三个 `robotics-*` Skills 加 `nature-shared`。其余三个通用组件可按需要安装。

## 主要适配

### `robotics-writing`

- 增加 CS conference、CS journal 和 generic 路由。
- 将 claim 对齐到公平 baseline、独立 seeds/episodes、消融、OOD、跨机器人泛化和部署约束。
- 仅在目标明确属于 Nature Portfolio 时加载 Nature 专属写作与投稿规则。

### `robotics-reviewer`

- 默认生成三份相互隔离的模拟审稿意见，再进行独立综合。
- 优先使用目标 venue、track 和年份的当前官方规则；无法核实时明确退回通用 rubric。
- 检查数据泄漏、比较公平性、统计单位、跨 embodiment、sim-to-real、控制频率、安全与复现。

### `robotics-response`

- 明确区分 `journal-revision` 与 `conference-rebuttal`。
- 会议路径先核对当届官方规则、字数或字符预算、可见性以及允许修改范围。
- 不虚构实验、结果、引用、修改位置，也不把尚未执行的工作写成已经完成。

## 安装

推荐在 Codex 中使用内置的 `$skill-installer`。将下面这段提示词复制到一个 Codex 任务中：

```text
使用 $skill-installer 从下面的 GitHub 仓库安装论文工作流 Skills：

https://github.com/kisaramei/robotics-publication-skills

请安装以下目录：
- skills/robotics-writing
- skills/robotics-reviewer
- skills/robotics-response
- skills/nature-polishing
- skills/nature-ref-verifier
- skills/nature-statistics
- skills/nature-shared

请保留每个 Skill 的完整目录结构，不要只复制 SKILL.md。
如果存在同名 Skill，请先报告，不要直接覆盖。
安装后检查相对引用是否完整；如果新 Skill 没有出现，请重启 Codex。
```

Codex 可以从其他 GitHub 仓库安装本地 Skills。详细机制见 [OpenAI 官方 Skills 文档](https://learn.chatgpt.com/docs/build-skills)。

> [!WARNING]
> `nature-shared` 必须与其他 Skill 目录保持同级。只复制 `SKILL.md`，或遗漏 `nature-shared`，会破坏 `static/`、`references/` 和共享规则的按需加载。

## 使用示例

```text
使用 $robotics-writing，根据这些实验结果重构论文 Introduction，并检查 claim 和 evidence 是否对齐。
```

```text
使用 $robotics-reviewer，按当前 CoRL 投稿标准模拟三位相互隔离的审稿人，最后汇总主要风险。
```

```text
使用 $robotics-response，根据这些评审意见和官方 author-response 规则准备会议 rebuttal。
```

也可以不显式指定 Skill，直接描述论文写作、投稿前审查或审稿意见回复任务，由 Codex 根据 Skill 描述选择工作流。

## 目录结构

```text
robotics-publication-skills/
├── LICENSE
├── README.md
└── skills/
    ├── robotics-writing/
    ├── robotics-reviewer/
    ├── robotics-response/
    ├── nature-polishing/
    ├── nature-ref-verifier/
    ├── nature-statistics/
    └── nature-shared/
```

## 验证状态

- 三个领域版均通过 Skill frontmatter 与名称一致性检查。
- Manifest 引用路径检查通过：writing 55/55、reviewer 10/10、response 16/16。
- 11 项路由与指令契约测试、7 项 response package 一致性测试通过。
- 三个领域版及其共享依赖均已在本仓库目录结构下通过引用完整性检查；四个保留组件来自固定的上游提交。

这些检查验证目录、路由和指令契约，不代替目标 venue 当届官方投稿规则。涉及页数、匿名、附件、artifact、rebuttal 时限或字数限制时，仍应以当前官方说明为准。

## 上游来源与修改声明

本项目派生自：

- 原始仓库：[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)
- 适配基线：[commit `ebd722e18808442688bd205917a3e774195c258f`](https://github.com/Yuan1z0825/nature-skills/commit/ebd722e18808442688bd205917a3e774195c258f)
- 获取日期：2026-09-02

修改范围集中在 `robotics-writing`、`robotics-reviewer` 和 `robotics-response`。这些目录分别由上游的 `nature-writing`、`nature-reviewer` 和 `nature-response` 派生；其名称、路由、领域检查和输出契约已经修改。`nature-polishing`、`nature-ref-verifier`、`nature-statistics` 与 `nature-shared` 保留自上述固定提交。

感谢原项目作者和贡献者公开这套 Skill 设计与实现。本项目保留原始来源和许可证信息，后续更新不会自动覆盖领域适配内容，而是先比较上游变化再选择性合并。

## License

本项目依据 [Apache License 2.0](LICENSE) 分发。再分发或修改时，请保留许可证、原始来源、版权与归属信息，并明确标注修改内容。
