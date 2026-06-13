# Audit Issue Backlog

| Issue ID | Title | Category | Affected area | Priority | Recommended fix | Should fix before v1.0 | Owner role | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AUD-P1-001 | 统一 8 个插件的 skill 写作规范 | Skill consistency | All plugins | P1 | 建立统一 skill drafting guide，固定事实、风险、建议、待确认事项和升级事项位置 | Yes | Legal workflow owner | 不改业务逻辑，先统一口径 |
| AUD-P1-002 | 统一模板免责声明和正式文件边界 | Template consistency | All templates | P1 | 在模板开头统一“不构成法律意见、不得直接发送/提交/发布” | Yes | Knowledge management owner | 尤其关注对外文件场景 |
| AUD-P1-003 | 新增律所私有试点指南 | Pilot readiness | Docs | P1 | 新增 `docs/private-pilot-guide.md` | Yes | Pilot lead | 进入真实脱敏试点前必须补 |
| AUD-P1-004 | 新增数据处理和脱敏指南 | Security | Docs / acceptance | P1 | 新增 `docs/data-handling-for-pilots.md` 和样例脱敏规则 | Yes | Compliance owner | privacy、employment、litigation 优先 |
| AUD-P1-005 | 明确公开仓库与私有部署边界 | Security / architecture | README / docs | P1 | 新增边界说明和禁止事项清单 | Yes | Maintainer | 防止误把公开仓库当生产环境 |
| AUD-P1-006 | 设计本地只读文件夹试点方案 | MCP readiness | connectors / docs | P1 | 只做本地只读目录示例，不接真实系统 | Yes | IT owner | v1.0 前不做写回 |
| AUD-P2-001 | 收敛宽表模板阅读体验 | Template consistency | Corporate / privacy / regulatory | P2 | 增加 Markdown 分段版本或短表模式 | No | Template owner | 不影响 alpha，但影响试点体验 |
| AUD-P2-002 | 优化 README 给非技术律师的入口 | Docs | README / quickstart | P2 | 增加“我该用哪个插件”选择表 | No | Docs owner | 提高可理解性 |
| AUD-P2-003 | 统一 cold-start 访谈骨架 | Skill consistency | All cold-start skills | P2 | 抽取统一 cold-start 模板，保留业务线差异 | No | Legal workflow owner | 便于 profile 标准化 |
| AUD-P2-004 | 增加试点评测仪表盘模板 | Evaluation | audit / docs | P2 | 提供 CSV 或 Markdown dashboard template | No | Evaluation owner | 便于试点复盘 |
| AUD-P2-005 | 统一来源核验记录格式 | Guardrails | Skills / templates | P2 | 固定来源、版本、日期、核验人角色、核验状态 | No | Quality owner | regulatory 已先行补强 |
| AUD-P3-001 | 检查 Windows 终端中文显示体验 | Developer experience | Docs / files | P3 | 复查 UTF-8、BOM 和 PowerShell 显示说明 | No | Maintainer | 不影响验证脚本 |

## 统计

- P0：0。
- P1：6。
- P2：5。
- P3：1。
