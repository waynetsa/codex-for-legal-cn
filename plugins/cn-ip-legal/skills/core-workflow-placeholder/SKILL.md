---
name: core-workflow-placeholder
description: 说明 cn-ip-legal 已从 scaffold 进入 MVP，核心 workflow 已拆分为权属链条、侵权初筛、授权审查、证据保全和函件/下架提纲；不提供法律意见。
---

# Core Workflow Placeholder

## Purpose

记录 `cn-ip-legal` 从 scaffold 进入 MVP 后的核心工作流拆分。后续不应继续在本占位技能中承载业务细节，而应使用具体 MVP skills。

## When to use

- 需要了解 `cn-ip-legal` 当前 MVP 能力边界时。
- 规划后续端到端验收或新 skill 拆分时。

## Inputs expected

- 团队 practice profile。
- 拟处理的 IP 或文化传媒事项类型。
- 目标输出：权属链条表、侵权初筛表、授权审查备忘录、证据保全清单、下架/函件提纲。

## Workflow

1. 先确认事项是否属于 `cn-ip-legal` MVP 范围。
2. 根据事项类型选择具体 skill：
   - `rights-chain-review`
   - `infringement-triage`
   - `ip-license-review`
   - `evidence-preservation-checklist`
   - `takedown-and-demand-letter-outline`
3. 如事项超出范围，记录为后续 backlog，不在本轮扩展。

## Output format

- 推荐使用的具体 skill。
- 所需输入材料清单。
- 待律师核验事项。
- 是否需要升级。

## Quality checks

- 是否标注“律师审阅用草稿”。
- 是否区分事实、风险、建议、待确认事项。
- 是否写明法律依据、权利基础、证据来源均“待律师核验”。
- 是否避免直接作出最终侵权、权属或责任结论。
- 是否将高风险、红旗风险、期限紧迫或证据灭失风险列入升级事项。

## Escalation / attorney review gate

以下事项必须由执业律师、主办律师或合伙人复核：对外发送函件、平台投诉、诉讼或仲裁提交、证据保全申请、权属链条重大缺口、独占/排他授权、重大金额、跨境授权、商业秘密、可能涉及行政或刑事风险、重大舆情风险。AI 输出不得直接作为法律意见、律师函、投诉材料或客户决策依据。

## Confidentiality notes

真实权利文件、合同、底稿、证据、平台后台截图、未公开内容素材、客户名称、个人信息和商业秘密必须在私有环境处理并脱敏。公开仓库只保存模板、流程和虚构样例，不得提交密钥、token、Cookie 或私有系统配置。

## Limitations

本技能不提供法律意见，不确认权属、侵权、混淆、损害赔偿、平台规则适用或诉讼胜率。涉及法律依据、案例、法规、法院观点和平台规则时，应写“待律师核验”。
