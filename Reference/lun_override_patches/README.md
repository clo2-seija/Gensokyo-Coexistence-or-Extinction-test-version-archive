# 月都原版覆盖差异附件

正文入口：[原版覆盖维护指南](../Renko_月都原版覆盖维护指南.md)。现行附件为 01、03—09，共 8 份；02 已退役，只保留移除历史，不再应用。

这些附件用于逐行审阅和维护，不是游戏加载文件，也不是可以直接部署的完整覆盖文件。

| 附件 | 对应文件 | 差异起点 |
| --- | --- | --- |
| `01.patch` | `common/ai_strategy/default.txt` | 本次核对的原版 |
| `02.patch`（已退役） | `common/ai_strategy/doctrines.txt`（覆盖已删除） | 历史原版快照，不再应用 |
| `03.patch` | `common/ai_templates/generic.txt` | 本次核对的原版 |
| `04.patch` | `common/ai_equipment/generic_naval.txt` | MOD 提交 `2cae441` |
| `05.patch` | `common/ai_equipment/generic_tank.txt` | MOD 提交 `2cae441` |
| `06.patch` | `common/ai_equipment/generic_planes.txt` | 本次核对的原版 |
| `07.patch` | `common/ai_navy/taskforce/generic_taskforce_templates.txt` | 本次核对的原版 |
| `08.patch` | `common/military_industrial_organization/organizations/00_generic_organization.txt` | MOD 提交 `2cae441` |
| `09.patch` | `common/military_industrial_organization/ai_bonus_weights/ai_bonus_weights.txt` | MOD 提交 `2cae441` |

历史终点均为 `aac2956` 的 MOD 文件；当前工作区已删除 02 对应覆盖，其余终点内容不变；源码内容在生成前统一按 UTF-8 解码、换行归一为 LF，并统一补齐文本末尾换行，因此附件用于比较内容，不用于还原源文件编码和换行。`manifest.json` 的 `files` 仅列现行 8 项，`removed_overrides` 保留退役 02；其中的 SHA256 则是原始文件字节的哈希，未做换行归一。

`vanilla_matches_git_head` 为 `false` 表示当前原版源文件未由该 HEAD 以完全相同字节保存（可能未收录或工作副本不同）；不表示已经发现游戏兼容性错误。历史首次引入的基线未完整追溯，不用本次快照冒充。

更新后重新生成附件时，应同步正文、账本和 manifest，明确新的起点、终点。不要将 `04`、`05`、`08`、`09` 的月都增量直接当作全部原版差异，否则会遗漏月都开发前就有的 MOD 改动。
