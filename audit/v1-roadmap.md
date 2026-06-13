# v1.0 Roadmap

## v1 readiness 修复后路线更新

v1.0 仍不定义为“更多插件”，而定义为“可控试点版本”。本轮已补齐 skill 写作标准、模板边界、私有试点指南、数据处理与脱敏指南、公开仓库与私有部署边界、试点反馈表和 v1 readiness review。

下一阶段应先做受控脱敏试点，不接真实 MCP，不接真实生产系统，不发布 v1.0 tag。只有在试点反馈、P2 收敛、安全边界复核和私有化部署边界完成后，才讨论 v1.0 发布。

`v1.0` 不定义为“更多插件”，而定义为“可控试点版本”。

## Phase 1：仓库质量修复

- Skill 口径统一。
- 模板字段统一。
- 输出长度优化。
- P2 backlog 收敛。
- README 和 quickstart 优化。
- UTF-8 和换行策略检查。

## Phase 2：试点工具包

- `private pilot guide`。
- `data handling guide`。
- `sample anonymization guide`。
- Practice profile examples。
- Pilot feedback form。
- Evaluation dashboard template。

## Phase 3：轻量本地集成

- 本地文件夹读取。
- 本地模板库。
- 不接真实外部系统。
- 只读优先。
- 不写回。

## Phase 4：律所私有化部署设计

- 权限。
- 日志。
- 审计。
- Matter 隔离。
- 客户隔离。
- 版本管理。
- 模板审批。

## Phase 5：v1.0 发布条件

- 8 个插件均通过统一审计。
- 关键 P1 为 0。
- P2 有明确处理计划。
- 试点指南完成。
- 私有化部署边界完成。
- 至少 3 个脱敏试点场景完成。
- 所有验证脚本通过。
- 无真实资料、无密钥、无私有配置。
- README 可以让非技术律师独立理解项目定位和使用路径。
- 安全和保密边界经过复核。

## 不进入 v1.0 的事项

- 不新增法律插件。
- 不接真实 MCP。
- 不接真实律所生产系统。
- 不把 AI 输出定位为正式法律意见。
