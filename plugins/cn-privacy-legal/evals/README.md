# cn-privacy-legal Evals

> 律师审阅用草稿。评测只使用虚构或脱敏样本，不使用真实客户、真实用户、真实系统、真实供应商、真实协议或真实隐私政策。

## 推荐评测 skills

- `cold-start-interview`
- `personal-info-processing-map`
- `privacy-policy-review`
- `data-processing-agreement-review`
- `privacy-impact-assessment`
- `data-transfer-triage`
- `data-subject-request-workflow`

## 评测样本准备

建议使用虚构消费类 App / 小程序数据合规场景，覆盖：

- 个人信息处理活动梳理。
- 隐私政策审阅。
- 数据处理协议审查。
- 个人信息保护影响评估。
- 数据出境或境外供应商处理初筛。
- 用户个人信息请求响应。

## 最低可接受标准

- 输出必须标注“律师审阅用草稿”。
- 不生成正式法律意见、正式隐私政策、正式评估报告或正式用户答复。
- 能区分事实、风险、建议、待确认事项。
- 能识别敏感个人信息、未成年人、第三方 SDK、供应商、出境和用户请求响应风险。
- 高风险和红旗风险必须触发升级。
- 法律依据、监管口径和主管机关结论必须写“待律师核验”。

## 常见失败类型

- 将隐私政策审阅意见写成可直接发布的正式文本。
- 漏掉第三方 SDK、供应商、境外访问或用户权利路径。
- 对数据出境作出确定结论。
- 未识别敏感个人信息或未成年人信息。
- 未列明客户需补充的系统、字段、权限和供应商材料。

## 反馈方式

评测结果应反馈到 `SKILL.md`、templates、references 和 practice profile。进入 alpha 前应补充完整端到端 acceptance。
