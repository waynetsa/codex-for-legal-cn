# Architecture

Codex for Legal CN 将中国法律工作流拆成可组合的插件、技能、团队口径、模板、参考资料、安全规则、评测和可选连接器。

```text
plugin -> skill -> practice profile -> templates/references -> guardrails -> evals -> optional connectors
```

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
