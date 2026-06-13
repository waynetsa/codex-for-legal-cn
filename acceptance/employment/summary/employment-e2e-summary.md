# cn-employment-legal 端到端验收总结

> 律师审阅用草稿；本轮只使用虚构材料，不构成法律意见。

## 一、本轮验收范围

本轮验证 `cn-employment-legal` MVP 是否能基于虚构员工解除争议和用工合规材料，完成以下路径：

- cold-start
- employment-contract-review
- employee-handbook-review
- termination-risk-triage
- non-compete-review
- outsourcing-dispatch-risk-check
- workplace-investigation-plan
- labor-dispute-evidence-pack

## 二、端到端路径是否完成

已完成。所有输入、输出、评测表、findings、summary 和 backlog 均已沉淀到 `acceptance/employment/`。

## 三、各 skill 通过项

| Skill | 通过项 |
|---|---|
| cold-start | 生成团队画像、风险偏好、升级事项、证据和个人信息规则 |
| employment-contract-review | 覆盖岗位、地点、期限、薪酬、社保、竞业、解除终止等合同风险 |
| employee-handbook-review | 覆盖制度内容、民主程序、公示送达、证据留存和个人信息提示 |
| termination-risk-triage | 能识别病假、特殊保护、解除程序、补偿和禁止直接执行事项 |
| non-compete-review | 能识别竞业范围、期限、地域、补偿、违约责任和商业秘密风险 |
| outsourcing-dispatch-risk-check | 能识别直接管理、考勤、设备、权限和混同管理风险 |
| workplace-investigation-plan | 能形成调查目标、范围、事实问题、证据、访谈和保护提示 |
| labor-dispute-evidence-pack | 能形成时间线、争点、证据目录、证明目的和三性提示 |

## 四、主要问题

- P1：解除风险初筛中的补偿或赔偿风险字段仍偏概括。
- P1：内部调查访谈提纲仍可更细。
- P1：劳动争议证据包缺少按争点分组的辅助视图。
- P2：部分表格较宽。
- P2：客户可读摘要仍可进一步模板化。
- P2：references 可补更细的裁员、待岗、调岗降薪清单。

## 五、是否达到 employment MVP acceptance 标准

达到。没有发现 P0 问题。P1 问题影响效率和精细度，但不阻碍虚构样例试跑。当前不建议立即发布 `v0.5.0-alpha`，建议先完成 employment alpha 修复。

## 六、是否建议标记为 alpha 可试用

暂不建议立即标记为 alpha 可试用。建议下一轮根据 `employment-improvement-backlog.md` 修复 P1/P2，再判断是否进入 `v0.5.0-alpha`。

## 七、下一步建议

合并本 PR 后，开一个 employment alpha 修复 PR，优先清理 P1，再视情况发布 `v0.5.0-alpha`。不要马上开发 `cn-regulatory-legal`。
