"""仅重建两种坦歼兵牌；依赖 resvg-py 和 Pillow。"""
from pathlib import Path
from io import BytesIO
import json
import resvg_py
from PIL import Image

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parents[1]

def atlas(frame):
    result = Image.new("RGBA", (frame.width * 2, frame.height))
    result.paste(frame, (0, 0))
    result.paste(frame, (frame.width, 0))
    return result

for entry in json.loads((SOURCE / "manifest.json").read_text(encoding="utf-8")):
    if "tankdestroyer" not in entry["key"]:
        continue
    layout = entry["export_layout"]
    hi = Image.open(BytesIO(resvg_py.svg_to_bytes(
        svg_path=str(SOURCE / entry["svg"]), width=608, height=336
    ))).convert("RGBA")
    large = hi.resize(tuple(layout["large_frame"]), Image.Resampling.LANCZOS)
    art = hi.crop(hi.getbbox())
    art.thumbnail(tuple(layout["small_art_max"]), Image.Resampling.LANCZOS)
    small = Image.new("RGBA", tuple(layout["small_frame"]))
    small.paste(art, ((small.width-art.width)//2, (small.height-art.height)//2))
    for slot, frame in [("large", large), ("map", small), ("text", small)]:
        atlas(frame).save(ROOT / entry["paths"][slot])
    print(entry["key"], "large", large.getbbox(), "small", small.getbbox())
