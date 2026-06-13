# Codex for Legal CN

## v1 readiness 修复

`v0.6.0-alpha` 之后，项目已补齐 v1 readiness 试点准备材料，进入“受控脱敏试点候选状态”。这不是 v1.0 正式发布，也不表示可以把真实客户资料放入公开仓库。

试点前请先阅读：

- [私有试点指南](docs/private-pilot-guide.md)
- [数据处理与样例脱敏指南](docs/data-handling-and-anonymization-guide.md)
- [公开仓库与私有部署边界](docs/public-vs-private-deployment-boundary.md)
- [试点反馈表](docs/pilot-feedback-form.md)
- [v1 readiness review](audit/v1-readiness-review.md)

当前仍禁止真实 MCP、真实生产系统、真实客户资料、真实案件材料、真实合同、真实个人信息和真实监管材料进入本公开仓库。所有输出仍仅为“律师审阅用草稿”，不构成法律意见。

## v0.6.0-alpha 后状态

`v0.6.0-alpha` 已使 8 个插件均达到 alpha 可试用状态。项目下一阶段进入整体仓库审计与 `v1.0` 路线规划，不再优先新增法律插件。

审计入口见 [audit/](audit/)。本阶段重点是试点准备、私有化边界、质量矩阵、统一模板口径和安全保密审计。项目仍是公开模板库，不提供法律意见，只产出“律师审阅用草稿”，不接入真实 MCP，不接入真实律所系统，不接收真实客户资料。

## cn-employment-legal 端到端验收

`cn-employment-legal` MVP 已新增虚构端到端验收包，入口见 [acceptance/employment/](acceptance/employment/)。本轮验收覆盖虚构员工解除争议、劳动合同审查、员工手册审阅、解除风险初筛、竞业限制、外包派遣、内部调查和劳动争议证据包。

验收结论：MVP 达到 acceptance 标准，P0 为 0，P1 为 3，P2 为 3。当前不建议立即发布 `v0.5.0-alpha`，建议先根据 employment backlog 做 alpha 修复。`cn-regulatory-legal` 仍为 scaffold。

## cn-employment-legal MVP 状态

`cn-employment-legal` 已从 scaffold 升级为第二阶段第四个 MVP 插件，面向中国大陆劳动用工法律服务场景。当前能力覆盖劳动合同审查、员工手册审阅、解除和用工调整风险初筛、竞业限制审查、外包派遣和灵活用工风险梳理、内部调查计划、劳动争议证据包整理。

该插件仍只生成“律师审阅用草稿”，不提供法律意见，不得直接作为正式解除通知、裁员方案、员工手册、仲裁申请、答辩意见或调查结论使用。后续端到端验收计划见 [acceptance/employment/](acceptance/employment/)。

当前状态：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal` 为 alpha 可试用；`cn-employment-legal` 为 MVP 待验收；`cn-regulatory-legal` 仍为 scaffold。

## cn-privacy-legal MVP 状态

`cn-privacy-legal` 已从 scaffold 升级为第二阶段第三个 MVP 插件，面向中国律所和企业客户的个人信息保护与数据合规工作流。当前能力包括个人信息处理活动梳理、隐私政策审阅、数据处理协议审查、个人信息保护影响评估、数据出境初筛和用户个人信息请求响应流程。

该插件仍只生成“律师审阅用草稿”，不提供法律意见，不得直接作为正式隐私政策、正式评估报告、监管提交材料或用户答复。当前仅完成 MVP 能力建设，尚未完成端到端 acceptance。后续验收计划见 [acceptance/privacy/](acceptance/privacy/)。

当前可试用状态：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal` 为 alpha 可试用；`cn-privacy-legal` 为 MVP 待验收；`cn-employment-legal` 和 `cn-regulatory-legal` 仍为 scaffold。

## cn-privacy-legal 端到端验收

`cn-privacy-legal` 已新增虚构端到端验收入口：[acceptance/privacy/](acceptance/privacy/)。本轮验收覆盖虚构消费类 App / 小程序数据合规事实包、虚构 privacy practice profile、虚构数据处理协议摘要、七个 privacy MVP skill 输出、评测表、findings、summary 和 improvement backlog。

验收材料不包含真实客户、真实企业、真实用户、真实个人信息、真实 App、真实小程序、真实 SDK、真实系统地址或真实供应商协议。当前结论：MVP 达到 acceptance 标准，但建议先根据 privacy backlog 做 alpha 修复，再考虑发布 `v0.4.0-alpha`。

## cn-privacy-legal v0.4.0-alpha 候选状态

`cn-privacy-legal` 已完成 MVP、虚构端到端 acceptance 和 alpha 修复回归。回归记录见 [acceptance/privacy/summary/privacy-regression-after-alpha-fixes.md](acceptance/privacy/summary/privacy-regression-after-alpha-fixes.md)。当前 P0 为 0，P1 已清零，剩余 P2 为不影响 alpha 试用的体验优化项。若主线验证通过，可作为 `v0.4.0-alpha` 候选发布。

