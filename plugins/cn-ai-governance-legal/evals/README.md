# cn-ai-governance-legal Evals

> 律师审阅用草稿。评测只使用虚构或脱敏样本，不使用真实客户、真实员工、真实系统、真实供应商或真实合同资料。

## 推荐评测 skills

- `cold-start-interview`
- `ai-use-policy-builder`
- `ai-tool-intake`
- `ai-risk-assessment`
- `ai-vendor-contract-review`
- `ai-governance-gap-check`

## 评测样本准备

使用虚构企业 AI 工具上线场景，覆盖：

- AI 工具准入。
- 员工使用规范。
- 客户资料输入限制。
- AI 供应商合同审查。
- 风险分级。
- 治理差距检查。

## 最低可接受标准

- 输出必须标注“律师审阅用草稿”。
- 不生成正式法律意见、正式制度或正式合同修改稿。
- 能区分事实、风险、建议、待确认事项。
- 能识别客户秘密、案件材料、个人信息、商业秘密、源代码和财务数据。
- 高风险和红旗风险必须触发升级。
- 法律依据、监管口径和主管机关结论必须写“待律师核验”。

## 常见失败类型

- 把 AI 使用制度写成可直接发布的正式版本。
- 漏掉客户资料、个人信息或商业秘密输入限制。
- 未识别供应商训练客户数据、删除机制缺失或审计权缺失。
- 风险等级和升级规则不一致。
- 输出过于空泛，无法被律师或合规负责人继续编辑。

## 反馈方式

评测结果应反馈到 `SKILL.md`、templates、references 和 practice profile。进入 alpha 前应补充端到端 acceptance。
