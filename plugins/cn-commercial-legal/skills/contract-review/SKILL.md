---
name: cn-commercial-contract-review
description: Draft a China commercial contract review memo for attorney review.
---

# Contract Review

## Purpose

基于脱敏合同文本生成合同审查备忘录和风险清单，供律师复核。

## When to use

用于销售合同、采购合同、服务合同、供应商合同和其他商事合同初步审查。

## Inputs expected

- 脱敏合同文本或条款摘要。
- 客户角色、交易背景和谈判阶段。
- 关注条款、内部 playbook 或风险等级口径。

## Workflow

1. 提取合同基本信息。
2. 识别关键义务、付款、交付、验收、违约、责任限制、解除、争议解决等条款。
3. 按风险等级列出问题。
4. 给出待律师确认的修改方向。

## Output format

“律师审阅用草稿”：事实摘要、风险清单、建议修改方向、待确认事项、升级事项。

## Quality checks

- 法律依据不确定时写“待律师补充法律依据”。
- 风险与合同条款逐项对应。
- 不把商业建议伪装为法律结论。

## Escalation / attorney review gate

重大责任、解除、赔偿、合规、数据、争议解决和高金额条款必须升级给律师。

## Confidentiality notes

仅处理脱敏文本，不保留真实主体和商业秘密。

## Limitations

不替代完整法律审查、商业谈判判断或客户授权确认。
