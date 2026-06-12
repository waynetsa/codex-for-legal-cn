# IP Regression After Alpha Fixes

> 律师审阅用草稿。本回归记录仅使用虚构材料，不构成法律意见。

## 修复对应的 P1/P2

| 编号 | backlog 问题 | 修复状态 | 主要修改位置 |
| --- | --- | --- | --- |
| P1-1 | 侵权初筛缺少比对材料优先级和比对方法说明 | 已修复 | `infringement-triage` skill、template、acceptance output |
| P1-2 | 授权审查替代表述颗粒度仍偏通用 | 已修复 | `ip-license-review` skill、template、acceptance output |
| P1-3 | 平台投诉材料清单可更细 | 已修复 | `takedown-and-demand-letter-outline` skill、template、reference、acceptance output |
| P2-1 | 权属链条表较宽 | 已缓解 | `rights-chain-review` skill、template、acceptance output |
| P2-2 | 证据保全清单字段较多 | 已缓解 | `evidence-preservation-checklist` skill、CSV template、acceptance output |
| P2-3 | acceptance README 可增加快速导航 | 已修复 | `acceptance/ip/README.md` |

## 修改过的 skills、templates、references

- Skills：`rights-chain-review`、`infringement-triage`、`ip-license-review`、`evidence-preservation-checklist`、`takedown-and-demand-letter-outline`。
- Templates：权属链条、侵权初筛、授权审查、证据保全 CSV、下架/函件提纲。
- References：`platform-takedown-workflow.md`、`china-ip-workflow-checklist.md`。

## 权属链条路径回归结果

权属链条输出已拆成核心权属链条、授权范围、权利缺口、升级事项四个短表。可改编、可转授权、可商业化、可平台传播、可海外使用均单独列项。

## 侵权初筛路径回归结果

已增加比对材料优先级、比对方法、需专业比对事项和下一步路径。输出继续避免最终侵权结论。

## 授权审查路径回归结果

已将替代表述拆分为授权方口径、被授权方口径和折中谈判语言，并单独列出客户商务决策和合伙人升级事项。

## 证据保全路径回归结果

已拆分证据分类表和紧急保全事项表，保留证明目的、来源、形成时间、保存方式、原始载体、三性提示、关联争点和待补强事项。

## 平台投诉 / 律师函提纲路径回归结果

已增加平台材料自查清单和提交前复核表，明确平台投诉、下架通知、律师函、商务沟通函和诉前保全准备的边界。

## 是否产生新的风险

未发现新的 P0 风险。新增字段可能增加填写工作量，但提升了律师复核和对外提交前的安全边界。

## P0/P1/P2 剩余数量

- P0：0
- P1：0
- P2：2，均为可接受体验优化项：表格紧凑视图和证据筛选视图后续可继续优化。

## 是否达到发布 v0.2.0-alpha 标准

达到。`cn-ip-legal` 已完成 MVP、acceptance、alpha 修复和 regression；P0 为 0，P1 清零，剩余 P2 不影响 alpha 试用。其他第二阶段插件仍为 scaffold。
