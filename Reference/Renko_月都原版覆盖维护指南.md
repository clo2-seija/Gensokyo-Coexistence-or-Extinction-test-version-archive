# 月都分支原版覆盖维护指南

适用代码：`aac2956` 加 2026-09-10 学说 AI 覆盖移除调整（当前工作区）。本指南面向幻想乡维护者，完整列出本轮月都开发涉及的 **8 个现行原版同路径脚本覆盖，以及 1 项移除记录**，不代表全 MOD 的原版覆盖清单。功能概览见 [作者交接说明](Renko_月都分支作者交接说明.md)，文件哈希和覆盖状态见 [追踪账本](vanilla_override_ledger.md)。

## 先区分两种基线

月都增量基线为 `2cae441`。现行覆盖中 4 个文件是本轮新复制原版；另外 4 个文件在本轮之前已有 MOD 自身覆盖，月都只在其上增加隔离或权重。这 4 个文件相对当前原版的其他差异不能归入本次月都修改，也不能在更新时丢弃。

以下各节提供可搜索的定义名和具体改动；配套 `lun_override_patches/01.patch` 至 `09.patch` 保存对应增量，其中 02 已退役，仅供历史追溯。新复制文件的补丁以本次核对的原版为起点，既有覆盖的补丁以 `2cae441` 中的 MOD 文件为起点。补丁是审阅附件，不能不看基线就自动套到升级后的游戏文件上。

## 01．通用 AI 策略

路径：`common/ai_strategy/default.txt`。本轮新复制原版，同路径覆盖，不需要新增 `replace_path`。附件：[01.patch](lun_override_patches/01.patch)。

**目的：** 避免月都专属招募与装备生产倾向同原版通用策略叠加，同时保留运输船需求及其他国家行为。

直接在 `allowed` 中增加 `NOT = { original_tag = LUN }` 的块：

- 陆军：`default_unit_production_super_heavies`、`default_unit_production_land_cruiser`、`default_paratroopers_production`、`default_major_SF_para`、`default_major_SF_marines`、`default_garrison_production`、`default_mountaineers_production`、`default_mobile_production`、`default_armored_production`、`highered_armored_production`。
- 陆空装备：`bba_air_prod_1`、`build_patrol_bombers`、`default_railway_gun_management`、`default_spyplanes_production`、`if_we_can_build_v1_rockets_we_want_rockets`、`if_we_can_build_v2_rockets_we_want_v2_rockets`、`if_we_can_build_sams_we_want_sams`、`if_we_can_build_nuclear_missiles_we_want_nuclear_missiles`。
- 海军：同名的 **两个** `default_role_ratios` 块、`ill_show_you_mine`、`ill_show_you_mine_2`、`dont_build_capitals_if_on_treaty`。不要用会吞掉重复键的字典处理两个比例块。

混合策略不能整块排除，当前拆分如下。新增块均排除 LUN，继承来源块原有 `enable`、`abort` 或 `abort_when_not_enabled`；载荷数值不变。

| 来源 | 移出的内容 | 新块 |
| --- | --- | --- |
| `default_unit_production` | 陆军 `role_ratio`：伞兵 0、山地 4、海军陆战队 0、装甲 2、步兵 80 | `Renko_default_unit_production_land_role_ratios` |
| 同上 | 空军 `unit_ratio`：战斗机 80、近支 10、战术轰炸机 10、战略轰炸机 5、海军轰炸机 10、重战 20；`equipment_production_factor`：重战 -40、战斗机 35、步兵 40、火炮 25 | `Renko_default_unit_production_land_air` |
| 同上 | 舰船 `unit_ratio`：主力舰 10、潜艇 10、屏卫舰 40 | `Renko_generic_default_unit_production_naval` |
| `default_surplus_management` | 陆军库存管理：步兵装备 10、支援装备 5、火炮 5、防空 3、反坦克 2 | `Renko_default_surplus_management_land_air` |
| `convoy_voy_voy_voy` | `role_ratio`：轻巡 -20、护航 25、布雷 -10；`unit_ratio`：屏卫 30、主力舰 -10 | `Renko_generic_convoy_voy_voy_voy_naval` |

