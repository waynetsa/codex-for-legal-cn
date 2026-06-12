# Regression After Alpha Fixes

> 律师审阅用草稿。本回归记录仅使用虚构材料，验证 P1/P2 可用性修复，不构成法律意见。

## 修复对应的 P1/P2

| 编号 | backlog 问题 | 处理结果 | 主要修改位置 |
| --- | --- | --- | --- |
| P1-1 | 合同替代表述仍需律师二次加工 | 已修复 | `contract-review` skill、合同审查模板、合同验收输出 |
| P1-2 | 并购重大性判断未充分连接估值、赔偿和先决条件 | 已修复 | `issue-extraction` skill、尽调摘要模板、并购验收输出 |
| P1-3 | 诉讼时间线需区分全量事件和关键事件 | 已修复 | `chronology-builder` skill、时间线 CSV 模板、诉讼验收输出 |
| P1-4 | 期限和保全字段需更突出 | 已修复 | `matter-intake`、`hearing-prep` skills、诉讼模板和验收输出 |
| P2-1 | eval sheet 可增加总体结论字段 | 已修复 | `shared/evals/sample-eval-sheet.csv` |
| P2-2 | acceptance 入口可增加文件索引 | 已修复 | `acceptance/README.md` |
| P2-3 | 部分输出表格较宽 | 已缓解 | `shared/templates/output-quality-checklist.md`；保留为后续体验优化 |

## 修改过的 skill 或 template

- 合同：`contract-review`、`deviation-memo`、`renewal-risk-check` 及合同审查、偏离清单、升级说明模板。
- 并购：`diligence-tabular-review`、`issue-extraction`、`closing-checklist`、`disclosure-schedule` 及尽调问题、摘要、交割清单、重大合同模板。
- 诉讼：`chronology-builder`、`matter-intake`、`hearing-prep`、`evidence-index`、`issue-chart`、`matter-status` 及时间线、证据目录、争点表、庭前准备、案件周报模板。
- 共享：评测样表、升级矩阵、风险等级说明、输出质量检查清单。

## 合同路径回归结果

- 替代表述已从原则性建议拆分为“建议修改方向 / 建议替代表述 / 建议谈判语言 / 客户商务决策”。
- 偏离清单增加 playbook 位置、原条款问题、风险等级、客户决策和合伙人升级字段。
- 续约和解除风险突出自动续约触发条件、通知期限、错过通知期后果、解除权对等性和数据返还义务。
- 高风险和红旗风险仍进入升级事项。

## 并购路径回归结果

- 尽调问题表增加估值、陈述保证、赔偿、交割条件和交割后义务字段。
- 重大红旗事项能够映射到交割前条件、披露清单和客户决策。
- 披露清单要求写明已确认事实、待补材料和律师核验点，避免空泛描述。

## 诉讼路径回归结果

- 时间线增加事件层级、关键程度、程序期限或证据期限、期限来源和升级字段。
- matter intake 与 hearing prep 增加期限与保全专项。
- 证据目录和争点表更接近律师可直接编辑格式。
- 周报强调简短进展、期限提醒和升级事项，避免写成完整案情分析。

## 是否产生新的风险

未发现新的 P0 风险。需要注意的是，新增字段可能让表格变宽；已通过输出质量检查清单要求必要时拆分为风险表、升级表和待确认表。

## 是否仍达到 alpha 可试用标准

仍达到。三个核心插件的端到端路径均保留“律师审阅用草稿”、待律师核验、升级事项和虚构材料边界。

## 是否建议进入 v0.1.1-alpha

建议进入 `v0.1.1-alpha` 候选。P1 已清零，P2 中“表格较宽”保留为可接受的体验优化项。
