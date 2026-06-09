---
name: cn-litigation-chronology-builder
description: Build a structured chronology from sanitized litigation facts and evidence.
---

# Chronology Builder

## Purpose

将脱敏事实材料整理为案件事实时间线，供律师复核和后续文书使用。

## When to use

用于案件分析、证据整理、庭前准备和团队同步。

## Inputs expected

- 脱敏事实陈述。
- 证据摘要、编号和日期。
- 争议焦点或请求方向。

## Workflow

1. 提取日期、事件、参与方和证据来源。
2. 区分已证实、待核实和矛盾事实。
3. 标注与争点或请求的关系。
4. 输出时间线表格。

## Output format

“律师审阅用草稿”：日期、事件、来源证据、事实状态、关联争点、待确认事项。

## Quality checks

- 不补造缺失日期。
- 同一事实多来源矛盾时明确标注。
- 不作未经律师确认的法律定性。

## Escalation / attorney review gate

关键事实、时效、证据真实性和庭审使用前必须由律师复核。

## Confidentiality notes

证据和事实材料不得进入公开仓库。

## Limitations

不替代证据原件核验、证人访谈或诉讼策略判断。
