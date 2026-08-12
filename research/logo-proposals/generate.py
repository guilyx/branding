#!/usr/bin/env python3
"""Generate the EL monogram proposals.

Round three. The first was thin fussy line icons; the second overcorrected into
heavy italic forms with diagonal speed-cuts, which reads as esports rather than
as a modern mark. Both were rejected, and both for the same underlying reason:
decoration standing in for structure.

This round is built on one rule instead - **everything lands on the grid**.

    UNIT   4       the module
    MARGIN 6       breathing room on every side; the mark never touches the box
    bar height == gap height == UNIT

That single equality does most of the work. An E of three bars and two gaps at
one module each is exactly five modules tall, so the rhythm is even by
construction rather than by eye, and the counters come out identical without
being tuned. It is the Bauhaus/Swiss construction, and it is why those marks
still look calm sixty years on.

What is deliberately absent, because it is what made the last two rounds look
rough: no italic lean, no diagonal terminals, no arrowheads, no dots, no seams,
no tapers. Every terminal is square or fully round, and the same one is used
throughout a given mark. If a mark needs a flourish to be interesting, it is
not finished.

    python3 generate.py            # writes svg/
    python3 generate.py --check    # audit only
"""

import argparse
import os
import re

ACCENT = "#8b95f0"
GROUND = "#0d0e12"

UNIT = 4.0
M = 6.0                       # margin: the mark lives inside 6..26
X0, X1 = M, 32.0 - M
Y0, Y1 = M, 32.0 - M

# The five horizontal bands of the E: bar, gap, bar, gap, bar.
BAND = [Y0 + i * UNIT for i in range(6)]   # 6, 10, 14, 18, 22, 26

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")


# --- primitives -----------------------------------------------------------

def r(x, y, w, h, rx=None, colour="currentColor"):
    a = f' rx="{rx:g}"' if rx else ""
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"'
            f'{a} fill="{colour}"/>')


def path(d, rule=None, colour="currentColor"):
    fr = f' fill-rule="{rule}"' if rule else ""
    return f'<path d="{d}" fill="{colour}"{fr}/>'


def svg(body, label, size=32):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" '
            f'width="{size}" height="{size}" role="img" aria-label="{label}">\n'
            f'{body}\n</svg>\n')


def paint(body, colour=ACCENT):
    return body.replace("currentColor", colour)


def tile(body, colour=ACCENT):
    return (f'  <rect width="32" height="32" rx="6" fill="{GROUND}"/>\n'
            + paint(body, colour))


def ind(parts, n=2):
    return "\n".join(" " * n + s for s in parts)


# The EL as an outline, for the marks that knock it out of a solid.
# Same grid: stem one module wide, bars one module tall, foot running longest.
EL_OUTLINE = (f"M{X0} {BAND[0]} H{X0 + 14} V{BAND[1]} H{X0 + UNIT} "
              f"V{BAND[2]} H{X0 + 12} V{BAND[3]} H{X0 + UNIT} "
              f"V{BAND[4]} H{X1} V{BAND[5]} H{X0} Z")


# --- concepts -------------------------------------------------------------

def a_module():
    """The reference construction. Bar height equals gap height equals one module."""
    a = [r(X0, BAND[0], 14, UNIT), r(X0, BAND[2], 12, UNIT),
         r(X0, BAND[4], X1 - X0, UNIT), r(X0, BAND[0], UNIT, Y1 - Y0)]
    return a, a


def b_round():
    """Same grid, fully round terminals. The radius is exactly half a module."""
    k = UNIT / 2
    a = [r(X0, BAND[0], 14, UNIT, k), r(X0, BAND[2], 12, UNIT, k),
         r(X0, BAND[4], X1 - X0, UNIT, k), r(X0, BAND[0], UNIT, Y1 - Y0, k)]
    return a, a


def c_detached():
    """Bars lifted clear of the stem by half a module. The join is implied."""
    g = UNIT / 2
    s = X0 + UNIT + g
    a = [r(X0, BAND[0], UNIT, Y1 - Y0),
         r(s, BAND[0], X1 - s, UNIT), r(s, BAND[2], X1 - s - 4, UNIT),
         r(s, BAND[4], X1 - s, UNIT)]
    b = [r(X0, BAND[0], UNIT, Y1 - Y0),
         r(s, BAND[0], X1 - s, UNIT), r(s, BAND[2], X1 - s - 3, UNIT),
         r(s, BAND[4], X1 - s, UNIT)]
    return a, b


def d_negative():
    """The mark is the void. A calm square, not a leaning slab."""
    block = "M3 3 H29 V29 H3 Z"
    inner = (f"M9 9 H23 V13 H13 V15 H21 V19 H13 V21 H23 V25 H9 Z")
    small = (f"M8.5 8.5 H23.5 V13 H12.5 V15 H21 V19.5 H12.5 V21 H23.5 V25.5 H8.5 Z")
    return ([path(block + " " + inner, rule="evenodd")],
            [path("M2.5 2.5 H29.5 V29.5 H2.5 Z " + small, rule="evenodd")])


