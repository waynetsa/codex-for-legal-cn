# Codex for Legal CN

## 项目简介

Codex for Legal CN 是面向中国律师事务所、公司法务、合规团队和法律科技团队的法律 AI 工作流模板库。

本项目把高频、可复核、可流程化的法律工作拆成 Codex plugins、skills、templates、references、evals、acceptance 和 pilot materials，帮助法律专业人士生成可编辑的工作底稿、风险清单、问题清单、证据目录、审查表和项目台账。

本项目不提供法律意见，不替代律师判断，不构成律师客户关系。所有输出均应作为“律师审阅用草稿”，由合格律师或负责人员复核后才能继续使用。

## 当前状态

- 当前版本：`v1.0.0`
- 当前阶段：controlled pilot-ready
- 当前状态：8 个插件均 alpha 可试用
- Release：`v1.0.0` GitHub Release 已发布
- QA：post-release QA 已完成
- 项目节奏：项目开发暂告段落，等待真实律所受控脱敏试点反馈
- 下一步：真实律所受控脱敏试点

Post-release QA 结果：

| 指标 | 结果 |
| --- | --- |
| P0 | 0 |
| P1 | 0 |
| P2 | 5 |
| P3 | 3 |
| 平均可用性评分 | 4.1 / 5 |
| 平均风险识别评分 | 4.3 / 5 |

当前收口状态见 [PROJECT_STATUS.md](PROJECT_STATUS.md)，发布后 QA 材料见 [post-release/](post-release/)。

## 安全边界

请先阅读本节，再使用任何插件、模板或样例。

- 本项目不是生产系统。
- 本项目不提供法律意见。
- 所有输出均为律师审阅用草稿。
- 不得把真实客户资料、真实案件材料、真实合同、真实个人信息、真实员工信息、真实监管材料、真实交易资料、真实内部调查材料放入公开仓库。
- 当前不接真实 MCP。
- 当前不接生产系统。
- 真实材料只能在授权私有环境处理，并需要权限控制、日志、审计、客户隔离、matter 隔离和律师复核。
- 任何正式法律文件、意见、函件、诉讼文书、交易文件、监管回复、劳动文件、平台投诉或其他对外材料，均必须由合格法律专业人士复核后使用。

## 8 个插件一览

| Plugin | 业务领域 | 主要能力 | 当前状态 |
| --- | --- | --- | --- |
| `cn-commercial-legal` | 合同与商事 | 合同审查、NDA 初筛、偏离清单、续约与解除风险 | alpha usable |
| `cn-corporate-legal` | 公司与并购 | 并购尽调、问题提取、披露清单、交割清单 | alpha usable |
| `cn-litigation-legal` | 诉讼与争议解决 | 案件 intake、时间线、证据目录、争点表、庭前准备、案件周报 | alpha usable |
| `cn-ip-legal` | 知识产权 | 权属链条、侵权初筛、授权审查、证据保全、平台投诉/函件提纲 | alpha usable |
| `cn-ai-governance-legal` | AI 治理 | AI 使用规则、工具准入、风险评估、供应商合同审查、治理差距检查 | alpha usable |
| `cn-privacy-legal` | 隐私与数据合规 | 个人信息处理地图、隐私政策审阅、数据处理协议、影响评估、数据出境初筛、用户请求响应 | alpha usable |
| `cn-employment-legal` | 劳动用工 | 劳动合同、员工手册、解除风险、竞业限制、外包派遣、内部调查、劳动争议证据包 | alpha usable |
| `cn-regulatory-legal` | 监管合规 | 监管动态影响、合规义务清单、问询响应、处罚风险初筛、整改计划、管理层简报 | alpha usable |

## 仓库目录结构

```text
plugins/          8 个法律工作流插件
shared/           共用 guardrails、模板、评分和升级规则
acceptance/       虚构端到端验收包
pilot/            v1 preflight 试点材料
post-release/     v1.0.0 发布后 QA
audit/            仓库审计、v1 readiness 和路线规划
docs/             使用指南、安全边界、试点指南
scripts/          验证脚本
release-notes/    发布说明
connectors/       MCP 连接器占位说明，不含真实连接器
```

