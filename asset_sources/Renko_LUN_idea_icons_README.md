# 月都难度民族精神徽章源稿

两枚徽章使用统一金属盾框，游戏只读取最终 PNG；后续修改从 SVG 源稿导出即可。

| 精神 | SVG 源稿（相对本目录） | 最终 PNG（相对 MOD 根目录） |
|---|---|---|
| 量子扰动 | Renko_LUN_quantum_disturbance/Renko_LUN_quantum_disturbance.svg | gfx/interface/ideas/Renko_LUN_quantum_disturbance.png |
| 永恒之月 | Renko_LUN_eternal_moon/Renko_LUN_eternal_moon.svg | gfx/interface/ideas/Renko_LUN_eternal_moon.png |

## 注册与导出

- 民族精神定义：common/ideas/Renko_LUN_ideas.txt。
- 图标注册：interface/Gensokyo_ideas.gfx 的「月都独立难度民族精神」分节。
- picture 分别为 Renko_LUN_quantum_disturbance、Renko_LUN_eternal_moon；注册名在其前面加 GFX_idea_。
- SVG：512×512、透明画布；最终游戏贴图：64×64 RGBA PNG。
- 使用 resvg_py.svg_to_bytes(svg_path=源文件路径, width=512, height=512) 渲染，再用 Pillow Image.Resampling.LANCZOS 缩至 64×64。
- 量子扰动使用原子轨道及紫色错位碎片；永恒之月使用银色弦月。
- 工作预览不放入 gfx；只保留被注册直接引用的最终 PNG。

两图已做视觉、尺寸、透明通道及注册引用检查；未实机验证。
