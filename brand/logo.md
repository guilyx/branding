# The mark

Three filled circles at the vertices of an equilateral triangle, joined by a
faint outline.

![the swarm mark](../assets/logo/mark-accent.svg)

## Why this

Three agents holding a formation. It is the smallest possible drawing of the
thing I actually work on — decentralized swarms, where no node is in charge and
the shape is a consequence of local rules rather than a leader. Three is the
minimum count where "formation" means anything at all.

It also survives being small, which a monogram in a hexagon did not.

## Construction

On a 32 × 32 grid:

| Element | Geometry |
| :--- | :--- |
| Apex node | centre `(16, 8.5)`, r `2.1` |
| Left node | centre `(8.5, 21)`, r `2.1` |
| Right node | centre `(23.5, 21)`, r `2.1` |
| Link path | `M16 8.5 L8.5 21 L23.5 21 Z`, stroke `1.1`, opacity `0.45` |

Nodes are solid; the link path is deliberately weaker than the nodes, so the
agents read as the subject and the formation as the consequence.

## Files

| File | Use |
| :--- | :--- |
| `assets/logo/mark-accent.svg` | Default. Accent nodes, transparent ground. |
| `assets/logo/mark-mono.svg` | `currentColor` — inherits from context. Use in nav bars and buttons. |
| `assets/logo/favicon.svg` | 6px-radius ground tile plus the mark. Browser tabs. |
| `assets/logo/mark-lockup.svg` | Mark plus `guilyx` wordmark, horizontal. |

## Rules

- **Minimum size** 20 px. Below that the link path muddies — use a version with
  the path removed rather than shrinking further.
- **Clear space** at least the node radius (r) on every side.
- **Rotation** is allowed, and only in multiples of 120° — the mark is
  rotationally symmetric at that interval, so it lands back on itself. The
  site's nav uses a 120° turn on hover.
- **Colour**: accent nodes on a dark ground, or `currentColor` mono. Never a
  gradient, never more than one hue.
- **Don't** add a fourth node, fill the triangle, outline the nodes, place the
  mark on a busy photo, or set it in a circle or rounded square other than the
  favicon tile.

## Wordmark

`guilyx` — lowercase, always, in the mono face (JetBrains Mono, 400). The
lowercase is not a stylisation; it is how the handle is written everywhere else.

The full name **Erwin Lejeune** is set in the display face (Space Grotesk) and
is not part of the mark — it is typography, and it changes size and weight with
context.
