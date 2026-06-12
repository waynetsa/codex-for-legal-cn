# AI Governance Regression After Alpha Fixes

> 律师审阅用草稿。本回归记录基于虚构材料生成，不构成法律意见。

## 本轮修复对应的 P1/P2

| 编号 | 原问题 | 修复状态 | 主要修改位置 |
| --- | --- | --- | --- |
| P1-1 | AI 供应商合同审查的建议替代表述仍偏通用 | 已修复 | `ai-vendor-contract-review` skill、template、acceptance output |
| P1-2 | 治理差距整改路线图缺少责任角色、截止时间和验收证据 | 已修复 | `ai-governance-gap-check` skill、template、acceptance output |
| P1-3 | AI 工具准入需区分试点、灰度上线和正式上线 | 已修复 | `ai-tool-intake` skill、template、acceptance output |
| P2-1 | 部分输出表格较宽 | 已缓解 | acceptance outputs 拆为核心表、控制表、升级表 |
| P2-2 | AI 使用制度草稿缺少员工培训和签收附件 | 已修复 | `ai-use-policy-builder` template、acceptance output |
| P2-3 | reference 可补充事故响应和输出监控 | 已修复 | `ai-vendor-review-checklist.md`、`china-ai-governance-workflow-checklist.md`、`law-firm-internal-ai-use-checklist.md` |

## 修改过的 skills、templates、references

- Skills：`ai-use-policy-builder`、`ai-tool-intake`、`ai-risk-assessment`、`ai-vendor-contract-review`、`ai-governance-gap-check`。
- Templates：`ai-use-policy-outline.md`、`ai-tool-intake-form.md`、`ai-risk-assessment-table.md`、`ai-vendor-contract-review-memo.md`、`ai-governance-gap-checklist.md`。
- References：`china-ai-governance-workflow-checklist.md`、`ai-vendor-review-checklist.md`、`law-firm-internal-ai-use-checklist.md`。
- Profile：`practice-profile.template.md`。

## AI 使用制度路径回归结果

制度输出已拆成制度框架、禁止输入清单、审批矩阵、人工复核清单、培训签收和升级事项。客户交付、外部发布、自动回复、自动决策、合同或法律材料输出均触发复核。

## AI 工具准入路径回归结果

准入输出已增加工具类型、部署方式、员工个人账号、供应商安全材料、合同和隐私政策字段，并增加“可低风险试用 / 条件性试用 / 暂缓上线 / 禁止上线，待人工复核”分级。

## AI 风险评估路径回归结果

风险评估已围绕输入、处理、输出、使用后果展开，并增加供应商依赖、审计不可追踪、责任人、上线前整改和升级字段。

## AI 供应商合同审查路径回归结果

供应商审查已增加“供应商口径 / 客户口径 / 折中谈判语言”表，并将客户商务决策事项和合伙人升级事项独立展示。

## AI 治理差距检查路径回归结果

整改路线图已按 30/90/180 天拆分，并为每项整改增加目标、责任部门、交付物、优先级、依赖条件、截止时间、验收证据和管理层决策字段。

## 是否产生新的风险

未发现新的 P0 风险。新增字段可能增加填写工作量，但提升了准入、谈判、整改和复核的可执行性。

## P0/P1/P2 剩余数量

- P0：0
- P1：0
- P2：1，属于可接受体验优化项：后续可继续优化紧凑视图和表格阅读体验。

## 是否达到发布 v0.3.0-alpha 标准

达到。`cn-ai-governance-legal` 已完成 MVP、acceptance、alpha 修复和 regression；P0 为 0，P1 清零，剩余 P2 不影响 alpha 试用。`cn-privacy-legal`、`cn-employment-legal`、`cn-regulatory-legal` 仍为 scaffold。
