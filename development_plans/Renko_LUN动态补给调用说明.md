# 月都动态装备与部队补给

日期：2026-09-09；新开局基线。已授权实施。

## 唯一公开调用

```hoi4
Renko_LUN_grant_dynamic_equipment = yes
```

用于事件、国策、决议等效果块；内部固定转入LUN，不将装备发给调用者。LUN不存在或首都不受其控制时整包不执行。无AI/工业/难度门槛，无自动周期、永久领取标记或倍率。

每次在首都创建4个现有月都步兵师和4个现有月都装甲师；满装备参数1.0，经验参数沿用日本N档的步兵0.30、装甲0.40。缺少这两份编制定义时调用现有编制创建效果；不解锁科技、不创建设计，不反向调用整编月之军势效果。

额外陆军库存按仓库现有编制的need逐项求和，与本轮新建8师的基准编制需求为1:1；不把额外库存当作扣除新建部队装备后的净值。是否实际扣库存、实际代际和完整配装须游戏内验证。玩家改编编制或后续改动单位need时需重算表，不是运行时读取玩家编制。

动态科技选择/已定型旗标→脚本本地化数字后缀→meta_effect拼接型号→add_equipment_to_stockpile。无variant_name，按用户要求沿用日本底盘代数方式。同底盘最终选取最新设计属于待实测行为，不作为静态结论。

普通装备以真正解锁型号的科技为准；装甲及飞机按军备局定型标记选代，不按日历提前刷先进型号。未解锁/未定型的装备跳过，不送未来科技。支援装备/卡车检查科技，装甲支援车/直升机检查对应特殊项目。全部类型已就绪时达到下表完整1:1额外补给。

## 陆军后续库存

| 装备原型 | 4步兵 | 4装甲 | 合计 |
|---|---:|---:|---:|
| infantry_equipment | 5560 | 6200 | 11760 |
| support_equipment | 140 | 320 | 460 |
| artillery_equipment | 96 | 24 | 120 |
| medium_tank_chassis | 0 | 1120 | 1120 |
| medium_tank_destroyer_chassis | 0 | 480 | 480 |
| medium_tank_aa_chassis | 0 | 72 | 72 |
| heavy_tank_destroyer_chassis | 0 | 40 | 40 |
| armored_support_vehicle | 0 | 120 | 120 |
| medium_tank_flame_chassis | 0 | 60 | 60 |
| helicopter_equipment | 0 | 180 | 180 |
| motorized_equipment | 0 | 100 | 100 |

## 空军

战斗机250、CAS100、舰载战斗机100、舰载攻击机100、空天母舰60；只发已有定型机种。本轮1:1要求用于陆军后续库存，空军沿用已确认单包。

## 维护来源

- 编制：common/scripted_effects/Renko_LUN_templates_scripted_effects.txt
- 单位need：当前MOD覆盖与本机原版common/units合并读取。
- 模式参考：日本JAP_equipment_scripted_loc.txt、JAP_equipment_scripted_effects.txt、JAP_templates_scripted_effects.txt的N档。

## 2026-09-09 数量传递修正（待检验）

移除共享装备helper中的参数宏及调用块参数；调用方先设置原生Renko_LUN_supply_amount变量，以yes调用，库存命令读取LUN.Renko_LUN_supply_amount，helper结束后清理。飞机与共享陆军库存调用同步修正，原有数量、定型/科技条件、代际及部队创建逻辑保持不变。未实机验证。

## 2026-09-09 停止抵抗奖励入口（已实现，待检验）

新增common/on_actions/Renko_LUN_capitulation_supply_on_actions.txt。在on_capitulation中以FROM = { tag = LUN }确认引擎认定的胜利国为月都，随后转入LUN，调用一次Renko_LUN_grant_dynamic_equipment。不要求和谈结束；不以仅参战或阵营关系替代胜利国判定。每次符合条件的停止抵抗均可调用，无冷却或一次性旗标。

奖励沿用既有完整陆空补给包，包括4步兵师、4装甲师及陆空库存；既有首都控制条件与科技/设计跳过规则不变。不调用海军补给。未实机验证。
