---
name: cn-commercial-renewal-risk-check
description: Check renewal, termination, notice, and survival risks in China commercial contracts.
---

# Renewal Risk Check

## Purpose

识别合同续约、自动续期、解除、通知期限、存续义务和退出安排风险。

## When to use

用于合同到期前、续约谈判、解除评估或合同管理台账更新。

## Inputs expected

- 脱敏合同文本。
- 当前履行状态、到期日和拟采取动作。
- 已发或拟发通知的摘要。

## Workflow

1. 提取期限、续约、解除和通知条款。
2. 判断关键日期和前置条件。
3. 标出错过期限或触发违约的风险。
4. 输出律师复核清单。

## Output format

“律师审阅用草稿”：关键日期、条款依据、风险、建议动作、待确认事项。

## Quality checks

- 日期计算必须说明假设。
- 不确认未提供的通知送达事实。
- 无来源时写“待律师补充法律依据”。

## Escalation / attorney review gate

拟解除、拒绝续约、索赔或发送正式通知前必须由律师复核。

## Confidentiality notes

不得公开真实履约记录、交易金额或争议背景。

## Limitations

不替代事实调查、送达证明核验和正式法律意见。
