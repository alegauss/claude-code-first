"""Draw the site's social card, a 1200 x 630 PNG of the mark and the title (CCF76).

Standard library only, as the rest of the build: every shape is a signed distance, so
the edges are smoothed without a rasterizer, and the title is drawn in a stroke alphabet
of capsules and arcs, which covers the letters of "Claude Code First" and refuses any
other. The mark is guide/icon.svg's drawing, in its own 160-unit coordinates.

    python scripts/og_card.py [--out og.png]
"""

from __future__ import annotations

import argparse
import math
import struct
import sys
import zlib
from pathlib import Path

WIDTH, HEIGHT = 1200, 630
GROUND = (23, 20, 28)
INK = (245, 238, 241)
ROSE = (232, 121, 154)  # #E8799A, the hub's bright accent
SEAL = (214, 84, 120)  # #D65478
WHITE = (255, 255, 255)
TITLE = "Claude Code First"


# ---------- distances, in pixels ----------

def capsule(a, b, r):
    (ax, ay), (bx, by) = a, b
    dx, dy = bx - ax, by - ay
    length = dx * dx + dy * dy or 1e-9

    def d(x, y):
        t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / length))
        return math.hypot(x - ax - t * dx, y - ay - t * dy) - r
    return d, (min(ax, bx) - r, min(ay, by) - r, max(ax, bx) + r, max(ay, by) + r)


def arc(c, radius, start, end, r):
    """A stroke along a circle from `start` to `end` degrees, counter-clockwise, y up."""
    cx, cy = c
    span = (end - start) % 360 or 360
    ends = [(cx + radius * math.cos(math.radians(a)), cy - radius * math.sin(math.radians(a))) for a in (start, end)]

    def d(x, y):
        angle = (math.degrees(math.atan2(cy - y, x - cx)) - start) % 360
        if angle <= span:
            return abs(math.hypot(x - cx, y - cy) - radius) - r
        return min(math.hypot(x - ex, y - ey) for ex, ey in ends) - r
    reach = radius + r
    return d, (cx - reach, cy - reach, cx + reach, cy + reach)


def disc(c, radius):
    cx, cy = c
    return (lambda x, y: math.hypot(x - cx, y - cy) - radius), (cx - radius, cy - radius, cx + radius, cy + radius)


def box_frame(x0, y0, x1, y1, corner, r):
    """The outline of a rounded rectangle, stroked `r` either side of its edge."""
    cx, cy, hx, hy = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 - corner, (y1 - y0) / 2 - corner

    def d(x, y):
        qx, qy = abs(x - cx) - hx, abs(y - cy) - hy
        inside = math.hypot(max(qx, 0.0), max(qy, 0.0)) + min(max(qx, qy), 0.0) - corner
        return abs(inside) - r
    return d, (x0 - r, y0 - r, x1 + r, y1 + r)


# ---------- the stroke alphabet ----------
# Units of the x-height, baseline at 0 and y down; W is the half-width of every stroke.
W = 0.11
X, CAP = 1.0, 1.42
R = 0.5 - W


def bowl():
    return [("arc", (0.5, -0.5), R, 0, 360)]


GLYPHS = {
    "C": (1.2, [("arc", (0.71, -0.71), 0.71 - W, 48, 312)]),
    "F": (0.86, [("line", (W, -CAP + W), (W, -W)), ("line", (W, -CAP + W), (0.8, -CAP + W)),
                 ("line", (W, -0.76), (0.68, -0.76))]),
    "a": (1.0, bowl() + [("line", (0.5 + R, -X + W), (0.5 + R, -W))]),
    "d": (1.0, bowl() + [("line", (0.5 + R, -CAP + W), (0.5 + R, -W))]),
    "e": (1.0, [("arc", (0.5, -0.5), R, 0, 318), ("line", (0.5 - R, -0.5), (0.5 + R, -0.5))]),
    "i": (2 * W, [("line", (W, -X + W), (W, -W)), ("dot", (W, -1.3), W * 1.15)]),
    "l": (2 * W, [("line", (W, -CAP + W), (W, -W))]),
    "o": (1.0, bowl()),
    "r": (0.66, [("line", (W, -X + W), (W, -W)), ("arc", (0.5, -0.5), R, 62, 180)]),
    "s": (0.8, [("arc", (0.4, -0.735), 0.265 - W, 30, 225), ("arc", (0.4, -0.265), 0.265 - W, 210, 45),
                ("line", (0.4 - 0.11, -0.625), (0.4 + 0.11, -0.375))]),
    "t": (0.62, [("line", (0.28, -1.3), (0.28, -W)), ("line", (W, -X + W), (0.6, -X + W))]),
    "u": (1.0, [("line", (0.5 - R, -X + W), (0.5 - R, -0.5)), ("arc", (0.5, -0.5), R, 180, 360),
                ("line", (0.5 + R, -X + W), (0.5 + R, -W))]),
    " ": (0.42, []),
}
TRACK = 0.16


