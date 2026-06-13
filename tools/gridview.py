"""Overlay a labeled pixel grid on an image so we can read exact coordinates
for label-blanking and pin placement. Usage: python gridview.py <img> [step]"""
import sys
from PIL import Image, ImageDraw, ImageFont

def main():
    path = sys.argv[1]
    step = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    im = Image.open(path).convert("RGB")
    w, h = im.size
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except Exception:
        font = ImageFont.load_default()
    for x in range(0, w, step):
        d.line([(x, 0), (x, h)], fill=(0, 200, 255), width=1)
        d.text((x + 2, 2), str(x), fill=(0, 90, 255), font=font)
        d.text((x + 2, h - 18), str(x), fill=(0, 90, 255), font=font)
    for y in range(0, h, step):
        d.line([(0, y), (w, y)], fill=(0, 200, 255), width=1)
        d.text((2, y + 2), str(y), fill=(0, 90, 255), font=font)
        d.text((w - 40, y + 2), str(y), fill=(0, 90, 255), font=font)
    out = path.rsplit(".", 1)[0] + "_grid.png"
    im.save(out)
    print(f"{out}  size={w}x{h}")

main()
