# Roadmap

## 当前阶段：Employment MVP

- 已发布：`v0.4.0-alpha`，六个插件达到 alpha 可试用：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal`。
- 本轮新增：`cn-employment-legal` 从 scaffold 升级为 MVP，覆盖劳动合同审查、员工手册审阅、解除风险初筛、竞业限制、外包派遣、内部调查和劳动争议证据整理。
- 仍为 scaffold：`cn-regulatory-legal`。

下一步应为 `cn-employment-legal` 增加虚构员工解除争议和用工合规端到端验收包；不要马上开发 `cn-regulatory-legal`。

## 当前阶段：Privacy MVP

- 已完成：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal` alpha 可试用。
- 本轮新增：`cn-privacy-legal` 从 scaffold 升级为 MVP，覆盖个人信息处理活动梳理、隐私政策审阅、数据处理协议审查、影响评估、数据出境初筛和用户请求响应。
- 本轮新增：`cn-privacy-legal` 虚构端到端 acceptance、findings 和 improvement backlog。
- 仍为 scaffold：`cn-employment-legal`、`cn-regulatory-legal`。

下一步应根据 `acceptance/privacy/summary/privacy-improvement-backlog.md` 判断是否先做 privacy alpha 修复，再考虑发布 `v0.4.0-alpha`。不要同时深挖 employment 和 regulatory。

## v0.4.0-alpha Candidate

候选条件：

- PR #13 已合并。
- Privacy alpha 修复 PR 已合并。
- `cn-privacy-legal` 完成 MVP、acceptance、alpha 修复和 regression。
- P0 为 0，P1 为 0，P2 仅为可接受体验优化项。
- 验证脚本全部通过，且未发现 `.env`、私钥、密钥文件或 `practice-profile.md`。

满足以上条件后，可发布 `v0.4.0-alpha`。`cn-employment-legal` 和 `cn-regulatory-legal` 仍保持 scaffold。

仓库地址：https://github.com/waynetsa/codex-for-legal-cn

## 已完成

- 三个核心插件：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`。
- cold-start interview 与 practice profile 模板。
- 合同、并购、诉讼核心 templates、references 和虚构 examples。
- 共享 guardrails：律师复核、保密、个人信息、来源引用和免责声明。
- 共享 evals：评测规则、样例评测表和插件评测说明。
- GitHub Actions 自动验证。
- MCP connector placeholders。

## 下一阶段规划

- `cn-privacy-legal`：隐私与个人信息保护工作流。
- `cn-ai-governance-legal`：AI 治理、算法和模型合规工作流。
- `cn-employment-legal`：劳动用工工作流。
- `cn-regulatory-legal`：监管合规和监管监测工作流。
- `cn-ip-legal`：知识产权工作流。
- 私有化部署指引。
- 真实 MCP 连接器样例。
- 律所内部评测看板。

## 长期方向

- 更细颗粒度的 practice profile 版本管理。
- 脱敏评测集和回归评测流程。
- 权限审批、审计日志和连接器安全基线。
- 面向法律教育和律所知识管理的教程。

## 当前下一步

当前优先事项不是直接扩展第二阶段新插件，而是根据 `acceptance/summary/improvement-backlog.md` 修复三个核心插件的 alpha 试用问题。建议先完成一轮核心插件修复 PR，再规划隐私合规、AI 治理、劳动用工、监管监测和知识产权插件。

## v0.1.1-alpha candidate

当前阶段：根据 `acceptance/summary/improvement-backlog.md` 修复核心三插件的 alpha 可用性问题。

- P1：合同替代表述、并购重大性映射、诉讼时间线、期限和保全提示。
- P2：评测表总体结论、acceptance 文件索引、宽表输出体验。
- 下一步优先发布 `v0.1.1-alpha`，并用虚构合同、虚构并购资料室和虚构诉讼案件再次试跑。

第二阶段新插件仍应等待核心三插件稳定后再规划。

## Phase 2 Scaffold

第一阶段核心三插件已进入 `v0.1.1-alpha` 基线：

- `cn-commercial-legal`
- `cn-corporate-legal`
- `cn-litigation-legal`

第二阶段五个插件进入 scaffold 阶段：

- `cn-privacy-legal`
- `cn-ai-governance-legal`
- `cn-employment-legal`
- `cn-regulatory-legal`
- `cn-ip-legal`

当前原则：先建立目录、manifest、cold-start interview、profile 模板、references/templates/evals 占位和验证覆盖。下一步应逐个选择一个第二阶段插件做 MVP，不建议五个插件同时深度开发。

## cn-ip-legal MVP

`cn-ip-legal` 已作为第二阶段第一个 MVP 插件进入开发，覆盖权属链条、侵权初筛、授权审查、证据保全和下架/函件提纲。

下一步不是继续扩展其他第二阶段插件，而是为 `cn-ip-legal` 增加虚构内容 IP 争议端到端验收包，验证：

- cold-start profile 是否可用。
- rights-chain-review 是否能识别权利缺口。
- infringement-triage 是否避免最终侵权结论。
- ip-license-review 是否能输出可编辑条款审查表。
- evidence-preservation-checklist 是否覆盖证据三性和保全提示。
- takedown-and-demand-letter-outline 是否明确不得直接发送。

## cn-ip-legal Acceptance

`cn-ip-legal` 已完成 MVP，并新增虚构端到端验收包。下一步应根据 `acceptance/ip/summary/ip-improvement-backlog.md` 判断是否先做 IP alpha 修复，再发布 `v0.2.0-alpha`。

当前不建议马上开发其他第二阶段插件 MVP。

## v0.2.0-alpha Candidate

发布候选条件：

- PR #7 已合并。
- IP alpha 修复 PR 已合并。
- `cn-ip-legal` 完成 MVP、acceptance、alpha 修复和 regression。
- P0 为 0，P1 为 0，P2 仅为可接受体验优化项。
- 验证脚本全部通过。

满足以上条件后，可发布 `v0.2.0-alpha`。其他第二阶段插件仍保持 scaffold。
## 当前阶段：AI Governance MVP

- 已完成：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal` alpha 可试用。
- 已完成：`cn-ip-legal` MVP、端到端 acceptance、alpha 修复，达到 alpha 可试用。
- 已完成：`cn-ai-governance-legal` 从 scaffold 升级为 MVP。
- 本轮新增：`cn-ai-governance-legal` 虚构端到端 acceptance、findings 和 improvement backlog。
- 本轮完成：`cn-ai-governance-legal` alpha 修复和 regression，达到 `v0.3.0-alpha` 候选条件。
- 仍为 scaffold：`cn-privacy-legal`、`cn-employment-legal`、`cn-regulatory-legal`。

`v0.3.0-alpha` 候选条件：PR #10 合并、AI governance 修复 PR 合并、验证脚本通过、无敏感文件、P0 为 0、P1 清零或降级为可接受 P2。下一步建议发布后优先选择 `cn-privacy-legal` 做 MVP，不要同时深挖 employment 和 regulatory。
