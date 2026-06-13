# Usage for Admins

## 受控试点准备事项

管理者、IT 和合规负责人在试点前应先确认：

- 试点材料为虚构材料、严格脱敏材料或经授权的私有环境材料。
- 公开仓库不保存真实客户资料、真实案件材料、真实合同、真实个人信息、真实监管材料或密钥。
- 暂不接入真实 MCP、真实生产系统、文档系统、合同系统、案件系统、法研数据库或监管数据库。
- 试点范围、参与律师、评分方式、停止条件和反馈回收方式已经明确。

建议先阅读 [私有试点指南](private-pilot-guide.md)、[数据处理与样例脱敏指南](data-handling-and-anonymization-guide.md)、[公开仓库与私有部署边界](public-vs-private-deployment-boundary.md) 和 [试点反馈表](pilot-feedback-form.md)。

本指南面向律所知识管理、IT、风控、合规和法律科技负责人。

## 模板版本管理

- 将公开仓库模板作为基础版本。
- 律所内部模板应放在私有仓库或受控文档库中。
- 每次更新模板时记录版本、负责人、适用团队、变更原因和复核人。
- 不要把真实客户模板、收费模板或第三方专有模板提交到公开仓库。

## 权限审批

- 明确谁可以使用插件、读取材料、创建本地 practice profile。
- 对客户材料、案件材料、交易资料和证据设置事项级权限。
- 对任何写回、发送、签署、提交机构的动作设置人工确认。
- 使用 `shared/templates/escalation-matrix.md` 作为最低升级基线。

## 脱敏评测集

- 由负责律师选择适合复盘的历史事项。
- 由知识管理或法律科技团队脱敏。
- 由风控或合规负责人确认可用于内部评测。
- 使用 `shared/evals/sample-eval-sheet.csv` 记录评分、误报、漏报和整改事项。

## GitHub Actions

本仓库的 `.github/workflows/validate.yml` 会在 push 和 pull request 时运行：

- `validate_structure.py`
- `validate_skill_metadata.py`
- `validate_plugin_manifests.py`
- `validate_no_private_materials.py`

管理员应检查 PR 页面中的 Actions 状态。失败时先修复结构、元数据、manifest 或疑似敏感材料问题，再合并。

## MCP 连接器规划

真实 MCP 连接器只应在私有部署中启用。接入前需确认：

- 客户授权和事项范围。
- 最小权限和只读优先。
- 审计日志、撤销授权和访问隔离。
- 是否涉及个人信息、商业秘密、跨境传输或第三方处理。
- 写回动作的人工确认人和审批流程。
