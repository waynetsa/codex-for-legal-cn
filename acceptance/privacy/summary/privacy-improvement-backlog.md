# Privacy Improvement Backlog

> 律师审阅用草稿。本 backlog 基于虚构验收样例生成，不构成法律意见。本轮只记录问题，不修复。

## 总览

- P0：0
- P1：3
- P2：3

## P0

暂无 P0 问题。

## P1

| 编号 | 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRIV-P1-001 | 敏感个人信息判断说明还不够细，尤其是位置信息、未成年人和客服敏感描述的触发条件 | `personal-info-processing-map`, `privacy-impact-assessment` | `plugins/cn-privacy-legal/skills/*`, `acceptance/privacy/output/*` | 增加敏感个人信息判断短表和默认升级条件 | P1 | 是 | 是 |
| PRIV-P1-002 | 数据处理协议角色判断路径较粗，需更清楚区分委托处理、共同处理和第三方接收方 | `data-processing-agreement-review` | `plugins/cn-privacy-legal/skills/data-processing-agreement-review/SKILL.md` | 在 workflow 和模板中增加角色判断路径和待律师核验列 | P1 | 是 | 是 |
| PRIV-P1-003 | 影响评估输出有风险等级，但剩余风险、整改责任人和管理层接受机制不够明确 | `privacy-impact-assessment` | `plugins/cn-privacy-legal/templates/privacy-impact-assessment-outline.md` | 增加剩余风险等级、责任部门、整改期限和风险接受人 | P1 | 是 | 是 |

## P2

| 编号 | 问题描述 | 影响 skill | 影响文件 | 建议修复方式 | 优先级 | 是否需要律师复核 | 是否建议进入下一轮 PR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRIV-P2-001 | 处理活动台账宽表较长，影响非技术律师快速阅读 | `personal-info-processing-map` | `templates/personal-info-processing-map.csv`, `acceptance/privacy/output/personal-info-processing-map-result.md` | 拆成核心处理活动表、第三方接收方表、升级事项表 | P2 | 否 | 是 |
| PRIV-P2-002 | 用户请求响应答复提纲未按查询、复制、删除、注销分别拆分 | `data-subject-request-workflow` | `templates/data-subject-request-workflow.md` | 增加分类型答复提纲 | P2 | 是 | 是 |
| PRIV-P2-003 | 数据出境参考资料可增加远程运维、境外客服、集团内访问的场景化问题清单 | `data-transfer-triage` | `references/data-transfer-triage-checklist.md` | 增加场景化问题清单 | P2 | 是 | 是 |

## 发布判断

P0 为 0，P1 可控，但仍建议先完成 privacy alpha 修复，再考虑发布 `v0.4.0-alpha`。
