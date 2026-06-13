# Evaluation Guide

## Employment 后续验收维度

`cn-employment-legal` 已进入 MVP，尚未完成端到端 acceptance。后续评测应使用虚构员工解除争议和用工合规材料，重点检查：

- 是否识别劳动合同、员工手册、解除风险、竞业限制、外包派遣、内部调查和劳动争议证据整理的核心风险。
- 是否对特殊保护人员、民主程序、公示送达、仲裁或诉讼期限写明“待律师核验”。
- 是否避免生成正式法律意见、正式解除通知、正式员工手册、正式仲裁材料或正式调查结论。
- 是否把高风险和红旗风险写入升级事项。

评测结果应反馈到 `plugins/cn-employment-legal/skills/`、`templates/`、`references/` 和后续 acceptance backlog。

## Privacy 后续验收维度

`cn-privacy-legal` 已进入 MVP，并已新增虚构端到端 acceptance。读取顺序建议：

1. `acceptance/privacy/README.md`
2. `acceptance/privacy/planned-e2e-scenarios.md`
3. `acceptance/privacy/input/`
4. `acceptance/privacy/output/`
5. `acceptance/privacy/eval/privacy-findings.md`
6. `acceptance/privacy/summary/privacy-improvement-backlog.md`

Privacy 评测建议覆盖：

- 个人信息处理活动台账完整性。
- 个人信息类型和敏感个人信息识别。
- 隐私政策收集清单、第三方共享、用户权利路径、保存期限、未成年人和跨境提示。
- 数据处理协议中的角色、处理范围、安全措施、分包、审计、删除和责任承担。
- 个人信息保护影响评估中的必要性、风险控制和剩余风险。
- 数据出境或境外供应商处理初筛是否避免确定性结论。
- 用户请求响应流程是否覆盖身份核验、责任部门、留痕和律师复核。

所有评测材料必须虚构或脱敏，不得使用真实个人信息、真实隐私政策、真实数据处理协议或真实供应商材料。

Privacy alpha 修复后的回归结果读取 `acceptance/privacy/summary/privacy-regression-after-alpha-fixes.md`。评测负责人应确认 P0 为 0、P1 清零、剩余 P2 仅为体验优化项，再建议进入 `v0.4.0-alpha` 发布。

本指南用于律所内部评测 Codex for Legal CN 的三个核心插件。评测对象是工作流输出质量，不是律师法律结论的正确率。

## 为什么要评测

法律 AI 工作流必须能被复核、能发现遗漏、能控制风险。评测可以帮助团队判断 skill、template、reference 和 practice profile 是否真正减少律师整理时间，是否引入误报、漏报或错误升级。

## 谁来评测

- 负责律师：判断事实、风险和输出可用性。
- 合伙人或项目负责人：判断重大风险、升级规则和客户沟通口径。
- 知识管理或法律科技团队：维护样本、记录评分、推动模板更新。
- 风控或合规负责人：检查保密、个人信息和对外使用边界。

## 用什么材料评测

只能使用虚构样例、充分脱敏历史项目或内部批准的训练材料。不得使用真实客户名、真实案件名、真实合同、真实证据、真实个人信息或未获授权的第三方模板。

## 如何准备脱敏历史样本

1. 选择已完成且适合复盘的合同、尽调或诉讼事项。
2. 删除或替换所有可识别主体、人员、地址、账号、案号、交易编号和联系方式。
3. 修改金额、日期、行业特征和交易结构，避免组合识别。
4. 保留结构性信息，例如条款类型、文件类型、证据关系、风险类型。
5. 由负责律师确认样本可用于内部评测。

## 如何打分

使用 `shared/evals/eval-rubric.md` 的 1 到 5 分标准。每次评测至少记录：样本、插件、skill、评测人、日期、维度、分数、是否漏报、是否误报、来源是否可追踪、是否需要律师复核。

## 如何记录误报和漏报

- 漏报：样本预设的重大问题没有被识别。
- 误报：输出把不存在或低影响事项错误标为中高风险。
- 错误升级：应升级未升级，或普通事项过度升级。
- 来源问题：引用无法追溯，或把客户陈述写成已核实事实。

## 如何反馈到项目文件

- 如果常见遗漏来自 workflow，修改对应 `SKILL.md`。
- 如果输出格式难以编辑，修改 `templates/`。
- 如果风险口径不一致，修改 `profiles/practice-profile.template.md` 或本地 practice profile。
- 如果检查维度不足，修改 `references/`。
- 如果人工复核不清楚，修改 `shared/guardrails/` 和 `shared/templates/escalation-matrix.md`。

## 评测频率建议

- 新增或大幅修改 skill 前后各评测一次。
- 每个插件至少保留 3 到 5 个虚构或脱敏样本。
- 律所内部部署时，建议每月抽样复核，重大模板变更后重新评测。

## 发布新版本前门槛

建议发布前满足：

- 结构和元数据验证通过。
- 样本中无红旗风险漏报。
- 高风险事项升级准确。
- 输出不含真实敏感信息。
- 负责律师确认输出可作为“律师审阅用草稿”继续编辑。

