# MCP Readiness Audit

## v1 readiness 修复后状态

本轮新增 [公开仓库与私有部署边界](../docs/public-vs-private-deployment-boundary.md)，明确真实 MCP 和生产系统接入不属于当前阶段。

结论更新：

- 当前仍不接真实 MCP、真实监管数据库、真实律所文档系统、合同系统、案件系统或法研数据库。
- 后续如进入私有化部署设计，应坚持最小权限、只读优先、不默认写回、按客户和 matter 隔离。
- 任何 MCP 接入前必须完成审批、权限、日志、审计、留存、删除和事故响应设计。
- v1 前更适合先设计“只读本地文件夹 / 本地模板库”示例，而不是直接接真实外部系统。

## 审计对象

- `connectors/`
- `connectors/placeholders/`
- `connectors/examples/mcp-config.template.json`

## 当前判断

当前 connector 设计仍为占位和模板说明，不接真实系统，不包含真实凭证，不应被理解为已经可连接律所生产系统。

## Readiness 检查

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 是否只是占位 | 是 | placeholder 文件清楚表达未来方向 |
| 是否说明不接真实系统 | 基本说明 | 建议 v1.0 前在 README 和 docs 中再强化 |
| 最小权限 | 待设计 | 未来应默认只读 |
| 只读优先 | 建议采用 | v1.0 前只做只读本地文件夹示例 |
| Matter 隔离 | 待设计 | 真实试点前必须按 matter 隔离 |
| 客户隔离 | 待设计 | 不能跨客户检索 |
| 日志和审计 | 待设计 | 必须记录检索来源、使用人、时间和输出 |

## 第一批真实试点候选 connector

优先级建议：

1. Document management：适合只读文档目录试点。
2. Contract lifecycle management：适合合同模板和条款库试点。
3. Litigation case management：适合案件材料目录和时间线试点。
4. Legal research：仅在授权和来源核验清楚时考虑。
5. Dataroom：适合并购尽调，但权限风险较高。
6. Collaboration：适合内部反馈，不适合作为第一批资料源。
7. Storage：可作为本地只读文件夹示例的底层抽象。

## v1.0 建议

v1.0 前只做“只读文件夹 / 本地文档目录”接入示例，不接真实企业系统。真实接入前需完成审批、日志、权限、审计、客户隔离和 matter 隔离设计。
