#!/usr/bin/env python3
"""Generate the EL signature-mark proposals.

Second round. The first was ten thin-stroke line drawings and it was rejected
on sight, correctly - that is the visual language of an icon set, not of a
personal mark.

What the reference marks (Jumpman, Federer's RF, Kobe's sheath, CR7) actually
share, and what this round is built on:

  Solid mass, not outline.  Weight is presence. A 2.4px stroke has none.
  One fused figure.         The letters are a single shape, not two adjacent
                            glyphs. Federer's R and F share a spine and a cut.
  Contrast.                 Thick stems against thin arms. Uniform weight reads
                            as an icon; modulated weight reads as a mark.
  Subtractive.              The RF monogram removes lines rather than adding
                            them, and its counters do as much work as its
                            strokes.
  A signature move.         Jumpman is a silhouette of the thing the person is
                            known for. Here that is flight - hence the lean and
                            the swept terminals.

Every mark below is a closed filled path. None of them use `stroke`.

    python3 generate.py            # writes svg/
    python3 generate.py --check    # colour audit only
"""

import argparse
import os
import re

ACCENT = "#8b95f0"
GROUND = "#0d0e12"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")

LEAN = 9.0  # degrees of forward shear; the flight lean


# --- primitives -----------------------------------------------------------

def path(d, rule=None, colour="currentColor"):
    fr = f' fill-rule="{rule}"' if rule else ""
    return f'<path d="{d}" fill="{colour}"{fr}/>'


def leaned(body, deg=LEAN, cx=16, cy=16):
    """Shear about the centre so the mark leans forward without translating."""
    return (f'  <g transform="translate({cx} {cy}) skewX({-deg:g}) '
            f'translate({-cx} {-cy})">\n{body}\n  </g>')


def svg(body, label, size=32):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" '
            f'width="{size}" height="{size}" role="img" aria-label="{label}">\n'
            f'{body}\n</svg>\n')


def paint(body, colour=ACCENT):
    return body.replace("currentColor", colour)


def tile(body, colour=ACCENT):
    return (f'  <rect width="32" height="32" rx="6" fill="{GROUND}"/>\n'
            + paint(body, colour))


def ind(parts, n=4):
    return "\n".join(" " * n + s for s in parts)


# --- the solid EL ligature ------------------------------------------------
#
# One closed outline. Heavy stem, arms to the right, and - the fix that makes
# the L legible - a deliberately uneven rhythm: the gap above the foot is
# roughly twice the gap between the two upper arms, and the foot runs longest.
# The eye reads stem-plus-foot as L first, then picks up the upper arms as E.
# With even gaps it reads as an E with a wide base and the L disappears.

STEM_L, STEM_R = 6.0, 12.4
CUT = 2.3


def el_path(top_y=(5.5, 9.8), mid_y=(12.4, 16.4), bot_y=(21.5, 26.5),
            top=22.5, mid=19.5, bot=27.0, cut=CUT):
    t0, t1 = top_y; m0, m1 = mid_y; b0, b1 = bot_y
    return (f"M{STEM_L} {t0} H{top} L{top - cut:g} {t1} H{STEM_R} "
            f"V{m0} H{mid} L{mid - cut:g} {m1} H{STEM_R} "
            f"V{b0} H{bot} L{bot - cut:g} {b1} H{STEM_L} Z")


# --- concepts -------------------------------------------------------------
# Eight silhouettes, not one silhouette eight times. Squint and they should
# still be told apart.

def a_slipstream():
    """The base mark: one fused mass, leaning, terminals cut on the diagonal."""
    return ([path(el_path())],
            [path(el_path(top=22.0, mid=18.5, bot=26.0, cut=1.5))])


def b_corner():
    """Two masses: a heavy L angle, with a compact E set into its corner."""
    ell = "M4.5 4 H11 V21.2 H28 L25.4 27 H4.5 Z"
    e = ("M14.6 6 H25.5 L23.6 9.4 H18.6 V11.6 H23.5 L21.6 14.8 H18.6 "
         "V16.6 H25.5 L23.6 19.6 H14.6 Z")
    ellb = "M4.5 4 H11.4 V21.2 H28 L26.2 27 H4.5 Z"
    eb = ("M14.6 6 H25.5 L24.0 9.6 H19.0 V11.6 H23.5 L22.0 14.8 H19.0 "
          "V16.4 H25.5 L24.0 19.6 H14.6 Z")
    return [path(ell + " " + e)], [path(ellb + " " + eb)]


def c_contra():
    """Extreme contrast: a slab stem, arms pared to a third of its weight."""
    d = ("M5 4.5 H14 V27.5 H5 Z "
         "M14 4.5 H27 L25.2 7.6 H14 Z "
         "M14 14.4 H23 L21.2 17.5 H14 Z "
         "M14 24.4 H29 L27.2 27.5 H14 Z")
    db = ("M5 4.5 H14.4 V27.5 H5 Z "
          "M14.4 4.5 H26.6 L25.4 8.0 H14.4 Z "
          "M14.4 14.2 H22.6 L21.4 17.7 H14.4 Z "
          "M14.4 24.0 H28.6 L27.4 27.5 H14.4 Z")
    return [path(d)], [path(db)]


