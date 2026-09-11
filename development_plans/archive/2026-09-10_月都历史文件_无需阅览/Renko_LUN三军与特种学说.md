> **历史文件，无需阅览。** 本文已于 2026-09-10 归档，仅留存开发过程，不作为当前实施计划、待办或维护要求。
> 当前内容请阅读[月都分支作者交接说明](../../../Reference/Renko_月都分支作者交接说明.md)及其中的维护指南。以下保留归档前正文，旧路径、数量与阶段结论可能过时。

# 月都三军与特种学说

日期：2026-09-09。状态：已实施，专项静态检查通过；新开局待检验。
分支：`codex/renko-strengthen-lunar-capital`。

## 已确认范围与来源

用户澄清为三军各四个、共十二个子学说，保留四轨结构；另有三个主学说与一个特种子学说“月之军势”。日本 MOD 常态效果按当前本机文件复制，不包含“风林火山”。

主学说取日本 1936 初始化：陆军 `grand_battleplan`，海军 `new_base_strike`，空军 `new_operational_integrity`。子学说取日本自身国别偏好；“雷击至上”源文件存在 `base = 0` 乘权重的设置，采用其日本专属偏好意图，月都副本使用有效的正基础权重。日本源文件不修改。

日本属国脚本只作授予语法参考：它使用贸易袭击、哨戒艇、装甲袭击舰，与日本自身学说不同；其陆军 `commandos` 与 `defensive_postures` 同属步兵轨道，且海军少了潜艇轨道，不能照抄为完整十三轨决议。

| 月都名称 | 日本来源标识 | 日本来源文件 |
| --- | --- | --- |
| 月人缜密战备 | `grand_battleplan` | `common/doctrines/grand_doctrines/land_grand_doctrines.txt` |
| 月人卓越单兵 | `commandos` | `common/doctrines/subdoctrines/land/infantry_subdoctrines.txt` |
| 月人空中骑兵 | `air_cavalry` | `common/doctrines/subdoctrines/land/combat_support_subdoctrines.txt` |
| 月人精简装甲 | `streamlined_deployment` | `common/doctrines/subdoctrines/land/armor_subdoctrines.txt` |
| 月人纵深渗透 | `infiltration_tactics` | `common/doctrines/subdoctrines/land/operations_subdoctrines.txt` |
| 月人航空制海 | `new_base_strike` | `common/doctrines/grand_doctrines/sea_grand_doctrines.txt` |
| 月人远洋潜航 | `long_range_submarines` | `common/doctrines/subdoctrines/sea/navy_submarine_doctrines.txt` |
| 月人雷击至上 | `torpedo_primacy` | `common/doctrines/subdoctrines/sea/navy_screen_doctrines.txt` |
| 月人航母集群 | `massed_carrier_fleet` | `common/doctrines/subdoctrines/sea/navy_carrier_doctrines.txt` |
| 月人主力防空 | `battleship_antiair_screen` | `common/doctrines/subdoctrines/sea/navy_capital_subdoctrines.txt` |
| 月人空域统合 | `new_operational_integrity` | `common/doctrines/grand_doctrines/air_grand_doctrines.txt` |
| 月人制空协同 | `air_subdoctrine_fighter_central_field` | `common/doctrines/subdoctrines/air/air_fighter_aircraft_subdoctrines.txt` |
| 月人航空雷击 | `air_subdoctrine_naval_torpedo_tactics` | `common/doctrines/subdoctrines/air/air_strike_aircraft_subdoctrines.txt` |
| 月人远程护航 | `air_subdoctrine_long_range_escort` | `common/doctrines/subdoctrines/air/air_medium_aircraft_subdoctrines.txt` |
| 月人空中堡垒 | `air_subdoctrine_flying_fortresses` | `common/doctrines/subdoctrines/air/air_heavy_aircraft_subdoctrines.txt` |

27 条来源（3 主学说、12 子学说、12 轨道）及源文件哈希见 `Renko_LUN_doctrine_sources.json`。

## 实现

