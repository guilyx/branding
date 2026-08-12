# Logo proposals — EL / EK as graphs

**Status:** proposals, nothing adopted. The swarm mark in
[`../brand/logo.md`](../brand/logo.md) remains current until one of these
replaces it.

Eight monograms read as graphs. Files in
[`logo-proposals/svg/`](logo-proposals/svg/), regenerate with
[`logo-proposals/generate.py`](logo-proposals/generate.py).

Four variations each: `-a` primary, `-b` small cut, `-c` favicon tile,
`-d` `currentColor` mono.

## The idea

An E is three horizontal bars hanging off a vertical. That is not a shape that
needs graph imagery *added* to it — **it already is a layered graph**: a trunk
with three ranks. So nothing here decorates a letter with nodes, which is
precisely what made round one fail. The graph is the letterform.

Two readings of the second letter, both built:

| Letter | Reading |
| :--- | :--- |
| **L** | The backbone. The vertical the ranks hang off, running past the last of them and turning — an orchestrator trunk with a base. |
| **K** | The fan-out. Its vertex is a branch node, its arms are edges to children. A K drawn as a graph *is* a fork. |

The three ranks sit at y = 8, 16, 24 in every mark, so the set can be compared
directly. Grid discipline, upright stance and generous margins carry over from
round three; edges are strokes, because a graph has edges and drawing them as
filled quads would be pedantry — but they are heavy and round-capped, never
hairlines. The audit fails the build on a hairline edge, a gradient, an
off-brand colour, or any shear.

## The eight

| # | Mark | Letters | Idea |
| :--- | :--- | :--- | :--- |
| A | **rank** | EL | Trunk with three ranks, each ending in a node. The plainest reading. |
| B | **fork** | EK | One branch node, three edges out. |
| C | **bus** | EL | Nodes at the junctions, not the tips — three taps off a backbone. |
| D | **capsule** | EL | The ranks are node capsules on a spine. Workflow-graph register. |
| E | **pipeline** | EL | A node at both ends of every rank. Three stages, explicitly bounded. |
| F | **ek** | EK | E and K as two graphs side by side — ranks, then the fork they feed. |
| G | **backbone** | EL | E finishes, the trunk runs past it and turns. |
| H | **orchestrator** | — | One node holds the work and hands it out. The others only receive. |

## Two collisions, before anything else

**B is very close to the share icon.** One node left, edges fanning right to
nodes, is the Android/Material share glyph with an extra child added. That is
one of the most recognised interface symbols in the world, and a personal mark
should not have to fight it. The idea is good; this particular arrangement of
it is spoken for. Worth either re-composing (vertical fan, or the branch node
on the right) or dropping.

**H does not read as letters at all.** It is a pleasant network glyph, and it
is the same failure as the triskelion in round one — interesting shape, no
initials. Kept in the set only so the comparison is honest; it should not be
adopted as-is.

## The rest

**F is the standout.** It is the only mark in four rounds that reads
unambiguously as two letters *and* carries the concept — the K is a genuine
fork, vertex node and all, and the E's three ranks feed it. If the brief is
"initials plus orchestration", this is the closest thing to a direct answer.

**G is the most legible EL.** The E completes, then the trunk carries on past
it and turns, so the L is a separate event rather than a longer bottom bar.

**A, C and E are the same skeleton with the nodes moved** — tips, junctions,
both ends. That is deliberate: it is the one axis worth testing directly,
because it changes what the mark says. Tips read as outputs, junctions read as
taps off a bus, both ends read as bounded stages. C is the most distinctive of
the three; A the calmest.

**D drifts toward a list icon.** Detaching the capsules from the spine costs
the E its joins, and what is left resembles a reorder or menu glyph. Less
severe than B, but the same category of problem.

## Constraints kept

Ink & Iris only — `#8b95f0` on `#0d0e12`. No second hue, no gradients, nothing
sheared. All 32 files pass `generate.py --check`.

Adopting any of these means rewriting `validate_mark.py` against the new
geometry and giving `brand/logo.md` a new construction table and rationale.
