# 月都分支开发交接说明

本次为月之都（LUN）补齐专属军队、学说、装备设计、军工与持续补给，并增加建设、占领整合和配套 AI，以及独立难度、莲子的协助和正邪削弱舰队。保留原有登场剧情、国策前置与宣战节奏，主要通过“月战最高司令部”“月都军备局”和年度科技决议承接功能。

本文统一汇总截至 2026-09-10 的同一轮月都开发，包含 `2cae441` 起的既有开发、`1339c1b` 基线及本轮难度与补给收尾更新；早期撤回方案不计入成果。本文为唯一现行作者交接入口。路径均相对 MOD 根目录。原版覆盖的逐文件修改与升级方法见 [原版覆盖维护指南](Renko_月都原版覆盖维护指南.md)。

2026-09-10 文件整合：79 个相关脚本和本地化文件收拢为 18 个，功能及原文保持不变；下表已更新为现行路径。整合映射、语法边界和静态验证见 [月都文件整合记录](../development_logs/Renko_2026-09-10_月都文件整合.md)。未实机验证。

## 功能与文件

| 模块 | 最终改动 | 主要维护文件 |
| --- | --- | --- |
| 登场与国策接口 | “修补破碎的国土”设置司令部初始化旗标；删除登场时旧山地师模板和 100 师刷兵。月都首个入侵准备国策删除旧模板和 125 师刷兵，改为调用两批陆空补给，H/L 四批；对中国及周边宣战阶段同为两批／四批，第三阶段另发一批海军，保留其余奖励。 | `common/national_focus/kyo-focus.txt`、`common/national_focus/luner-capital.txt` |
| 司令部与补给范围 | 新增专属决议入口。“连接山海”给予月都补给范围 +9999%，并一次性为全球各州添加 50 当地补给；州补给敌我共享，不能当作月都独占奖励。 | `common/decisions/categories/Renko_LUN_categories.txt`、`common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`、`common/scripted_effects/Renko_LUN_supply_scripted_effects.txt`、`common/ideas/Renko_LUN_ideas.txt`、`common/dynamic_modifiers/Renko_LUN_supply_dynamic_modifiers.txt` |
| 侵军兵种与训练 | 新增侵军步兵、中坦、中坦歼三种特种营，以及中防空、重坦歼两种团属支援。中坦歼每营 40 辆；装甲营仅平原、沙漠攻击及移动 +5%，两种支援不附带地形修正。“精锐士兵训练”提高特种部队容量。 | `common/units/Renko_LUN_invasion_units.txt`、`common/technologies/Renko_LUN_technologies.txt`、`history/countries/LUN - Lunarians.txt`、`common/ideas/Renko_LUN_ideas.txt` |
| 三军学说 | 新增 3 个主学说、12 个三军子学说、12 条独立轨道和“月之军势”特种学说；司令部决议一键授予。 | `common/doctrines/grand_doctrines/Renko_LUN_grand_doctrines.txt`、`common/doctrines/subdoctrines/Renko_LUN_subdoctrines.txt`、`common/doctrines/tracks/Renko_LUN_doctrine_tracks.txt`、`common/scripted_effects/Renko_LUN_military_scripted_effects.txt` |
| 整编与增援 | 新增步兵、装甲、骑兵镇压三套编制。整编先解锁所需科技及九项基础陆空设计，再生成 80 步兵师、20 装甲师并调用三批补给；满足入口条件时合计 92 步兵师、32 装甲师。镇压模板不生成地图部队。 | `common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`、`common/scripted_effects/Renko_LUN_military_scripted_effects.txt`、`common/ai_templates/Renko_LUN_templates.txt` |
| 年度科技与军备设计 | 1936—1945 共十批、321 项年度科技，次年 1 月开放领取。军备局提供陆海空分代设计，保留科技提前解锁与日期保底；后续追加正规航母三代设计，九项初始陆空设计并入整编。 | `common/decisions/Renko_LUN_annual_technology_decisions.txt`、`common/decisions/Renko_LUN_armaments_bureau_decisions.txt`、`common/scripted_effects/Renko_LUN_equipment_design_scripted_effects.txt`；分类在 `common/decisions/categories/` 下同主题文件 |
| 月人制造与特供模块 | 新增专属军工组织“月人制造”，奖励集中于初始特质“高天原制造商”；新增免费工艺政策和 12 个专属坦克模块，同步 16 项装甲设计与 AI 目标。隐藏科技由月都国家历史授予；EASY 下幻想乡可通过“奥术解密”解锁同一套营与配件。 | `common/military_industrial_organization/organizations/Renko_LUN_organization.txt`、`common/military_industrial_organization/policies/Renko_LUN_policies.txt`、`common/units/equipment/modules/Renko_LUN_special_tank_modules.txt`、`common/technologies/Renko_LUN_technologies.txt` |
| 陆空动态补给 | 每批在受控首都生成 4 步兵师、4 装甲师，并按现行编制发放陆军储备和飞机。整编、入侵准备国策、月都作为胜利方的停止抵抗事件均可调用；AI 整编后每 180 天追加一批及后勤库存，H/L 的该陆空循环和胜利补给各增至两批。首次整编三批不翻倍。 | `common/scripted_effects/Renko_LUN_supply_scripted_effects.txt`、`common/scripted_localisation/Renko_LUN_dynamic_supply_scripted_loc.txt`、`common/on_actions/Renko_LUN_capitulation_supply_on_actions.txt`、`common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`、`common/scripted_effects/Renko_LUN_supply_scripted_effects.txt` |
| 月海舰队 | 控制港口即可领取一次性舰队及民族精神，并开启 AI 每 365 天补给。每批目标为 6 护航航母、9 重巡、4 正规航母、16 战列舰与 10 潜艇，共 45 艘；一次性决议三批共 135 艘，实际生成受设计、舰载机与港口条件限制。超重战列及潜母按定型状态替换部分普通舰。 | `common/scripted_effects/Renko_LUN_supply_scripted_effects.txt`、`common/ideas/Renko_LUN_ideas.txt`；入口仍在司令部决议文件 |
| 军事与生产 AI | 独立步兵／装甲招募比例、XP／PP 管理、陆空库存调产、海军角色权重与装备设计目标。步兵类型师超过 200 时抵消其新增招募权重。舰队分为巡逻、打击、潜艇破交，制海舰队允许追加编组，组建月海舰队后提高登陆倾向。 | `common/ai_strategy/Renko_LUN_strategy.txt`；`common/ai_equipment/Renko_LUN_designs.txt`；`common/ai_navy/fleet/Renko_LUN_fleet_templates.txt`、`common/ai_navy/taskforce/Renko_LUN_taskforce_templates.txt`；调产循环在 `common/decisions/Renko_LUN_armaments_bureau_decisions.txt` 与 `common/scripted_effects/Renko_LUN_military_scripted_effects.txt` |
| 基建与工业 | 可重复补满控制州基础设施；一次性增加 40 地图外民工、40 军工，控制港口后可领取 30 地图外船坞。建筑 AI 按民工、船坞比例纠偏，其余优先军工。 | `common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`；`common/ai_strategy/Renko_LUN_strategy.txt`、`common/scripted_triggers/Renko_LUN_construction_scripted_triggers.txt` |
| 资源、人力与占领 | 首都获得石油 200，钢、铝、钨、铬、橡胶、煤各 100，附带资源与燃油增益；人力低于 100 万时可重复征召 100 万，重新启用间隔 1 天；正邪完成“翻转主义”后永久封锁该人力决议，保留显示并提示原因。新增月都统制占领法案；控制且顺从度达到 50 的非核心州可逐州免费整合。 | `common/decisions/Renko_LUN_lunar_war_high_command_decisions.txt`；`common/ideas/Renko_LUN_ideas.txt`、`common/occupation_laws/Renko_LUN_occupation_laws.txt` |
| 国家精神调整 | 月球指挥网新增陆军师进攻速度 +30%；净化兵器序列仅保留夺取制空权任务效率 +15%、跨空域力量投射 +10%、陆军攻击和防御各 +10%；移除其余修正及装备加成。 | `common/ideas/difficulty.txt` |
| 调试、本地化与素材 | 增加调试模式下的“莲子的工具箱”，可直接部署月都并让日本吞并幻想乡。新增中英文本；侵军兵牌共 15 张 PNG；补齐工坊部署资源与描述符。 | `common/decisions/Renko_debug_toolbox_decisions.txt`、`common/decisions/categories/Renko_debug_toolbox_categories.txt`；`localisation/simp_chinese/`、`localisation/English/` 的 `Renko_LUN_*` 和 `Renko_debug_toolbox_*`；`interface/Renko_LUN_invasion_unit_icons.gfx`、`gfx/interface/counters/`、`gfx/texticons/`、`asset_sources/Renko_LUN_invasion_units/`、`descriptor.mod` |

