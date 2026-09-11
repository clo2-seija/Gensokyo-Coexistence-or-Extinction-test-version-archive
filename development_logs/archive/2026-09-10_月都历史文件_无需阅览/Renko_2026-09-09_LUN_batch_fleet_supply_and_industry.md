> **历史文件，无需阅览。** 本文已于 2026-09-10 归档，仅留存开发过程，不作为当前实施计划、待办或维护要求。
> 当前内容请阅读[月都分支作者交接说明](../../../Reference/Renko_月都分支作者交接说明.md)及其中的维护指南。以下保留归档前正文，旧路径、数量与阶段结论可能过时。

# 月都舰队、补给与军工配套批次总览

- 日期：2026-09-09；作者：Renko。
- 分支：`codex/renko-strengthen-lunar-capital`。
- 基线提交：`eb515d381466dfcab5c7b9b2c542a9a1bdd41641`。
- 用户授权将本批已完成内容与开发日志统一提交；本次为本地提交，不包含远端推送。
- 本批共 31 个新增或修改文件，无删除文件。下列实现及状态为本批最终口径；分项日志此前的“未提交”描述属于当时记录。

## 一、港口判定与月海舰队

- 海军补给入口改用 `any_controlled_state = { naval_base > 0 }`，允许使用控制但尚未法理拥有的港口州。
- 新增“组建月海舰队”决议：0 政治点、仅一次、AI 意愿 100、优先级 70；无额外学说采用或完成条件。
- 决议立即给予“月海舰队”民族精神，再调用海军动态补给 3 次。
- 单次补给保持 40 艘，三次合计 120 艘；按现有设计覆盖三套目标水面编组及潜艇分队的船数，不代表脚本直接建立对应任务部队。
- 科技、特殊项目和设计不足时，沿用原有降级或跳过规则。舰载机进入库存，不直接建立空军联队。
- 民族精神一次性给予 30 项国家修正与 3 项装备修正；不含通用海军伤害、通用海军防御或顾问解锁。
- `screening_without_screens = 0.60` 与对应学说 `0.30` 同时生效时，修正相加为 `0.90`；决议本身不保证取得该学说。

## 二、补给数量写法修正

- 移除造舰 helper 的数量参数宏，采用 8 个固定数量批次，9 个调用位置通过 `= yes` 调用；循环内逐艘创建。
- 不采用已被用户实测否定的 `create_ship amount` 批量写法。
- 陆空库存共 33 个调用位置先设置 `Renko_LUN_supply_amount`，再调用 16 个共享 helper；库存效果读取 `LUN.Renko_LUN_supply_amount`，执行完清理变量。
- 继续通过既有 `meta_effect` 与脚本本地化选择装备类型，保留原有数量、科技与特殊项目分支。
- 旧有“可解析”结论只代表静态结构，不能证明参数效果实际有效。替换后的实现仍待实机检验。

## 三、停止抵抗补给与整编增援

- 新增独立 `on_capitulation`：引擎认定的胜利方 `FROM` 为月都时，在 LUN 国家作用域调用一次陆空动态补给。
- 不等待和谈；不增加周期性钩子、冷却或一次性领取标记。保留既有补给入口的首都控制条件。
- 创建陆军编制后，原直接生成步兵从 100 师降为 80 师，直接生成装甲仍为 20 师，再调用陆空补给 3 次。
- 条件满足时合计 92 个步兵师、32 个装甲师，另有 3 批陆空库存补给；本地化同步该数量。

## 四、莲子特供装甲配件

- 新增 12 个独立配件，涵盖燃油-电力引擎、燃气涡轮发动机、易维护改装、自动装弹机、火炮稳定器、附加机枪、烟幕发射器、燃油桶、锥膛炮转接器、交错负重轮及两级防空炮。
- 数值按用户指定参考完整移植，包括造价、可靠性、资源和转换成本；汽油、柴油引擎无数值差异，保留原模块。
- 使用原版槽位类别和图标；特供防空炮的父级引用同步衔接，不全局覆盖原模块。
- 新增隐藏科技，仅由月都新开局历史授予；无科技树位置且禁止常规研究。
- 同步 16 套陆军设计的创建脚本、AI 目标设计及允许模块清单。