## 重要提醒

不能把 AI 输出准确率当作律师结论准确率。AI 评测只说明工作流在样本上的辅助质量，任何正式法律判断仍必须由合格法律专业人士作出。

## 如何读取 acceptance 评测结果

`acceptance/` 目录中的评测结果用于判断 `v0.1.0-alpha` 是否达到可试用基线：

- `acceptance/*/eval/*-eval-sheet.csv` 记录逐项评分。
- `acceptance/*/eval/*-findings.md` 记录通过项、失败项和改进建议。
- `acceptance/summary/e2e-summary.md` 给出总体结论。
- `acceptance/summary/improvement-backlog.md` 是下一轮修复 PR 的输入。

评测得分低于 3 分的维度必须进入 backlog。不能把 AI 输出准确率当作律师结论准确率。

## 如何读取 alpha 回归结果

端到端验收后的修复记录位于 `acceptance/summary/regression-after-alpha-fixes.md`。评测负责人可按以下方式使用：

- 先看 P1/P2 是否已处理，确认是否仍有阻碍试用的问题。
- 再看合同、并购、诉讼三条路径的回归结果，判断输出是否更适合律师继续编辑。
- 对仍未解决的体验问题，写入下一轮 backlog，不要把 AI 输出准确率等同于律师结论准确率。
- 发布新版本前，应再次运行验证脚本，并用虚构样例至少试跑一次核心路径。

## 第二阶段插件评测状态

第二阶段五个插件当前尚未进入端到端验收。它们的 `evals/` 目录只包含占位说明和样例目录，不代表已有可用评测集。

进入 MVP 前，每个第二阶段插件至少需要：

- 虚构输入材料。
- 对应 practice profile。
- skill 输出样例。
- 评测表。
- findings 文件。
- summary 和 improvement backlog。

## cn-ip-legal 后续验收维度

`cn-ip-legal` 已进入 MVP，后续 acceptance 应至少评测：

- 权属链条是否完整列出权利对象、来源、授权范围、期限、地域、转授权、改编和商业化。
- 侵权初筛是否区分相似点、差异点、权利基础、证据缺口和待律师核验事项。
- 授权审查是否覆盖授权性质、渠道、收益、审计、瑕疵担保、侵权责任和到期后处理。
- 证据保全清单是否包含证明目的、形成时间、原始载体、真实性、合法性、关联性和待补强事项。
- 下架/函件提纲是否明确不得自动发送或直接作为正式律师函、投诉材料提交。
- 高风险、红旗风险、证据灭失风险和对外发送动作是否触发升级。

## 如何读取 IP Acceptance 结果

IP 验收结果位于 `acceptance/ip/`：

- `eval/ip-eval-sheet.csv`：逐项评分。
- `eval/ip-findings.md`：通过项、失败项和需修复方向。
- `summary/ip-e2e-summary.md`：是否达到 IP MVP acceptance 标准。
- `summary/ip-improvement-backlog.md`：P0/P1/P2 后续修复项。

若 P0 为 0 且 P1 可控，应先开 IP alpha 修复 PR，再考虑发布 `v0.2.0-alpha`。

## 如何读取 IP Regression 结果

IP alpha 修复后的回归记录位于 `acceptance/ip/summary/ip-regression-after-alpha-fixes.md`。评测负责人应重点查看：

- P1 是否全部修复。
- 剩余 P2 是否只影响体验，不影响 alpha 试用。
- 是否仍保持“不作最终法律结论”和“待律师核验”。
- 是否仍无真实客户资料、真实证据或密钥。
## AI Governance 后续验收维度

`cn-ai-governance-legal` 已进入 MVP，并已新增虚构端到端 acceptance。读取顺序建议：

1. `acceptance/ai-governance/input/`
2. `acceptance/ai-governance/output/`
3. `acceptance/ai-governance/eval/ai-governance-findings.md`
4. `acceptance/ai-governance/summary/ai-governance-improvement-backlog.md`

AI governance 评测建议覆盖：

- cold-start 是否能形成可填写的 AI 治理 practice profile。
- AI 使用制度草稿是否区分允许、需审批、禁止场景。
- AI 工具准入是否识别客户秘密、案件材料、个人信息、商业秘密、源代码和财务数据。
- AI 风险评估是否覆盖保密、个人信息、商业秘密、知识产权、幻觉、自动化决策、声誉风险。
- AI 供应商合同审查是否覆盖客户数据训练、删除机制、审计权、分包、跨境、输出权属和责任限制。
- AI 治理差距检查是否能形成 30/90/180 天整改路线图。

评测材料必须虚构或脱敏，所有法律依据、监管口径和主管机关结论均需写“待律师核验”。AI governance alpha 修复后的回归结果读取 `acceptance/ai-governance/summary/ai-governance-regression-after-alpha-fixes.md`；若 P0 为 0、P1 清零且剩余 P2 仅为体验优化，可进入 alpha 发布。
