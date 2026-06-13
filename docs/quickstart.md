# Quickstart

## 使用虚构 employment 样例试跑

`cn-employment-legal` 已新增端到端验收入口：`acceptance/employment/`。普通试跑建议按以下顺序阅读：

1. `input/fictional-employment-practice-profile.md`
2. `input/fictional-employee-termination-fact-pack.md`
3. `input/fictional-employee-handbook-summary.md`
4. `input/fictional-non-compete-and-outsourcing-summary.md`
5. `output/` 下各技能输出
6. `eval/employment-findings.md`
7. `summary/employment-improvement-backlog.md`

所有材料均为虚构样例，输出均为“律师审阅用草稿”，不得作为正式解除通知、员工手册、调查结论、仲裁申请或答辩意见。

## cn-employment-legal MVP 试用提示

`cn-employment-legal` 已进入 MVP，但尚未完成端到端 acceptance。试用时只应使用虚构或脱敏材料，不得放入真实员工姓名、身份证件、手机号、工资、社保、公积金、绩效、病假、孕产、工伤、投诉举报、内部调查、仲裁或诉讼材料。

最短试用路径：

```text
请使用 cn-employment-legal 的 employment-contract-review 技能，基于团队 practice profile，审查这份虚构劳动合同摘要，输出风险等级、逐条审查意见、客户决策事项和合伙人升级事项。所有输出标注“律师审阅用草稿”。
```

后续验收计划见 `acceptance/employment/`。

## cn-privacy-legal MVP 试用提示

`cn-privacy-legal` 已进入 MVP，但尚未完成端到端 acceptance。试用时只应使用虚构或脱敏材料，真实用户数据、员工数据、客户数据、日志、设备信息、定位、身份证件、联系方式、未成年人信息和供应商协议不得放入公开仓库。

可先按以下提示试跑：

```text
请使用 cn-privacy-legal 的 personal-info-processing-map 技能，基于虚构消费类小程序的数据字段和业务流程，生成个人信息处理活动台账草稿，列明处理目的、个人信息类型、敏感个人信息提示、第三方接收方、境外处理、待补材料和升级事项。
```

```text
请使用 cn-privacy-legal 的 privacy-policy-review 技能，审阅这份虚构隐私政策摘要，输出律师审阅用草稿、风险等级、建议修改方向、待律师核验事项和升级事项。
```

```text
请使用 cn-privacy-legal 的 data-transfer-triage 技能，对虚构境外供应商远程访问场景做初筛，只列可能适用路径为“待律师核验”，不得作出确定出境合规结论。
```

完整端到端验收尚未开始，计划入口见 `acceptance/privacy/`。

## 使用虚构 Privacy 样例试跑

`acceptance/privacy/` 已提供虚构消费类 App / 小程序数据合规验收包。建议按以下顺序阅读和试跑：

1. `acceptance/privacy/input/fictional-consumer-app-privacy-fact-pack.md`
2. `acceptance/privacy/input/fictional-privacy-practice-profile.md`
3. `acceptance/privacy/input/fictional-data-processing-agreement-summary.md`
4. `acceptance/privacy/output/`
5. `acceptance/privacy/eval/privacy-findings.md`
6. `acceptance/privacy/summary/privacy-improvement-backlog.md`

真实项目试用前，必须在私有环境中使用脱敏材料，并由负责律师确认 profile、模板、复核规则和客户授权边界。

Privacy alpha 修复后的回归结论见 `acceptance/privacy/summary/privacy-regression-after-alpha-fixes.md`。若要试用，仍应只使用虚构或脱敏材料，正式隐私政策、正式评估报告、出境合规结论和用户答复必须由律师或合规负责人复核。

本指南面向普通法律工作者和项目管理员。请先确认你使用的是脱敏材料或虚构样例。

