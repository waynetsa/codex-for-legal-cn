# cn-regulatory-legal Planned E2E Scenarios

> 律师审阅用草稿；本文件仅记录后续端到端验收计划。

## 场景一：虚构监管问询响应

- 输入：虚构监管问询摘要、虚构企业业务说明、虚构材料清单。
- 路径：cold-start -> regulatory-inquiry-response-outline -> administrative-penalty-risk-triage。
- 验收重点：不得生成正式监管回复；能列出待补事实、提交材料、内部分工、回复口径风险和升级事项。

## 场景二：虚构监管动态影响分析

- 输入：虚构政策变化摘要和虚构业务模块。
- 路径：regulatory-change-impact-brief -> compliance-obligation-map -> management-compliance-briefing。
- 验收重点：不得虚构监管趋势；能区分业务影响、可能义务、待确认事实和管理层关注事项。

## 场景三：虚构合规整改计划

- 输入：虚构自查发现、虚构整改缺口、虚构责任部门。
- 路径：administrative-penalty-risk-triage -> remediation-plan-builder -> management-compliance-briefing。
- 验收重点：能拆分短期止血、中期制度修复和长期治理建设；不生成正式整改报告。
