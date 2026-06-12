# Quickstart

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