def text_width(text: str) -> float:
    return sum(GLYPHS[c][0] for c in text) + TRACK * (len(text) - 1)


def text_shapes(text: str, left: float, baseline: float, size: float) -> list:
    """The title's strokes in pixels, `size` being the x-height."""
    missing = sorted(set(text) - set(GLYPHS))
    if missing:
        raise ValueError(f"the card's alphabet has no glyph for {''.join(missing)!r}")
    shapes, pen = [], left
    for char in text:
        advance, strokes = GLYPHS[char]
        at = lambda p: (pen + p[0] * size, baseline + p[1] * size)  # noqa: E731
        for kind, *args in strokes:
            if kind == "line":
                shapes.append(capsule(at(args[0]), at(args[1]), W * size))
            elif kind == "arc":
                shapes.append(arc(at(args[0]), args[1] * size, args[2], args[3], W * size))
            else:
                shapes.append(disc(at(args[0]), args[1] * size))
        pen += (advance + TRACK) * size
    return shapes


def mark_shapes(left: float, top: float, size: float) -> list:
    """guide/icon.svg, drawn in a `size` pixel square."""
    k = size / 160
    p = lambda x, y: (left + x * k, top + y * k)  # noqa: E731
    return [
        (box_frame(*p(30, 20), *p(114, 132), 14 * k, 5.5 * k), ROSE),
        (capsule(p(53, 51), p(91, 51), 5 * k), ROSE),
        (capsule(p(53, 73), p(77, 73), 5 * k), ROSE),
        (disc(p(112, 112), 30 * k), SEAL),
        (capsule(p(98, 112), p(108, 122), 5 * k), WHITE),
        (capsule(p(108, 122), p(126, 103), 5 * k), WHITE),
    ]


# ---------- the card ----------

def render(title: str = TITLE) -> bytearray:
    pixels = bytearray(bytes(GROUND) * (WIDTH * HEIGHT))
    size = 46.0
    mark = 300
    ink = (24.5 / 160 * mark, 142 / 160 * mark)  # where the mark's drawing starts and ends in its square
    gap = 44
    left = (WIDTH - (ink[1] - ink[0]) - gap - text_width(title) * size) / 2 - ink[0]
    layers = mark_shapes(left, (HEIGHT - mark) / 2, mark)
    baseline = HEIGHT / 2 + size * (CAP / 2)
    layers += [(shape, INK) for shape in text_shapes(title, left + ink[1] + gap, baseline, size)]
    for (distance, (x0, y0, x1, y1)), colour in layers:
        for y in range(max(0, int(y0) - 1), min(HEIGHT, int(y1) + 2)):
            row = y * WIDTH
            for x in range(max(0, int(x0) - 1), min(WIDTH, int(x1) + 2)):
                cover = 0.5 - distance(x + 0.5, y + 0.5)
                if cover <= 0:
                    continue
                cover = min(cover, 1.0)
                i = (row + x) * 3
                for ch in range(3):
                    pixels[i + ch] = round(pixels[i + ch] + (colour[ch] - pixels[i + ch]) * cover)
    return pixels


def png(pixels: bytes, width: int = WIDTH, height: int = HEIGHT) -> bytes:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    stride = width * 3
    raw = b"".join(b"\x00" + bytes(pixels[y * stride:(y + 1) * stride]) for y in range(height))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


def write(path: Path, title: str = TITLE) -> None:
    path.write_bytes(png(render(title)))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", default="og.png")
    args = parser.parse_args(argv)
    write(Path(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
