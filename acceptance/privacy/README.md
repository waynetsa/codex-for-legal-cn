# cn-privacy-legal 端到端验收

> 律师审阅用草稿。本目录仅使用虚构材料，不包含真实客户、真实企业、真实用户、真实个人信息、真实 App、真实小程序、真实隐私政策、真实 SDK 清单或真实供应商协议。

本目录用于验证 `cn-privacy-legal` MVP 是否能支持中国个人信息保护与数据合规的最小可试用路径。本轮只做 acceptance，不修复 backlog，不发布新 tag。

## 验收路径

1. `cold-start-interview`：生成隐私与数据合规团队画像和 practice profile 摘要。
2. `personal-info-processing-map`：梳理个人信息处理活动台账。
3. `privacy-policy-review`：审阅虚构隐私政策摘要。
4. `data-processing-agreement-review`：审查虚构数据处理协议摘要。
5. `privacy-impact-assessment`：生成影响评估初稿结构。
6. `data-transfer-triage`：对境外供应商处理和远程访问做初筛。
7. `data-subject-request-workflow`：整理用户请求响应流程。

## 目录说明

- `input/`：虚构事实包、practice profile 和数据处理协议摘要。
- `output/`：各 skill 生成的律师审阅用草稿。
- `eval/`：评测表和 findings。
- `summary/`：总体验收报告和 improvement backlog。

## Privacy MVP Acceptance 最低标准

- 能识别业务场景、处理目的和处理活动。
- 能识别个人信息类型和敏感个人信息。
- 能梳理第三方共享、委托处理、共同处理、公开披露和境外处理场景。
- 能审阅隐私政策的主要结构和缺口。
- 能审查数据处理协议中的角色、范围、安全、再委托、审计、删除返还、责任承担等核心风险。
- 能生成影响评估初稿，但不得作为正式评估报告。
- 能完成数据出境或境外供应商处理初筛，但不得作出确定合规结论。
- 能整理用户个人信息请求响应流程，但不得直接发送正式答复。
- 高风险和红旗风险必须进入升级事项。
- 法律依据必须标注“待律师核验”。
- 输出必须能被律师、法务或合规负责人继续编辑。
- 不得出现真实客户资料、真实个人信息、真实系统信息、真实供应商信息。
- 不得生成正式法律意见或正式监管提交材料。

## 本轮结论入口

- 总结：`summary/privacy-e2e-summary.md`
- backlog：`summary/privacy-improvement-backlog.md`
- 评测：`eval/privacy-findings.md`
