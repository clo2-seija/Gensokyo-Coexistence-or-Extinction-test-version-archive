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
- 关联记录：development_logs/2026-09-09_月都补给修复与海军生产.md。未实机验证。
