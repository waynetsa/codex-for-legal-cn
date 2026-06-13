# MCP Readiness Audit

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
