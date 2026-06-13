# Audit Issue Backlog

## v1 readiness 修复后状态

本节为 `fix/v1-readiness` 分支追加状态，不删除原始审计问题记录。项目定位仍为公开法律 AI 工作流模板库，不提供法律意见，只产出“律师审阅用草稿”，不得接入真实 MCP、真实生产系统或真实客户资料。

| Issue ID | 修复后状态 | 处理说明 | 后续安排 |
| --- | --- | --- | --- |
| AUD-P1-001 | 已修复 | 新增 `docs/skill-authoring-standard.md`，统一 SKILL.md 结构、草稿边界、律师复核闸门、事实/风险/建议/待确认事项/升级事项写法。抽查未发现“必然违法”“无需律师复核”等强结论表述。 | v1 前按该标准做一次小批量口径校准，不做业务能力扩展。 |
| AUD-P1-002 | 已修复 | 新增 `docs/template-authoring-standard.md`、`shared/templates/common-disclaimer-footer.md`、`shared/templates/formal-document-boundary.md`，统一模板免责声明和正式文件边界。 | 后续模板改版时逐步引用统一页脚。 |
| AUD-P1-003 | 已修复 | 新增 `docs/private-pilot-guide.md`，明确试点目标、插件批次、材料要求、律师评分、停止条件和试点后决策。 | 合并后可作为受控脱敏试点入口。 |
| AUD-P1-004 | 已修复 | 新增 `docs/data-handling-and-anonymization-guide.md`，明确公开仓库允许/禁止材料、脱敏步骤、残余风险和私有环境前提。 | 试点前必须先完成材料脱敏复核。 |
| AUD-P1-005 | 已修复 | 新增 `docs/public-vs-private-deployment-boundary.md`，明确公开仓库、私有部署和 MCP 接入边界。 | v1 前仍不接真实 MCP 或真实生产系统。 |
| AUD-P1-006 | 已缓解并降级 | 本轮明确当前仅允许“受控脱敏试点候选”，真实系统接入仍不在当前阶段；MCP readiness 仅作为未来审批、权限、日志、审计设计依据。 | 降级为 P2：v1 前可补充只读本地文件夹示例方案，但不阻碍脱敏试点候选。 |
| AUD-P2-001 | 已缓解 | 新增模板写作标准，要求宽表拆分为核心表、待补材料、升级事项、决策事项等短表。 | 后续模板精修时逐步落地。 |
| AUD-P2-002 | 已缓解 | README、quickstart、architecture、evaluation-guide、律师/管理员/安全文档增加 v1 readiness 与试点入口。 | 继续根据试点反馈优化入口文案。 |
| AUD-P2-003 | 保留为 v1 前优化 | cold-start 体验统一需要逐个插件小修，属于可用性优化，不影响受控脱敏试点候选。 | v1 readiness 后单独开小 PR 处理。 |
| AUD-P2-004 | 已修复 | 新增 `docs/pilot-feedback-form.md`，提供可复制的试点评分字段。 | 试点时用该表回收质量数据。 |
| AUD-P2-005 | 已缓解 | skill 与 template 写作标准增加来源、事实、法律依据和人工核验要求。 | v1 前可继续统一引用格式。 |
| AUD-P3-001 | 仅记录 | Windows 终端中文显示乱码属于环境显示问题，不影响仓库文件编码和项目可用性。 | 后续可补充 Windows UTF-8 显示提示。 |

### 最终计数

| 优先级 | 修复后数量 | 状态 |
| --- | ---: | --- |
| P0 | 0 | 未发现阻碍试点或严重误用问题。 |
| P1 | 0 | 已修复或降级，达到受控脱敏试点候选要求。 |
| P2 | 4 | 均为体验、格式或后续示例优化，不阻碍受控脱敏试点候选。 |
| P3 | 1 | 仅记录为未来环境体验优化。 |

结论：P1 已清零，可以进入“受控脱敏试点候选状态”。这不等于 v1.0 发布，不等于允许真实客户资料进入公开仓库，也不等于可以接入真实 MCP 或生产系统。

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
