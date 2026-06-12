# AI Governance Planned E2E Scenarios

> 律师审阅用草稿。以下场景均为后续验收规划，不包含真实客户或真实系统信息。

## 场景一：企业 AI 办公助手上线

- 虚构企业计划上线 AI 办公助手。
- 涉及文档摘要、会议纪要、营销文案和客服回复建议。
- 需要验证 `ai-tool-intake`、`ai-risk-assessment` 和 `ai-use-policy-builder`。

## 场景二：AI 供应商合同审查

- 虚构供应商提供 AI SaaS 和模型 API。
- 条款涉及客户数据训练、日志保留、删除机制、审计权、分包、SLA 和责任限制。
- 需要验证 `ai-vendor-contract-review`。

## 场景三：律所内部 AI 使用治理

- 虚构律所希望制定 AI 使用规则。
- 需要禁止输入客户资料、案件材料、个人信息和律师工作底稿。
- 需要验证 `cold-start-interview`、`ai-use-policy-builder` 和 `ai-governance-gap-check`。

## 场景四：企业 AI 治理差距盘点

- 虚构企业已有多个 AI 试点，但缺少工具台账、审批、供应商管理、员工培训和审计机制。
- 需要验证 `ai-governance-gap-check` 输出整改路线图。

## 本轮输出文件

- `input/fictional-enterprise-ai-tool-rollout-fact-pack.md`
- `input/fictional-ai-governance-practice-profile.md`
- `output/cold-start-result.md`
- `output/ai-use-policy-builder-result.md`
- `output/ai-tool-intake-result.md`
- `output/ai-risk-assessment-result.md`
- `output/ai-vendor-contract-review-result.md`
- `output/ai-governance-gap-check-result.md`
- `eval/ai-governance-eval-sheet.csv`
- `eval/ai-governance-findings.md`
- `summary/ai-governance-e2e-summary.md`
- `summary/ai-governance-improvement-backlog.md`

## 本轮状态

本轮已补充完整虚构端到端验收包。验收结论和后续修复建议见 `summary/`，本轮不修复 backlog，不发布新 tag。
