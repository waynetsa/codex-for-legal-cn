# Simulated Lawyer Roles

## v1 preflight 修复后状态

三类模拟律师反馈均已追加 preflight 状态。评分含义统一如下：

- `go`：仅表示适合进入受控脱敏试点或 v1.0 release candidate，不表示可生产使用。
- `conditional-go`：表示仍需补字段、补边界或补律师复核说明。
- `no-go`：表示存在 P0/P1 或严重误用风险。

本轮修复后未保留 P0/P1，P2 已清零，P3 保留为 v1 后体验优化。

## 合伙人

关注风险边界、客户决策、升级事项、法律责任和交付质量。

评分重点：

- `output_usability_score`
- `risk_identification_score`
- `editing_required_level`
- `missed_issue_notes`
- `false_positive_notes`
- `confidentiality_issue_found`
- `go_no_go_recommendation`

## 主办律师 / 资深律师

关注事实结构、证据、条款、输出可编辑性、是否减少重复劳动。

评分重点：

- 输出是否便于继续修改
- 风险和证据缺口是否清楚
- 是否能减少初步整理时间
- 是否需要重写结构

## 初级律师

关注是否易用、是否能帮助搭框架、是否能减少遗漏、是否容易照着改。

评分重点：

- 输入材料能否转成清晰工作底稿
- 模板字段是否容易理解
- 是否提示待补材料和升级事项
- 是否有正式法律意见口吻
