# Palette study — August 2026

Five candidates were built and rendered against the live
[elejeune.me v4](https://github.com/guilyx/v4) build, not mocked up. Each kept
the same structural principle — one dark ground, one restrained accent, mono
labels — and varied only the colour identity.

**Outcome:** Ink & Iris adopted. Bone & Rust kept on file as runner-up.

## What was being replaced

A navy/mint scheme in which all eight tokens were byte-identical to
[bchiang7/v4](https://github.com/bchiang7/v4). Full accounting in
[`differentiation.md`](differentiation.md).

## The brief

- Dark enough for long reading; sober, not neon.
- Exactly one saturated colour, spent sparingly.
- Nowhere near mint-on-navy — the hue family itself had to move.
- Legible at `muted` and above without straining.

## Candidates

### Ink & Iris — adopted

| bg | raised | line | muted | body | heading | accent |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `#0d0e12` | `#15171d` | `#252833` | `#7c8291` | `#a5aab8` | `#e4e6ec` | `#8b95f0` |

Neutral-cool near-black with a periwinkle accent. Keeps the calm of a dark
technical page while moving the accent to a hue that carries none of the
original's association.

*Argued against at the time:* cool-dark plus cool-accent is the most common
register in developer portfolios, so it differentiates least of the five. That
was accepted knowingly — the priority was removing the copied identity, not
winning a novelty contest, and the structural changes shipped alongside it do
more differentiating work than the hue would have.

### Bone & Rust — runner-up

| bg | raised | surface | line | muted | body | heading | accent |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `#f5f3ee` | `#ffffff` | `#ebe7de` | `#dbd6cb` | `#6f6b62` | `#4b4842` | `#1b1a17` | `#b0472b` |

Light, editorial, print-adjacent. The cleanest possible break: nobody confuses
a paper-white portfolio with a dark one. Would flatter the photography page far
more than any dark ground.

*Cost:* the hero flock, the project promo artwork, and the navigation tint all
need re-tuning for a light ground. Deferred, not rejected.

### Basalt & Dune — considered

| bg | raised | line | muted | body | heading | accent |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `#12100e` | `#1a1714` | `#2e2925` | `#8d8577` | `#b9b0a3` | `#ece5da` | `#d9a05b` |

Warm volcanic neutral under brass. Sand in the ground as a quiet nod to Abu
Dhabi; brass reads as instrumentation rather than screen-glow. Was the initial
recommendation.

*Why not:* the warmth pulled the whole page toward a hospitality/portfolio-
template register that fit the writing less well than the cooler options.

### Graphite & Ember — considered

| bg | raised | line | muted | body | heading | accent |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `#0e0e10` | `#16161a` | `#292930` | `#7f7f88` | `#a9a9b0` | `#ededee` | `#e2643c` |

A true neutral grey with hot-metal orange — the maximum available distance from
navy/mint in both ground and accent. Reads workshop and welding.

*Why not:* the most assertive of the five. The orange demands attention on every
screen it appears on, which fights the "sober" requirement.

### Field Olive — considered

| bg | raised | line | muted | body | heading | accent |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `#101210` | `#171a16` | `#272b25` | `#848a7b` | `#aeb3a5` | `#e7e9e1` | `#a3b76c` |

Desaturated moss on near-black — green, but the opposite end of the saturation
range from mint. Suits the field-robotics and defence side of the work.

*Why not:* it is still a green accent on a near-black ground. The two colours
look nothing alike side by side, but the one-sentence description of the
palette matches the thing being moved away from. Not worth the ambiguity.

## Method

The five were applied by rewriting the `@theme` block in `src/styles/global.css`
and rebuilding, so every screenshot is the real site. The harness that did it is
worth rebuilding if this exercise ever repeats: patch tokens → `astro build` →
`astro preview` → screenshot hero and one content section → restore.

One refactor came out of the study and shipped: the hero flock used to have its
colour hardcoded as an RGB triple in the canvas script, which meant a palette
change touched two files. It now reads `--color-agent` at runtime.
