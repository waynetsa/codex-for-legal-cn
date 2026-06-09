# Quickstart

本文面向普通法律工作者，说明如何在 Codex 中试用 `codex-for-legal-cn`。

## 安装

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
```

如果你的电脑没有系统 Python，可以使用 Codex 或组织 IT 提供的 Python 运行脚本。

## 复制或启用插件

把需要的插件目录复制或引用到 Codex 可识别的插件路径：

- `plugins/cn-commercial-legal`
- `plugins/cn-corporate-legal`
- `plugins/cn-litigation-legal`

律所内部建议由知识管理或 IT 团队统一维护版本。

## 从 cold-start 开始

第一次使用时，不要直接审合同或案件材料。先调用对应插件的 `cold-start-interview`，回答团队名称、客户类型、风险偏好、升级规则、复核人和输出格式等问题。Codex 会生成 `practice-profile.md` 草稿，负责律师确认后再用于后续技能。

`practice-profile.md` 是本地工作文件，不应提交到公开仓库。

## 常用调用示例

合同审查：

```text
请使用 cn-commercial-legal 的 contract-review 技能，基于本项目 practice profile，审查我上传的供应商服务合同，输出风险等级表、逐条修改建议、待客户决策事项和需合伙人升级事项。
```

NDA 初筛：

```text
请使用 cn-commercial-legal 的 nda-triage 技能，把这份 NDA 分成绿色、黄色或红色，并说明是否可快速放行。
```

合同偏离清单：

```text
请使用 cn-commercial-legal 的 deviation-memo 技能，对比合同文本和团队 playbook，生成偏离清单、建议谈判语言和审批人。
```

并购尽调：

```text
请使用 cn-corporate-legal 的 diligence-tabular-review 技能，读取资料室文件清单，生成一张尽调问题表，列明文件摘要、风险点、重大性、待追问问题和披露建议。
```

交割清单：

```text
请使用 cn-corporate-legal 的 closing-checklist 技能，根据尽调问题和交易结构生成交割前、交割日、交割后事项清单。
```

披露清单：

```text
请使用 cn-corporate-legal 的 disclosure-schedule 技能，根据尽调问题生成披露清单初稿，并标明待律师核验点和客户确认事项。
```

诉讼时间线：

```text
请使用 cn-litigation-legal 的 chronology-builder 技能，根据案件材料生成事实时间线，列明日期、事件、参与方、证据来源、争议程度和待核实事项。
```

证据目录：

```text
请使用 cn-litigation-legal 的 evidence-index 技能，整理证据目录，列明证据编号、证明目的、三性提示、原件情况和待补强事项。
```

庭前准备：

```text
请使用 cn-litigation-legal 的 hearing-prep 技能，根据事实时间线、证据目录和争点表生成庭前准备提纲。
```

## 使用材料要求

只上传脱敏材料。真实客户名称、真实案件材料、商业秘密、个人信息、证据原文和未公开交易安排不得进入公开仓库。所有输出均为“律师审阅用草稿”，正式发送、提交、签署或依赖前必须由律师复核。
