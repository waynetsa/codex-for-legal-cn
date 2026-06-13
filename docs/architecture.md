# Architecture

## 当前插件成熟度

- Alpha 可试用：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`、`cn-privacy-legal`。
- MVP 待验收：`cn-employment-legal`。
- Scaffold：`cn-regulatory-legal`。

整体仍遵循：`plugin -> skill -> practice profile -> templates/references -> guardrails -> evals -> optional connectors`。`cn-employment-legal` 本轮只补 MVP 工作流，不接入真实 MCP，不做端到端验收。

## 当前插件成熟度状态

- Alpha 可试用：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`、`cn-ai-governance-legal`。
- MVP + acceptance + alpha fix candidate：`cn-privacy-legal`。
- Scaffold：`cn-employment-legal`、`cn-regulatory-legal`。

`cn-privacy-legal` 遵循同一架构：`plugin -> skill -> practice profile -> templates/references -> guardrails -> evals -> optional connectors`。当前已补齐个人信息保护与数据合规 MVP 工作流、虚构端到端 acceptance 和 alpha 修复回归；本阶段不接入真实 MCP、不使用真实个人信息或客户资料。

Codex for Legal CN 将中国法律工作流拆成可组合的插件、技能、团队口径、模板、参考资料、安全规则、评测和可选连接器。

```text
plugin -> skill -> practice profile -> templates/references -> guardrails -> evals -> optional connectors
```

## 第二阶段 Scaffold 层

第二阶段新增插件目前只进入 scaffold 层：有插件 manifest、两个基础 skill、practice profile 模板、templates/references/evals 占位目录，但没有完成业务模板、评测样例或端到端验收。

当前可试用路径仍以三个核心插件为主：

- `cn-commercial-legal`
- `cn-corporate-legal`
- `cn-litigation-legal`

第二阶段插件进入 MVP 前，应先为单个插件补齐具体 skills、模板、reference checklist、guardrails 接入、eval 样例和 acceptance 路径。

## cn-ip-legal 状态

`cn-ip-legal` 已从 scaffold 升级为第二阶段第一个 MVP 插件。它拥有独立 skills、templates、references、eval 指引和 planned acceptance 目录，但尚未完成端到端 acceptance。

其他第二阶段插件仍保持 scaffold，不应在当前架构中被描述为 alpha-ready 或 MVP-ready。

## Plugin

Plugin 是一个执业领域或业务场景包。每个插件包含 `.codex-plugin/plugin.json`，声明名称、说明、技能目录和默认提示。

## Skill

Skill 是可执行工作流说明，例如合同审查、NDA 初筛、尽调问题提取或案件时间线。每个 `SKILL.md` 都包含输入要求、处理步骤、输出格式、质量检查、保密提示和律师复核闸门。

## Practice Profile

Practice profile 记录团队或项目的风险口径、审批层级、客户行业、输出偏好和禁止事项。它不是法律结论，而是让 Codex 生成更贴近团队习惯的工作底稿。

## Templates and References

Templates 提供输出结构。References 提供检查清单、术语和流程说明。二者都不得包含真实客户资料或第三方专有模板。

## Guardrails

Guardrails 是跨插件共用的安全规则，包括律师复核、保密、个人信息处理、来源引用和免责声明。所有 skill 都必须遵守这些规则。

## Evals

Evals 用于评估输出是否可被律师继续使用，包括遗漏率、误报、来源可追踪性、升级判断和律师复核耗时。

## Optional Connectors

Connectors 是未来私有部署中的 MCP 接入层，负责在授权范围内读取或写入文档系统、合同系统、案件系统、法研数据库、资料室或协作工具。本公开仓库只提供占位文档和模板，不包含真实连接器、真实 API 地址或密钥。

## cn-ip-legal Acceptance 状态

`cn-ip-legal` 当前状态为 MVP + acceptance under review。它已有虚构端到端验收包，但尚未根据 IP backlog 完成 alpha 修复。其他第二阶段插件仍为 scaffold。

## 当前插件成熟度

- `cn-commercial-legal`：alpha 可试用。
- `cn-corporate-legal`：alpha 可试用。
- `cn-litigation-legal`：alpha 可试用。
- `cn-ip-legal`：MVP + acceptance + alpha fix candidate。
- `cn-privacy-legal`：scaffold。
- `cn-ai-governance-legal`：scaffold。
- `cn-employment-legal`：scaffold。
- `cn-regulatory-legal`：scaffold。
## 插件成熟度状态

- Alpha 可试用：`cn-commercial-legal`、`cn-corporate-legal`、`cn-litigation-legal`、`cn-ip-legal`。
- MVP + acceptance + alpha fix candidate：`cn-ai-governance-legal`。
- Scaffold：`cn-privacy-legal`、`cn-employment-legal`、`cn-regulatory-legal`。

`cn-ai-governance-legal` 当前遵循同一架构：`plugin -> skill -> practice profile -> templates/references -> guardrails -> evals -> optional connectors`。本阶段不接入真实 MCP 或真实系统。
