# 幻想乡命名备用素材：群星自用整合

保存日期：2026-09-13。用途：供以后编写幻想乡 MOD 的命名内容时参考；尚未接入 HOI4 游戏配置。

来源：本机《群星》“自用整合4.5适配版”（版本1.7.0）的“东方幻想乡”名称表，ID 为 `selfint_touhou`，配套物种显示名为“幻想乡少女”。与本机“自用整合”版本1.6.4的名称表和名称本地化文件逐字节一致。

- 配置来源：`self_integration_4_5/common/name_lists/SELFINT_TOUHOU.txt`
- 文字来源：`self_integration_4_5/localisation/simp_chinese/name_lists/selfint_name_list_l_simp_chinese.yml`
- 配置 SHA256：`46D253C508B8F3A7BBE3BC411F6FEDACD502E6E7D7896F26B0932049D616F23D`
- 本地化 SHA256：`3C6B3DFA37516A94F125662EC20DB3F1502451C250D74FC7F68AC108425AD7E8`

以下保留原始来源标识符与名称，不改写为本项目标识符。源文件只提供简体中文语言头，部分舰名保留英文或日文。`$O$` 是来源中的群星编号占位符；将来用于 HOI4 时需另行转换语法。此次未收录舰队、舰船设计级别和人物命名。

## 陆军

名称／格式词条数：15。

### 原始配置节选

```text
	army_names = {
		generic = { sequential_name = selfint_touhou_army_generic_ORD }
		defense_army = { sequential_name = selfint_touhou_army_defense_ORD }
		assault_army = { sequential_name = selfint_touhou_army_assault_ORD }
		slave_army = { sequential_name = selfint_touhou_army_slave_ORD }
		clone_army = { sequential_name = selfint_touhou_army_clone_ORD }
		perfected_clone_army = { sequential_name = selfint_touhou_army_clone_ORD }
		undead_army = { sequential_name = selfint_touhou_army_undead_ORD }
		robotic_army = { sequential_name = selfint_touhou_army_robotic_ORD }
		robotic_defense_army = { sequential_name = selfint_touhou_army_robotic_defense_ORD }
		psionic_army = { sequential_name = selfint_touhou_army_psionic_ORD }
		xenomorph_army = { sequential_name = selfint_touhou_army_xenomorph_ORD }
		gene_warrior_army = { sequential_name = selfint_touhou_army_gene_ORD }
		occupation_army = { sequential_name = selfint_touhou_army_occupation_ORD }
		individual_machine_occupation_army = { sequential_name = selfint_touhou_army_occupation_ORD }
		robotic_occupation_army = { sequential_name = selfint_touhou_army_occupation_ORD }
		primitive_army = { sequential_name = selfint_touhou_army_primitive_ORD }
		industrial_army = { sequential_name = selfint_touhou_army_industrial_ORD }
		postatomic_army = { sequential_name = selfint_touhou_army_postatomic_ORD }
	}
```

### 名称原文

```yaml
 selfint_touhou_army_generic_ORD: "第$O$幻想乡部队"
 selfint_touhou_army_defense_ORD: "第$O$天狗守备队"
 selfint_touhou_army_assault_ORD: "第$O$妖怪进攻队"
 selfint_touhou_army_slave_ORD: "第$O$仆从部队"
 selfint_touhou_army_clone_ORD: "第$O$幻影部队"
 selfint_touhou_army_undead_ORD: "第$O$亡灵部队"
 selfint_touhou_army_robotic_ORD: "第$O$人偶部队"
 selfint_touhou_army_robotic_defense_ORD: "第$O$人偶铁卫"
 selfint_touhou_army_psionic_ORD: "第$O$幽明部队"
 selfint_touhou_army_xenomorph_ORD: "第$O$妖兽部队"
 selfint_touhou_army_gene_ORD: "第$O$原铸战团"
 selfint_touhou_army_occupation_ORD: "第$O$驻防部队"
 selfint_touhou_army_primitive_ORD: "第$O$原始妖怪部队"
 selfint_touhou_army_industrial_ORD: "第$O$工业妖怪部队"
 selfint_touhou_army_postatomic_ORD: "第$O$后原子妖怪部队"
```

## 殖民地／行星

名称／格式词条数：40。

### 原始配置节选

```text
	planet_names = {
		generic = {
			names = {
				selfint_touhou_planet_00 selfint_touhou_planet_01 selfint_touhou_planet_02 selfint_touhou_planet_03
				selfint_touhou_planet_04 selfint_touhou_planet_05 selfint_touhou_planet_06 selfint_touhou_planet_07
				selfint_touhou_planet_08 selfint_touhou_planet_09 selfint_touhou_planet_10 selfint_touhou_planet_11
				selfint_touhou_planet_12 selfint_touhou_planet_13 selfint_touhou_planet_14 selfint_touhou_planet_15
				selfint_touhou_planet_16 selfint_touhou_planet_17 selfint_touhou_planet_18 selfint_touhou_planet_19
				selfint_touhou_planet_20 selfint_touhou_planet_21 selfint_touhou_planet_22 selfint_touhou_planet_23
				selfint_touhou_planet_24 selfint_touhou_planet_25 selfint_touhou_planet_26 selfint_touhou_planet_27
				selfint_touhou_planet_28 selfint_touhou_planet_29 selfint_touhou_planet_30 selfint_touhou_planet_31
				selfint_touhou_planet_32 selfint_touhou_planet_33 selfint_touhou_planet_34 selfint_touhou_planet_35
				selfint_touhou_planet_36 selfint_touhou_planet_37 selfint_touhou_planet_38 selfint_touhou_planet_39
			}
		}
	}
```

### 名称原文