作者：waynetsa
仓库地址：https://github.com/waynetsa/codex-for-legal-cn

## 项目是什么

Codex for Legal CN 是一个面向中国律师事务所、公司法务团队、法律科技团队和法律教育场景的 Codex 插件与技能库。它将法律工作中高频、可复核、可流程化的工作拆成 Codex skills 和 plugins，用于生成律师审阅用草稿、风险清单、项目台账和工作底稿。

本项目不提供法律意见。所有输出仅供执业律师或合规负责人审阅。任何对客户、法院、仲裁机构、监管机构、交易对手发送、提交、签署或依赖的内容，必须由合格法律专业人士复核。

不得把真实客户资料、案件材料、商业秘密、个人信息上传到公开仓库。公开仓库只放模板、流程、示例和脱敏样例。

## 适合谁使用

- 中国律师事务所的合伙人、律师、律师助理和知识管理团队。
- 公司法务、合规、采购、销售合同管理团队。
- 法律科技产品、工程和评测团队。
- 法律 AI 教学、实训和诊所课程。

## 当前包含哪些插件

- `cn-commercial-legal`：合同审查、NDA 初筛、合同偏离清单、续约和解除风险提示。
- `cn-corporate-legal`：并购尽调资料室审阅、问题提取、披露清单和交割清单。
- `cn-litigation-legal`：案件 intake、事实时间线、证据目录、争点表、庭前准备和案件周报。

## 第三轮新增能力

- 权限与保密 guardrails：律师复核闸门、保密规则、个人信息处理、来源引用规则和免责声明。
- 评测体系：共享评分标准、样例评测表、三个插件的评测说明和虚构评测样本。
- GitHub Actions：在 push 和 pull request 时自动验证仓库结构、skill 元数据、插件 manifest 和敏感材料模式。
- MCP 连接器占位：提供文档管理、合同系统、案件系统、法研数据库、电子签、资料室、协作系统和存储系统的接入原则，不包含真实连接器。

## 为什么需要 cold-start interview

法律工作高度依赖团队口径、客户授权、风险偏好和复核规则。每个插件都提供 `cold-start-interview`，用于先生成团队或项目专用的 `practice-profile.md` 草稿，再由负责律师确认。后续技能读取该 profile，以统一风险等级、输出风格、升级规则和禁止事项。

## 律所如何接入自己的 playbook

- 把合伙人审查口径写入本地 `practice-profile.md`，该文件已被 `.gitignore` 忽略，不应提交公开仓库。
- 把脱敏后的模板放入对应插件的 `templates/`。
- 把检查清单、术语和流程说明放入 `references/`。
- 把人工复核、保密、引用和输出质量规则放入 `shared/guardrails/`。
- 真实系统接入只应在私有部署中按 `connectors/` 原则规划。

