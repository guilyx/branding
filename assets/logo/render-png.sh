#!/usr/bin/env bash
# Render the brand SVGs to PNG.
#
# The PNGs in this directory are generated, never hand-drawn — run this after
# any change to the SVGs rather than editing the bitmaps.
#
# Requires: a Chromium with headless screenshot support, and python3 with
# Pillow (`pip install pillow`) for the crop step.
#
#   ./render-png.sh
#   CHROME=/usr/bin/chromium ./render-png.sh
#
# Why it renders large and crops: headless Chromium silently returns a fully
# blank image when the window is only a few dozen pixels across, which is
# exactly the size most of these assets want. So every asset is painted at the
# top-left of a comfortably large window and then cut back to size.
set -euo pipefail

CHROME="${CHROME:-$(command -v chromium || command -v chromium-browser || command -v google-chrome || true)}"
if [[ -z "$CHROME" || ! -x "$CHROME" ]]; then
  echo "error: no chromium found. Set CHROME=/path/to/chromium" >&2
  exit 1
fi
python3 -c "import PIL" 2>/dev/null || { echo "error: python3 with Pillow required (pip install pillow)" >&2; exit 1; }

cd "$(dirname "$0")"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# The canvas every asset is painted onto. Must comfortably exceed the widest
# asset (mark-lockup at 4x = 560 px) and stay clear of Chromium's small-window
# blank-capture behaviour.
CANVAS=700

# mark-mono.svg and mark-lockup.svg are authored with `currentColor` so they
# inherit from their host. A PNG cannot inherit, so they are baked at
# --color-heading. Reach for the SVG whenever the mark must take its context's
# colour.
MONO_COLOR="#e8eaf0"

# render <svg> <out.png> <width> <height> [color]
render() {
  local svg="$1" out="$2" w="$3" h="$4" color="${5:-}"
  local page="$tmp/page.html" raw="$tmp/raw.png"
  local body
  body="$(cat "$svg")"
  [[ -n "$color" ]] && body="${body//currentColor/$color}"

  cat >"$page" <<HTML
<!doctype html><meta charset="utf-8">
<style>
  html,body{margin:0;padding:0;background:transparent}
  svg{display:block;width:${w}px;height:${h}px}
</style>
$body
HTML

  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --default-background-color=00000000 \
    --window-size="${CANVAS},${CANVAS}" \
    --virtual-time-budget=2000 \
    --run-all-compositor-stages-before-draw \
    --screenshot="$raw" "file://$page" 2>/dev/null

  python3 -c "
from PIL import Image
im = Image.open('$raw').convert('RGBA').crop((0, 0, $w, $h))
if im.getextrema()[3][1] == 0:
    raise SystemExit('blank render: $out')
im.save('$out')
"
  echo "  $out  (${w}x${h})"
}

echo "mark-accent"
render mark-accent.svg mark-accent@1x.png 32 32
render mark-accent.svg mark-accent@2x.png 64 64
render mark-accent.svg mark-accent@4x.png 128 128

echo "mark-mono (baked $MONO_COLOR)"
render mark-mono.svg mark-mono@1x.png 32 32 "$MONO_COLOR"
render mark-mono.svg mark-mono@2x.png 64 64 "$MONO_COLOR"
render mark-mono.svg mark-mono@4x.png 128 128 "$MONO_COLOR"

echo "mark-lockup (baked $MONO_COLOR)"
render mark-lockup.svg mark-lockup@1x.png 140 32 "$MONO_COLOR"
render mark-lockup.svg mark-lockup@2x.png 280 64 "$MONO_COLOR"
render mark-lockup.svg mark-lockup@4x.png 560 128 "$MONO_COLOR"

echo "favicon"
for s in 16 32 48 180 512; do
  render favicon.svg "favicon-${s}.png" "$s" "$s"
done

echo "done"