def d_stack():
    """E over L, offset - a staggered silhouette rather than a single column."""
    e = ("M5 3.5 H21.5 L19.6 7 H10 V9.2 H18.5 L16.6 12.5 H10 "
         "V14.8 H21.5 L19.6 18.2 H5 Z")
    ell = "M13 19.5 H18.5 V25 H29 L27.1 28.5 H13 Z"
    eb = ("M5 3.5 H21 L19.6 7.2 H10.4 V9.2 H18 L16.6 12.7 H10.4 "
          "V14.6 H21 L19.6 18.2 H5 Z")
    ellb = "M12.6 19.5 H18.6 V25 H29 L27.6 28.5 H12.6 Z"
    return [path(e + " " + ell)], [path(eb + " " + ellb)]


def e_vector():
    """The foot runs out into an arrowhead. The mark points where it is going."""
    base = el_path(bot=23.0)
    head = "M22.0 21.5 L29.5 24.0 L22.0 26.5 Z"
    baseb = el_path(bot=22.5, cut=1.5)
    headb = "M21.6 21.5 L29.0 24.0 L21.6 26.5 Z"
    return [path(base + " " + head)], [path(baseb + " " + headb)]


def f_wing():
    """Arms raked hard from root to tip. Squinted at, a swept wing, not a letter."""
    d = ("M6 4.5 H26.5 L18.6 9.6 H12.4 V12.6 H22.5 L16.4 16.6 H12.4 "
         "V20.6 H29 L20.5 27.5 H6 Z")
    db = ("M6 4.5 H25.5 L19.2 9.8 H12.4 V12.6 H21.5 L17.0 16.6 H12.4 "
          "V20.6 H28 L21.5 27.5 H6 Z")
    return [path(d)], [path(db)]


def g_shield():
    """EL held in a crest. The only enclosed mark in the set."""
    crest = "M3.5 3 H28.5 V18.5 L16 29.5 L3.5 18.5 Z"
    cut = el_path(top_y=(7.5, 10.4), mid_y=(12.2, 15.0), bot_y=(17.6, 20.5),
                  top=21.5, mid=19.0, bot=23.5, cut=1.6)
    cutb = el_path(top_y=(7.5, 10.6), mid_y=(12.4, 15.0), bot_y=(17.4, 20.5),
                   top=21.0, mid=18.6, bot=23.0, cut=1.1)
    return ([path(crest + " " + cut, rule="evenodd")],
            [path(crest + " " + cutb, rule="evenodd")])


def h_counter():
    """The letterform is the hole. Maximum contrast, and it holds up smallest."""
    block = "M2 2 H30 V30 H2 Z"
    cut = el_path(top_y=(6.5, 10.2), mid_y=(12.6, 16.0), bot_y=(20.4, 24.6),
                  top=21.0, mid=18.5, bot=24.5, cut=2.0)
    small = el_path(top_y=(6.5, 10.4), mid_y=(12.8, 16.0), bot_y=(20.2, 24.6),
                    top=20.5, mid=18.0, bot=24.0, cut=1.4)
    return ([path(block + " " + cut, rule="evenodd")],
            [path("M1.5 1.5 H30.5 V30.5 H1.5 Z " + small, rule="evenodd")])


CONCEPTS = [
    ("a-slipstream", "EL slipstream", a_slipstream,
     "One fused mass, leaning, terminals cut on the diagonal. The base mark."),
    ("b-corner", "EL corner", b_corner,
     "Two masses: a heavy L angle with a compact E set into its corner."),
    ("c-contra", "EL contra", c_contra,
     "A slab stem against arms pared to a third of its weight."),
    ("d-stack", "EL stack", d_stack,
     "E over L, offset - a staggered silhouette rather than one column."),
    ("e-vector", "EL vector", e_vector,
     "The foot runs out into an arrowhead. The mark points where it is going."),
    ("f-wing", "EL wing", f_wing,
     "Arms raked hard from root to tip. Squinted at, a swept wing."),
    ("g-shield", "EL crest", g_shield,
     "EL held in a crest - the only enclosed mark in the set."),
    ("h-counter", "EL counter", h_counter,
     "The letterform is the hole. Maximum contrast, holds up smallest."),
]


def build():
    os.makedirs(OUT, exist_ok=True)
    written = []
    for slug, label, fn, _ in CONCEPTS:
        primary, small = fn()
        files = {
            "a": svg(paint(leaned(ind(primary))), f"{label} - primary"),
            "b": svg(paint(leaned(ind(small))), f"{label} - small cut", size=20),
            "c": svg(tile(leaned(ind(small))), f"{label} - tile"),
            "d": svg(leaned(ind(primary)), f"{label} - mono"),
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
        if stray or "Gradient" in src or "url(#" in src:
            print(f"FAIL {os.path.basename(p)}: {stray or 'gradient'}")
            bad += 1
        if "stroke=" in src:
            print(f"FAIL {os.path.basename(p)}: uses stroke; these are solid forms")
            bad += 1
    print(f"{len(paths) - bad}/{len(paths)} clean")
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.parse_args()
    files = build()
    print(f"wrote {len(files)} files to {OUT}")
    check(files)
