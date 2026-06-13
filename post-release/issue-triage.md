律师审阅用草稿

基于虚构或模拟脱敏试点样例生成

不构成法律意见

# Post-release QA Issue Triage

## 结论

- P0：0
- P1：0
- P2：5
- P3：3

未发现阻碍真实律所受控脱敏试点的问题。P2 可在真实脱敏试点前修复或带入试点观察；P3 作为未来体验优化。

## P2

| issue_id | package | affected plugin / skill | description | severity | recommended action | should fix before real anonymized pilot | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-P2-01 | corporate-diligence | cn-corporate-legal | 部分交易清单字段仍需贴合具体团队的责任人和状态列习惯。 | P2 | 在真实脱敏试点前准备团队字段映射。 | 否 | 可带入试点观察。 |
| QA-P2-02 | privacy-ai-governance | cn-ai-governance-legal, cn-privacy-legal | AI 准入和隐私评估之间的交接节点可进一步标准化。 | P2 | 在试点反馈表中增加跨插件交接评分。 | 否 | 不影响安全边界。 |
| QA-P2-03 | employment-regulatory | cn-employment-legal, cn-regulatory-legal | 劳动争议策略和监管回复口径的联动提示可更细。 | P2 | 真实试点中收集 HR、合规和律师协同反馈。 | 否 | 已有升级事项控制。 |
| QA-P2-04 | all packages | pilot feedback | 缺少统一评分汇总看板。 | P2 | 后续增加 spreadsheet 或 markdown dashboard 模板。 | 否 | 不影响当前 QA。 |
| QA-P2-05 | all packages | docs | 私有试点操作步骤可按律所 IT 流程再细化。 | P2 | 根据首轮真实脱敏试点补充。 | 否 | 当前边界已经明确。 |

## P3

| issue_id | package | affected plugin / skill | description | severity | recommended action | should fix before real anonymized pilot | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-P3-01 | all packages | output format | 部分表格仍可进一步压缩宽度。 | P3 | 后续体验优化。 | 否 | 不影响试点。 |
| QA-P3-02 | all packages | wording | 个别中英术语可继续统一为中国法律法务惯用表达。 | P3 | 后续文案统一。 | 否 | 不影响试点。 |
| QA-P3-03 | all packages | feedback roles | 可增加知识管理或 IT 合规角色反馈。 | P3 | 后续扩展评测角色。 | 否 | 不属于本轮范围。 |