**必须保留：** 原 `default_unit_production` 中运输船基础生产权重 15、最低 1 船坞；原 `convoy_voy_voy_voy` 中运输船生产权重 50 及航线威胁启停条件。原库存管理块未迁出的内容继续保留。其他国家得到的载荷总和与触发时机应与所用原版一致。

**联动：** `common/ai_strategy/Renko_LUN_strategy.txt`、`Renko_LUN_strategy.txt`、`Renko_LUN_strategy.txt`。升级新增通用策略时，先判断是否与月都专属策略重叠，再决定是否隔离，不能只机械查找旧块名。

## 02．已移除：学说附带的 AI 比例

`common/ai_strategy/doctrines.txt` 的 MOD 覆盖已于 2026-09-10 移除，恢复直接读取原版；不再维护 LUN 排除和陆军比例拆分。现有描述符未替换 `common/ai_strategy`，不需修改描述符。

当前指定的月都三军学说／子学说使用 `Renko_LUN_*` 独立 ID，不匹配原版相应学说条件；专属步兵、装甲和镇压模板也使用独立角色。原版两项骑兵比例 -100 的条件分别为“工厂超过 20 且日期晚于 1938.1.1”与“拥有摩托化步兵科技”，它们会恢复正常判定，但不直接修改月都独立角色权重。

若以后改用原版学说或通用招募角色，则接受原版策略的正常作用，再按实际问题评估。本次不新增替代隔离。月都专属学说、授予效果与军事策略均保留。以上为静态条件核对，未实机验证。

[02.patch](lun_override_patches/02.patch) 仅保留已撤销改动的历史证据，**不再应用**；当前生效附件为 01、03—09。

## 03．通用陆军模板

路径：`common/ai_templates/generic.txt`。本轮新复制原版，目录已受 `descriptor.mod` 的 `replace_path="common/ai_templates"` 替换。附件：[03.patch](lun_override_patches/03.patch)。

在以下 10 个模板的 `blocked_for` 增加 `LUN`：`armor_generic`、`garrison_generic`、`suppression_generic`、`infantry_generic`、`mountaineers_generic`、`marines_generic`、`paratrooper_generic`、`rangers_generic`、`landcruiser_generic`、`super_heavy_generic`。原排除名单保留；**`hq_generic` 不排除 LUN，内容保持原版。**

本文件不提供月都新编制；专属模板在 `common/ai_templates/Renko_LUN_templates.txt`。由于是整目录替换，删除本文件不会自动恢复原版通用模板；游戏更新增加其他模板文件时也不会自动加载，需维护者审查是否纳入。

## 04．通用海军设计

路径：`common/ai_equipment/generic_naval.txt`。本轮前已有同路径覆盖；本次只增加 10 处 `blocked_for` 的 `LUN`。附件：[04.patch](lun_override_patches/04.patch)。

受影响组：`destroyers`、`generic_escorts`、`naval_light_cruiser`、`naval_cruiser_heavy`、`naval_capital_battleship`、`naval_super_heavy_battleship`、`naval_capital_bc`、`naval_carrier`、`naval_carrier_light`、`naval_submarine`。

原 MOD 已重写设计、模块选择与优先级，与原版存在大量差异；这些不是月都新增。维护时先保留／迁移原 MOD 设计，再恢复各组 LUN 排除。月都设计由 `common/ai_equipment/Renko_LUN_designs.txt` 承接；不改通用组的模块或数值来加强月都。

## 05．通用坦克设计

路径：`common/ai_equipment/generic_tank.txt`。本轮前已有同路径覆盖；本次只为以下 17 组增加或扩充 `blocked_for = { LUN }`。附件：[05.patch](lun_override_patches/05.patch)。

