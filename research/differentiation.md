# Differentiation from bchiang7/v4

elejeune.me v4 started from
[Brittany Chiang's v4](https://v4.brittanychiang.com/)
([source](https://github.com/bchiang7/v4), MIT). This is the honest accounting
of what was taken, what was replaced, and what is still owed.

## The colour problem

The first build did not resemble her palette — it *was* her palette. All eight
tokens were byte-identical to `src/styles/variables.js`:

| Ours | Value | Hers |
| :--- | :--- | :--- |
| `--color-bg` | `#0a192f` | `--navy` |
| `--color-bg-raised` | `#112240` | `--light-navy` |
| `--color-line` | `#233554` | `--lightest-navy` |
| `--color-heading` | `#ccd6f6` | `--lightest-slate` |
| `--color-body` | `#a8b2d1` | `--light-slate` |
| `--color-muted` | `#8892b0` | `--slate` |
| `--color-faint` | `#495670` | `--dark-slate` |
| `--color-accent` | `#64ffda` | `--green` |

Mint-on-navy is the thing people recognise her site by. Replaced wholesale with
[Ink & Iris](../brand/palette.md); the alternatives considered are in
[`palette-study.md`](palette-study.md).

## Structural tells, and what replaced them

Colour was the loudest problem but not the only one. Each of these was a
recognisable device of hers, and each was replaced with something that says
something true about this particular career.

### Numbered section headings → section keys

Hers: `01.` `02.` `03.` in the accent, followed by the title and a trailing
rule.

The numbering was never honest here — About, Trajectory, Builds and Contact are
parallel, not a sequence, so ordinals encoded nothing. Replaced with a small
rotated square and a lowercase mono key above the title. The navigation dropped
its matching numbers at the same time.

### Vertical tab list → trajectory timeline

Hers: a vertical tab list with a sliding accent marker, one job visible at a
time.

Replaced with a horizontal timeline — a label gutter and a bar per role,
positioned by date across a year axis, still selectable for detail. This is the
change that earns itself: **three roles currently run concurrently** (SIRB.AI,
TII, Unchained Labs), and two earlier ones overlapped as well. A tab list hides
concurrency completely; the timeline makes it the first thing you see. The
component is better for this data than the thing it replaced, which is a
stronger position than "merely different".

### Fixed side rails → footer

Hers: social icons fixed to the lower left, vertical email fixed to the lower
right, each with a short vertical line.

Instantly recognisable, and on a page this quiet they were the loudest thing on
screen. Removed entirely. Socials moved to the footer; the email address moved
into the hero, where it is the second thing after the spec block.

### Greeting formula → spec block

Hers: "Hi, my name is / **Name.** / tagline. / paragraph / CTA".

The greeting formula was hers line for line. Replaced with a key/value spec
block — `role`, `based`, `building`, `also` — a register borrowed from Erwin's
own [GitHub profile README](https://github.com/guilyx/guilyx), which has
introduced him as a YAML document for years. Using his existing self-
presentation is both more personal and provably not lifted.

### Section titles

"Where I've Worked" and "Get In Touch" were hers verbatim. Now *Trajectory*
(a path-planning term, and his actual field), *Background*, *Selected Builds*,
and *Open Channel*.

### Brand mark

The first mark was a monogram in a hexagon, which is generic and read poorly at
small sizes. Replaced with the [swarm mark](../brand/logo.md) — three agents
holding a formation.

## What is still owed

Plenty, and it should be said plainly:

- the overall page shape — a single column, generous vertical rhythm, one
  content section per screen
- the restraint: one accent, one display face, no gradients
- mono type as the label voice
- the ghost-button treatment
- the underline-slide link hover
- the idea that a developer portfolio can be quiet

These are craft decisions worth learning from, and the site is better for them.
The footer credits her v4 directly, and it should stay there.

## What was ours from the start

- the boids flocking simulation behind the hero, and the decision to make the
  hero background a live artefact of the subject matter
- the promo artwork for the featured projects — a rendered flock, a terminal
  session, a docs-drift pull request
- Astro 5 + Tailwind 4 + vanilla TypeScript (hers is Gatsby + styled-components)
- the content-collection blog and photo pages