学说附带 AI 比例已恢复原版，不再维护 `common/ai_strategy/doctrines.txt` 覆盖；月都专属学说与招募策略保持。现行原版覆盖共 8 项，移除历史另行保留。

## 维护时应一起修改的接口

- **编制与补给**：改营数或装备需求时，同步赠送模板、AI 目标和陆空补给储备。储备按固定编制计算，不会随玩家改编自动更新。
- **装备与海军**：设计名称、定型旗标、AI 目标、允许模块和动态补给必须一致。航母另联动舰载机型号及数量；巡逻扩容后，生产权重仍沿用此前设定，不能从刷船数反推生产比例。
- **国家与作用域**：国家存在性写成 `LUN = { exists = yes }`；海军入口检查“控制港口”。停止抵抗事件的 `FROM` 是胜利方，补给落在 LUN 作用域。
- **节奏与循环**：陆空 180 天、海军 365 天循环由对应决议启动，生产调整另有 30 天任务；没有新增日／月钩子。以新开局为维护基线。

## 四档独立难度

最高司令部沿用 Renko_LUN_lunar_war_high_command_initialized 解锁。一次性零费用决议仅在 KYO 存在时显示，AI 权重 1000，执行后在 KYO 作用域发送 Renko_LUN_difficulty.1，不保证 AI 于解锁当日立即执行。事件不配图、不设详情页，中文标题为「月都难度调整选单」。

