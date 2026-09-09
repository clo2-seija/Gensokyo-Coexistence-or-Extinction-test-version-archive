# 月人工艺 MIO 政策

- 新增月都专用政策 `Renko_LUN_lunarian_craftsmanship_policy`，显示名称“月人工艺”。
- 使用 MIO 的 `owner = { tag = LUN }` 限定所属国家；无额外规模或科技门槛，`cost = 0`。
- `equipment_bonus / same_as_mio`：可靠性 `0.20`、生产资源需求 `-0.20`，覆盖该 MIO 适用的装备。
- AI 采用权重 `100000`，提供极高倾向；不强制切换政策。
- 复用原版机械天才政策图标，补充中英本地化。现有本地化保留 UTF-8 BOM 与 CRLF；新增政策与日志使用 UTF-8 / LF。
- 静态检查政策范围、数值、权重、本地化与图标引用；尚未实机验证。

## 本批提交归档

本项随本批统一提交，范围、验证结论与交接状态见 [Renko_2026-09-09_LUN_batch_fleet_supply_and_industry.md](Renko_2026-09-09_LUN_batch_fleet_supply_and_industry.md)。此前“未提交”文字保留为过程记录；实机状态仍为待检验。
