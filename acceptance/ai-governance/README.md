# cn-ai-governance-legal Acceptance Plan

> 律师审阅用草稿。本目录目前只保存计划，不保存真实客户、真实员工、真实系统、真实供应商合同或真实业务数据。

`cn-ai-governance-legal` 已进入 MVP 开发阶段。本轮只补充插件能力、模板、参考清单和评测样例，不做完整端到端 acceptance，不发布新 tag。

## 后续验收目标

后续将使用虚构企业 AI 工具上线场景，验证以下路径是否可用：

- `cold-start-interview`
- `ai-use-policy-builder`
- `ai-tool-intake`
- `ai-risk-assessment`
- `ai-vendor-contract-review`
- `ai-governance-gap-check`

## 验收边界

- 所有输入必须虚构或脱敏。
- 所有输出必须标注“律师审阅用草稿”。
- 不生成正式法律意见、正式制度或正式合同修改稿。
- 不接入真实 MCP、真实供应商系统或真实企业系统。
- 不写真实密钥、token、API key、Cookie 或私有配置。

## 最低验收标准草案

- 能识别 AI 工具准入风险和审批角色。
- 能区分允许、需审批、禁止使用场景。
- 能识别客户秘密、案件材料、个人信息、商业秘密、源代码和财务数据输入限制。
- 能覆盖 AI 供应商训练使用、数据删除、审计权、分包、跨境和输出权属风险。
- 能输出 AI 治理差距清单和 30/90/180 天整改路线图。
- 高风险和红旗风险必须进入升级事项。
- 法律依据、监管口径和主管机关结论必须写“待律师核验”。
