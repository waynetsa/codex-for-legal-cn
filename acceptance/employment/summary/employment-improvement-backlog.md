# cn-employment-legal Improvement Backlog

> 律师审阅用草稿；本文件仅记录虚构验收发现，不构成法律意见。

## 汇总

- P0：0
- P1：3
- P2：3

## P0

无。

## P1

### EMP-P1-001 解除风险初筛中的补偿或赔偿风险字段仍偏概括

- 问题描述：`termination-risk-triage-result.md` 能提示补偿或赔偿风险待律师核验，但缺少测算材料、测算口径、客户决策事项和责任人字段。
- 影响 skill：`termination-risk-triage`
- 影响文件：`plugins/cn-employment-legal/skills/termination-risk-triage/SKILL.md`、`templates/termination-risk-triage-table.md`
- 建议修复方式：增加“补偿或赔偿测算材料清单”“待客户确认口径”“管理层决策人”字段。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

### EMP-P1-002 内部调查访谈提纲仍可更细

- 问题描述：`workplace-investigation-plan-result.md` 已列访谈对象和重点，但未拆分开放问题、封闭确认、证据确认、风险告知和反报复提示。
- 影响 skill：`workplace-investigation-plan`
- 影响文件：`plugins/cn-employment-legal/skills/workplace-investigation-plan/SKILL.md`、`templates/workplace-investigation-plan.md`
- 建议修复方式：把访谈提纲拆成结构化问题表，并加入访谈前提示和记录确认字段。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

### EMP-P1-003 劳动争议证据包缺少按争点分组视图

- 问题描述：证据目录已完整，但律师仍需二次整理哪些证据支持哪个争点。
- 影响 skill：`labor-dispute-evidence-pack`
- 影响文件：`plugins/cn-employment-legal/skills/labor-dispute-evidence-pack/SKILL.md`、`templates/labor-dispute-evidence-pack.md`
- 建议修复方式：增加“争点-证据映射表”和“证据缺口按争点汇总表”。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

## P2

### EMP-P2-001 部分表格较宽

- 问题描述：合同审查、竞业和争议证据包输出字段较多，在移动端或窄屏阅读体验一般。
- 影响 skill：多个 employment skills
- 影响文件：templates 和 acceptance output
- 建议修复方式：拆分为核心表、待补材料表、升级事项表。
- 优先级：P2
- 是否需要律师复核：否
- 是否建议进入下一轮 PR：可选

### EMP-P2-002 客户可读摘要仍可进一步模板化

- 问题描述：当前输出偏律师内部工作底稿，缺少一段简短客户摘要模板。
- 影响 skill：`employment-contract-review`、`termination-risk-triage`
- 影响文件：相关 templates
- 建议修复方式：增加“可给客户看的简明摘要草稿”，但保留律师复核提醒。
- 优先级：P2
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：可选

### EMP-P2-003 references 可补更细的裁员、待岗、调岗降薪清单

- 问题描述：当前 termination checklist 覆盖解除和调整，但裁员、待岗、调岗降薪可进一步拆分。
- 影响 skill：`termination-risk-triage`
- 影响文件：`references/termination-risk-triage-checklist.md`
- 建议修复方式：新增三个小节，分别列出事实、程序、证据和升级事项。
- 优先级：P2
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：可选
## Alpha 修复后状态

> 以下为追加记录，不删除原始 backlog。

| 编号 | 优先级 | 修复后状态 | 说明 |
|---|---|---|---|
| EMP-P1-001 | P1 | 已修复 | 解除风险初筛已增加补偿或赔偿测算材料清单、测算口径、客户决策事项、责任人和待律师核验事项。 |
| EMP-P1-002 | P1 | 已修复 | 内部调查访谈提纲已结构化为开放问题、封闭确认、证据确认、风险告知、记录确认和反报复提示。 |
| EMP-P1-003 | P1 | 已修复 | 劳动争议证据包已增加争点-证据映射表和证据缺口按争点汇总表。 |
| EMP-P2-001 | P2 | 已缓解，保留为可接受体验优化项 | 宽表已拆为多个短表；复杂事项仍可能需要横向滚动，但不影响 alpha 试用。 |
| EMP-P2-002 | P2 | 已修复 | 增加客户可读摘要草稿，且保留律师复核提醒。 |
| EMP-P2-003 | P2 | 已修复 | termination reference 已补充裁员、待岗、调岗降薪专项清单。 |

最终状态：P0 为 0，P1 为 0，P2 为 1 个可接受体验优化项。若验证通过并完成合并，建议发布 `v0.5.0-alpha`。