## 快速开始

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
python scripts/validate_plugin_manifests.py
python scripts/validate_no_private_materials.py
```

## 示例调用方式

```text
请使用 cn-commercial-legal 的 contract-review 技能，基于本项目 practice profile，审查我上传的供应商服务合同，输出风险等级表、逐条修改建议、待客户决策事项和需合伙人升级事项。
```

```text
请使用 cn-corporate-legal 的 diligence-tabular-review 技能，读取资料室文件清单，生成一张尽调问题表，列明文件摘要、风险点、重大性、待追问问题和披露建议。
```

```text
请使用 cn-litigation-legal 的 chronology-builder 技能，根据案件材料生成事实时间线，列明日期、事件、参与方、证据来源、争议程度和待核实事项。
```

## 后续路线图

详见 [ROADMAP.md](ROADMAP.md)。下一阶段可规划隐私合规、AI 治理、劳动用工、监管监测、知识产权插件，以及私有化部署、真实 MCP 连接器样例和律所内部评测看板。

## 贡献方式

欢迎提交新的 skill、模板、脱敏评测样例和流程说明。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，不得提交真实客户资料、真实案件材料、商业秘密或个人信息。

## 免责声明

本项目是法律工作流模板项目，不包含法律意见，不替代律师判断，不构成律师客户关系。任何正式法律文件、意见、函件、诉讼文书或交易文件均必须由合格法律专业人士复核后使用。

## 端到端验收样例

`acceptance/` 目录提供 `v0.1.0-alpha` 的三条虚构端到端验收路径：

- 合同审查路径。
- 并购尽调路径。
- 诉讼案件路径。

这些样例只使用虚构材料，用于验证三个核心插件能否生成可编辑的“律师审阅用草稿”。后续改进应优先参考 `acceptance/summary/improvement-backlog.md`。

## Alpha 可用性修复状态

三个核心插件已经完成端到端验收，验收材料位于 `acceptance/`。当前进入 `v0.1.1-alpha` 候选阶段，重点修复合同谈判语言、并购交易文件影响映射、诉讼期限和保全提示等 P1/P2 可用性问题。

## 第二阶段插件骨架

`v0.1.1-alpha` 之后，本仓库新增五个第二阶段插件骨架：

- `cn-privacy-legal`
- `cn-ai-governance-legal`
- `cn-employment-legal`
- `cn-regulatory-legal`
- `cn-ip-legal`

这些插件目前仅为 scaffold，用于保留目录结构、manifest、cold-start interview 骨架、practice profile 模板、references/templates/evals 占位。它们尚未达到 alpha 可试用标准，也未完成端到端验收。

## cn-ip-legal MVP

`cn-ip-legal` 是第二阶段第一个进入 MVP 的插件，面向中国知识产权和文化传媒法律工作流。当前 MVP 覆盖：

- 权属链条整理。
- 版权、商标、角色形象、音乐、游戏素材等侵权初筛。
- IP 授权许可条款审查。
- 维权或应诉证据整理和保全清单。
- 平台投诉、下架通知、律师函或沟通函内部提纲。

`cn-ip-legal` 仍不提供法律意见，所有输出均为“律师审阅用草稿”。它尚未完成端到端 acceptance，后续将使用虚构内容 IP 争议包进行验收。其他第二阶段插件仍保持 scaffold 状态。

## cn-ip-legal 端到端验收

`cn-ip-legal` MVP 已新增虚构端到端验收入口：`acceptance/ip/`。该目录包含虚构内容 IP 争议事实包、虚构 IP practice profile、虚构授权合同摘要、六个 MVP skill 输出、评测表、findings、summary 和 improvement backlog。

本验收不包含真实客户、真实案件、真实作品、真实合同、真实权利文件、真实证据或真实个人信息。`cn-ip-legal` 当前状态为 MVP 已验收，是否进入 alpha 可试用需根据 IP backlog 完成下一轮修复后再判断。

## cn-ip-legal v0.2.0-alpha 候选状态

`cn-ip-legal` 已完成 MVP、虚构端到端 acceptance 和 alpha 修复回归。当前 P0 为 0，P1 已清零，剩余 P2 均为不影响 alpha 试用的体验优化项。若主线验证通过，可作为 `v0.2.0-alpha` 候选发布。
## cn-ai-governance-legal MVP 状态

`cn-ai-governance-legal` 已从 scaffold 升级为第二阶段第二个 MVP 插件，用于律所内部 AI 使用治理和企业客户 AI 工具、AI 项目、AI 供应商、AI 使用场景治理。当前能力包括 AI 使用制度草稿、AI 工具准入、AI 风险评估、AI 供应商合同审查和 AI 治理差距检查。

该插件已完成虚构端到端验收和 alpha 修复，回归记录见 [acceptance/ai-governance/summary/ai-governance-regression-after-alpha-fixes.md](acceptance/ai-governance/summary/ai-governance-regression-after-alpha-fixes.md)。当前状态为 `v0.3.0-alpha` 候选：P0 为 0，P1 已清零，剩余 P2 为可接受体验优化项。`cn-privacy-legal`、`cn-employment-legal`、`cn-regulatory-legal` 仍为 scaffold。
# cn-employment-legal v0.5.0-alpha 候选状态

`cn-employment-legal` 已完成 MVP、虚构端到端 acceptance 和 alpha 修复回归，当前达到 `v0.5.0-alpha` 候选状态。回归记录见 `acceptance/employment/summary/employment-regression-after-alpha-fixes.md`。

当前状态：

- `cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal`：alpha 可试用。
- `cn-employment-legal`：MVP + acceptance + alpha fix candidate。
- `cn-regulatory-legal`：scaffold。
# cn-regulatory-legal MVP 开发状态

`cn-regulatory-legal` 已从 scaffold 升级为 MVP，成为第二阶段最后一个进入 MVP 的插件。当前已具备监管动态影响分析、合规义务清单、监管问询响应提纲、行政处罚风险初筛、整改计划和管理层合规简报工作流。

当前状态：

- `cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal`、`cn-employment-legal`：alpha 可试用。
- `cn-regulatory-legal`：MVP，尚未完成端到端 acceptance。

后续入口：`acceptance/regulatory/`。

## cn-regulatory-legal 端到端验收入口

`cn-regulatory-legal` 已完成 MVP，本轮新增虚构监管问询和整改端到端验收包。入口见 `acceptance/regulatory/`，包括虚构输入材料、律师审阅用草稿输出、评测表、验收发现、总结和 improvement backlog。

当前不建议直接发布 `v0.6.0-alpha`；下一步应先根据 regulatory backlog 做 alpha 修复。

## cn-regulatory-legal v0.6.0-alpha 候选状态

`cn-regulatory-legal` 已完成 MVP、虚构端到端 acceptance 和 alpha 修复回归。回归记录见 `acceptance/regulatory/summary/regulatory-regression-after-alpha-fixes.md`。当前 P0 为 0，P1 已清零，剩余 P2 为不影响 alpha 试用的体验优化项。若主线验证通过，可作为 `v0.6.0-alpha` 候选发布。

当前状态：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal`、`cn-employment-legal`、`cn-regulatory-legal` 均达到 alpha 可试用候选状态。项目仍只生成“律师审阅用草稿”，不提供法律意见，不接入真实 MCP 或真实监管数据库。