## 五、月人工艺 MIO 政策

- 月都专用，费用 0，无额外规模或科技门槛。
- 对 MIO 适用装备给予可靠性 +20%、生产资源需求 -20%。
- AI 采用权重 100000，提供极高倾向，不强制切换。
- 复用原版机械天才政策图标，补齐中英本地化。

## 六、验证与交接状态

- 本批脚本结构解析、UTF-8 解码、本地化 BOM 和 Git 空白检查通过。
- 复核舰队一次性条件及 3 次调用、控制港口判定、已否定参数写法的移除、整编 80+20 与后续 3 次补给、海军精神条目数量。
- 配件任务已逐项核对 12 个模块数值和原版槽位、16 套脚本与 AI 设计一致性、隐藏科技与历史发放、图标和纹理、本地化键。
- MIO 政策范围、费用、两项数值、AI 权重及中英本地化检查通过。
- 尚未实机验证本批新增内容与修正后的生成数量；“待检验”状态保留。静态通过不代表加载、战斗、AI 采用或实际生成数量已获验证。
- 保留既有文件编码及换行格式；新增脚本和日志使用 UTF-8 / LF，新增本地化使用 UTF-8 BOM / LF。

## 文件清单

- `common/ai_equipment/Renko_LUN_land_designs.txt`
- `common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`
- `common/ideas/Renko_LUN_lunar_sea_fleet_ideas.txt`
- `common/military_industrial_organization/policies/Renko_LUN_policies.txt`
- `common/on_actions/Renko_LUN_capitulation_supply_on_actions.txt`
- `common/scripted_effects/Renko_LUN_dynamic_supply_scripted_effects.txt`
- `common/scripted_effects/Renko_LUN_equipment_design_scripted_effects.txt`
- `common/scripted_effects/Renko_LUN_naval_supply_scripted_effects.txt`
- `common/scripted_effects/Renko_LUN_templates_scripted_effects.txt`
- `common/technologies/Renko_LUN_special_tank_modules_tech.txt`
- `common/units/equipment/modules/Renko_LUN_special_tank_modules.txt`
- `development_logs/Renko_2026-09-09_LUN_batch_fleet_supply_and_industry.md`
- `development_logs/Renko_2026-09-09_LUN_lunarian_craftsmanship_policy.md`
- `development_logs/Renko_2026-09-09_LUN_special_tank_modules.md`
- `development_logs/Renko_2026-09-09_LUN海军动态补给.md`
- `development_logs/Renko_2026-09-09_LUN海军进度与换机交接.md`
- `development_logs/Renko_2026-09-09_月海舰队决议与民族精神.md`
- `development_logs/Renko_2026-09-09_月都停止抵抗陆空补给.md`
- `development_logs/Renko_2026-09-09_月都整编增援调整.md`
- `development_logs/Renko_2026-09-09_月都补给数量语法修正.md`
- `development_plans/Renko_LUN动态补给调用说明.md`
- `development_plans/Renko_LUN海军动态补给调用说明.md`
- `history/countries/LUN - Lunarians.txt`
- `localisation/English/Renko_LUN_lunar_sea_fleet_l_english.yml`
- `localisation/English/Renko_LUN_mio_l_english.yml`
- `localisation/English/Renko_LUN_special_tank_modules_l_english.yml`
- `localisation/English/Renko_LUN_templates_l_english.yml`
- `localisation/simp_chinese/Renko_LUN_lunar_sea_fleet_l_simp_chinese.yml`
- `localisation/simp_chinese/Renko_LUN_mio_l_simp_chinese.yml`
- `localisation/simp_chinese/Renko_LUN_special_tank_modules_l_simp_chinese.yml`
- `localisation/simp_chinese/Renko_LUN_templates_l_simp_chinese.yml`