## 安装和检查

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
python scripts/validate_plugin_manifests.py
python scripts/validate_no_private_materials.py
```

## 从 cold-start 开始

1. 选择插件，例如 `plugins/cn-commercial-legal`。
2. 运行 `cold-start-interview`。
3. 生成本地 `practice-profile.md` 草稿。
4. 由负责律师确认风险等级、可让步事项、不可让步事项和升级规则。
5. 不要把本地 `practice-profile.md` 提交到公开仓库。

## 调用示例

合同审查：

```text
请使用 cn-commercial-legal 的 contract-review 技能，基于本项目 practice profile，审查我上传的供应商服务合同，输出风险等级表、逐条修改建议、待客户决策事项和需合伙人升级事项。
```

并购尽调：

```text
请使用 cn-corporate-legal 的 diligence-tabular-review 技能，读取资料室文件清单，生成一张尽调问题表，列明文件摘要、风险点、重大性、待追问问题和披露建议。
```

诉讼时间线：

```text
请使用 cn-litigation-legal 的 chronology-builder 技能，根据案件材料生成事实时间线，列明日期、事件、参与方、证据来源、争议程度和待核实事项。
```

## 查看 GitHub Actions

每次提交或 PR 都会触发自动验证。打开 GitHub PR 页面，查看 Checks 或 Actions 是否通过。失败时，先修复脚本提示的问题再合并。

## connectors 只是占位

`connectors/` 目录只说明 MCP 连接器的设计原则和配置模板，不会连接真实系统。真实文档管理、合同系统、案件系统或法研数据库接入，必须在私有环境中由 IT、知识管理、风控或合规负责人审批。

## 私有环境准备真实连接器

1. 明确客户授权和事项范围。
2. 默认只读、最小权限。
3. 设置审计日志和撤销授权。
4. 禁止跨客户检索。
5. 写回、发送、签署、提交动作必须人工确认。
6. 真实 API 地址、token、Cookie 和本地密钥不得提交到 GitHub。

## 使用虚构样例试跑三个插件

可以使用 `acceptance/` 中的虚构材料做端到端试跑：

1. 合同审查：读取 `acceptance/commercial/input/`，对照 `acceptance/commercial/output/`。
2. 并购尽调：读取 `acceptance/corporate/input/`，对照 `acceptance/corporate/output/`。
3. 诉讼案件：读取 `acceptance/litigation/input/`，对照 `acceptance/litigation/output/`。

试跑后填写对应 `eval/*-eval-sheet.csv`，并把问题写入 `acceptance/summary/improvement-backlog.md`。不要使用真实客户资料替换这些样例。

## 最短试用路径

1. 打开 `acceptance/README.md`，选择合同、并购或诉讼路径。
2. 先阅读对应 `input/` 下的虚构材料和 practice profile。
3. 按 `acceptance/runbook.md` 的顺序调用对应 skill。
4. 对照 `acceptance/*/output/` 查看律师审阅用草稿的参考格式。
5. 使用 `acceptance/*/eval/` 和 `acceptance/summary/regression-after-alpha-fixes.md` 判断输出是否达到 alpha 可试用标准。

真实项目试用前，应在私有环境中准备脱敏材料，并由负责律师确认模板、profile 和复核规则。

## 第二阶段插件说明

`cn-privacy-legal`、`cn-ai-governance-legal`、`cn-employment-legal`、`cn-regulatory-legal`、`cn-ip-legal` 目前只是 scaffold。普通使用者不应把它们当成可试用工作流；它们只适合用来讨论后续 MVP 拆分、团队访谈问题和 profile 结构。

## cn-ip-legal MVP 试用提示

`cn-ip-legal` 已进入 MVP，但尚未完成端到端 acceptance。试用时仅应使用虚构或脱敏材料，并从以下技能中选择：

- `rights-chain-review`：整理内容项目权属链条。
- `infringement-triage`：进行侵权风险初筛，不作最终侵权结论。
- `ip-license-review`：审查授权许可条款。
- `evidence-preservation-checklist`：整理证据保全清单。
- `takedown-and-demand-letter-outline`：生成下架、投诉或函件内部提纲。

所有输出均应标注“律师审阅用草稿”，对外发送、平台提交或诉讼使用前必须由负责律师复核。

## 使用虚构 IP 样例试跑

1. 打开 `acceptance/ip/input/fictional-content-ip-dispute-fact-pack.md`。
2. 读取 `acceptance/ip/input/fictional-ip-practice-profile.md`。
3. 按 `acceptance/ip/planned-e2e-scenarios.md` 的顺序试跑六个 IP skills。
4. 对照 `acceptance/ip/output/` 查看律师审阅用草稿。
5. 使用 `acceptance/ip/eval/ip-eval-sheet.csv` 和 `acceptance/ip/eval/ip-findings.md` 评估输出质量。

真实项目不得使用公开仓库材料承载客户资料或证据。

## cn-ip-legal Alpha 试用路径

1. 阅读 `acceptance/ip/README.md` 和 `acceptance/ip/input/` 下的虚构样例。
2. 按顺序试用 `rights-chain-review`、`infringement-triage`、`ip-license-review`、`evidence-preservation-checklist`、`takedown-and-demand-letter-outline`。
3. 对照 `acceptance/ip/summary/ip-regression-after-alpha-fixes.md` 检查输出是否满足 alpha 标准。
4. 真实项目必须在私有环境使用脱敏材料，并由负责律师复核。
## AI Governance MVP 试用提示

`cn-ai-governance-legal` 已进入 MVP，并已补充虚构端到端验收包。建议先使用 `acceptance/ai-governance/input/` 中的虚构样例试跑：

```text
请使用 cn-ai-governance-legal 的 ai-tool-intake 技能，对这个虚构 AI 工具上线场景做准入初筛，输出律师审阅用草稿、风险等级、待补材料、审批角色和升级事项。
```

```text
请使用 cn-ai-governance-legal 的 ai-vendor-contract-review 技能，审查这份虚构 AI SaaS 服务条款摘要，重点关注客户数据训练、删除机制、审计权、分包、跨境、输出权属和责任限制。
```

完整端到端验收入口见 `acceptance/ai-governance/`。alpha 修复后的回归结论见 `acceptance/ai-governance/summary/ai-governance-regression-after-alpha-fixes.md`。
# Employment 插件试用路径

`cn-employment-legal` 当前处于 MVP + acceptance + alpha fix candidate 状态。试用时请只使用虚构或脱敏材料，并从 `acceptance/employment/` 读取样例：

1. 读取 `acceptance/employment/input/` 中的虚构员工解除争议和用工合规材料。
2. 按 cold-start、劳动合同审查、员工手册审阅、解除风险初筛、竞业限制、外包派遣、内部调查、劳动争议证据包的顺序试跑。
3. 对照 `acceptance/employment/output/` 查看律师审阅用草稿格式。
4. 对照 `acceptance/employment/summary/employment-regression-after-alpha-fixes.md` 查看 alpha 修复后的回归结果。

不得使用真实员工信息、工资、社保、病假、绩效、调查材料或仲裁诉讼材料。
# Regulatory 插件试用提示

`cn-regulatory-legal` 当前已进入 MVP，但尚未完成端到端 acceptance。试用时请只使用虚构或脱敏材料：

1. 先使用 `cold-start-interview` 生成监管合规团队 practice profile 草稿。
2. 根据事项选择监管动态影响分析、合规义务清单、监管问询响应提纲、行政处罚风险初筛、整改计划或管理层简报。
3. 所有法律依据、监管口径、期限和事实来源均写“待律师核验”。
4. 不得将输出直接作为正式监管回复、正式整改报告、正式对外公告或正式合规结论。

## 使用虚构 Regulatory 样例试跑

1. 读取 `acceptance/regulatory/input/` 中的虚构监管问询、监管动态、practice profile 和整改背景。
2. 按 cold-start、监管动态影响分析、合规义务清单、监管问询响应提纲、行政处罚风险初筛、整改计划、管理层简报顺序试跑。
3. 对照 `acceptance/regulatory/output/` 检查输出格式。
4. 对照 `acceptance/regulatory/eval/` 和 `acceptance/regulatory/summary/` 判断是否达到 MVP acceptance 标准。

## Regulatory alpha 回归结果

`cn-regulatory-legal` alpha 修复后的回归结论见 `acceptance/regulatory/summary/regulatory-regression-after-alpha-fixes.md`。试用时仍应只使用虚构或脱敏材料；监管回复、整改承诺、对外披露和管理层决策材料必须经律师、合规负责人和管理层复核后方可使用。
