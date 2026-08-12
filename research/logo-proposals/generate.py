#!/usr/bin/env python3
"""Generate the initials-based logo proposals.

Ten concepts, three variations each, all on the same 32x32 grid and the same
Ink & Iris accent, so the comparison is between ideas rather than between
execution quality.

    python3 generate.py            # writes svg/ next to this file
    python3 generate.py --check    # colour audit only

Variations, for every concept:
    -a  primary, accent on transparent, full detail
    -b  small-size cut: fewer elements, heavier stroke, tuned for 20px
    -c  favicon tile, ground plus mark

The -b cut is the one that matters. brand/logo.md records that the previous
monogram was dropped because it did not survive being small, so every proposal
here has to answer that objection before anything else about it is worth
discussing.
"""

import argparse
import os
import re

ACCENT = "#8b95f0"
GROUND = "#0d0e12"
W = 2.4          # primary stroke
WB = 3.0         # small-cut stroke
R = 2.0          # node radius

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")


# --- primitives -----------------------------------------------------------

def p(d, w=W, colour="currentColor", cap="round", opacity=None):
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{w}" '
            f'stroke-linecap="{cap}" stroke-linejoin="round"{o}/>')


def dot(x, y, r=R, colour="currentColor"):
    return f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{colour}"/>'


def ring(x, y, r, w=1.6, colour="currentColor"):
    return (f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="none" '
            f'stroke="{colour}" stroke-width="{w}"/>')


def rect(x, y, s, rx=0.7, colour="currentColor"):
    return (f'<rect x="{x:g}" y="{y:g}" width="{s:g}" height="{s:g}" '
            f'rx="{rx:g}" fill="{colour}"/>')


def svg(body, label, size=32, view=32):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view} {view}" '
            f'width="{size}" height="{size}" role="img" aria-label="{label}">\n'
            f'{body}\n</svg>\n')


def paint(body, colour=ACCENT):
    """Resolve currentColor to a literal so the file renders standalone.

    Substitution rather than a wrapping <g stroke=...>: an element-level
    stroke="currentColor" beats a group attribute, and currentColor inside an
    <img> resolves against the SVG's own default - black - not the host page.
    Wrapping looks like it works right up until the file is used the normal way.
    """
    return body.replace("currentColor", colour)


def tile(body, colour=ACCENT):
    return (f'  <rect width="32" height="32" rx="6" fill="{GROUND}"/>\n'
            + paint(body, colour))


def ind(parts, n=4):
    pad = " " * n
    return "\n".join(pad + s for s in parts)


# --- the EL ligature, shared by most concepts -----------------------------
#
# E and L share the spine. The bottom bar runs longer than the top, which is
# what makes the same figure read as both letters instead of just an E.

SPINE_X, TOP_Y, MID_Y, BOT_Y = 11, 7, 16, 25
BAR_TOP, BAR_MID, BAR_BOT = 21, 18, 25

LIGATURE = f"M{BAR_TOP} {TOP_Y} H{SPINE_X} V{BOT_Y} H{BAR_BOT} M{SPINE_X} {MID_Y} H{BAR_MID}"


# --- concepts -------------------------------------------------------------
# Each returns (primary_parts, small_parts). Both are lists of SVG strings
# using currentColor; the wrappers above decide the actual paint.

def c01_waypoint():
    """EL as a planned mission: the ligature is the path, the bar-ends are waypoints."""
    a = [p(LIGATURE), dot(BAR_TOP, TOP_Y, 1.9), dot(BAR_MID, MID_Y, 1.9),
         dot(BAR_BOT, BOT_Y, 1.9)]
    b = [p(LIGATURE, WB), dot(BAR_TOP, TOP_Y, 2.2), dot(BAR_BOT, BOT_Y, 2.2)]
    return a, b


def c02_formation():
    """L holds the axis; the E's three bars break formation and sweep right."""
    axis = f"M{SPINE_X} 6 V{BOT_Y} H25"
    a = [p(axis), p("M14 8 H22", W), p("M15.5 14 H22", W), p("M17 20 H22", W)]
    b = [p(axis, WB), p("M15 9 H22", WB), p("M17 17 H22", WB)]
    return a, b


