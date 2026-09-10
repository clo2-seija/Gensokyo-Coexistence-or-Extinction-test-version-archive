> **历史文件，无需阅览。** 本文已于 2026-09-10 归档，仅留存开发过程，不作为当前实施计划、待办或维护要求。
> 当前内容请阅读[月都分支作者交接说明](../../../Reference/Renko_月都分支作者交接说明.md)及其中的维护指南。以下保留归档前正文，旧路径、数量与阶段结论可能过时。

# 月都军备局装备设计实现

日期：2026-09-09。用户已确认并授权实施。基线：新开局。

## 规则

- 陆军5类、海军7类、空军5类，共48个设计。装备名为英文，不带Renko前缀；内部标识保留Renko。
- 日期为保底，原日本科技/项目条件满足即可提前。基础型直接开放；1940年改良；1941年中坦、中歼、舰攻补强及空天母舰；1943年先进。
- 超重战列舰、潜水空母从1940年加入；喷火坦克只保留日本两代。
- 逐项复用日本 create_equipment_variant 的 type、modules、upgrades、parent_version、role_icon_index；名称与MIO适配月都，移除日本专属 name_group，国别跟踪改为本国持久flag。
- 对应日本特殊属国决议的底盘授予与项目解锁先于设计执行，保留 allow_without_tech = yes。模块科技不要求补齐。
- 独立陆海空AI设计文件只允许LUN。AI目标与实际设计一致，并以已定型flag启用，避免提前自行创建。通用AI设计逐组排除LUN。
- 本轮未改年度科技名单、研究槽、生产比例、舰队编组、周期钩子或其他国家设计内容。海军专用角色沿用日本七类并改为Renko_LUN前缀；舰队/生产策略是后续独立工作，不将静态设计路由当作舰队生产验证。

## 译名

MOD `localisation/English/country_gensokyo_l_english.yml` 中第183、186、193行等采用 Lunar Capital，形容词为 Lunarian。军备局使用 Lunar Capital Armaments Bureau。
外部交叉核对：东方LostWord官方英文网站 https://global.touhoulostword.com/2022/08/31/189851/ 使用 Lunar Capital Stasis Plan；这是该衍生游戏的官方英文用法，不宣称是ZUN原作统一官方英译。

## 设计排期

