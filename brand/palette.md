# Palette — Ink & Iris

**Status:** current, adopted August 2026.
**Replaces:** a navy/mint scheme that was copied verbatim from a third party
(see [`../research/differentiation.md`](../research/differentiation.md)).

Neutral-cool near-black under a periwinkle accent. The ground is deliberately
*neutral* cool rather than blue — there is only a few degrees of hue in it, so
it reads as ink rather than navy. The accent carries all the colour the system
has.

## Tokens

| Role | Token | Hex | Notes |
| :--- | :--- | :--- | :--- |
| Ground | `--color-bg` | `#12141b` | Page background. Never lighten for "sections". |
| Raised | `--color-bg-raised` | `#1a1d26` | Cards, panels, code blocks. |
| Surface | `--color-surface` | `#1a1d26` | Alias of raised; kept separate so they can diverge later. |
| Hairline | `--color-line` | `#2c3040` | Borders, rules, inactive timeline bars. |
| Heading | `--color-heading` | `#e8eaf0` | Headings and emphasised inline text. |
| Body | `--color-body` | `#aeb3c2` | Running text. |
| Muted | `--color-muted` | `#858b9c` | Secondary text, captions. |
| Faint | `--color-faint` | `#616779` | Labels, keys, disabled. Lowest legible step. |
| Accent | `--color-accent` | `#8b95f0` | See budget below. |
| Accent wash | `--color-accent-soft` | `rgba(139,149,240,0.08)` | Hover fills only. |
| Agent | `--color-agent` | `#858b9c` | The hero flock. Texture, not decoration — tracks `muted`. |

## The accent budget

The accent is the only saturated colour in the system, so it is spent
deliberately. It gets used for:

- small mono labels and section keys
- inline links and their hover rules
- the active state of one control at a time (the selected timeline bar)
- the brand mark
- focus rings

It does **not** get used for: headings, body copy, large fills, icon sets,
decorative gradients, or more than one active element in the same view. If a
screen has more than roughly three accent moments, one of them is decoration
and should come out.

The wash (`accent-soft`) exists so hover states can read without introducing a
second saturated value.

## Contrast

Checked against the ground (`#12141b`):

| Pair | Ratio | Verdict |
| :--- | ---: | :--- |
| heading on ground | 15.3:1 | AAA |
| body on ground | 8.8:1 | AAA |
| muted on ground | 5.4:1 | AA (normal text) |
| accent on ground | 6.7:1 | AA (normal text) |
| faint on ground | 3.3:1 | **labels ≥ 14 px only** — not for running text |

Lifting the ground in August 2026 cost the accent its AAA rating: against the
old `#0d0e12` it measured 7.6:1, against `#12141b` it measures 6.7:1. That is an
accepted trade. The accent is spent on links, small mono labels and one active
control at a time — never on running text — so AA is the bar that actually
applies to it, and the lift bought back the raised surfaces and hairlines that
were disappearing into the ground on OLED displays.

`faint` is the one token that needs care: it is intended for mono keys and
metadata at small-but-not-tiny sizes, never for prose. If a block of text needs
to be quiet, use `muted`.

## Runner-up: Bone & Rust

Kept on file as the strongest alternative — a light, editorial direction that
would flatter a photography page far more than any dark ground.

| Role | Hex |
| :--- | :--- |
| Ground | `#f5f3ee` |
| Raised | `#ffffff` |
| Surface | `#ebe7de` |
| Hairline | `#dbd6cb` |
| Heading | `#1b1a17` |
| Body | `#4b4842` |
| Muted | `#6f6b62` |
| Faint | `#98938a` |
| Accent | `#b0472b` |

Adopting it would mean re-tuning the hero flock, the project promo artwork, and
the navigation tint for a light ground — roughly a day's work, not a token swap.
The other three candidates considered are documented in
[`../research/palette-study.md`](../research/palette-study.md).

## Changing the palette

Both the site and this repo read from the same values, so:

1. Update the table above and the files in [`../tokens/`](../tokens/).
2. Update `src/styles/global.css` in `guilyx/v4` (the `@theme` block).
3. Regenerate: `public/favicon.svg`, the `theme-color` meta tag, and the
   project promo artwork under `src/assets/projects/`.

The hero flock reads `--color-agent` at runtime, so it follows automatically.
