# 原版覆盖追踪账本

## common/ai_strategy/default.txt

- 状态：现有覆盖继续使用，本轮扩展月都海军生产隔离。
- 原版源与 MOD 路径：common/ai_strategy/default.txt；同路径文件覆盖，无新增 replace_path。
- 本机原版基线：13b7ff9933f16ea2a3cb7c6cd8f0e0e07a8c4fbc；声明适配版本 1.19.2.0。
- 本次源文件 SHA256：AF298A10143013FB50E38DA23841E4480021E6BAA18A85D3CD7BC498A9A08668。
- 历史引入日期未追溯；保留既有陆空排除。本轮将 default_unit_production、convoy_voy_voy_voy 的非运输船载荷移至同条件、排除 LUN 的独立块；原运输船载荷及其启停保留。
- 两个 default_role_ratios、ill_show_you_mine、ill_show_you_mine_2、dont_build_capitals_if_on_treaty 排除 LUN。
- 原版海军设计及 taskforce 已有 LUN 排除，本轮未重复改动。其他国家专属海军策略的国家筛选不包含 LUN。
- 验证：本轮前后通用 ai_strategy 简单载荷逐项排序一致；这是保留其他国家效果的静态证据，不是游戏内行为验证。
- 关联记录：development_logs/archive/2026-09-10_月都历史文件_无需阅览/2026-09-09_月都补给修复与海军生产.md。未实机验证。

## 2026-09-10 月都分支完整登记

本节登记本轮涉及的 9 个原版同路径文件；后续移除 02，当前生效 8 项；上文保留 9 月 9 日海军隔离的历史记录。逐文件修改、适用范围和维护步骤统一见 [月都原版覆盖维护指南](Renko_月都原版覆盖维护指南.md)，功能见 [作者交接说明](Renko_月都分支作者交接说明.md)。

- MOD 核对提交：`aac29560d8050da42d7425a64e55775840a77255`；月都增量基线：`2cae4412b1850fcc054afe233c0c13c013675e1f`。
- 描述符声明适配 `1.19.2.0`；本机原版 Git HEAD 为 `13b7ff9933f16ea2a3cb7c6cd8f0e0e07a8c4fbc`。这是核对时的基线，不统一冒称首次引入基线。
- 下表 SHA256 来自 2026-09-10 的实际原版源文件。各文件首次引入时的游戏版本、源哈希与 Git 基线未完整追溯，标记为未追溯，不以当前值补造历史。
- 原版源路径与 MOD 目标路径均为表中相同相对路径。除 `common/ai_templates/generic.txt` 处于既有整目录替换范围外，其余为同路径文件覆盖，无本轮新增 `replace_path`。
- `lun_override_patches/manifest.json` 记录每份补丁的起点哈希、MOD 终点哈希、当前原版哈希及是否与原版 Git HEAD 文件一致。原版 Git 未收录／与工作副本不同的条目不能仅靠提交号复原，维护时以哈希识别源文件。
- 核对状态：新增复制文件与当前原版差异、既有覆盖文件与 MOD 增量基线差异已逐项检查；既有覆盖的历史原版差异尚未迁移。未实机验证。

