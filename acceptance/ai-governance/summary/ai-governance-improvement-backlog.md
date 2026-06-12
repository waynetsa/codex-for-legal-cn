# AI Governance Improvement Backlog

> 律师审阅用草稿。本 backlog 基于虚构验收材料形成，不构成法律意见。

## P0

当前未发现 P0 阻碍项。

## P1

| 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| AI 供应商合同审查的建议替代表述仍偏通用 | ai-vendor-contract-review | plugins/cn-ai-governance-legal/skills/ai-vendor-contract-review/SKILL.md; templates/ai-vendor-contract-review-memo.md | 增加供应商口径、客户口径、折中谈判语言三栏 | P1 | 是 | 是 |
| 治理差距整改路线图缺少责任角色、截止时间和验收证据 | ai-governance-gap-check | plugins/cn-ai-governance-legal/skills/ai-governance-gap-check/SKILL.md; templates/ai-governance-gap-checklist.md | 在 30/90/180 天整改建议中增加责任角色、截止时间、验收证据 | P1 | 是 | 是 |
| AI 工具准入可进一步区分试点、灰度上线和正式上线 | ai-tool-intake | plugins/cn-ai-governance-legal/skills/ai-tool-intake/SKILL.md; templates/ai-tool-intake-form.md | 增加上线阶段、试点期限、复盘条件和退出条件 | P1 | 是 | 是 |

## P2

| 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| 部分输出表格较宽 | all | acceptance/ai-governance/output/*.md | 增加紧凑视图和详细视图 | P2 | 否 | 可选 |
| AI 使用制度草稿缺少员工培训和签收附件 | ai-use-policy-builder | templates/ai-use-policy-outline.md | 增加培训记录和签收确认模板 | P2 | 是 | 是 |
| reference 可补充事故响应和输出监控 | references | references/ai-vendor-review-checklist.md; references/china-ai-governance-workflow-checklist.md | 增加事故响应、输出监控、定期复盘检查项 | P2 | 是 | 可选 |

## 发布判断

P0 为 0，P1 可控。建议下一轮先做 AI governance alpha 修复，修复后再考虑发布 `v0.3.0-alpha`，本轮不发布新 tag。

## Alpha 修复后状态

| 原优先级 | 问题描述 | 当前状态 | 是否影响发布 |
| --- | --- | --- | --- |
| P1 | AI 供应商合同审查的建议替代表述仍偏通用 | 已修复 | 不影响 |
| P1 | 治理差距整改路线图缺少责任角色、截止时间和验收证据 | 已修复 | 不影响 |
| P1 | AI 工具准入需区分试点、灰度上线和正式上线 | 已修复 | 不影响 |
| P2 | 部分输出表格较宽 | 已缓解，保留为后续体验优化 | 不影响 |
| P2 | AI 使用制度草稿缺少员工培训和签收附件 | 已修复 | 不影响 |
| P2 | reference 可补充事故响应和输出监控 | 已修复 | 不影响 |

最终判断：P0 为 0，P1 为 0，P2 仅剩可接受体验优化项。建议发布 `v0.3.0-alpha`。