def c03_frame():
    """The L is a tf frame - the two axes every robotics stack starts from."""
    axes = "M11 6 V25.5 H26"
    heads = "M8.6 8.4 L11 5.6 L13.4 8.4 M23.6 23.1 L26.4 25.5 L23.6 27.9"
    a = [p(axes), p(heads, 1.9),
         p("M11 9.5 H18.5", W), p("M11 14.5 H16", W), p("M11 19.5 H18.5", W)]
    b = [p("M11 6 V25.5 H26", WB), p("M11 10.5 H18", WB), p("M11 17.5 H18", WB)]
    return a, b


def c04_pulse():
    """The E's middle stroke is a clock line. Embedded, and it dates the work."""
    frame = f"M{BAR_TOP} {TOP_Y} H{SPINE_X} V{BOT_Y} H{BAR_BOT}"
    clock = "M11 16.5 H13.5 V12.5 H17 V16.5 H20.5 V12.5 H23"
    a = [p(frame), p(clock, 1.9)]
    # One pulse, not two: at 14px a second cycle closes up into a solid block.
    b = [p(frame, WB), p("M11 16 H15 V12.5 H19 V16 H22", 2.6)]
    return a, b


def c05_occupancy():
    """EL as occupied cells on a costmap. The letters are the obstacle."""
    grid = [
        "11110",
        "10000",
        "10000",
        "11100",
        "10000",
        "10000",
        "11111",
    ]
    cell, gap = 3.0, 0.5
    x0 = 16 - (5 * (cell + gap) - gap) / 2
    y0 = 16 - (7 * (cell + gap) - gap) / 2
    a = [rect(x0 + c * (cell + gap), y0 + r * (cell + gap), cell)
         for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "1"]

    # Three cells wide is the floor. Four still merges into a smear at 14px.
    coarse = ["111", "100", "110", "100", "111"]
    cb, gb = 5.6, 0.9
    xb = 16 - (4 * (cb + gb) - gb) / 2
    yb = 16 - (5 * (cb + gb) - gb) / 2
    b = [rect(xb + c * (cb + gb), yb + r * (cb + gb), cb, 0.9)
         for r, row in enumerate(coarse) for c, ch in enumerate(row) if ch == "1"]
    return a, b


def c06_trace():
    """Routed like a PCB - 45-degree corners, vias where the bars terminate."""
    route = ("M21 7 H12.6 L11 8.6 V23.4 L12.6 25 H25 "
             "M11 16 H16.4 L18 16")
    a = [p(route, 2.2), ring(21, 7, 1.9, 1.5), ring(25, 25, 1.9, 1.5),
         ring(18, 16, 1.6, 1.4)]
    b = [p("M21 7 H12.6 L11 8.6 V23.4 L12.6 25 H25 M11 16 H18", WB),
         dot(21, 7, 1.9), dot(25, 25, 1.9)]
    return a, b


def c07_rotor():
    """The airframe is the ligature; every extremity carries a rotor."""
    arms = f"M{SPINE_X} {TOP_Y} H19 M{SPINE_X} {TOP_Y} V{BOT_Y} H23 M{SPINE_X} {MID_Y} H17"
    a = [p(arms, 2.2), ring(11, 7, 2.6), ring(21.6, 7, 2.6),
         ring(11, 25, 2.6), ring(25.6, 25, 2.6)]
    b = [p(f"M{SPINE_X} {TOP_Y} H18 M{SPINE_X} {TOP_Y} V{BOT_Y} H22 M{SPINE_X} {MID_Y} H16", WB),
         dot(11, 7, 2.4), dot(25, 25, 2.4)]
    return a, b


def c08_bt_kl():
    """KL as a behaviour tree: one root, two children, and the ground it stands on."""
    # The K's lower arm has to stop well clear of the foot, or the two merge
    # into a single diagonal and the mark reads as a lone K.
    spine = "M9 6 V25 H25"
    arms = "M9 13.5 L17 6.5 M9 13.5 L16 20.5"
    a = [p(spine), p(arms, 2.2), dot(9, 13.5, 1.9), dot(17, 6.5, 1.9), dot(16, 20.5, 1.9)]
    b = [p("M9 6 V25 H25", WB), p("M9 13.5 L17 7 M9 13.5 L16 20", WB)]
    return a, b


