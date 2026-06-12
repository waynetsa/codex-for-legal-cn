---
name: core-workflow-placeholder
description: 说明 cn-ai-governance-legal MVP 的核心工作流拆分和后续扩展边界；仅作规划，不提供法律意见。
---

# Core Workflow Placeholder

## Purpose

说明 `cn-ai-governance-legal` 从 scaffold 升级为 MVP 后的工作流边界，帮助维护者理解后续应如何拆分、评测和验收。所有内容均为“律师审阅用草稿”。

## When to use

- 需要快速了解 AI 治理插件当前包含哪些 MVP skills。
- 准备为本插件新增端到端 acceptance 前。
- 维护者需要判断某个需求是否属于本插件范围。

## Inputs expected

- 律所或企业 AI 治理需求描述。
- 目标输出类型：制度草稿、工具准入表、风险评估、供应商合同审查、治理差距清单。
- 是否涉及真实客户资料、员工数据、供应商合同或系统清单。

## Workflow

1. 判断需求是否属于 AI 治理，而不是隐私合规、劳动用工、监管监测或知识产权专项插件。
2. 将需求路由到以下 MVP skills：
   - `cold-start-interview`
   - `ai-use-policy-builder`
   - `ai-tool-intake`
   - `ai-risk-assessment`
   - `ai-vendor-contract-review`
   - `ai-governance-gap-check`
3. 如需求需要真实系统接入、真实 MCP、自动写回或自动审批，标记为超出本阶段范围。
4. 如需求涉及正式制度发布、合同谈判或客户可依赖结论，触发律师复核。

## Output format

- 需求摘要
- 推荐 skill
- 输入材料清单
- 输出草稿类型
- 需律师核验事项
- 超出本阶段范围的事项
- 升级事项

## Quality checks

- 是否标注“律师审阅用草稿”。
- 是否避免把其他插件的业务范围混入本插件。
- 是否禁止直接对外发送、提交或正式发布。
- 是否提示真实资料必须脱敏或在私有环境处理。

## Escalation / attorney review gate

正式 AI 制度、供应商合同意见、跨境处理、个人信息、客户秘密、案件材料、商业秘密、自动化决策和重大声誉风险均需律师或合伙人复核。

## Confidentiality notes

公开仓库不得保存真实客户、真实供应商、真实系统、真实员工或真实合同信息。示例必须虚构。

## Limitations

本技能仅用于路由和规划，不执行完整评估，不提供法律意见，不接入真实系统。
