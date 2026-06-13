# Guardrails Audit

## 审计对象

- `shared/guardrails/`
- `shared/templates/risk-rating-scale.md`
- `shared/templates/escalation-matrix.md`
- `shared/templates/output-quality-checklist.md`

## 检查结果

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 律师复核闸门覆盖所有插件 | 基本覆盖 | 各插件均有 attorney review gate，但表达可进一步统一 |
| 保密规则清楚 | 通过 | 已覆盖客户资料、个人信息、商业秘密、案件材料等 |
| 个人信息处理提醒 | 通过 | privacy、employment、AI governance 等插件均有强调 |
| 来源引用规则 | 基本覆盖 | 法律依据、期限、监管口径均要求待律师核验；建议补统一引用格式 |
| 非法律意见免责声明 | 基本覆盖 | README、docs、skills、templates 大体一致，但可统一为固定句式 |
| 风险等级和升级矩阵覆盖 8 个业务线 | 基本覆盖 | 业务线差异较大，建议增加按插件示例 |
| 试点使用免责声明 | 待补 | 建议新增面向真实律所脱敏试点的免责声明 |

## 需要补强

- 增加 `docs/private-pilot-guide.md` 或同类试点指南。
- 增加“公开仓库不处理真实资料，私有试点需另行审批”的固定免责声明。
- 增加统一来源核验格式：来源、版本、日期、核验人角色、核验状态。
- 增加按 matter 隔离、客户隔离、权限审计的 guardrail 提示。
