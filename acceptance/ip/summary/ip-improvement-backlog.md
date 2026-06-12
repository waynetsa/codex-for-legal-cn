# IP Improvement Backlog

> 律师审阅用草稿。本 backlog 基于虚构验收材料形成，不构成法律意见。

## P0

当前未发现 P0 阻碍项。

## P1

| 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| 侵权初筛缺少比对材料优先级和比对方法说明 | infringement-triage | plugins/cn-ip-legal/skills/infringement-triage/SKILL.md; plugins/cn-ip-legal/templates/infringement-triage-table.md | 增加“比对材料优先级”“比对方法”“需专业比对事项”字段 | P1 | 是 | 是 |
| 授权审查替代表述颗粒度仍偏通用 | ip-license-review | plugins/cn-ip-legal/skills/ip-license-review/SKILL.md; plugins/cn-ip-legal/templates/ip-license-review-memo.md | 区分授权方口径、被授权方口径和折中谈判语言 | P1 | 是 | 是 |
| 平台投诉材料清单可更细 | takedown-and-demand-letter-outline | plugins/cn-ip-legal/templates/takedown-demand-letter-outline.md; plugins/cn-ip-legal/references/platform-takedown-workflow.md | 增加平台材料自查清单和提交前复核表 | P1 | 是 | 是 |

## P2

| 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- |
| 权属链条表较宽 | rights-chain-review | plugins/cn-ip-legal/templates/rights-chain-table.md; acceptance/ip/output/rights-chain-review-result.md | 提供紧凑版和详细版两种输出 | P2 | 否 | 可选 |
| 证据保全清单字段较多 | evidence-preservation-checklist | plugins/cn-ip-legal/templates/evidence-preservation-checklist.csv | 增加按“维权/应诉/平台投诉”筛选字段 | P2 | 否 | 可选 |
| acceptance README 可增加快速导航 | all | acceptance/ip/README.md | 增加输入、输出、评测、summary 的文件清单表 | P2 | 否 | 可选 |

## Alpha 修复后状态

| 原优先级 | 问题描述 | 当前状态 | 是否影响发布 |
| --- | --- | --- | --- |
| P1 | 侵权初筛缺少比对材料优先级和比对方法说明 | 已修复 | 不影响 |
| P1 | 授权审查替代表述颗粒度仍偏通用 | 已修复 | 不影响 |
| P1 | 平台投诉材料清单可更细 | 已修复 | 不影响 |
| P2 | 权属链条表较宽 | 已缓解，后续可继续优化紧凑视图 | 不影响 |
| P2 | 证据保全清单字段较多 | 已缓解，后续可继续优化筛选视图 | 不影响 |
| P2 | acceptance README 可增加快速导航 | 已修复 | 不影响 |

最终判断：P0 为 0，P1 为 0，P2 仅剩可接受体验优化项。建议发布 `v0.2.0-alpha`。
