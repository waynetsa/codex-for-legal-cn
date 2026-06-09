# Codex for Legal CN

作者：waynetsa  
仓库地址：https://github.com/waynetsa/codex-for-legal-cn

## 项目是什么

Codex for Legal CN 是一个面向中国律师事务所、公司法务团队、法律科技团队和法律教育场景的 Codex 插件与技能库。它将法律工作中高频、可复核、可流程化的工作拆成 Codex skills 和 plugins，用于生成律师审阅用草稿、风险清单、项目台账和工作底稿。

本项目参考成熟法律工作流项目的架构思想，包括 practice-area plugins、skills、cold-start interview、practice profile、templates、connectors、guardrails、evals 和 usage docs，但所有内容均按 Codex 生态与中国大陆法律工作场景重新组织。

## 适合谁使用

- 中国律师事务所的合伙人、律师、律师助理和实习生。
- 公司法务、合规、采购、销售合同管理团队。
- 法律科技产品、知识管理和 IT 团队。
- 法学院、法律诊所和法律 AI 教学场景。

## 第一阶段包含哪些插件

第一阶段只提供三个核心插件骨架：

- `cn-commercial-legal`
- `cn-corporate-legal`
- `cn-litigation-legal`

## 三个核心插件分别能做什么

`cn-commercial-legal` 面向合同审查、NDA 初筛、供应商合同审查、销售合同审查、采购合同审查、合同偏离清单、续约和解除风险提示。

`cn-corporate-legal` 面向公司与并购项目，包括尽调资料室审阅、重大合同清单、披露清单、交割清单、股权结构、公司治理、资质许可、诉讼仲裁、行政处罚、税务和劳动风险初筛。

`cn-litigation-legal` 面向诉讼与争议解决，包括案件 intake、事实时间线、证据目录、争点表、诉讼策略备忘录、保全清单、开庭准备提纲、代理词或答辩状初稿结构、案件周报。

## 为什么需要 cold-start interview

法律工作高度依赖背景信息。cold-start interview 用于在正式处理材料前收集事项类型、角色、交易或案件阶段、适用法域、关键风险口径、输出格式和人工复核要求，减少 Codex 在信息不足时直接生成结论。

## 律所如何接入自己的 playbook

律所可以把内部知识沉淀为：

- `profiles/` 中的 practice profile，用于记录团队偏好、风险等级、客户行业和审批规则。
- `templates/` 中的审查备忘录、问题清单、交割清单和周报模板。
- `references/` 中的检查清单、术语表和内部流程说明。
- `shared/guardrails/` 中的保密、个人信息、引用和律师复核规则。

公开仓库只应保存模板、流程、示例和脱敏样例。真实客户资料、案件材料、商业秘密和个人信息不得提交到公开仓库。

## 安全与保密边界

本项目不提供法律意见。所有输出仅供执业律师或合规负责人审阅。任何对客户、法院、仲裁机构、监管机构、交易对手发送、提交、签署或依赖的内容，必须由合格法律专业人士复核。

不得把真实客户资料、案件材料、商业秘密、个人信息上传到公开仓库。公开仓库只放模板、流程、示例和脱敏样例。

## 快速开始

1. 克隆仓库：

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
```

2. 检查项目结构：

```bash
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
```

3. 在 Codex 中选择需要的插件目录，例如 `plugins/cn-commercial-legal`，先运行 `cold-start-interview`，再调用具体 skill。

## 示例调用方式

可以在 Codex 中这样描述任务：

```text
使用 cn-commercial-legal 的 contract-review skill。请基于脱敏后的合同文本，输出律师审阅用草稿，区分事实、风险、建议和待确认事项。
```

```text
使用 cn-corporate-legal 的 diligence-tabular-review skill。请基于脱敏资料室清单生成尽调问题台账。
```

```text
使用 cn-litigation-legal 的 chronology-builder skill。请基于脱敏事实材料生成案件时间线。
```

## 后续路线图

详见 [ROADMAP.md](ROADMAP.md)。第一轮只建立项目骨架；后续将补充具体工作流、示例材料、评测集和连接器说明。

## 贡献方式

欢迎提交新的 skill、模板、评测样例和流程说明。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，不得提交真实客户资料、真实案件材料、商业秘密或个人信息。

## 免责声明

本项目是法律工作流模板项目，不包含法律意见，不替代律师判断，不构成律师客户关系。任何正式法律文件、意见、函件、诉讼文书或交易文件均必须由合格法律专业人士复核后使用。