```yaml
 selfint_touhou_planet_00: "核反应堆核心"
 selfint_touhou_planet_01: "无缘冢"
 selfint_touhou_planet_02: "灼热地狱"
 selfint_touhou_planet_03: "魔界"
 selfint_touhou_planet_04: "魔法森林"
 selfint_touhou_planet_05: "香霖堂"
 selfint_touhou_planet_06: "间歇泉"
 selfint_touhou_planet_07: "永远亭"
 selfint_touhou_planet_08: "迷途竹林"
 selfint_touhou_planet_09: "妖怪的树海"
 selfint_touhou_planet_10: "废洋馆"
 selfint_touhou_planet_11: "旧都"
 selfint_touhou_planet_12: "莲台野"
 selfint_touhou_planet_13: "迷途之家"
 selfint_touhou_planet_14: "博丽神社"
 selfint_touhou_planet_15: "再思之道"
 selfint_touhou_planet_16: "幻梦界"
 selfint_touhou_planet_17: "灵魔殿"
 selfint_touhou_planet_18: "梦幻馆"
 selfint_touhou_planet_19: "鸟船遗迹"
 selfint_touhou_planet_20: "地灵殿"
 selfint_touhou_planet_21: "太阳花田"
 selfint_touhou_planet_22: "人间之里"
 selfint_touhou_planet_23: "天狗要塞"
 selfint_touhou_planet_24: "妖怪之山"
 selfint_touhou_planet_25: "红魔馆"
 selfint_touhou_planet_26: "辉针城"
 selfint_touhou_planet_27: "命莲寺"
 selfint_touhou_planet_28: "雾之湖"
 selfint_touhou_planet_29: "玄武之泽"
 selfint_touhou_planet_30: "九天瀑布"
 selfint_touhou_planet_31: "风神之湖"
 selfint_touhou_planet_32: "大蛤蟆之池"
 selfint_touhou_planet_33: "三途河"
 selfint_touhou_planet_34: "可能性空间移动船"
 selfint_touhou_planet_35: "白玉楼"
 selfint_touhou_planet_36: "冥界"
 selfint_touhou_planet_37: "彼岸"
 selfint_touhou_planet_38: "有顶天"
 selfint_touhou_planet_39: "月都"
```

## 舰船

名称／格式词条数：32。

### 原始配置节选

```text
	ship_names = {
		generic = {
			selfint_touhou_ship_00 selfint_touhou_ship_01 selfint_touhou_ship_02 selfint_touhou_ship_03
			selfint_touhou_ship_04 selfint_touhou_ship_05 selfint_touhou_ship_06 selfint_touhou_ship_07
			selfint_touhou_ship_08 selfint_touhou_ship_09 selfint_touhou_ship_10 selfint_touhou_ship_11
			selfint_touhou_ship_12 selfint_touhou_ship_13 selfint_touhou_ship_14 selfint_touhou_ship_15
			selfint_touhou_ship_16 selfint_touhou_ship_17 selfint_touhou_ship_18 selfint_touhou_ship_19
			selfint_touhou_ship_20 selfint_touhou_ship_21 selfint_touhou_ship_22 selfint_touhou_ship_23
			selfint_touhou_ship_24 selfint_touhou_ship_25 selfint_touhou_ship_26 selfint_touhou_ship_27
			selfint_touhou_ship_28 selfint_touhou_ship_29 selfint_touhou_ship_30 selfint_touhou_ship_31
		}
	}
```

### 名称原文

```yaml
 selfint_touhou_ship_00: "Magic Absorber（魔法吸收器）"
 selfint_touhou_ship_01: "QED「495年的波纹」"
 selfint_touhou_ship_02: "Unknown（未知）「原理不明的妖怪玉」"
 selfint_touhou_ship_03: "Unknown（未知）「姿态不明的空鱼」"
 selfint_touhou_ship_04: "Unknown（未知）「轨道不明的鬼火」"
 selfint_touhou_ship_05: "「20XX年 死后之旅」"
 selfint_touhou_ship_06: "「Super Scope 3D」"
 selfint_touhou_ship_07: "「アナーキーバレットヘル」"
 selfint_touhou_ship_08: "「一寸之壁」"
 selfint_touhou_ship_09: "「七个一寸法师」"
 selfint_touhou_ship_10: "「七个小人」"
 selfint_touhou_ship_11: "「三位一体论狂想曲」"
 selfint_touhou_ship_12: "「三月精」"
 selfint_touhou_ship_13: "「不可能弹幕结界」"
 selfint_touhou_ship_14: "「不合时令的蝶雨」"
 selfint_touhou_ship_15: "「不朽的弹幕」"
 selfint_touhou_ship_16: "「不死鸟重生」"
 selfint_touhou_ship_17: "「不死鸟附体」"
 selfint_touhou_ship_18: "「乌鸦的暗影」"
 selfint_touhou_ship_19: "「二大宗教九字护身法」"
 selfint_touhou_ship_20: "「五个季节」"
 selfint_touhou_ship_21: "「人类与妖怪的境界」"
 selfint_touhou_ship_22: "「人类真好啊」"
 selfint_touhou_ship_23: "「伪阿波罗」"
 selfint_touhou_ship_24: "「信仰之山」"
 selfint_touhou_ship_25: "「信仰之针」"
 selfint_touhou_ship_26: "「信仰心增加祈愿之仪」"
 selfint_touhou_ship_27: "「假面丧心舞 暗黑能乐」"
 selfint_touhou_ship_28: "「光学迷彩」"
 selfint_touhou_ship_29: "「全人类的绯想天」"
 selfint_touhou_ship_30: "「全妖怪的绯想天」"
 selfint_touhou_ship_31: "「八云之巢」"
```
