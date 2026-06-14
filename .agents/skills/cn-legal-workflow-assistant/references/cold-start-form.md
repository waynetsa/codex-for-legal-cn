# Cold-start Form

Use this form before any substantive workflow analysis.

## Required Questions

Ask these questions in concise Chinese. Ask no more than 8 questions at once.

1. 你的团队或个人 playbook 是什么？如没有，可以写“使用默认”。
2. 本次风险偏好是什么？稳健、平衡、激进，或自定义。
3. 你希望输出采用什么格式？例如 Markdown 表格、备忘录、清单、项目台账。
4. 哪些事项必须升级给合伙人、负责人、管理层或客户决策人？
5. 本次有哪些禁止事项？例如不得出具正式法律意见、不得对外发送、不得处理未授权材料。
6. 哪些节点必须由律师复核？
7. 常用语气和交付物风格是什么？例如简洁、审慎、管理层可读、律师工作底稿。
8. 是否允许生成本次会话 practice profile 草稿？默认只在会话中使用，不写入仓库。

## Conservative Defaults

Use these defaults when the user says "使用默认":

- 风险偏好：稳健、宁可多提示风险。
- 输出格式：结构化 Markdown 表格 + 待补材料 + 升级事项。
- 升级规则：高风险、红旗风险、不确定法律依据、涉及对外提交、涉及真实客户决策时升级。
- 禁止事项：不得生成正式法律意见、不得直接对外发送、不得处理未授权真实材料。
- 律师复核节点：任何正式交付前均需律师复核。
- 语气风格：审慎、清晰、面向律师继续编辑。

## Minimum Viable Input List

If the user cannot answer all questions, ask for at least:

1. 选择的工作流和主工作流。
2. 是否使用默认风险偏好和输出格式。
3. 是否确认材料已获授权在私有环境处理。
4. 是否允许生成本次会话 practice profile 草稿。
