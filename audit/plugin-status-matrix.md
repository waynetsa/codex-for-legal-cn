# Plugin Status Matrix

| Plugin | Business area | Status | MVP completed | Acceptance completed | Alpha fixes completed | Regression completed | Templates completed | References completed | Eval sample completed | Key risks | Next step toward v1.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cn-commercial-legal` | 合同审查 | ready for controlled pilot | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 谈判语言需适配律所风格；真实合同不得进公开仓库 | 试点模板风格统一和脱敏样例指南 |
| `cn-corporate-legal` | 并购尽调 | needs pilot validation | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 尽调事项复杂，字段可能过宽 | 增加资料室脱敏试点指南 |
| `cn-litigation-legal` | 诉讼案件管理 | ready for controlled pilot | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 期限和程序提示必须始终待律师核验 | 增加案件材料脱敏和证据目录示例 |
| `cn-ip-legal` | 知识产权 | ready for controlled pilot | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 权属链条和授权范围依赖事实文件 | 用虚构 IP 包扩展评测维度 |
| `cn-ai-governance-legal` | AI 治理 | needs pilot validation | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 容易被误用为正式制度或准入结论 | 补私有试点和审批矩阵示例 |
| `cn-privacy-legal` | 隐私与数据合规 | needs private deployment guide | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 真实个人信息和日志不得进入公开仓库 | 优先补数据处理和脱敏指南 |
| `cn-employment-legal` | 劳动用工 | needs pilot validation | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 员工个人信息、工资、病假、调查材料敏感 | 补 HR 试点边界和材料脱敏规范 |
| `cn-regulatory-legal` | 监管合规 | needs template refinement | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 监管口径、期限和处罚风险必须待律师核验 | 收敛宽表和管理层简报格式 |

## 总体判断

8 个插件均已达到 alpha 可试用，但 v1.0 应定义为“可控试点版本”，不是“更多插件版本”。下一步重点是试点工具包、私有化部署边界和统一质量审计。
