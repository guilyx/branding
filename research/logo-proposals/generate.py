#!/usr/bin/env python3
"""Generate the EL / EK monogram proposals - graph and orchestration reading.

Round four. The previous three were pure letterforms; this one starts from what
the letters already are.

An E is three horizontal bars hanging off a vertical. That is not a shape that
needs graph imagery added to it - it *is* a layered graph: a trunk with three
ranks. So nothing here decorates a letter with nodes. The graph is the
letterform, which is the difference between this and round one, where dots were
sprinkled onto strokes to make them interesting.

The two readings of the second letter:

    L is the backbone.  The vertical the ranks hang off, running past the last
                        of them and turning - an orchestrator trunk with a base.
    K is the fan-out.   Its vertex is a branch node and its arms are edges to
                        children. A K drawn as a graph is a fork, exactly.

Kept from round three, because that register was right: strict grid, upright,
generous margins, one weight per element class, nothing decorative. The three
ranks sit on y = 8, 16, 24 in every mark, so they can be compared directly.

Edges are strokes here - a graph has edges, and drawing them as filled quads
would be pedantry. They are heavy and round-capped, never hairlines.

    python3 generate.py            # writes svg/
"""

import argparse
import os
import re

ACCENT = "#8b95f0"
GROUND = "#0d0e12"

RANK = (8.0, 16.0, 24.0)   # the three ranks, on grid, in every mark
EW = 3.0                   # edge weight
NR = 2.9                   # node radius - deliberately wider than the edge,
                           # so a node reads as a node and not as a thickening

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")


# --- primitives -----------------------------------------------------------

def edge(x1, y1, x2, y2, w=EW, colour="currentColor"):
    return (f'<path d="M{x1:g} {y1:g} L{x2:g} {y2:g}" fill="none" '
            f'stroke="{colour}" stroke-width="{w:g}" stroke-linecap="round"/>')


def node(x, y, r=NR, colour="currentColor"):
    return f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{colour}"/>'


def pill(x, y, w, h, colour="currentColor"):
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
            f'rx="{h / 2:g}" fill="{colour}"/>')


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


# --- concepts -------------------------------------------------------------

def a_rank():
    """Trunk with three ranks, each terminating in a node. The plainest reading."""
    t = [edge(8, 6.2, 8, 25.8), edge(8, RANK[0], 18, RANK[0]),
         edge(8, RANK[1], 15, RANK[1]), edge(8, RANK[2], 23, RANK[2]),
         node(18, RANK[0]), node(15, RANK[1]), node(23, RANK[2])]
    b = [edge(8, 6.2, 8, 25.8, 3.4), edge(8, RANK[0], 17.5, RANK[0], 3.4),
         edge(8, RANK[1], 15, RANK[1], 3.4), edge(8, RANK[2], 22.5, RANK[2], 3.4),
         node(17.5, RANK[0], 3.1), node(15, RANK[1], 3.1), node(22.5, RANK[2], 3.1)]
    return t, b


def b_fork():
    """One branch node, three edges out. The K read: a fork is what a K is."""
    t = [edge(8.5, 16, 22, RANK[0]), edge(8.5, 16, 22, RANK[1]),
         edge(8.5, 16, 22, RANK[2]),
         node(22, RANK[0], 2.6), node(22, RANK[1], 2.6), node(22, RANK[2], 2.6),
         node(8.5, 16, 3.8)]
    b = [edge(8.5, 16, 21.5, RANK[0], 3.4), edge(8.5, 16, 21.5, RANK[1], 3.4),
         edge(8.5, 16, 21.5, RANK[2], 3.4),
         node(21.5, RANK[0], 2.9), node(21.5, RANK[1], 2.9), node(21.5, RANK[2], 2.9),
         node(8.5, 16, 4.1)]
    return t, b


def c_bus():
    """Nodes at the junctions instead of the tips - three taps off a backbone."""
    t = [edge(8, 5.6, 8, 26.4, 2.4), edge(8, RANK[0], 19, RANK[0]),
         edge(8, RANK[1], 16, RANK[1]), edge(8, RANK[2], 24, RANK[2]),
         node(8, RANK[0], 3.3), node(8, RANK[1], 3.3), node(8, RANK[2], 3.3)]
    b = [edge(8, 5.6, 8, 26.4, 2.8), edge(8, RANK[0], 18.5, RANK[0], 3.4),
         edge(8, RANK[1], 16, RANK[1], 3.4), edge(8, RANK[2], 23.5, RANK[2], 3.4),
         node(8, RANK[0], 3.6), node(8, RANK[1], 3.6), node(8, RANK[2], 3.6)]
    return t, b


def d_capsule():
    """The ranks are node capsules on a spine. The register of a workflow graph."""
    h = 5.0
    t = [edge(7.5, 8, 7.5, 24, 2.6),
         pill(10.5, RANK[0] - h / 2, 11, h), pill(10.5, RANK[1] - h / 2, 8.5, h),
         pill(10.5, RANK[2] - h / 2, 14, h)]
    b = [edge(7.6, 8, 7.6, 24, 3.0),
         pill(10.8, RANK[0] - 2.8, 10.5, 5.6), pill(10.8, RANK[1] - 2.8, 8, 5.6),
         pill(10.8, RANK[2] - 2.8, 13.5, 5.6)]
    return t, b


