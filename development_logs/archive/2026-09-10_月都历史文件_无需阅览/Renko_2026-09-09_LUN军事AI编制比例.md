> **历史文件，无需阅览。** 本文已于 2026-09-10 归档，仅留存开发过程，不作为当前实施计划、待办或维护要求。
> 当前内容请阅读[月都分支作者交接说明](../../../Reference/Renko_月都分支作者交接说明.md)及其中的维护指南。以下保留归档前正文，旧路径、数量与阶段结论可能过时。

# 月都军事 AI 编制比例

> **禁止合并：月都配套尚未完成，不要将 codex/renko-strengthen-lunar-capital 分支合并到 main 或其他分支。当前提交仅用于保存和同步开发进度，不代表可合并、可发布或已通过游戏验证。**

> 装备设计及相关配套仍待完成，装甲实际满装、AI 招募和闪退修复均未完成游戏内验证。配套完成后须重新评估，并取得明确合并授权。

- 日期：2026-09-09；分支 codex/renko-strengthen-lunar-capital，新开局基线。
- 参考日本特殊属国 JAP_rework_special_subject_army_templates.txt 的常驻 role_ratio 和 abort_when_not_enabled；数量统计参考 JAP_ai_template_infantry_should_suppress_for_division_count。
- 用户授权复制本机原版 common/ai_strategy/default.txt、doctrines.txt。同路径覆盖，原文件不改；目标目录此前无这两文件。
- default 的 11 个陆军比例策略组、doctrines 的 8 个陆军比例策略组对 LUN 屏蔽。两个混合组拆出陆军 role_ratio 至 Renko 前缀组，沿用全部原启停条件，保留原组非陆军效果；其他国家维持原有策略值。
- 新建 common/ai_strategy/Renko_LUN_military.txt，统一月都军事策略入口。步兵常驻 +100、装甲常驻 +100；步兵类型师超过 200 时叠加 -100，合计 0；回落至 200 或以下时撤销抵扣。
- has_army_size 按步兵类型统计，非仅按 Renko Lunar Infantry Division 名称计数；不使用总师数作为门槛。
- 不新增周期钩子、flag、事件、装备生产策略或镇压编制权重；不修改上一轮决议及其 AI 权重。
- 未运行游戏，策略加载、引擎刷新与实际招募行为待检验；角色权重为 0 不等于强制撤销已有招募队列或删除部队。本次按用户授权纳入月都分支提交与推送，仅同步开发进度。

## 隔离的原版策略

- default.txt: default_unit_production
- default.txt: default_unit_production_super_heavies
- default.txt: default_unit_production_land_cruiser
- default.txt: default_paratroopers_production
- default.txt: default_major_SF_para
- default.txt: default_major_SF_marines
- default.txt: default_garrison_production
- default.txt: default_mountaineers_production
- default.txt: default_mobile_production
- default.txt: default_armored_production
- default.txt: highered_armored_production
- doctrines.txt: DOCTRINE_stop_making_horsies
- doctrines.txt: DOCTRINE_no_cavalry
- doctrines.txt: DOCTRINE_MW_mobile_warfare_ratios
- doctrines.txt: DOCTRINE_SF_superior_firepower_ratios
- doctrines.txt: DOCTRINE_SF_concentrated_fire_plans_ratios
- doctrines.txt: DOCTRINE_GB_grand_battle_plan_ratios
- doctrines.txt: DOCTRINE_MA_mass_assault_ratios
- doctrines.txt: DOCTRINE_MA_large_front_operations_ratios

## 静态验证

- 19 个陆军比例组均对 LUN 隔离；逐组比较所有原 ai_strategy 值、enable/abort 条件，拆分前后保持一致，非目标组内容不变。
- 门槛演算：199/200 师为 100，201 师为 0，回到 200 师恢复 100；装甲始终 100。该演算不代表游戏内刷新测试。
- 三个脚本括号平衡，UTF-8 无 BOM／LF；工作区差异空白检查通过（保留上一轮旧文件 CRLF）。

## 补充 XP 与 PP 管理

- 按用户要求，在 Renko_LUN_military.txt 增加 Renko_LUN_xp_and_pp_management，完整沿用 Japan_rework/common/ai_strategy/Jap_rework_ai_production.txt 中 operations_JAP_dont_waste_xp 的 7 项参数，仅替换国家范围为 LUN 与策略标识符。
- 陆军 division_template XP 优先级 -9999；三军 upgrade_xp_cutoff 均为 9999；idea、decision、admiral 的 PP 优先级均为 100。
- 静态核对：7 项 type/id/value 与源文件完全一致，原有编制比例内容逐字节保留，新内容 UTF-8 无 BOM／LF，括号平衡。
- 用户报告缺少 XP/PP 管理会导致闪退；本轮按要求补齐，闪退修复状态为待检验，未运行游戏验证。
- 不涉及本地化修改；本次按用户授权纳入月都分支提交与推送，仅同步开发进度。

## 提交前复核

- 本轮 18 个文件一并提交；本地 AGENTS.md、descriptor.mod、工坊补齐资源与审计文件不纳入。
- 完整暂存检查中，原版复制文件保留原版行尾空白；已核对其来源。拆分策略留下的空白缩进行已清理，新编制文件末尾多余空行已移除；未改动策略语义。
- 本次推送仅用于同步未完成的开发进度，禁止据此合并本分支。
