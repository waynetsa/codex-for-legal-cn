# Documentation Audit

## 审计对象

- `README.md`
- `ROADMAP.md`
- `docs/quickstart.md`
- `docs/architecture.md`
- `docs/evaluation-guide.md`
- `docs/usage-for-lawyers.md`
- `docs/usage-for-admins.md`
- `docs/safety-and-confidentiality.md`
- `docs/localization-principles.md`

## 检查结果

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| 非技术律师是否能看懂 | 基本可以 | README 信息较多，建议增加“我该用哪个插件”的导览 |
| 安装和试用是否清楚 | 基本清楚 | quickstart 可继续压缩普通用户路径 |
| 如何选择插件是否清楚 | 待增强 | 建议新增插件选择表 |
| 如何运行 cold-start 是否清楚 | 基本清楚 | 可补统一 cold-start runbook |
| 如何使用虚构样例是否清楚 | 清楚 | acceptance 目录较完整 |
| 如何进行私有化试点是否清楚 | 待补 | 需要新增律所试点指南 |
| 如何禁止真实材料进入公开仓库是否清楚 | 清楚 | 但可增加更显眼的公开/私有边界图 |

## 建议新增文档

- `docs/private-pilot-guide.md`
- `docs/data-handling-for-pilots.md`
- `docs/sample-anonymization-guide.md`
- `docs/plugin-selection-guide.md`
- `docs/pilot-feedback-form.md`

## 结论

docs 已能支撑 alpha 使用和审计阅读，但 v1.0 前应让非技术律师能更快理解项目定位、插件选择、试点边界和禁止事项。