| 难度 | 选项名称 | 最终效果 |
|---|---|---|
| EASY | §7白雪纷飞的程度(EASY)§! | 给月都量子扰动；给 KYO 解锁莲子的协助 |
| NORMAL | §6漫天风霜的程度(NORMAL)§! | 无额外奖励或惩罚 |
| HARD | §4暴雪蔽日的程度(HARD)§! | 隐藏设置月都高于 NORMAL 旗标，使指定来源陆空增援翻倍 |
| LUNATIC | §O雪虐风饕的程度(LUNATIC)§! | 同 HARD，并给月都永恒之月 |

H/L 使用同一 LUN 国家旗标 Renko_LUN_difficulty_above_normal，设置过程隐藏，公开红色提示「月都获得更多额外装备补给」。没有新日/月钩子或旧存档迁移分支。

量子扰动 Renko_LUN_quantum_disturbance 仅以 tag = KYO 的 targeted_modifier 提供攻击 -50%、防御 -50%、主力舰攻击 -30%。不加突破惩罚，也不作用于其他对手。中文描述为作者提供的莲子保护梅莉所见世界、干涉月都装备的故事；英文沿用 Merry / Renko 称呼。图标是原子盾徽。

永恒之月 Renko_LUN_eternal_moon：生产效率保持 +100%、进攻不损耗堑壕（1）、作战准备下降率 -100%、固定堑壕上限 +6。仅 L 选项授予；图标是弦月盾徽。

## 莲子的协助与奥术解密

Renko_KYO_lunar_technology_category 只对 original_tag = KYO 开放，并仅在 EASY 设置 Renko_KYO_arcane_decryption_unlocked 后显示；描述留空，完成唯一决议后空组隐藏。分类独立于原月面决战指挥部的路线旗标。

奥术解密零费用、一次性、与 LUN 交战时可执行；AI 权重 1000。实际 set_technology 隐藏，公开提示与描述均为「获得月都的特殊作战营和配件。」

授予 Renko_LUN_invasion_units_tech 与 Renko_LUN_special_tank_modules_tech，永久解锁三种营、两种支援连及十二种坦克配件。不直接生成装备库存、设计或军队，不绕过生产与特种部队容量要求。科技定义只更新授予来源注释。