| 编号 | 原版源／MOD 目标 | 本次改动及覆盖历史 | 当前原版 SHA256 |
| --- | --- | --- | --- |
| [01](lun_override_patches/01.patch) | `common/ai_strategy/default.txt` | 本轮新增；拆分陆空、舰船载荷并隔离 LUN，保留运输船。 | `AF298A10143013FB50E38DA23841E4480021E6BAA18A85D3CD7BC498A9A08668` |
| [03](lun_override_patches/03.patch) | `common/ai_templates/generic.txt` | 本轮新增；10 模板排除 LUN，HQ 保留；沿用 common/ai_templates 整目录替换。 | `BB40BE1918B9A8E595593B98816E384BEAEB58843B8784D468FB2DAE8E606253` |
| [04](lun_override_patches/04.patch) | `common/ai_equipment/generic_naval.txt` | 既有覆盖；10 设计组增加 LUN 排除，原 MOD 设计不改。 | `690B7DDF73BCD604440C668301D8DBD84A511E1362E65749982FB47669456B35` |
| [05](lun_override_patches/05.patch) | `common/ai_equipment/generic_tank.txt` | 既有覆盖；17 设计组增加 LUN 排除，原 MOD 设计不改。 | `8042B41A7D08009B4F429E320886675056FE9722FA813ED5006FF7A8CFB10646` |
| [06](lun_override_patches/06.patch) | `common/ai_equipment/generic_planes.txt` | 本轮新增；11 设计组增加 LUN 排除。 | `87548F9512ADA1C1674A315405076F18A098350D3898E90E1326476E596DED76` |
| [07](lun_override_patches/07.patch) | `common/ai_navy/taskforce/generic_taskforce_templates.txt` | 本轮新增；8 有效特遣队模板增加 LUN 排除。 | `8B1B9553FD29F325FCB1D4AE79157140126B62B7E3C2749B5F69FAAD61309821` |
| [08](lun_override_patches/08.patch) | `common/military_industrial_organization/organizations/00_generic_organization.txt` | 既有覆盖；6 公共 MIO 增加 LUN 排除。 | `8AB828D60A35316DFE49FB038133B1ECB2ABBF5F1F85858F1040A2258C8EC743` |
| [09](lun_override_patches/09.patch) | `common/military_industrial_organization/ai_bonus_weights/ai_bonus_weights.txt` | 既有文件；default 增加 submarine_carrier_size = 1，通用评价权重。 | `CECBD2693AD8223589FB6464003F96D8F82CFB4D2F06A57ED40FCFC60A263A2A` |

### 对应实现日志（历史文件，无需阅览）

以下记录均已归入 `development_logs/archive/2026-09-10_月都历史文件_无需阅览/`，仅用于追溯；日常维护阅读现行指南即可。省略目录的文件名也位于该归档目录。

- 01—03：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/Renko_2026-09-09_LUN军事AI编制比例.md`、`Renko_2026-09-09_LUN三编制与首批军势.md`；01 另见 `Renko_2026-09-09_LUN陆空轻量生产.md`、`2026-09-09_月都补给修复与海军生产.md`。
- 04—06：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/Renko_2026-09-09_LUN军备局装备设计.md`。
- 07：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/Renko_2026-09-09_LUN海军编组.md`。
- 08—09：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/Renko_2026-09-09_月人制造.md`。
- 本次文档核对：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/2026-09-10_月都作者交接资料整理.md`。

## 2026-09-10 移除学说 AI 覆盖

- 状态：已移除 `common/ai_strategy/doctrines.txt` 的 MOD 文件，直接沿用原版；不再重放原 7 处排除及 1 处陆军比例拆分。
- 原因：当前月都指定学说与招募角色使用独立 ID，取消低收益维护；原版骑兵减产策略恢复正常判定，不直接改写月都专属角色。未来改回原版学说／角色时接受原版策略。
- 覆盖方式：撤销同路径文件覆盖；描述符无 common/ai_strategy 目录替换，无须新增或移除 replace_path。
- 当前维护量：4 个本轮复制文件＋4 个既有覆盖，共 8 项。原 02.patch 及哈希迁入退役记录，仅供追溯，不用于当前部署。
- 关联日志：`development_logs/archive/2026-09-10_月都历史文件_无需阅览/2026-09-10_月都学说AI覆盖移除.md`。静态核对通过，未实机验证。

| 历史编号 | 已移除路径 | 历史修改 | 移除前核对的原版 SHA256 |
| --- | --- | --- | --- |
| [02](lun_override_patches/02.patch) | `common/ai_strategy/doctrines.txt` | 已移除；历史曾隔离 8 组陆军比例，其中 1 组只拆陆军效果。 | `92D00604DC51B3F9A303C0F2BBBD46BA8F939B3AD848DD0DAAF9F6EC348E6E41` |
