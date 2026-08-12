# Logo proposals — EL monograms

**Status:** proposals, nothing adopted. The swarm mark in
[`../brand/logo.md`](../brand/logo.md) remains current until one of these
replaces it.

Eight EL monograms, minimal and upright. Files in
[`logo-proposals/svg/`](logo-proposals/svg/), regenerate with
[`logo-proposals/generate.py`](logo-proposals/generate.py).

Four variations each: `-a` primary, `-b` small cut, `-c` favicon tile,
`-d` `currentColor` mono for inlining.

## Three rounds, and what each got wrong

| Round | What it was | Why it failed |
| :--- | :--- | :--- |
| 1 | Ten thin-stroke line drawings — waypoints, tf frames, costmaps, behaviour trees | The visual language of an icon set. A 2.4px stroke has no presence, and letters drawn as adjacent glyphs never fuse into a figure. |
| 2 | Eight heavy italic forms with diagonal speed-cuts | Overcorrection. Chunky, leaning and cut reads as esports, not as a modern mark. |
| 3 | This set | — |

Both earlier rounds failed for the same underlying reason: **decoration standing
in for structure.** Round one added dots and arrowheads to make thin shapes
interesting; round two added lean and rake to make heavy shapes interesting.
Neither fixed the letterform.

## The rule this round is built on

Everything lands on the grid:

```
UNIT    4      the module
MARGIN  6      breathing room on every side; the mark never touches the box
bar height == gap height == UNIT
```

That single equality does most of the work. An E of three bars and two gaps at
one module each is exactly five modules tall, so the rhythm comes out even **by
construction rather than by eye**, and the counters are identical without being
tuned. It is the Bauhaus/Swiss construction, and it is why those marks still
look calm decades on.

Deliberately absent, because it is what made the last two rounds look rough:
no italic lean, no diagonal terminals, no arrowheads, no dots, no seams, no
tapers. Every terminal is square or fully round, and a given mark uses only
one of the two. `generate.py --check` fails the build on a stroke, a gradient,
an off-brand colour, or any shear or rotation.

## The eight

| # | Mark | Idea |
| :--- | :--- | :--- |
| A | **module** | The reference construction. Bar height equals gap height equals one module. |
| B | **round** | The same grid, fully round terminals — radius exactly half a module. |
| C | **detached** | Bars lifted clear of the stem by half a module. The join is implied. |
| D | **negative** | The mark is the void. A calm square, not a leaning slab. |
| E | **corner** | Two elements at one weight: an L angle, and an E of three bars beside it. |
| F | **line** | Even geometric monoline. One weight, square joins, nothing added. |
| G | **apex** | E on top, the stem running past it and turning. Both letters, one figure. |
| H | **tone** | L at full strength, E ghosted behind it. Hierarchy by tone, not shape. |

All eight hold at 12px.

### Notes before choosing

**G is the most legible as two letters.** The E finishes, the stem carries on
past it and turns — so the L is a separate event rather than a longer bottom
bar. A, B, C, D and F all read as a strong E with the L implied by the foot,
which is a legitimate choice but a different one.

**E reads "LE", not "EL"** — the angle sits left so the eye takes it first.
*LEJEUNE Erwin* is the formal order, so this may be a feature; flipping it
would undo the composition that makes the mark work.

**H is the only one that reuses an existing brand device.** The swarm mark
already sets its link path at 0.45 so the nodes read as the subject; this
applies the same idea to the two letters. It is also the quietest, and the
first to disappear against a busy background.

**D holds up smallest** — the figure is carried by area rather than by stroke
width — and is the loudest of the set.

**F is the lightest.** At 3 units against the 4-unit grid it is the one that
would sit most comfortably next to body text, and the one most at risk of
looking thin when embroidered or engraved.

## Constraints kept

Ink & Iris only — `#8b95f0` on `#0d0e12`. No second hue, no gradients, no
strokes, nothing sheared. All 32 files pass `generate.py --check`.

These are not run through `validate_mark.py`: it encodes the swarm mark's exact
geometry and would reject all eight by construction. Adopting one means
rewriting that validator against the new geometry and giving `brand/logo.md` a
new construction table and rationale.
