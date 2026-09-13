# 海军分支同步 main（2026-09-13）

- 目标分支：`codex/renko-gensokyo-naval-focus`，合并前 `f46c1b8`。
- 来源：本次 fetch 得到的 `origin/main`，`5f8c21d`，合入 7 个提交；本地 main 保持 `80299f8`。
- 内容：月都海军平衡及鱼雷减伤修正、河童工业决议修复、中英文本修订、正式版 1.1 描述符、致谢及发布资料。
- 无冲突合并；逐文件比较确认 25 个上游文件与 origin/main 一致，13 个海军分支独有文件保持不变，包括联合舰队、国策、初始化与设计编辑器。
- 本地 AGENTS.md、启动器名称与 remote_file_id 移除设置、预览图及工坊审计文件保留；本地 PSD 已与上游新增文件核对 SHA256 一致。
- Git 无未解决冲突；diff --check 有上游自带的换行/尾随空格警告，未额外格式化上游文件。
- 未运行游戏，新开局效果待检验。本轮只提交本地合并，不推送。

## 关键代码与文本

月都国家精神：`navy_capital_ship_attack_factor_against = -0.50`。
月都军工组织：`naval_speed = 0.10`、`surface_visibility = -0.05`、`lg_attack = 0.10`、`naval_torpedo_damage_reduction_factor = 0.10`，移除 `lg_armor_piercing = 0.10`。
河童工业决议改用 `fire_only_once = yes` 与 `is_owned_and_controlled_by = ROOT`，移除导致目标失效的 active flag 路径。

致谢本地化原文：
```yaml
 KR_welcome_splash_tab_4_content_9: "特别感谢 : KR团队 、 Fumo friday offical 、 FUMOISM 、此岸的白色旅人 还有任何游玩模组的人"
```

所有同步代码及中英本地化完整原文差异可通过 `git diff f46c1b8 HEAD -- common localisation` 审阅。
