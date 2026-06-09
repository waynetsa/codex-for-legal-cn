---
name: cn-commercial-deviation-memo
description: Create a deviation memo comparing contract terms against an approved playbook.
---

# Deviation Memo

## Purpose

将合同条款与律所或客户 playbook 进行对比，形成偏离清单。

## When to use

用于标准合同、客户模板、供应商模板或交易对手修订稿的偏离审查。

## Inputs expected

- 脱敏合同文本。
- 已批准的 playbook 或标准条款摘要。
- 风险等级和审批规则。

## Workflow

1. 识别合同条款和对应 playbook 项。
2. 标记一致、轻微偏离、重大偏离和缺失条款。
3. 写明偏离影响和建议处理方式。
4. 生成升级清单。

## Output format

“律师审阅用草稿”：偏离清单、风险等级、建议、审批或升级对象。

## Quality checks

- 每项偏离必须对应具体条款或缺失项。
- 无 playbook 支持时写明待律师确认。
- 不自行创建未授权标准。

## Escalation / attorney review gate

重大偏离、审批例外和客户授权不足事项必须交由律师确认。

## Confidentiality notes

内部 playbook 可能属于敏感资料，公开仓库不得保存真实版本。

## Limitations

依赖输入 playbook 的完整性，不判断商业上是否接受偏离。
