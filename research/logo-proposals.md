# Logo proposals — EL signature marks

**Status:** proposals, nothing adopted. The swarm mark in
[`../brand/logo.md`](../brand/logo.md) remains current until one of these
replaces it.

Eight marks built on the initials **EL**, in the register of a personal
signature mark rather than an icon. Files in
[`logo-proposals/svg/`](logo-proposals/svg/), regenerate with
[`logo-proposals/generate.py`](logo-proposals/generate.py).

Four variations each:

| Suffix | What it is |
| :--- | :--- |
| `-a` | Primary. Accent, full detail. |
| `-b` | Small cut. Simplified, tuned for 16px and below. |
| `-c` | Favicon tile. |
| `-d` | `currentColor` mono, for inlining. |

## The first round, and why it was scrapped

Round one was ten thin-stroke line drawings — waypoints, tf frames, costmaps,
behaviour trees. It was rejected on sight, and correctly: **that is the visual
language of an icon set, not of a personal mark.** A 2.4px stroke has no
presence, and letters drawn as adjacent glyphs never fuse into a figure.

What the reference marks actually share:

| Principle | What it means here |
| :--- | :--- |
| **Solid mass, not outline** | Weight is presence. Every mark below is a closed filled path; none use `stroke`. |
| **One fused figure** | Federer's R and F share a spine and a cut. The letters are one shape, not two. |
| **Contrast** | Thick stems against thin arms. Uniform weight reads as an icon. |
| **Subtractive** | The RF monogram *removes* lines rather than adding them; its counters do as much work as its strokes. |
| **A signature move** | Jumpman is a silhouette of the thing the person is known for. Here that is flight — hence the 9° lean and the swept terminals. |

## Making the L legible

The hard problem in a fused EL: if E and L share a spine, you get an E with a
long bottom bar and the L vanishes.

The fix in most of these is **rhythm, not geometry** — the gap above the foot
runs roughly twice the gap between the two upper arms, and the foot runs
longest. The eye takes stem-plus-foot as an L first, then picks up the upper
arms as an E. With even gaps it collapses back into a wide-based E every time.

**It works better in some than others, and that is the main thing to judge.**
Two of the eight show two distinct letters unambiguously; the rest read as a
strong single glyph that *implies* the L. Both are legitimate — Jumpman is not
a letter at all — but it is a real choice, not a detail.

## The eight

| # | Mark | Idea | Two letters? | 12px |
| :--- | :--- | :--- | :--- | :--- |
| A | **slipstream** | One fused mass, leaning, diagonal terminals. The base. | implied | clean |
| B | **corner** | A heavy L angle with a compact E in its corner. | **yes** | clean |
| C | **contra** | A slab stem against arms a third its weight. | implied | clean |
| D | **stack** | E over L, offset. | **yes** | clean |
| E | **vector** | The foot runs out into an arrowhead. | implied | clean |
| F | **wing** | Arms raked hard root to tip. | implied | clean |
| G | **crest** | EL held in a shield — the only enclosed mark. | implied | soft |
| H | **counter** | The letterform is the hole. | implied | **best** |

### Notes worth having before choosing

**B reads "LE", not "EL".** The heavy angle sits on the left, so the eye takes
the L first. That may be a feature — *LEJEUNE Erwin* is the formal order — but
it is not what was asked for, and flipping the composition would undo the
corner idea that makes the mark work. Worth a decision rather than a fix.

**D is the most legible and the least athletic.** Stacking guarantees both
letters read, at the cost of the single-gesture quality the others have.

**H holds up smallest by a clear margin**, because the figure is carried by the
largest possible area of contrast rather than by the width of a stroke. It is
also the loudest, and the only one that would fight a busy page.

**G is the only enclosed mark**, which puts it closest to a sports crest and
furthest from the rest of the system — `brand/logo.md` currently forbids
containers outside the favicon tile, so adopting it means amending that rule.

## Constraints kept

Ink & Iris only — `#8b95f0` on `#0d0e12`. No second hue, no gradients, no
strokes. All 32 files pass the audit in `generate.py --check`, which fails on
any of the three.

These are deliberately not run through `validate_mark.py`: that validator
encodes the swarm mark's exact geometry and would reject all eight by
construction. If one is adopted, that script needs rewriting against the new
geometry, and `brand/logo.md` needs a new construction table and rationale.
