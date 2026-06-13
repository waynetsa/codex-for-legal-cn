# Roadmap

## 当前阶段：v1.0 release candidate

受控虚构试点已完成，v1 preflight 修复已完成。下一步不是继续开发插件，而是人工确认 release notes、人工确认是否创建 `v1.0.0` tag 和 GitHub Release。

该候选状态仍不是生产部署。真实 MCP、真实生产系统和真实客户资料仍不进入当前公开仓库。

## 下一阶段：受控脱敏试点

v1 readiness 修复后，下一阶段不是新增插件，也不是直接发布 v1.0，而是准备 1 到 3 个虚构或严格脱敏试点包，选择少量律师进行受控试点。

## 受控脱敏试点模拟状态

已新增完全虚构的 `pilot/` 试点包，覆盖 commercial、litigation、IP 三条路径，并模拟合伙人、主办律师 / 资深律师、初级律师反馈。当前结论为 `conditional-go`：等待根据 pilot feedback 做最后一轮 v1 preflight 修复后，再进入真实律所受控脱敏试点；暂不发布 v1.0。

试点前置材料：

- [私有试点指南](docs/private-pilot-guide.md)
- [数据处理与样例脱敏指南](docs/data-handling-and-anonymization-guide.md)
- [公开仓库与私有部署边界](docs/public-vs-private-deployment-boundary.md)
- [试点反馈表](docs/pilot-feedback-form.md)

v1.0 前仍不得接入真实 MCP、真实生产系统或真实客户资料。v1.0 发布条件应以试点反馈、P2 收敛、安全边界复核和私有化部署边界完成为准。

## v1.0 路线摘要

`v0.6.0-alpha` 之后，路线重点从新增插件转为可控试点 readiness。`v1.0` 应定义为“可控试点版本”，而不是“更多插件版本”。

阶段路径：

1. 仓库质量修复：统一 skill 口径、模板字段、输出长度和 P2 backlog。
2. 试点工具包：补齐 private pilot guide、data handling guide、sample anonymization guide、practice profile examples、pilot feedback form。
3. 轻量本地集成：仅设计本地文件夹和本地模板库的只读示例，不接真实外部系统。
4. 私有化部署设计：权限、日志、审计、matter 隔离、客户隔离、版本管理和模板审批。
5. v1.0 发布条件：8 个插件统一审计通过，关键 P1 为 0，试点指南完成，至少 3 个脱敏试点场景完成，验证脚本通过且无真实资料或密钥。

详细路线见 `audit/v1-roadmap.md`。

## 当前阶段：Employment Acceptance

- `cn-employment-legal` 已完成 MVP，并新增虚构端到端 acceptance。
- 本轮新增：`acceptance/employment/`，覆盖虚构员工解除争议和用工合规试跑材料、输出、评测、findings、summary 和 backlog。
- 当前结论：P0 为 0，P1 为 3，P2 为 3。建议先做 employment alpha 修复，再判断是否发布 `v0.5.0-alpha`。
- `cn-regulatory-legal` 仍为 scaffold，不建议马上开发。

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
# v0.5.0-alpha 候选条件

`cn-employment-legal` 的发布候选条件为：

- PR #16 employment acceptance 已进入 main。
- employment alpha 修复 PR 已进入 main。
- `validate_structure.py`、`validate_skill_metadata.py`、`validate_plugin_manifests.py`、`validate_no_private_materials.py` 全部通过。
- P0 为 0，P1 清零，剩余 P2 仅为不影响 alpha 试用的体验优化项。
- `acceptance/employment/summary/employment-regression-after-alpha-fixes.md` 记录回归结果。
- `cn-regulatory-legal` 仍保持 scaffold，不在本轮展开 MVP。
# cn-regulatory-legal 下一步

`cn-regulatory-legal` 已进入 MVP。下一步应为该插件增加虚构监管问询和整改端到端验收包，完成 acceptance findings 和 improvement backlog 后，再决定是否进行 alpha 修复和发布 `v0.6.0-alpha`。

本阶段不接入真实监管数据库，不接入真实 MCP，不使用真实客户或真实监管材料。

## Regulatory Acceptance 后状态

`cn-regulatory-legal` 已完成 MVP，并新增虚构监管问询和整改端到端 acceptance。下一步根据 `acceptance/regulatory/summary/regulatory-improvement-backlog.md` 判断是否先做 alpha 修复；当前建议先修复 P1/P2，再考虑发布 `v0.6.0-alpha`。

## v0.6.0-alpha 候选条件

`cn-regulatory-legal` 的发布候选条件为：

- PR #19 regulatory acceptance 已进入 main。
- regulatory alpha 修复 PR 已进入 main。
- `validate_structure.py`、`validate_skill_metadata.py`、`validate_plugin_manifests.py`、`validate_no_private_materials.py` 全部通过。
- P0 为 0，P1 清零，剩余 P2 仅为不影响 alpha 试用的体验优化项。
- `acceptance/regulatory/summary/regulatory-regression-after-alpha-fixes.md` 记录回归结果。
- 文档明确说明 8 个插件均达到 alpha 可试用状态。

满足以上条件后，可发布 `v0.6.0-alpha`。下一阶段不再新增法律插件，应先做整体仓库审计和 v1.0 路线规划。