| 类别 | 英文设计名 | 保底时间 | 日本原设计 |
|---|---|---|---|
| medium_tank | Moonwarden Mk.36 | 落地即刻 | `JAP_cr_basic_medium_tank_jap_97` |
| medium_tank | Moonwarden Mk.40 | 1940-01-01 | `JAP_cr_improved_medium_tank_jap_type_3` |
| medium_tank | Moonwarden Mk.40A | 1941-01-01 | `JAP_cr_improved_medium_tank_jap_type_3_kai` |
| medium_tank | Moonwarden Mk.43 | 1943-01-01 | `JAP_cr_advanced_medium_tank_jap_type_5` |
| medium_td | Moonpiercer Mk.36 | 落地即刻 | `JAP_cr_basic_medium_td_jap_ho_ni_1` |
| medium_td | Moonpiercer Mk.40 | 1940-01-01 | `JAP_cr_improved_medium_td_jap_ho_ni_3` |
| medium_td | Moonpiercer Mk.40A | 1941-01-01 | `JAP_cr_advanced_medium_td_jap_ho_ni_3_kai` |
| medium_td | Moonpiercer Mk.43 | 1943-01-01 | `JAP_cr_advanced_medium_td_jap_na_to` |
| medium_aa | Skyveil Mk.36 | 落地即刻 | `JAP_cr_basic_medium_aa_jap_type_1_kai` |
| medium_aa | Skyveil Mk.40 | 1940-01-01 | `JAP_cr_improved_medium_aa_jap_type_2_kai` |
| medium_aa | Skyveil Mk.43 | 1943-01-01 | `JAP_cr_advanced_medium_aa_jap_type_3` |
| heavy_td | Heavenbreaker Mk.36 | 落地即刻 | `JAP_cr_basic_heavy_td_jap_type_3` |
| heavy_td | Heavenbreaker Mk.40 | 1940-01-01 | `JAP_cr_improved_heavy_td_jap_ho_ri` |
| heavy_td | Heavenbreaker Mk.43 | 1943-01-01 | `JAP_cr_advanced_heavy_td_jap_type_3` |
| medium_flame | Pureflame Mk.36 | 落地即刻 | `JAP_cr_basic_medium_flame_tank_jap_s_ki` |
| medium_flame | Pureflame Mk.40 | 1940-01-01 | `JAP_cr_improved_medium_flame_tank_jap_ka_ha` |
| escort_carrier | Moonhaven-class Mk.36 | 落地即刻 | `JAP_cr_cv_ryujo` |
| escort_carrier | Moonhaven-class Mk.40 | 1940-01-01 | `JAP_cr_cv_zuiho` |
| escort_carrier | Moonhaven-class Mk.43 | 1943-01-01 | `JAP_cr_cv_ryuho` |
| battleship | Celestial Throne-class Mk.36 | 落地即刻 | `JAP_cr_bb_nagato` |
| battleship | Celestial Throne-class Mk.40 | 1940-01-01 | `JAP_cr_bb_kaga` |
| battleship | Celestial Throne-class Mk.43 | 1943-01-01 | `JAP_cr_bb_musashi` |
| super_battleship | Eternal Palace-class Mk.40 | 1940-01-01 | `JAP_cr_bb_tsushima` |
| super_battleship | Eternal Palace-class Mk.43 | 1943-01-01 | `JAP_cr_bb_owari` |
| heavy_cruiser | Silver Edict-class Mk.36 | 落地即刻 | `JAP_cr_ca_aoba` |
| heavy_cruiser | Silver Edict-class Mk.40 | 1940-01-01 | `JAP_cr_ca_unzen` |
| heavy_cruiser | Silver Edict-class Mk.43 | 1943-01-01 | `JAP_cr_ca_azuma` |
| submarine | Moonshadow-class Mk.36 | 落地即刻 | `JAP_cr_ss_i19` |
| submarine | Moonshadow-class Mk.40 | 1940-01-01 | `JAP_cr_ss_i13` |
| submarine | Moonshadow-class Mk.43 | 1943-01-01 | `JAP_cr_ss_i16` |
| submarine_carrier | Hidden Heaven-class Mk.40 | 1940-01-01 | `JAP_cr_ss_i404` |
| fighter | Moonlance Mk.36 | 落地即刻 | `JAP_cr_fighter_ki27` |
| fighter | Moonlance Mk.40 | 1940-01-01 | `JAP_cr_fighter_ki43` |
| fighter | Moonlance Mk.43 | 1943-01-01 | `JAP_cr_fighter_ki84` |
| cas | Purifying Rain Mk.36 | 落地即刻 | `JAP_cr_cas_ki32` |
| cas | Purifying Rain Mk.40 | 1940-01-01 | `JAP_cr_cas_ki51` |
| cas | Purifying Rain Mk.43 | 1943-01-01 | `JAP_cr_cas_ki102` |
| cv_fighter | Silverwing Mk.36 | 落地即刻 | `JAP_cr_cv_fighter_a5m` |
| cv_fighter | Silverwing Mk.40 | 1940-01-01 | `JAP_cr_cv_fighter_a6m2` |
| cv_fighter | Silverwing Mk.43 | 1943-01-01 | `JAP_cr_cv_fighter_a7m2` |
| cv_attacker | Tidal Spear Mk.36 | 落地即刻 | `JAP_cr_cv_attacker_b5n` |
| cv_attacker | Tidal Spear Mk.40 | 1940-01-01 | `JAP_cr_cv_attacker_b6n` |
| cv_attacker | Tidal Spear Mk.40A | 1941-01-01 | `JAP_cr_cv_attacker_b6n_kai` |
| cv_attacker | Tidal Spear Mk.43 | 1943-01-01 | `JAP_cr_cv_attacker_b7a` |
| mothership | Palace of Eternity Mk.41 | 1941-01-01 | `JAP_cr_mothership` |

## 验证

静态验证结果见对应开发日志。尚未运行游戏；新开局决议显示、提前与到期领取、底盘可生产性、MIO实际附着和AI选择仍待检验。

## 原版AI覆盖来源

用户已批准复制 `common/ai_equipment/generic_planes.txt`，仅在原版11个通用飞机组的blocked_for加入LUN，保留其余结构。原版SHA-256：`87548f9512ada1c1674a315405076f18a098350d3898e90e1326476e596ded76`。这是AI设计路由文件，不是科研定义。

## 正规航母补充（2026-09-09）

天舟级Heavenly Ark-class：Mk.36复用赤城、Mk.40复用翔鹤、Mk.43复用信浓，保底为落地/1940/1943；配件原样保留，role_icon_index=7，月人制造。定型先授予对应舰体，AI专属组按定型旗标启用。未追加现代核动力航母。
