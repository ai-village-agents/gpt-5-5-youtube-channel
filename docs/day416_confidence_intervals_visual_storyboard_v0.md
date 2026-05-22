# Day 416 confidence-interval visual storyboard v0

Status: **visual planning only; no assets rendered, no audio, no captions, and no upload approval.**  
Script basis: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Source map: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)

## Visual principle

The video should teach one reusable visual grammar:

```text
point estimate = dot
confidence interval = horizontal rail
zero reference = vertical line
practical action threshold = second vertical line, clearly labeled illustrative
source boundary = small label such as "one paired slice / one study"
```

Avoid dense tables. Let the same rail motif become more informative across the
video.

## Palette and layout

Use a calm dark technical palette consistent with the channel's recent visual
style, but make the interval rail high-contrast and uncluttered.

```text
background: #10131a or #111827
panel: #151923
text: #f4f1ea
muted text: #b9c0cf
positive rail/dot: #86efac
uncertainty rail: #7dd3fc
zero line: #f4f1ea at 55% opacity
practical threshold: #fbbf24
caveat tags: #2b3445 panels with #b9c0cf text
warning/caution accent: #f59e0b
```

Suggested persistent lower label, small and unobtrusive:

```text
one study • paired slice • confidence interval as reading aid
```

## Scene-by-scene storyboard

| Scene | Main visual | Motion | On-screen text | Caption/readability risk |
|---|---|---|---|---|
| 01 — The lonely number | Large centered card with `+0.29` and tiny label `reported gap`. Empty space around it. | Card fades in alone; background grid barely visible. | `+0.29` / `reported gap` / later: `a headline, not the whole result` | Keep subtitle band clear; do not put bottom label below safe caption area. |
| 02 — Put the line back | Same `+0.29` becomes a dot on a rail from `+0.14` to `+0.45`; zero line left of rail. | Rail draws outward from dot; endpoint labels appear after the rail. | `Gemini paired SELF−OTHER` / `+0.29 [ +0.14, +0.45 ]` / `one paired slice` | Exact bracket text is dense; use large type and avoid extra table columns. |
| 03 — If the line crosses zero | Claude rail from `−0.07` to `+0.30`, dot at `+0.12`, zero line intersects rail. | Previous rail slides upward into comparison slot; Claude rail draws below it. Zero line pulses once. | `Claude paired SELF−OTHER` / `+0.12 [ −0.07, +0.30 ]` / `crosses zero ≠ no effect` | The caveat line must not look like a verdict; use muted/caution styling. |
| 04 — If the dot is near zero | Kimi rail from `−0.30` to `+0.34`, dot near zero. | Dot appears first near zero; rail expands wide on both sides. | `Kimi paired SELF−OTHER` / `+0.01 [ −0.30, +0.34 ]` / `near-zero dot • uncertainty both sides` | Avoid visual implying Kimi is bad; no red X, no downward quality icon. |
| 05 — Your decision line may be somewhere else | Return to Gemini rail; add amber vertical line at `+0.50` outside interval. | Threshold line slides in after narration says “illustrative.” | `hypothetical action threshold` / `+0.50` / `statistical direction ≠ practical decision` | The threshold must be visibly labeled hypothetical, not study-derived. |
| 06 — The interval is not the whole evidence map | Interval card stays center; three small caveat tags orbit/stack: `prompt set`, `paired slice`, `judge family`, plus optional `decision context`. | Tags appear one at a time; rail remains visible but slightly dimmed. | `intervals do not erase design questions` | Do not overcrowd; four tags max. |
| 07 — The five-question habit | Five checklist cards, revealed one by one, each with a tiny rail icon. | Cards stack vertically or 2+3 grid, timed to narration. | `1 point estimate` / `2 plausible range` / `3 zero or threshold?` / `4 narrow enough?` / `5 design caveat?` | This is the densest scene; use short labels, not full question text, if captions are on. |
| 08 — Closing | Return to original `+0.29` card; attach rail; final composition is number plus line. | Lonely number fades into full dot-and-rail graphic; final line locks. | `Keep the number.` / `Keep the line around it.` | Leave final card on screen long enough for reading after narration. |

## Accessibility / comprehension checks for future render

- Every interval should be understandable without color alone: dot, rail,
  endpoint labels, and zero line must differ by shape/position, not just hue.
- Endpoint labels should use `−` and `+` signs consistently; if fonts render
  minus poorly, use hyphen-minus only after visual inspection.
- If the spoken narration rounds a value, the visual can carry the exact bracket
  value, but the mismatch must not look like an error.
- The phrase `SELF−OTHER` is technical; keep the small label but let narration
  explain only “displayed-self-label gap.”
- Avoid three-line captions over the checklist scene; the visual already carries
  text load.

## Non-goals

- Do not animate a statistical distribution unless the script is revised to
  explain it; the current lesson is dot/rail reading, not sampling theory.
- Do not show a fake p-value, significance star, or verdict stamp.
- Do not use red/green good-bad coding for model families.
- Do not make the `+0.50` practical threshold look like a study finding.

## Current decision

This storyboard makes v1 easier to render later, but no production gate is open.
Before any render, make a fresh render plan, generate captions, perform full
motion/caption/audio review, collect or disposition peer feedback, and write a
publish-now rationale. Do not upload from this storyboard.
