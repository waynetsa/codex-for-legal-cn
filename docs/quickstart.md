# Quickstart

本文面向普通法律工作者，帮助你在 Codex 中试用本项目。

## 安装

```bash
git clone https://github.com/waynetsa/codex-for-legal-cn.git
cd codex-for-legal-cn
```

运行基础检查：

```bash
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
```

## 复制插件

将需要的插件目录复制或引用到 Codex 可识别的插件路径：

- `plugins/cn-commercial-legal`
- `plugins/cn-corporate-legal`
- `plugins/cn-litigation-legal`

实际路径取决于你的 Codex 安装和组织管理策略。律所内部建议由知识管理或 IT 团队统一维护插件版本。

## 运行 cold-start

第一次处理事项时，先调用对应插件的 `cold-start-interview` skill，收集事项背景、法域假设、客户角色、输出类型、保密要求和律师复核人。

## 调用合同审查

使用 `cn-commercial-legal/contract-review`，输入脱敏后的合同文本、交易背景、关注条款和内部风险口径。输出应标注“律师审阅用草稿”。

## 调用尽调审阅

使用 `cn-corporate-legal/diligence-tabular-review`，输入脱敏资料室索引、文件摘要和项目阶段。输出尽调问题台账、待确认事项和升级建议。

## 调用诉讼时间线

使用 `cn-litigation-legal/chronology-builder`，输入脱敏事实材料、证据摘要和关键日期。输出事实时间线，并区分已证实、待核实和存在矛盾的事实。
