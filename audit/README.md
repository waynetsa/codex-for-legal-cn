# Repository Audit for v1.0 Readiness

本目录用于记录 `v0.6.0-alpha` 之后的整体仓库审计和 `v1.0` 路线规划。

审计目标不是发布正式法律产品，而是判断本项目是否具备进入真实律所“脱敏、受控、律师复核”试点的条件。项目定位保持不变：不提供法律意见，只产出“律师审阅用草稿”。

## 审计范围

- 8 个插件状态。
- Skill 一致性。
- 模板一致性。
- Guardrails 一致性。
- Acceptance 覆盖。
- Docs 可读性。
- 安全与保密。
- MCP readiness。
- 试点准备。
- `v1.0` 路线。

## 本轮边界

- 不开发新插件。
- 不接入真实 MCP。
- 不接入真实律所系统、监管数据库、文档系统、合同系统、案件系统或法研数据库。
- 不加入真实客户资料、真实案件材料、真实合同、真实个人信息或真实监管材料。
- 不写密钥、token、API key、Cookie 或私有系统配置。
- 不发布新 tag 或 `v1.0` release。

## 文件索引

- `v0.6.0-alpha-overview.md`：版本总览。
- `plugin-status-matrix.md`：插件状态矩阵。
- `skill-consistency-audit.md`：skill 一致性审计。
- `template-consistency-audit.md`：模板一致性审计。
- `guardrails-audit.md`：guardrails 审计。
- `acceptance-coverage-audit.md`：acceptance 覆盖审计。
- `docs-audit.md`：文档可读性审计。
- `security-and-confidentiality-audit.md`：安全与保密审计。
- `mcp-readiness-audit.md`：MCP readiness 审计。
- `pilot-readiness-checklist.md`：试点准备清单。
- `v1-roadmap.md`：`v1.0` 路线图。
- `issue-backlog.md`：统一问题清单。
