# IP Findings

> 律师审阅用草稿。本评测仅使用虚构材料，不构成法律意见。

## 通过项

- cold-start 能形成 IP 团队画像、风险偏好、证据处理规则和复核节点。
- rights-chain-review 能识别网络剧、角色、海报、音乐、游戏皮肤和品牌标识的主要权利对象。
- 权利缺口识别有效，能发现角色授权、音乐、字体、背景纹理等问题。
- infringement-triage 区分相似点、差异点、证据缺口和可能抗辩方向，未作最终侵权结论。
- ip-license-review 能识别排他授权、转授权、权利瑕疵担保、结算审计和到期后处理风险。
- evidence-preservation-checklist 包含证明目的、形成时间、保存方式、三性提示和待补强事项。
- takedown-and-demand-letter-outline 明确不得直接发送或提交。
- 高风险和红旗风险均进入升级事项。
- 法律依据、平台规则和证据判断均标注“待律师核验”或“待律师判断”。

## 失败项

无 P0 失败项。

## 需要修 skill 的问题

- `infringement-triage` 可增加“比对材料优先级”和“比对方法说明”字段。
- `ip-license-review` 可进一步要求替代表述区分授权方口径和被授权方口径。

## 需要修 template 的问题

- `takedown-demand-letter-outline.md` 可增加平台材料清单细分。
- 部分宽表可提供紧凑版或拆分版。

## 需要修 reference 的问题

- `platform-takedown-workflow.md` 可增加平台投诉前材料自查清单。

## 是否达到 IP MVP acceptance 标准

达到。当前输出可以支持律师基于虚构材料完成 IP MVP 端到端试跑，但仍建议先做 IP alpha 修复后再发布 `v0.2.0-alpha`。

## 是否建议进入下一轮 IP alpha 修复

建议。下一轮应优先处理 P1：侵权比对优先级、授权替代表述颗粒度、平台材料清单。
