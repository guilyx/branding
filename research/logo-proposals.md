# Logo proposals — initials + domain

**Status:** proposals, nothing adopted. The swarm mark in
[`../brand/logo.md`](../brand/logo.md) remains current until one of these
replaces it.

Ten concepts built around the initials **EL**, **EEK** and **KL**, each
carrying something from the actual work — path planning, flight, tf frames,
clock lines, costmaps, board routing, behaviour trees. Files in
[`logo-proposals/svg/`](logo-proposals/svg/), regenerate with
[`logo-proposals/generate.py`](logo-proposals/generate.py).

Three variations each:

| Suffix | What it is |
| :--- | :--- |
| `-a` | Primary. Accent on transparent, full detail. |
| `-b` | Small cut. Fewer elements, heavier stroke, tuned for 20px. |
| `-c` | Favicon tile. Ground plus mark. |

## The test that matters

`brand/logo.md` records that the previous monogram was dropped because it did
not survive being small. Any initials-based mark has to answer that objection
first, so every concept was rendered at 20px and 14px before anything else
about it was considered.

Two concepts were cut during the round for failing on their own terms, and it
is worth recording why:

- **A triskelion** — three identical arms at 120°, echoing the interval the
  current mark turns on. It made a pleasant shape and read as a *mechanical
  fitting*. Nothing about it said "initials", which is the exact failure this
  round exists to correct. Replaced by `09-mirror`.
- **The first `08-bt`** put the K's lower arm too close to the L's foot; the
  two merged into one diagonal and the mark read as a lone K. Widened.

## The ten

| # | Concept | Initials | The domain half | 14px |
| :--- | :--- | :--- | :--- | :--- |
| 01 | **waypoint** | EL | The ligature as a planned route, bar-ends as waypoints | clean |
| 02 | **formation** | EL | L holds the axis, the E's bars sweep right like a flight | clean |
| 03 | **frame** | EL | The L is a tf frame — the two axes every stack opens with | clean |
| 04 | **pulse** | EL | The E's middle stroke is a clock line | tight |
| 05 | **occupancy** | EL | Letters as occupied cells on a costmap | **poor** |
| 06 | **trace** | EL | Routed like a board: 45° corners, vias at the terminals | clean |
| 07 | **rotor** | EL | The ligature is the airframe, each extremity a rotor | clean |
| 08 | **bt** | KL | K as a root with two children, L as the ground | clean |
| 09 | **mirror** | EEK | One spine: E reflected into E, K taking the right side | clean |
| 10 | **register** | EL | Bracketed, in the lowercase-machine voice | clean |

### The EL ligature

Seven of the ten share one construction: **E and L on a common spine, with the
bottom bar running longer than the top.** That length difference is the whole
trick — it is what makes a single figure read as both letters instead of just
an E. Concepts 01–07 vary what happens at the terminals and along the middle
stroke; the skeleton underneath is identical, which is why they sit together
as a family rather than as ten unrelated sketches.

### Reading the shortlist

If the priority is **survives everywhere and says robotics without
explaining itself**, the strongest are `01-waypoint`, `06-trace` and
`02-formation`. All three hold at 14px, and none of them need a caption.

`07-rotor` is the most literal about drones and the most charming at large
sizes; its rings collapse to dots below about 18px, which the `-b` cut handles
by making that collapse deliberate rather than accidental.

`05-occupancy` is the one to be honest about: it is genuinely good at 64px and
above, and it is mud at 14px. Even coarsened to a three-cell-wide grid it loses
the counters. It would work as a large-format mark — a header, a slide, a
sticker — with something else carrying the favicon. That is a real cost, and
the reason the current mark avoids per-cell detail entirely.

`10-register` is the most on-voice — `brand/voice.md` describes a deliberate
two-register system, and brackets are the machine register made visible. It is
also the least about robotics specifically.

## Constraints kept

These are proposals, not adopted marks, so they are not checked by
`validate_mark.py` — that validator encodes the *swarm mark's* geometry
specifically and would reject all ten by construction. What was kept:

- Ink & Iris only: `#8b95f0` on `#0d0e12`. No second hue, no gradients.
  All 30 files pass the colour audit in `generate.py --check`.
- The favicon tile is the same `rx=6` ground tile the current mark uses.
- One idea per mark. Nothing here needs two things explained at once.

Whichever is adopted still needs a `currentColor` mono cut before it ships —
these render at a literal accent so they can be compared side by side, and a
mono variant is what makes one file serve dark UI, light UI and print.
