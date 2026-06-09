# Contributing

感谢参与 Codex for Legal CN。

仓库地址：https://github.com/waynetsa/codex-for-legal-cn

## 可以贡献什么

- 新的 Codex skill。
- 新的模板、检查清单和工作底稿格式。
- 脱敏或完全虚构的评测样例。
- 文档、术语表、本地化原则和安全规则。

## 不得提交什么

- 真实客户资料。
- 真实案件材料。
- 商业秘密。
- 个人信息或敏感个人信息。
- 第三方专有模板、收费资料或未经授权的文档。
- 未经核验的法律依据、案例或监管口径。

## 贡献要求

- 默认使用简体中文。
- 法律输出模板应标注“律师审阅用草稿”。
- 涉及中国法时，默认适用中国大陆法律语境。
- 如无法提供来源，请写“待律师补充法律依据”。
- 新增 skill 时，请包含 YAML frontmatter，并覆盖 Purpose、When to use、Inputs expected、Workflow、Output format、Quality checks、Escalation / attorney review gate、Confidentiality notes、Limitations。

## 提交流程

1. Fork 本仓库。
2. 新建分支。
3. 运行验证脚本：

```bash
python scripts/validate_structure.py
python scripts/validate_skill_metadata.py
```

4. 提交 Pull Request，并说明新增内容是否含有虚构样例、脱敏样例或纯模板内容。