## 如何开始

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
python scripts/validate_plugin_manifests.py
python scripts/validate_no_private_materials.py
```

真实律所试点前，请先阅读：

- [Private pilot guide](docs/private-pilot-guide.md)
- [Data handling and anonymization guide](docs/data-handling-and-anonymization-guide.md)
- [Public vs private deployment boundary](docs/public-vs-private-deployment-boundary.md)
- [Pilot feedback form](docs/pilot-feedback-form.md)
- [Project status](PROJECT_STATUS.md)
- [Post-release QA](post-release/)

## cold-start interview 和 practice profile

每个插件都有 `cold-start-interview`，用于先了解团队自己的 playbook、风险偏好、输出格式、升级规则、禁止事项和律师复核节点，再生成或指导填写 practice profile。后续 skills 会根据 profile 统一审查口径和输出风格。

Practice profile 用于统一：

- 风险偏好
- 审查口径
- 输出格式
- 升级规则
- 禁止事项
- 律师复核节点

`practice-profile.md` 不应提交到公开仓库。真实项目的 practice profile 只能在授权私有环境中使用，并应避免包含真实客户资料、个人信息、案件材料、合同原文、监管材料、账号信息或私有系统配置。

## 受控脱敏试点路径

项目当前建议的下一步是真实律所受控脱敏试点，而不是新增插件、接入真实 MCP 或进入生产部署。

推荐试点步骤：

1. 选择一个律所团队。
2. 选择 1 到 3 个插件。
3. 准备虚构或严格脱敏材料。
4. 在私有环境填写 practice profile。
5. 运行相关 skills。
6. 由律师打分。
7. 记录漏报、误报、重写成本、节省时间。
8. 根据反馈开 `v1.0.x` 修复 PR。

试点前请阅读：

- [Private pilot guide](docs/private-pilot-guide.md)
- [Data handling and anonymization guide](docs/data-handling-and-anonymization-guide.md)
- [Public vs private deployment boundary](docs/public-vs-private-deployment-boundary.md)
- [Pilot feedback form](docs/pilot-feedback-form.md)
- [Post-release QA](post-release/)

## 验证与质量控制

本项目包含以下质量控制材料：

- structure validation
- skill metadata validation
- plugin manifest validation
- private material scanning
- acceptance packages
- regression records
- audit reports
- pilot feedback
- post-release QA

常用验证命令：

```bash
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
python scripts/validate_plugin_manifests.py
python scripts/validate_no_private_materials.py
```

如 `validate_no_private_materials.py` 对安全说明、虚构样例或禁用事项产生 warning，应核验其是否只是规则说明或占位内容；不得放宽对真实密钥、真实个人信息、真实客户资料或私有配置的检查。

## 适合使用的场景

- 法律 AI 工作流原型设计。
- 律所知识管理和模板化建设。
- 律师训练结构化审查思维。
- 虚构或严格脱敏材料试点。
- 私有部署前的流程设计。
- 合规、法务、律师团队评测 AI 工作流。

## 不适合使用的场景

- 直接出具法律意见。
- 直接对客户、法院、仲裁机构、监管机构、交易对手、员工、平台或公众发送文件。
- 在公开仓库处理真实客户资料。
- 自动化提交、签署、发布或备案。
- 未经律师复核直接依赖输出。
- 连接真实生产系统或真实 MCP 后直接处理敏感资料。
- 替代律师判断。

## 版本演进摘要

- `v0.1.x`：完成合同、并购、诉讼三条核心路径，并建立 guardrails、evals、GitHub Actions 和 MCP 占位。
- `v0.2.0-alpha`：新增知识产权工作流。
- `v0.3.0-alpha`：新增 AI 治理工作流。
- `v0.4.0-alpha`：新增隐私与数据合规工作流。
- `v0.5.0-alpha`：新增劳动用工工作流。
- `v0.6.0-alpha`：新增监管合规工作流，8 个插件均达到 alpha 可试用。
- `v1.0.0`：完成整体审计、v1 readiness、受控虚构试点、post-release QA，进入 controlled pilot-ready 阶段。

## 贡献方式

欢迎提交：

- templates
- skills
- references
- evals
- 虚构样例
- 严格脱敏样例
- 文档改进
- 试点反馈总结

禁止提交：

- 真实客户资料
- 真实案件材料
- 真实合同
- 真实个人信息
- 真实员工信息
- 真实监管材料
- 真实交易资料
- 密钥、token、API key、Cookie
- 私有系统配置
- 生产系统连接信息

贡献前请阅读：

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [Data handling and anonymization guide](docs/data-handling-and-anonymization-guide.md)
- [Public vs private deployment boundary](docs/public-vs-private-deployment-boundary.md)

## 免责声明

本项目是法律工作流模板项目，不包含法律意见，不替代律师判断，不构成律师客户关系。

任何正式法律文件、意见、函件、诉讼文书、交易文件、监管回复、劳动文件、平台投诉或对外材料，均必须由合格法律专业人士复核后使用。
