---
name: core-workflow-placeholder
description: 说明 中国个人信息与数据合规工作流 后续 MVP 可拆分的具体 skills；当前仅为 scaffold，占位规划，不处理真实事项。
---

# Core Workflow Placeholder

## Purpose

说明 `cn-privacy-legal` 后续 MVP 可能拆分的具体 skills，并为第二阶段规划保留结构。本阶段只做骨架，不展开完整业务内容。所有输出均为“律师审阅用草稿”。

## When to use

- 规划第二阶段插件路线图时。
- 讨论该插件是否进入 MVP 开发时。
- 为后续模板、references、evals 设计目录边界时。

## Inputs expected

- 拟处理的事项类型：个人信息保护、数据处理协议、数据出境、隐私影响评估、隐私政策审阅、数据合规清单。
- 目标用户：律所团队、公司法务、知识管理、合规负责人或法律教育场景。
- 预期输出：清单、表格、备忘录、台账或复核提纲。

## Workflow

1. 确认当前插件仅为 scaffold，不用于真实事项处理。
2. 根据团队 profile 判断后续优先拆分哪些具体 skills。
3. 记录所需模板、参考清单、评测样例和 guardrails。
4. 将具体业务能力留到后续 MVP PR 中逐项展开。

## Output format

后续可拆分 skills 建议：

- `privacy-policy-review`
- `data-processing-agreement-review`
- `cross-border-data-transfer-check`
- `privacy-impact-assessment`
- `data-compliance-checklist`

每个后续 skill 在 MVP 阶段应补充 Purpose、When to use、Inputs expected、Workflow、Output format、Quality checks、Escalation / attorney review gate、Confidentiality notes、Limitations。

## Quality checks

- 是否明确“scaffold only”。
- 是否没有写成正式法律意见。
- 是否没有虚构具体法规条文、案例、监管观点或法院观点。
- 是否没有加入真实客户或真实案件材料。

## Escalation / attorney review gate

本占位技能不得直接用于客户交付。任何正式使用前，必须由对应业务领域律师确认 skill、template、reference、eval 和 guardrail。

## Confidentiality notes

只允许使用虚构、脱敏或公开可复核的材料规划插件。不得提交真实客户名、真实项目名、真实合同、真实个人信息、商业秘密或密钥。

## Limitations

本文件只描述未来拆分方向，不提供可试用 MVP 能力。进入 MVP 前必须单独创建 PR，补充完整工作流、模板、评测样本和安全边界。
