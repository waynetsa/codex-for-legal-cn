# v1 Readiness Review

## v1 preflight 修复后结论

受控虚构试点和 v1 preflight 修复已完成。P0 为 0，P1 为 0，P2 已清零，P3 保留为 v1 后体验优化。项目达到 v1.0 release candidate，但仍需人工确认 release notes、tag 和 GitHub Release。

该结论不等于生产部署，不等于允许真实客户资料进入公开仓库，不等于允许接入真实 MCP 或生产系统。

## 受控虚构试点模拟结果

本轮新增 `pilot/` 目录，使用完全虚构材料完成 3 个试点包：

- commercial-contract
- litigation-dispute
- content-ip

模拟律师平均可用性评分为 4.1，平均风险识别评分为 4.2。P0 为 0，P1 为 0。结论为 `conditional-go`：可以准备真实律所受控脱敏试点，但尚不建议发布 v1.0，不得接入真实 MCP，不得使用未脱敏真实客户资料。

## 本轮修复范围

本轮根据 `audit/issue-backlog.md` 完成 v1 readiness 文档和边界加固：

- Skill 写作规范。
- 模板写作规范。
- 统一免责声明和正式文件边界。
- 私有试点指南。
- 数据处理和样例脱敏指南。
- 公开仓库与私有部署边界。
- 试点反馈表。
- 审计文件状态更新。

未新增法律插件，未开发新业务 workflow，未接入真实 MCP，未接入真实系统，未加入真实客户资料，未发布新 tag。

## P1 修复情况

| Issue ID | 状态 | 说明 |
| --- | --- | --- |
| AUD-P1-001 | 已修复 | 新增 `docs/skill-authoring-standard.md`。 |
| AUD-P1-002 | 已修复 | 新增 `docs/template-authoring-standard.md`、`shared/templates/common-disclaimer-footer.md`、`shared/templates/formal-document-boundary.md`。 |
| AUD-P1-003 | 已修复 | 新增 `docs/private-pilot-guide.md`。 |
| AUD-P1-004 | 已修复 | 新增 `docs/data-handling-and-anonymization-guide.md`。 |
| AUD-P1-005 | 已修复 | 新增 `docs/public-vs-private-deployment-boundary.md`。 |
| AUD-P1-006 | 已缓解并降级 | 公开/私有边界和 MCP readiness 明确 v1 前只考虑本地只读文件夹示例；具体实现另行 PR。 |

## P2 处理情况

| Issue ID | 状态 | 说明 |
| --- | --- | --- |
| AUD-P2-001 | 已缓解 | 模板标准要求宽表拆分，复杂模板后续逐步调整。 |
| AUD-P2-002 | 已缓解 | README 和 quickstart 增加审计与试点入口；插件选择表后续优化。 |
| AUD-P2-003 | 保留为 v1 前优化 | cold-start 统一骨架建议后续单独处理。 |
| AUD-P2-004 | 已修复 | 新增 `docs/pilot-feedback-form.md`。 |
| AUD-P2-005 | 已缓解 | skill 和模板标准加入来源核验要求；后续可抽成共享模板。 |

## P3 处理情况

`AUD-P3-001` 仅记录：Windows 终端中文显示体验不影响验证脚本和仓库结构，后续可在开发者体验优化中处理。

## 是否达到受控脱敏试点候选状态

达到。前提是试点只使用虚构或严格脱敏材料，并遵守新增的私有试点、数据处理和公开/私有边界文档。

## 尚不能称为 v1.0 的原因

- 尚未完成至少 3 个脱敏试点场景。
- 尚未形成试点评测汇总。
- 本地只读文件夹示例尚未实现。
- P2 仍有部分体验优化项。
- 私有化部署权限、日志、审计和隔离设计仍是文档级准备。

## 进入 v1.0 前剩余事项

- 合并本轮 readiness PR。
- 准备 1 到 3 个虚构或严格脱敏试点包。
- 选择 2 到 3 名律师做受控试点。
- 汇总 pilot feedback。
- 收敛剩余 P2。
- 再决定是否进入 v1.0 发布准备。

## 下一步建议

进入受控脱敏试点候选阶段，但仍不使用真实客户资料进入公开仓库，不接真实 MCP，不接生产系统，不发布 v1.0 tag。
