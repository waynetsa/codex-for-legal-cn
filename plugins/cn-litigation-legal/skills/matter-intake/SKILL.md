---
name: cn-litigation-matter-intake
description: Draft a China litigation matter intake form for attorney review.
---

# Matter Intake

## Purpose

生成案件 intake 表，帮助团队初步记录案件背景、当事人、请求、程序状态和材料缺口。

## When to use

用于新案件接收、冲突检索准备、项目立项和初步会谈后整理。

## Inputs expected

- 脱敏案件描述。
- 当事人角色、请求或抗辩方向。
- 已有证据和关键日期。

## Workflow

1. 提取案件基本信息。
2. 分类事实、证据和程序状态。
3. 标记材料缺口、时效或期限风险。
4. 输出 intake 表。

## Output format

“律师审阅用草稿”：案件概况、当事人、请求、事实、证据、期限、待确认事项。

## Quality checks

- 不把客户陈述写成已证实事实。
- 关键期限必须标注来源或假设。
- 法律依据不足时写“待律师补充法律依据”。

## Escalation / attorney review gate

涉及诉讼时效、管辖、保全、紧急禁令或重大舆情时立即升级律师。

## Confidentiality notes

不得公开真实当事人、案号、证据和个人信息。

## Limitations

不替代冲突检索、委托手续或正式案件评估。