## 陆空与海军增援

Renko_LUN_grant_dynamic_equipment 和 Renko_LUN_grant_dynamic_navy 各自使用一条 custom_effect_tooltip，原实现置于 hidden_effect 内；公开调用显示概述，原本隐藏的调用继续隐藏。

| 陆空调用来源 | E/N 次数 | H/L 次数 |
|---|---:|---:|
| 第一阶段国策 prepare_for_invasion_to_earth_1 | 2 | 4 |
| 对中国宣战 prepare_for_invasion_to_earth_2 | 2 | 4 |
| 对邻国及列强宣战 prepare_for_invasion_to_earth_3 | 2 | 4 |
| 陆空循环 mission | 1 | 2 |
| on_capitulation：FROM 是月都 | 1 | 2 |

第三阶段另调用一次海军发放，不按 H/L 翻倍。额外陆空调用紧随原调用，数量一对一；国策调用在 every_country 外，避免随目标数成倍重复。首次整编军队等未指定来源不加倍。

总入口仍要求月都存在，陆空要求控制首都，海军要求控制海军基地。陆空入口每次本身生成四个步兵师、四个装甲师并发放储备装备，因此调用翻倍同时增加部队。原后勤周期、宣战目标及国策时间保持原样。

## 正邪削弱月海舰队

「扭转月都的命运」在 LUN 作用域隐藏设置 Renko_LUN_lunar_sea_fleet_disrupted；已拥有完整版时公开替换为 Renko_LUN_lunar_sea_fleet_disrupted_idea。若尚未组建，后续组建决议直接给削弱版；保险条件隐藏。

削弱版只保留 screening_without_screens = 0.60、主力舰防御 +10%、命中率 +10%、协同性 +10%、舰载机出击效率 +15%，无装备加成。原完整版精神、独立学说保持不变。

## 坦歼与徽章资源

步兵数值未修改。中坦歼恢复接近中坦的底盘尺度，保留低矮战斗室；重坦歼保留厚重战斗室并适当延长炮管、左移轮廓。

兵牌总尺寸仍为大图 152×42、小图 60×12，两帧一致。单帧透明边距（左/上/右/下）：中坦歼大图 6/11/6/4，小图 2/1/3/2；重坦歼大图 4/7/6/5，小图 2/1/3/1。地图与文本小图一致。

render_tankdestroyer_icons.py 依赖 resvg-py 与 Pillow，可按 manifest.json 重建六张坦歼贴图。两枚精神徽章也保留 SVG 源稿；仅实际注册的最终 PNG 放在 gfx，工作预览不入游戏目录。

## 验证状态与历史资料

本轮新增决议、本地化和图标注册已并入现有总文件；玩法详情统一维护在本文，逐文件清单及归并验证保留在 [本轮更新记录](../development_logs/2026-09-10_月都分支本轮更新与作者交接.md)。本轮没有新增或修改原版覆盖。

英文难度选项及新增精神／提示已有对应文本；事件英文标题和长正文仍为早期简短版本，尚未与后来指定的中文标题和完整说明同步。

代码已落地，开发记录包含结构、引用、编码及部分数量核对；本轮另已核对难度旗标、补给调用次数、隐藏提示、贴图尺寸与透明边距，以及文件归并前后定义、引用与内容一致性；未实机验证。补给实际入库、AI 招募／生产／编组、镇压模板选择及最新精神效果仍须以游戏与错误日志结果判断，不能把历史静态通过记录当作发布验收。

中间日志与计划已归档，标记为“历史文件，无需阅览”；日常维护只需阅读本说明和维护指南。历史内容不再作为当前待办。现行代码说明：早期“100 步兵＋20 装甲”、单批 40 艘／总计 120 艘、巡逻理想 4 航母＋6 重巡、整编 AI 权重 0 等记录均已被后续修改取代。早期 WIP 的装备设计缺口已有后续实现；归档不等于合并或发布授权。

工坊补齐资源属于加载配套，不是本次新绘素材；来源与哈希核对记录见 `development_logs/archive/2026-09-10_月都历史文件_无需阅览/2026-09-09_月都分支测试加载部署.md`。月都原作设定调查与尚未实现的设计讨论保留为参考，不列入完成项。