`generic_light_tanks`、`generic_light_tank_artillery`、`generic_light_tank_destroyers`、`generic_light_tank_anti_air`、`generic_medium_tanks`、`generic_medium_tank_artillery`、`generic_medium_tank_anti_air`、`generic_medium_tank_destroyer`、`generic_medium_flame_tanks`、`generic_amphibious_tanks`、`generic_medium_amphibious_tanks`、`generic_modern_tanks`、`generic_modern_tank_destroyer`、`generic_modern_tank_artillery`、`generic_modern_tank_anti_air`、`generic_heavy_tanks`、`generic_heavy_tank_destroyer`。

原 MOD 设计与当前原版差异另行保留；月都模块、升级目标与允许模块列表在 `common/ai_equipment/Renko_LUN_designs.txt` 联动维护，不写入此通用文件。

## 06．通用飞机设计

路径：`common/ai_equipment/generic_planes.txt`。本轮新复制原版，同路径覆盖，无新增 `replace_path`。附件：[06.patch](lun_override_patches/06.patch)。

只为 11 个设计组的 `blocked_for` 增加 `LUN`，保留原国家名单和全部设计：`generic_fighter`、`generic_cas`、`generic_naval_bomber`、`generic_cv_fighter`、`generic_cv_cas`、`generic_cv_naval_bomber`、`generic_tactical_bomber`、`generic_heavy_fighter`、`generic_scout_plane`、`generic_strategic_bomber`、`generic_maritime_patrol`。

升级时以新原版为底，向仍有效的各组添加 LUN，不能拿空名单覆盖新版已有排除。专属设计由 `common/ai_equipment/Renko_LUN_designs.txt` 承接。

## 07．通用海军特遣队

路径：`common/ai_navy/taskforce/generic_taskforce_templates.txt`。本轮新复制原版，同路径覆盖，无新增 `replace_path`。附件：[07.patch](lun_override_patches/07.patch)。

在 8 个有效模板的 `allowed` 内原有 `NOT` 中增加 `original_tag = LUN`：`StrikeForce_1`、`PatrolReconForce_1`、`PatrolDominanceForce_CA_1`、`PatrolDominanceForce_BC_1`、`ConvoyRaiding_1`、`ConvoySurfaceRaiding_1`、`ConvoyEscort_1`、`MineLaying_1`。注释掉的模板不计入，原排除条件、任务和舰种比例不改。

月都实际编组由 `Renko_LUN_taskforce_templates.txt` 和上层 `common/ai_navy/fleet/Renko_LUN_fleet_templates.txt` 承接。它们依赖护航航母 role 3、正规航母 role 7、重巡 role 1；升级改动设计 role 时需同时核对这两层。

## 08．通用军工组织

路径：`common/military_industrial_organization/organizations/00_generic_organization.txt`。本轮前已有同路径覆盖。附件：[08.patch](lun_override_patches/08.patch)。

仅在以下 6 家公共机构的 `allowed` 增加 `NOT = { original_tag = LUN }`：`generic_tank_organization`、`generic_escort_ship_organization`、`generic_general_aircraft_organization`、`generic_artillery_organization`、`generic_infantry_equipment_organization`、`generic_motorized_mechanized_organization`。其他模板／机构不作全局 LUN 排除。

月都改用 `Renko_LUN_organization.txt` 中的月人制造。该通用文件已有幻想乡国家排除和旧版内容，与当前原版还存在 DLC 条件、特质及通用火车机构等差异；不能把全部差异解释为这六行修改。升级须分别审查原有幻想乡适配与上游新增内容，再加这六处排除。月都装备原型、研究类别和初始特质继续在独立组织文件维护。

## 09．军工 AI 加成权重

路径：`common/military_industrial_organization/ai_bonus_weights/ai_bonus_weights.txt`。本轮前已有同路径文件。附件：[09.patch](lun_override_patches/09.patch)。