def e_corner():
    """Two elements, one weight: an L angle, and an E of three bars beside it."""
    w = 3.0
    g = 2.0
    ex = 14.0
    a = [r(X0, Y0, w, Y1 - Y0), r(X0, Y1 - w, X1 - X0, w)]
    a += [r(ex, Y0 + i * (w + g), X1 - ex - (2 if i == 1 else 0), w)
          for i in range(3)]
    return a, a


def f_line():
    """Even geometric monoline. One weight, square joins, nothing added."""
    w = 3.0
    a = [r(X0, Y0, w, Y1 - Y0), r(X0, Y0, 13, w),
         r(X0, 16 - w / 2, 11, w), r(X0, Y1 - w, X1 - X0, w)]
    b = [r(X0, Y0, 3.6, Y1 - Y0), r(X0, Y0, 13, 3.6),
         r(X0, 16 - 1.8, 11, 3.6), r(X0, Y1 - 3.6, X1 - X0, 3.6)]
    return a, b


def g_apex():
    """E sits on top, the stem runs on past it and turns. Both letters, one figure."""
    w = 3.4
    bars = [Y0, Y0 + 6.3, Y0 + 12.6]
    a = [r(X0, Y0, w, Y1 - Y0)]
    a += [r(X0, y, 13, w) for y in bars]
    a += [r(X0, Y1 - w, X1 - X0, w)]
    return a, a


def h_tone():
    """The L at full strength, the E ghosted behind it.

    Hierarchy carried by tone rather than by shape, which is the one device
    the existing swarm mark already uses - its link path sits at 0.45 so the
    nodes read as the subject. Same grid as the rest, no extra geometry.
    """
    ghost = ' opacity="0.45"'
    ell = [r(X0, BAND[0], UNIT, Y1 - Y0), r(X0, BAND[4], X1 - X0, UNIT)]
    e = [r(X0, BAND[0], 14, UNIT).replace("/>", ghost + "/>"),
         r(X0, BAND[2], 12, UNIT).replace("/>", ghost + "/>")]
    return e + ell, e + ell


CONCEPTS = [
    ("a-module", "EL module", a_module,
     "The reference. Bar height equals gap height equals one module."),
    ("b-round", "EL round", b_round,
     "The same grid with fully round terminals - radius exactly half a module."),
    ("c-detached", "EL detached", c_detached,
     "Bars lifted clear of the stem by half a module. The join is implied."),
    ("d-negative", "EL negative", d_negative,
     "The mark is the void. A calm square rather than a leaning slab."),
    ("e-corner", "EL corner", e_corner,
     "Two elements at one weight: an L angle, and an E of three bars beside it."),
    ("f-line", "EL line", f_line,
     "Even geometric monoline. One weight, square joins, nothing added."),
    ("g-apex", "EL apex", g_apex,
     "E on top, the stem running past it and turning. Both letters, one figure."),
    ("h-tone", "EL tone", h_tone,
     "L at full strength, E ghosted behind it. Hierarchy by tone, not shape."),
]


def build():
    os.makedirs(OUT, exist_ok=True)
    written = []
    for slug, label, fn, _ in CONCEPTS:
        primary, small = fn()
        files = {
            "a": svg(paint(ind(primary)), f"{label} - primary"),
            "b": svg(paint(ind(small)), f"{label} - small cut", size=20),
            "c": svg(tile(ind(small)), f"{label} - tile"),
            "d": svg(ind(primary), f"{label} - mono"),
        }
        for suffix, content in files.items():
            p = os.path.join(OUT, f"{slug}-{suffix}.svg")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(content)
            written.append(p)
    return written


def check(paths):
    allowed = {ACCENT.lower(), GROUND.lower()}
    bad = 0
    for p in paths:
        src = open(p, encoding="utf-8").read()
        stray = {c for c in re.findall(r"#[0-9a-fA-F]{6}", src)
                 if c.lower() not in allowed}
        problems = []
        if stray:
            problems.append(f"off-brand colour {stray}")
        if "Gradient" in src or "url(#" in src:
            problems.append("gradient")
        if "stroke=" in src:
            problems.append("stroke; these are solid forms")
        if "skew" in src or "rotate(" in src:
            problems.append("sheared or rotated; this round is upright")
        if problems:
            print(f"FAIL {os.path.basename(p)}: {'; '.join(problems)}")
            bad += 1
    print(f"{len(paths) - bad}/{len(paths)} clean")
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.parse_args()
    files = build()
    print(f"wrote {len(files)} files to {OUT}")
    check(files)
