# Improvement Backlog

## P0

当前未发现 P0 阻碍项。

## P1

| 问题描述 | 影响插件 | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| 合同替代表述仍需律师二次加工 | cn-commercial-legal | plugins/cn-commercial-legal/templates/contract-review-memo.md; plugins/cn-commercial-legal/skills/contract-review/SKILL.md | 增加替代表述示例结构和谈判语言字段 | P1 | 是 | 是 |
| 并购重大性判断未充分连接估值、赔偿和先决条件 | cn-corporate-legal | plugins/cn-corporate-legal/skills/issue-extraction/SKILL.md; plugins/cn-corporate-legal/templates/diligence-summary-memo.md | 增加交易文件影响分栏 | P1 | 是 | 是 |
| 诉讼时间线需更明确区分全量事件和关键事件 | cn-litigation-legal | plugins/cn-litigation-legal/skills/chronology-builder/SKILL.md; plugins/cn-litigation-legal/templates/chronology-table.csv | 增加“关键程度”和“程序期限”字段 | P1 | 是 | 是 |
| 期限和保全字段需更突出 | cn-litigation-legal | plugins/cn-litigation-legal/skills/matter-intake/SKILL.md; plugins/cn-litigation-legal/skills/hearing-prep/SKILL.md | 增加期限和保全专项输出要求 | P1 | 是 | 是 |

## P2

| 问题描述 | 影响插件 | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| eval sheet 可增加总体结论字段 | shared evals | shared/evals/sample-eval-sheet.csv | 增加 pass_fail 或 reviewer_action 字段 | P2 | 否 | 是 |
| acceptance 入口可增加文件索引 | acceptance | acceptance/README.md | 增加三条路径文件清单 | P2 | 否 | 是 |
| 部分输出表格较宽 | acceptance outputs | acceptance/*/output/*.md | 后续提供紧凑版模板 | P2 | 否 | 可选 |
