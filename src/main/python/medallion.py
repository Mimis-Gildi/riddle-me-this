#!/usr/bin/env python
"""
medallion — write The Hacker Tales channel medallion SVGs: Yggdrasil as a
wavy tryzub crown over three roots, Odin's eye at the fork. The watermark
variant drops the disk and ring and crops to the tree.

The eye white is a mask hole, not a fill: it shows whatever is behind the
picture (black in YouTube dark mode, white in light). One SVG per pupil colour.

USAGE:
    bin/medallion OUT_DIR
    rsvg-convert -w 800 -h 800 OUT_DIR/medallion-gold-on-teal-red.svg -o avatar.png

EXAMPLE:
    bin/medallion inbox && rsvg-convert -w 800 -h 800 inbox/medallion-gold-on-teal-red.svg -o inbox/hacker-tales-avatar.png
    rsvg-convert -w 800 -h 800 inbox/medallion-watermark-red.svg -o inbox/hacker-tales-watermark.png
"""
import math
import os
import sys

GOLD, TEAL = "#D9A93A", "#0D3A42"
PUPILS = [("red", "#D7263D"), ("pink", "#FF4FA3"), ("blue", "#2F6BFF")]


def bezier(p, t):
    u = 1 - t
    return tuple(u**3 * p[0][i] + 3 * u * u * t * p[1][i] + 3 * u * t * t * p[2][i] + t**3 * p[3][i] for i in (0, 1))


def normals(pts):
    out = []
    for i in range(len(pts)):
        ax, ay = pts[max(i - 1, 0)]
        bx, by = pts[min(i + 1, len(pts) - 1)]
        d = math.hypot(bx - ax, by - ay) or 1
        out.append((-(by - ay) / d, (bx - ax) / d))
    return out


def limb(p, w0, amp=0.0, waves=1.5, w1=3, n=96):
    """Outline ring of a cubic-bezier centreline, waved along its normal, tapering from w0 to w1."""
    base = [bezier(p, i / n) for i in range(n + 1)]
    pts = [(x + nx * amp * math.sin(2 * math.pi * waves * i / n) * (i / n) ** 0.7,
            y + ny * amp * math.sin(2 * math.pi * waves * i / n) * (i / n) ** 0.7)
           for i, ((x, y), (nx, ny)) in enumerate(zip(base, normals(base)))]
    left, right = [], []
    for i, ((x, y), (nx, ny)) in enumerate(zip(pts, normals(pts))):
        w = (w0 + (w1 - w0) * (i / n) ** 1.9) / 2
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    return left + right[::-1]


def path(ring):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in ring) + " Z"


def mirror(ring):
    return [(800 - x, y) for x, y in ring]


EYE_Y = 460
PRONG_SIDE = [(400, 420), (300, 440), (175, 380), (205, 150)]
PRONG_MID = [(400, 430), (400, 330), (400, 220), (400, 95)]
PRONG_INNER = [(392, 420), (350, 360), (300, 300), (305, 165)]
ROOT_SIDE = [(372, 495), (350, 575), (300, 630), (285, 715)]
ROOT_MID = [(400, 495), (400, 580), (400, 650), (400, 740)]


def svg(fg, bg, pupil, disk=True):
    side, inner = limb(PRONG_SIDE, 70, amp=20, waves=1.5), limb(PRONG_INNER, 58, amp=16, waves=1.5)
    root = limb(ROOT_SIDE, 56, amp=18, waves=1.25)
    limbs = [limb(PRONG_MID, 84, amp=18, waves=1.5), side, mirror(side), inner, mirror(inner),
             limb(ROOT_MID, 60, amp=16, waves=1.25), root, mirror(root)]
    paths = "\n".join(f'<path d="{path(r)}"/>' for r in limbs)
    view = "0 0 800 800" if disk else "60 80 680 680"
    ground = f'''<circle cx="400" cy="400" r="400" fill="{bg}"/>
<circle cx="400" cy="400" r="372" fill="none" stroke="{fg}" stroke-width="14"/>''' if disk else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" width="800" height="800">
<mask id="eye-white">
<rect width="800" height="800" fill="white"/>
<path d="M300,{EYE_Y} Q400,{EYE_Y - 78} 500,{EYE_Y} Q400,{EYE_Y + 78} 300,{EYE_Y} Z" fill="black"/>
</mask>
<g mask="url(#eye-white)">
{ground}
<g fill="{fg}">
{paths}
<path d="M270,{EYE_Y} Q400,{EYE_Y - 120} 530,{EYE_Y} Q400,{EYE_Y + 120} 270,{EYE_Y} Z"/>
</g>
</g>
<circle cx="400" cy="{EYE_Y}" r="32" fill="{fg}"/>
<circle cx="400" cy="{EYE_Y}" r="13" fill="{pupil}"/>
</svg>'''


def main(argv):
    if len(argv) != 1:
        raise SystemExit("usage: medallion OUT_DIR")
    for name, pupil in PUPILS:
        with open(os.path.join(argv[0], f"medallion-gold-on-teal-{name}.svg"), "w", encoding="utf-8") as f:
            f.write(svg(GOLD, TEAL, pupil))
    with open(os.path.join(argv[0], "medallion-watermark-red.svg"), "w", encoding="utf-8") as f:
        f.write(svg(GOLD, TEAL, PUPILS[0][1], disk=False))


if __name__ == "__main__":
    main(sys.argv[1:])