def c09_mirror():
    """EEK on one spine: E reflected into E, with K's arms taking the right side.

    An earlier attempt put three identical arms at 120 degrees. It made a
    pleasant shape and read as a mechanical fitting, not as initials - which
    is the exact failure this whole round exists to correct, so it was cut.
    """
    spine = "M16 6.5 V25.5"
    left = "M16 6.5 H9 M16 16 H11.5 M16 25.5 H9"      # E, mirrored
    right = "M16 16 L23.5 8 M16 16 L23.5 24"           # K
    a = [p(spine), p(left, 2.2), p(right, 2.2)]
    b = [p(spine, WB), p("M16 7 H9.5 M16 16 H12 M16 25 H9.5", WB),
         p("M16 16 L23 8.5 M16 16 L23 23.5", WB)]
    return a, b


def c10_register():
    """[EL] in the machine register - the lowercase-mono voice, as a mark."""
    brackets = "M10.5 6.5 H7 V25.5 H10.5 M22.5 6.5 H26 V25.5 H22.5"
    # The bottom bar has to run visibly past the top one or the figure reads
    # as a bracketed E and the L disappears entirely.
    inner = "M17 10 H13 V22 H21 M13 16 H16"
    a = [p(brackets, 1.9), p(inner, 2.2)]
    b = [p("M10 7 H7.5 V25 H10 M23 7 H25.5 V25 H23", 2.4),
         p("M17 10.5 H13 V21.5 H21 M13 16 H16", WB)]
    return a, b


CONCEPTS = [
    ("01-waypoint",  "EL waypoint path",     "EL", c01_waypoint,
     "The ligature read as a planned route; bar-ends are waypoints."),
    ("02-formation", "EL formation",         "EL", c02_formation,
     "L holds the axis, the E's bars sweep right like a flight of agents."),
    ("03-frame",     "EL tf frame",          "EL", c03_frame,
     "The L is the coordinate frame every robotics stack opens with."),
    ("04-pulse",     "EL clock pulse",       "EL", c04_pulse,
     "The E's middle stroke is a clock line. Embedded register."),
    ("05-occupancy", "EL occupancy grid",    "EL", c05_occupancy,
     "The letters drawn as occupied cells on a costmap."),
    ("06-trace",     "EL PCB trace",         "EL", c06_trace,
     "Routed like a board: 45-degree corners, vias at the terminals."),
    ("07-rotor",     "EL quadrotor",         "EL", c07_rotor,
     "The ligature is the airframe; each extremity carries a rotor."),
    ("08-bt",        "KL behaviour tree",    "KL", c08_bt_kl,
     "K as a root with two children, L as the ground it stands on."),
    ("09-mirror",    "EEK mirrored spine",   "EEK", c09_mirror,
     "One spine: E reflected into E, K taking the right side."),
    ("10-register",  "[EL] register",        "EL", c10_register,
     "Bracketed, in the lowercase-machine voice from brand/voice.md."),
]


def build():
    os.makedirs(OUT, exist_ok=True)
    written = []
    for slug, label, initials, fn, _ in CONCEPTS:
        primary, small = fn()
        files = {
            "a": svg(paint(ind(primary)), f"{label} - primary"),
            "b": svg(paint(ind(small)), f"{label} - small cut", size=20),
            "c": svg(tile(ind(small)), f"{label} - tile"),
        }
        for suffix, content in files.items():
            path = os.path.join(OUT, f"{slug}-{suffix}.svg")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            written.append(path)
    return written


def check(paths):
    """No gradients, no colours outside the brand. Same discipline as the mark."""
    allowed = {ACCENT.lower(), GROUND.lower(), "currentColor", "none"}
    bad = 0
    for path in paths:
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        found = set(re.findall(r"#[0-9a-fA-F]{6}", src))
        stray = {c for c in found if c.lower() not in allowed}
        if stray or "Gradient" in src or "url(#" in src:
            print(f"FAIL {os.path.basename(path)}: {stray or 'gradient'}")
            bad += 1
    print(f"{len(paths) - bad}/{len(paths)} clean"
          f"{'' if not bad else f' - {bad} need attention'}")
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    files = build()
    print(f"wrote {len(files)} files to {OUT}")
    check(files)
