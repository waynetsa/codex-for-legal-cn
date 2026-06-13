# Security and Confidentiality Audit

## 检查结果

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| `.gitignore` 覆盖常见敏感文件 | 基本覆盖 | 仍建议 v1.0 前复查 `.env.*`、证书、导出资料夹 |
| 验证脚本覆盖敏感材料扫描 | 通过 | `validate_no_private_materials.py` 能发现常见规则词并给出 OK/Warning |
| 是否存在真实资料风险 | 未发现 | 当前样例均为虚构或规则说明 |
| 是否所有样例明确虚构 | 基本通过 | acceptance 样例均标明虚构 |
| private profile 是否排除 | 通过 | 检查未发现 `practice-profile.md` |
| 是否需要 private pilot guide | 是 | 真实试点前必须补齐 |
| 是否需要 data handling guide | 是 | privacy、employment、litigation 等尤其需要 |
| 是否需要公开仓库与私有部署边界 | 是 | 建议 v1.0 前新增单独文档 |

## 风险提示

- 当前公开仓库只能保存模板、虚构样例和流程说明。
- 真实客户资料、真实案件材料、真实合同、真实个人信息、真实监管材料不得进入公开仓库。
- 未来私有试点也应优先只读、本地、脱敏，并保留日志和律师复核记录。

## 建议

- 新增 `docs/private-pilot-guide.md`。
- 新增 `docs/data-handling-for-pilots.md`。
- 新增 `docs/sample-anonymization-guide.md`。
- 将验证脚本的 WARNING 说明写入评测指南，避免误解为失败。
