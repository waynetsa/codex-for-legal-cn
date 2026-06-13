# cn-regulatory-legal Improvement Backlog

> 律师审阅用草稿；本文件只记录虚构验收发现，不构成法律意见。

## 汇总

- P0：0
- P1：3
- P2：3

## P0

无。

## P1

### REG-P1-001 行政处罚风险初筛的程序节点仍偏概括

- 问题描述：`administrative-penalty-risk-triage-result.md` 已提示程序节点和期限待律师核验，但未把来函、材料提交、陈述申辩、听证或复核等通用节点拆开。
- 影响 skill：`administrative-penalty-risk-triage`
- 影响文件：`plugins/cn-regulatory-legal/skills/administrative-penalty-risk-triage/SKILL.md`、`templates/administrative-penalty-risk-triage.md`
- 建议修复方式：增加“程序节点清单”和“节点材料缺口表”，继续避免具体法律结论。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

### REG-P1-002 整改计划的责任追踪字段可更细

- 问题描述：`remediation-plan-builder-result.md` 已包含责任部门、角色、交付物和验收标准，但缺少依赖条件、复核频率和逾期升级字段。
- 影响 skill：`remediation-plan-builder`
- 影响文件：`plugins/cn-regulatory-legal/skills/remediation-plan-builder/SKILL.md`、`templates/remediation-plan.md`
- 建议修复方式：新增依赖条件、复核频率、逾期升级和管理层复盘字段。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

### REG-P1-003 监管问询响应提纲可进一步强化“不得直接提交”的安全闸门

- 问题描述：输出已写不得直接提交，但“不宜直接回复事项”和“正式提交前复核清单”可更突出。
- 影响 skill：`regulatory-inquiry-response-outline`
- 影响文件：`plugins/cn-regulatory-legal/skills/regulatory-inquiry-response-outline/SKILL.md`、`templates/regulatory-inquiry-response-outline.md`
- 建议修复方式：独立列出正式提交前禁止项、审批链和律师复核清单。
- 优先级：P1
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：是

## P2

### REG-P2-001 合规义务清单宽表可读性一般

- 问题描述：`compliance-obligation-map-result.md` 字段完整但较宽。
- 影响 skill：`compliance-obligation-map`
- 影响文件：`templates/compliance-obligation-map.csv`、acceptance output
- 建议修复方式：补充 Markdown 分段模板，把责任部门、台账、缺口、升级事项拆成短表。
- 优先级：P2
- 是否需要律师复核：否
- 是否建议进入下一轮 PR：可选

### REG-P2-002 监管动态影响分析可增加来源核验记录

- 问题描述：当前已写“待律师核验”，但未单独列来源、版本、发布日期、核验人角色。
- 影响 skill：`regulatory-change-impact-brief`
- 影响文件：`templates/regulatory-change-impact-brief.md`
- 建议修复方式：新增“来源核验记录”小表。
- 优先级：P2
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：可选

### REG-P2-003 管理层简报可补董事会版摘要

- 问题描述：当前简报适合管理层阅读，但董事会或高层会议可能需要更压缩的一页版。
- 影响 skill：`management-compliance-briefing`
- 影响文件：`templates/management-compliance-briefing.md`
- 建议修复方式：新增“一页董事会摘要”区域。
- 优先级：P2
- 是否需要律师复核：是
- 是否建议进入下一轮 PR：可选
## Alpha 修复后状态

> 律师审阅用草稿。本节为本轮 regulatory alpha 修复后的状态追加，不删除原始问题记录。

| 编号 | 原优先级 | 修复后状态 | 说明 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- |
| REG-P1-001 | P1 | 已修复 | 行政处罚风险初筛已补充程序节点清单、节点材料缺口表和升级触发。 | 否 |
| REG-P1-002 | P1 | 已修复 | 整改计划已补充依赖条件、复核频率、逾期升级、管理层复盘和留痕要求。 | 否 |
| REG-P1-003 | P1 | 已修复 | 监管问询响应已补充正式提交前禁止项、审批链和律师复核清单。 | 否 |
| REG-P2-001 | P2 | 已缓解，保留为可接受体验优化项 | 已新增 Markdown 分段模板并更新验收输出；复杂业务仍可按模块拆分或使用 CSV。 | 后续体验优化 |
| REG-P2-002 | P2 | 已修复 | 监管动态影响分析已补充来源核验记录。 | 否 |
| REG-P2-003 | P2 | 已修复 | 管理层合规简报已补充一页董事会摘要。 | 否 |

## 修复后发布判断

- P0：0。
- P1：0。
- P2：1 个可接受体验优化项。
- 若验证脚本通过且未发现敏感文件，`cn-regulatory-legal` 可建议作为 alpha 可试用插件进入 `v0.6.0-alpha`。
