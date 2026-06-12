# 端到端验收 Runbook

本 runbook 面向非技术律师、知识管理人员和法律科技项目成员。

1. 选择插件：合同审查用 `cn-commercial-legal`，并购尽调用 `cn-corporate-legal`，诉讼案件用 `cn-litigation-legal`。
2. 读取 profile：先读对应 `acceptance/*/input/*practice-profile.md`，了解虚构团队的风险偏好、升级规则、输出格式和复核角色。
3. 使用虚构输入：只使用 `acceptance/*/input/` 下材料，不要替换为真实客户合同、资料室、案件材料或个人信息。
4. 按 skills 顺序执行：合同为 cold-start -> contract-review -> deviation-memo -> renewal-risk-check；并购为 cold-start -> diligence-tabular-review -> issue-extraction -> closing-checklist -> disclosure-schedule；诉讼为 matter-intake -> chronology-builder -> evidence-index -> issue-chart -> hearing-prep -> matter-status。
5. 保存输出：将每个 skill 的结果保存到 `acceptance/*/output/`。输出必须标注“律师审阅用草稿”，并区分事实、风险、建议、待确认事项和升级事项。
6. 填写评测表：使用 `shared/evals/sample-eval-sheet.csv` 字段格式，在 `eval/*-eval-sheet.csv` 中记录评分、误报、漏报、来源可追踪性和律师复核要求。
7. 记录问题：将通过项、失败项、模板问题和 skill 问题写入 `*-findings.md`；低于 3 分的维度必须进入 `acceptance/summary/improvement-backlog.md`。
8. 判断是否通过：对照 `acceptance-criteria.md`。三条路径均能生成可编辑草稿、红旗未漏报、无 P0 阻碍项，即认为达到 alpha 可试用标准。
