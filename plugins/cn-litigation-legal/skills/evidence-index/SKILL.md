---
name: cn-litigation-evidence-index
description: Create an evidence index from sanitized litigation materials.
---

# Evidence Index

## Purpose

生成证据目录草稿，帮助律师整理证据名称、来源、证明目的和待核验事项。

## When to use

用于证据交换、庭前会议、开庭准备和内部案件管理。

## Inputs expected

- 脱敏证据清单。
- 证据摘要、日期、来源和关联事实。
- 拟证明事项。

## Workflow

1. 整理证据编号和名称。
2. 关联事实时间线和争点。
3. 标注证明目的、形式要求和缺口。
4. 输出证据目录。

## Output format

“律师审阅用草稿”：编号、证据名称、日期、来源、证明目的、关联事实、待核验事项。

## Quality checks

- 不确认证据真实性。
- 不虚构证明目的。
- 证据缺口进入待确认事项。

## Escalation / attorney review gate

证据提交、真实性判断、证明责任和举证期限必须由律师确认。

## Confidentiality notes

不得公开真实证据、案号、个人信息和商业秘密。

## Limitations

不替代证据规则分析、原件核验或庭审策略。
