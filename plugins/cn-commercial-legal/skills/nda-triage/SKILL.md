---
name: cn-commercial-nda-triage
description: Triage a China NDA and produce a structured issue table for attorney review.
---

# NDA Triage

## Purpose

快速识别 NDA 中的保密范围、例外、期限、使用限制、返还销毁、违约责任和争议解决风险。

## When to use

用于项目早期 NDA、双向或单向保密协议、供应商或合作方保密安排初筛。

## Inputs expected

- 脱敏 NDA 文本。
- 客户披露方或接收方角色。
- 交易背景和保密信息类型。

## Workflow

1. 判断协议类型和客户角色。
2. 提取核心条款。
3. 标注偏离市场或内部口径的条款。
4. 输出需要律师进一步处理的问题。

## Output format

“律师审阅用草稿”表格：条款、现有表述、风险、建议、待确认事项。

## Quality checks

- 不虚构条款。
- 不扩大材料未载明的义务。
- 法律依据不足时写“待律师补充法律依据”。

## Escalation / attorney review gate

涉及高额违约金、无限期保密、竞业限制、个人信息或跨境披露时升级律师。

## Confidentiality notes

不得提交真实交易代号、技术秘密或商业计划。

## Limitations

仅为初筛，不替代律师对保密策略和谈判立场的判断。
