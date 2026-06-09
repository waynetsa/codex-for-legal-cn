# Codex for Legal CN

作者：waynetsa  
仓库地址：https://github.com/waynetsa/codex-for-legal-cn

## 项目是什么

Codex for Legal CN 是一个面向中国律师事务所、公司法务团队、法律科技团队和法律教育场景的 Codex 插件与技能库。它将法律工作中高频、可复核、可流程化的工作拆成 Codex skills 和 plugins，用于生成律师审阅用草稿、风险清单、项目台账和工作底稿。

本项目不提供法律意见。所有输出仅供执业律师或合规负责人审阅。任何对客户、法院、仲裁机构、监管机构、交易对手发送、提交、签署或依赖的内容，必须由合格法律专业人士复核。不得把真实客户资料、案件材料、商业秘密、个人信息上传到公开仓库。公开仓库只放模板、流程、示例和脱敏样例。

## 适合谁使用

- 中国律师事务所的合伙人、律师、律师助理和知识管理团队。
- 公司法务、合规、采购、销售合同管理团队。
- 法律科技产品、工程和评测团队。
- 法律 AI 教学、实训和诊所课程。

## 第一阶段包含哪些插件

第一阶段提供三个可试用 MVP 插件：

- `cn-commercial-legal`：商业合同审查、NDA 初筛、合同偏离、续约和解除风险提醒。
- `cn-corporate-legal`：并购尽调文件表格化审阅、问题提取、交割清单和披露清单。
- `cn-litigation-legal`：案件接收、事实时间线、证据目录、争点表、庭前准备和案件周报。

## 为什么需要 cold-start interview

法律工作高度依赖团队口径、客户授权、风险偏好和复核规则。每个插件都提供 `cold-start-interview`，用于先生成团队或项目专用的 `practice-profile.md` 草稿，再让负责律师确认。后续技能读取该 profile，以统一风险等级、输出风格、升级规则和禁止事项。

## 律所如何接入自己的 playbook

- 把合伙人审查口径写入 `profiles/practice-profile.template.md` 的副本中，并命名为本地 `practice-profile.md`。该文件已被 `.gitignore` 忽略，不应提交公开仓库。
- 把脱敏后的模板放入对应插件的 `templates/`。
- 把检查清单、术语和流程说明放入 `references/`。
- 把人工复核、保密、引用和输出质量规则放入 `shared/guardrails/`。

## 安全与保密边界

公开仓库只能保存模板、流程、检查清单、评测方法和明显虚构样例。真实客户资料、案件材料、商业秘密、个人信息、未公开交易信息、证据原文、内部报价和密钥不得提交。

## 快速开始

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
```

在 Codex 中先选择一个插件目录，例如 `plugins/cn-commercial-legal`，运行 `cold-start-interview`，生成并由负责律师确认 practice profile，再调用具体技能。

## 示例调用方式

合同审查：

```text
请使用 cn-commercial-legal 的 contract-review 技能，基于本项目 practice profile，审查我上传的供应商服务合同，输出风险等级表、逐条修改建议、待客户决策事项和需合伙人升级事项。
```

NDA 初筛：

```text
请使用 cn-commercial-legal 的 nda-triage 技能，把这份 NDA 分成绿色、黄色或红色，并说明是否可快速放行。
```

合同偏离清单：

```text
请使用 cn-commercial-legal 的 deviation-memo 技能，对比合同文本和团队 playbook，生成偏离清单、建议谈判语言和审批人。
```

并购尽调：

```text
请使用 cn-corporate-legal 的 diligence-tabular-review 技能，读取资料室文件清单，生成一张尽调问题表，列明文件摘要、风险点、重大性、待追问问题和披露建议。
```

交割清单：

```text
请使用 cn-corporate-legal 的 closing-checklist 技能，根据尽调问题和交易结构生成交割前、交割日、交割后事项清单。
```

披露清单：

```text
请使用 cn-corporate-legal 的 disclosure-schedule 技能，根据尽调问题生成披露清单初稿，并标明待律师核验点和客户确认事项。
```

诉讼时间线：

```text
请使用 cn-litigation-legal 的 chronology-builder 技能，根据案件材料生成事实时间线，列明日期、事件、参与方、证据来源、争议程度和待核实事项。
```

证据目录：

```text
请使用 cn-litigation-legal 的 evidence-index 技能，整理证据目录，列明证据编号、证明目的、三性提示、原件情况和待补强事项。
```

庭前准备：

```text
请使用 cn-litigation-legal 的 hearing-prep 技能，根据事实时间线、证据目录和争点表生成庭前准备提纲。
```

## 后续路线图

详见 [ROADMAP.md](ROADMAP.md)。第二轮仅把三个核心插件升级为可试用 MVP；后续再考虑权限控制、评测体系、GitHub Actions 和 MCP 连接器占位。

## 贡献方式

欢迎提交新的 skill、模板、脱敏评测样例和流程说明。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，不得提交真实客户资料、真实案件材料、商业秘密或个人信息。

## 免责声明

本项目是法律工作流模板项目，不包含法律意见，不替代律师判断，不构成律师客户关系。任何正式法律文件、意见、函件、诉讼文书或交易文件均必须由合格法律专业人士复核后使用。
