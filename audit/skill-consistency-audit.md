# Skill Consistency Audit

## 审计范围

审计对象为 8 个插件下的全部 `SKILL.md`。当前验证脚本确认 56 个 skill 文件具备必需 metadata。

## 结构一致性

标准结构：

- YAML frontmatter。
- Purpose。
- When to use。
- Inputs expected。
- Workflow。
- Output format。
- Quality checks。
- Escalation / attorney review gate。
- Confidentiality notes。
- Limitations。

## 通过项

- 全部 skill 已具备 YAML frontmatter，并通过 `validate_skill_metadata.py`。
- 全部插件均以“律师审阅用草稿”为主要输出定位。
- 主体口径均避免正式法律意见、正式对外文件或正式提交材料。
- 各插件均设置律师复核或升级闸门。
- 涉及法律依据、期限、监管口径、法院观点、仲裁或处罚风险时，基本均要求“待律师核验”。
- 涉及真实客户资料、个人信息、商业秘密、案件材料、合同或监管材料时，均要求脱敏或私有环境处理。

## 发现的问题

| 问题 | 影响 | 严重度 | 处理建议 |
| --- | --- | --- | --- |
| 个别旧文件在 Windows 终端显示为乱码，但验证和 Git 内容可正常处理 | 影响本地阅读体验 | P2 | v1.0 前统一检查 UTF-8 和换行策略 |
| 不同插件对“事实、风险、建议、待确认事项”的表述粒度不完全一致 | 影响输出审阅习惯 | P1 | 建立统一 skill 写作规范 |
| 部分 skill 对输出长度控制没有统一要求 | 可能导致草稿过长 | P2 | 增加“短表优先、必要时分段”的全局规则 |
| cold-start skill 的访谈深度因业务线不同存在风格差异 | 可接受，但试点时可能影响 profile 质量 | P2 | 制作统一 cold-start 访谈模板骨架 |

## 结论

未发现 P0。v1.0 前应优先统一 skill 写作规范、输出长度规则和 UTF-8 检查，不建议本轮对业务逻辑大改。