- 独立 `Renko_LUN_` 主学说与十二条轨道，保留日本的激活效果、五阶段奖励、四轨里程碑、精通度来源与军种经验花费。轨道独立，因此不会在月都专属主学说下出现通用子学说。主学说与子学说只向 `original_tag = LUN` 显示；子学说可用条件绑定对应主学说。日本 DLC/特种项目选择门槛改为月都国别门槛，奖励本身没有降配。
- 里程碑计数器沿用游戏既有 `*_milestone_var` 接口，避免与原版机制断开；其余新增文件、定义和奖励标识使用 Renko 前缀。
- 空中骑兵的直升机科研加成、完成直升机项目、医院与团属支援效果均保留；常态学说并非仅复制名称。
- “确立月都三军学说”放在既有月战最高司令部，免费、即时、一次性，AI 权重 100。先选四个主学说（特种为原版“精英特种部队”），再显式选择三军各 0—3 轨与特种第 0 轨，最后向十三项指定子学说各发 1000 精通度。
- “月之军势”只允许第一特种轨道，防止同一套二合一效果重复安装。第二特种轨道保留原版规则与玩家选择，不重复塞入此学说，也不额外赠送未指定学说。
- 未新增日/月钩子、旧档迁移、原版覆盖或兵种解锁补发。当前新局 LUN 已有侵军科技与海军陆战队科技，满足决议及精英特种主学说基础条件。

## 月之军势：五阶段二合一

每阶段 120 精通度，总计 600；两套日本来源各五阶段、每阶段 60。启用时合并两套特种容量奖励：平额 200、比例 2。

1. 月面军械定式：日本两级两栖设计降本映射到侵军实际装备；步兵装备成本 -15%，中坦、中坦歼、中防空与重坦歼底盘成本各 -10%。侵军步兵突破 +5%，丘陵攻/防/移 +15/+5/+10%，山地 +25/+10/+15%。
2. 白衣穿林：侵军中坦突破 +15%；步兵主动性 +0.01，森林攻/防/移 +10/+10/+10%，丛林 +15/+10/+10%，城市 +5/+5/+5%。
3. 奉敕合围：陆军制空优势加成 +10%、岸轰加成 +15%、登陆准备速度 +20%；两个装甲营防御 +5%、补给消耗 -0.02。
4. 侵军战列：仅侵军步兵 `combat_width = -0.2`，与日本特种步兵写法一致；软攻 +10%、补给消耗 -0.02、速度 +10%、组织 +10、防御 +10%、突破 +5%、登陆攻/防/移各 +10%。两个装甲营组织各 +5。
5. 月都之威：特种进攻 +20%；两个装甲营组织再 +5、防御 +10%。

原日本两栖坦克突破映射到侵军中坦；两栖机械化的非地形协同映射到侵军中坦和中坦歼；其地形加成不转给装甲。两个团属支援连通过对应装备降本受益，不增加地形或大额组织奖励。装备降本影响该国使用相同装备的所有编制，并非仅限侵军；改用可撤回的直接 `equipment_bonus`，不移植日本永久隐藏精神。

## 兵种地形调整

侵军步兵基础不变。侵军中坦和中坦歼仅保留平原、沙漠攻击与移动各 +5%；移除原有其他地形及防御加成。其基础攻防、组织、人力、装备需求均不改。支援连继续无地形字段。资产 manifest 与既有单位检查输出同步。

这些是单位修正；不把营级修正直接当作整师面板结论。减宽保持来源代码值，实际单位面板和混编地形汇总需要新局核验。

## 验证与待检验

- `tools/Renko_validate_lunar_doctrines.py`：27 项来源效果对照、3/12/1 结构、12 独立轨道、13 无冲突选槽、精通度覆盖、国别门槛、单位/装备/图标引用、中文本地化与地形边界。
- `tools/Renko_validate_lunar_invasion.py`：既有五单位、十五图标、装备与两语单位本地化检查。
- 新学说简中与英文各 178 个键，包括全部奖励名称、描述与决议提示。
- 待检验：新局司令部决议出现并自动/手动领取；四个主学说、十三子学说正确选中且满级；里程碑激活；侵军步兵减宽、地形与装备降本；其他国家不可见；切换学说后可撤回奖励；特种第二轨道保持原版逻辑。
- `RuntimeChecks: NOT RUN`。未运行游戏，不将静态通过当作玩法验证。