只在 `default` 块、`carrier_size = 1` 附近增加 `submarine_carrier_size = 1`，让 AI 权重表能够评价潜母容量。它是**通用 AI 评价权重**，不是月都专属修正，也不是直接增加一架飞机；月人制造的容量奖励定义仍在其独立组织文件。

升级时确认新版是否已经定义同一键；已有时评估保留值，避免重复添加。除此以外，不因维护月都而改动其他权重。

## 同步关注的非原版文件

下面是 MOD 原有文件的月都隔离修改，本机原版没有对应同路径文件，不应误计为新增原版覆盖：

| 目录 | 每个文件的本次修改 |
| --- | --- |
| `common/ai_templates/` | `armour.txt`、`cavalry.txt`、`infantry.txt`、`infantry_artillery_focus.txt`、`irregulars.txt`、`marines.txt`、`mountaineers.txt` 各增加一处 LUN 排除，原模板保持。它们与第 03 节同受整目录替换。 |
| `common/ai_equipment/` | `KR_battleships.txt`、`KR_carriers.txt`、`KR_DD_screens.txt`、`KR_heavy_cruisers.txt`、`KR_light_cruisers.txt`、`KR_SH_battleships.txt`、`KR_submarines.txt` 各增加一处 LUN 排除。 |
| `common/ai_equipment/` | `planes_cas.txt`、`planes_cv_cas.txt`、`planes_cv_fighter.txt`、`planes_cv_naval_bomber.txt`、`planes_fighter.txt`、`planes_heavy_fighter.txt`、`planes_maritime_patrol_plane.txt`、`planes_naval_bomber.txt`、`planes_scout_plane.txt`、`planes_strategic_bomber.txt`、`planes_tactical_bomber.txt` 各增加一处 LUN 排除。 |

国策 `kyo-focus.txt`、`luner-capital.txt`，国家历史 `LUN - Lunarians.txt` 和精神 `difficulty.txt` 也是 MOD 自有路径，修改点见交接说明。`Renko_LUN_*` 新文件主要是独立新增定义；不能为了“覆盖生效”随意给其所在目录增加 `replace_path`。现有另外两条目录替换为 `common/bookmarks`、`gfx/loadingscreens`，属于部署配套，不是月都 AI 隔离措施。

## 游戏更新后的维护流程

1. 先在专用维护分支保留当前 MOD 文件与账本，记录新游戏版本。不要直接编辑游戏安装目录，也不要直接向 `main` 提交。
2. 对照账本记录的原版 SHA256 查找变动。哈希相同可跳过逐行重做；哈希不同不等于必须丢弃 MOD 文件。当前哈希是本次核对快照，不能冒充所有文件首次引入时的哈希。
3. 对 4 个本轮新复制文件，以新原版为底重放本指南修改。对 4 个既有覆盖文件，先合并原 MOD 与新原版差异，再重放月都增量；`2cae441` 的 MOD 版本可用于识别哪些改动早已存在。
4. 检查所有新增策略／模板的国家路由。尤其保留混合策略中的运输船与非陆军效果、两个同名 `default_role_ratios`、HQ 例外及原有其他国家排除。新增原版文件还需核对 `common/ai_templates` 的整目录替换影响。
5. 更新独立月都文件的关联设计、编制、定型旗标与补给调用；不要恢复旧 `create_ship amount` 或参数化数量替换。当前舰船使用固定次数逐艘创建，库存使用 `Renko_LUN_supply_amount` 后清理。
6. 静态核对结构、定义引用、差异和编码，确认同一效果没有在原块与拆分块重复保留。更新账本的版本、源哈希、核对日期与开发日志；问题仍标记“待检验”，实际加载和 AI 行为另据游戏结果判断。

本次在文档核对后按维护简化要求移除学说 AI 覆盖，未实机验证，未修复既有覆盖与最新原版之间的历史差异。
