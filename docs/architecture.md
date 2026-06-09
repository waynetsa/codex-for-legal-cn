# Architecture

Codex for Legal CN 将法律工作拆成可组合的插件、技能、模板、参考材料、评测和安全规则。

## Plugin

Plugin 是一个执业领域或业务场景包。每个插件包含 `.codex-plugin/plugin.json`，声明名称、说明、技能目录和默认提示。

## Skill

Skill 是一个可执行工作流说明，例如合同审查、NDA 初筛、尽调问题提取或案件时间线。每个 `SKILL.md` 都包含 frontmatter、输入要求、处理步骤、输出格式、质量检查和律师复核闸门。

## Practice Profile

Practice profile 记录团队或项目的风险口径、常用模板、审批层级、客户行业和输出偏好。它不是法律结论，而是让 Codex 生成更贴近团队习惯的工作底稿。

## Template

Template 是输出结构，例如审查备忘录、偏离清单、尽调问题台账、证据目录和案件周报。模板必须是虚构或通用结构，不得包含真实客户信息。

## Reference

Reference 是检查清单、术语说明和流程说明。涉及法律依据时，应提供可核验来源；无来源时写“待律师补充法律依据”。

## Eval

Eval 用于评估 skill 输出是否可靠，包括遗漏率、准确率、格式可用性、律师复核耗时和升级判断一致性。

## Guardrail

Guardrail 是跨插件共用的安全规则，包括律师复核、保密、个人信息处理、来源引用和免责声明。

## Connector

Connector 是未来接入文档库、知识库、项目管理、表格和权限系统的接口说明。第一阶段只保留架构位置和文档原则，不接入真实系统。
