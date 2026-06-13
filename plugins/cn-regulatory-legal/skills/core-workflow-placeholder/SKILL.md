---
name: core-workflow-placeholder
description: 说明 cn-regulatory-legal MVP 已拆分的核心监管合规工作流，以及本技能仅作为导航占位使用。
---

# Core Workflow Placeholder

## Purpose

为 `cn-regulatory-legal` 提供工作流导航。本插件已进入 MVP 阶段，核心能力拆分为监管动态影响分析、合规义务清单、监管问询响应、行政处罚风险初筛、整改计划和管理层合规简报。

## When to use

- 用户不确定应该使用哪个 regulatory skill 时。
- 需要了解监管合规插件的 MVP 能力边界时。

## Inputs expected

- 用户的监管合规事项描述。
- 行业、监管主题、材料类型和期望输出。

## Workflow

1. 判断用户事项属于监管动态、合规义务、问询响应、处罚风险、整改计划还是管理层简报。
2. 推荐对应技能。
3. 提醒用户仅使用虚构或脱敏材料。
4. 提醒所有输出均为“律师审阅用草稿”，不构成法律意见。

## Output format

- 推荐技能名称。
- 适用原因。
- 所需输入材料。
- 安全边界和律师复核提示。

## Quality checks

- 是否避免把本技能当作正式业务输出。
- 是否提示不得使用真实监管材料或客户资料。
- 是否提示法律依据和监管口径待律师核验。

## Escalation / attorney review gate

如用户请求正式监管回复、正式整改报告、正式合规结论、处罚判断或对外公告，应停止并要求律师复核。

## Confidentiality notes

不得输入真实监管材料、客户经营数据、个人信息、商业秘密或私有配置。

## Limitations

本技能仅用于导航，不生成正式监管合规成果。