def e_pipeline():
    """A node at both ends of every rank. Three stages, explicitly bounded."""
    t = [edge(8, 8, 8, 24, 2.6),
         edge(8, RANK[0], 20, RANK[0]), edge(8, RANK[1], 17, RANK[1]),
         edge(8, RANK[2], 24, RANK[2]),
         node(8, RANK[0], 2.5), node(8, RANK[1], 2.5), node(8, RANK[2], 2.5),
         node(20, RANK[0], 2.5), node(17, RANK[1], 2.5), node(24, RANK[2], 2.5)]
    b = [edge(8, 8, 8, 24, 3.0),
         edge(8, RANK[0], 19.5, RANK[0], 3.4), edge(8, RANK[1], 17, RANK[1], 3.4),
         edge(8, RANK[2], 23.5, RANK[2], 3.4),
         node(19.5, RANK[0], 3.0), node(17, RANK[1], 3.0), node(23.5, RANK[2], 3.0)]
    return t, b


def f_ek():
    """E and K as two graphs side by side - ranks, then the fork they feed."""
    t = [edge(6, 7.4, 6, 24.6, 2.6),
         edge(6, RANK[0], 12, RANK[0]), edge(6, RANK[1], 12, RANK[1]),
         edge(6, RANK[2], 12, RANK[2]),
         edge(18, 6.4, 18, 25.6, 2.6),
         edge(18, 16, 26, 7.6), edge(18, 16, 26, 24.4),
         node(18, 16, 3.2), node(26, 7.6, 2.4), node(26, 24.4, 2.4)]
    b = [edge(6.5, 7.4, 6.5, 24.6, 3.0),
         edge(6.5, RANK[0], 12, RANK[0], 3.2), edge(6.5, RANK[1], 12, RANK[1], 3.2),
         edge(6.5, RANK[2], 12, RANK[2], 3.2),
         edge(19, 6.4, 19, 25.6, 3.0),
         edge(19, 16, 26, 8.4, 3.2), edge(19, 16, 26, 23.6, 3.2),
         node(19, 16, 3.4)]
    return t, b


def g_backbone():
    """E finishes, the trunk runs past it and turns. The L is a separate event."""
    t = [edge(9, 6.4, 9, 25.4), edge(9, 8, 19, 8), edge(9, 14, 17, 14),
         edge(9, 20, 19, 20), edge(9, 25.4, 24, 25.4),
         node(19, 8, 2.6), node(17, 14, 2.6), node(19, 20, 2.6), node(24, 25.4, 2.6)]
    b = [edge(9, 6.4, 9, 25.4, 3.4), edge(9, 8, 18.5, 8, 3.4),
         edge(9, 14, 17, 14, 3.4), edge(9, 20, 18.5, 20, 3.4),
         edge(9, 25.4, 23.5, 25.4, 3.4),
         node(18.5, 8, 2.9), node(17, 14, 2.9), node(18.5, 20, 2.9)]
    return t, b


def h_orchestrator():
    """One node holds the work and hands it out. The others only receive."""
    t = [edge(9.5, 9.5, 22, RANK[0]), edge(9.5, 9.5, 20, RANK[1]),
         edge(9.5, 9.5, 23, RANK[2]),
         node(22, RANK[0], 2.4), node(20, RANK[1], 2.4), node(23, RANK[2], 2.4),
         node(9.5, 9.5, 4.4)]
    b = [edge(9.5, 9.5, 21.5, RANK[0], 3.4), edge(9.5, 9.5, 20, RANK[1], 3.4),
         edge(9.5, 9.5, 22.5, RANK[2], 3.4),
         node(21.5, RANK[0], 2.8), node(20, RANK[1], 2.8), node(22.5, RANK[2], 2.8),
         node(9.5, 9.5, 4.8)]
    return t, b


CONCEPTS = [
    ("a-rank", "EL rank", a_rank,
     "Trunk with three ranks, each ending in a node. The plainest reading."),
    ("b-fork", "EK fork", b_fork,
     "One branch node, three edges out. A K drawn as a graph is a fork."),
    ("c-bus", "EL bus", c_bus,
     "Nodes at the junctions, not the tips - three taps off a backbone."),
    ("d-capsule", "EL capsule", d_capsule,
     "The ranks are node capsules on a spine. Workflow-graph register."),
    ("e-pipeline", "EL pipeline", e_pipeline,
     "A node at both ends of every rank. Three stages, explicitly bounded."),
    ("f-ek", "EK pair", f_ek,
     "E and K as two graphs side by side - ranks, then the fork they feed."),
    ("g-backbone", "EL backbone", g_backbone,
     "E finishes, the trunk runs past it and turns. The L is a separate event."),
    ("h-orchestrator", "EL orchestrator", h_orchestrator,
     "One node holds the work and hands it out. The others only receive."),
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
        if re.search(r'stroke-width="([01](\.\d+)?|2(\.[0-3])?)"', src):
            problems.append("hairline edge; edges carry weight in this round")
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
