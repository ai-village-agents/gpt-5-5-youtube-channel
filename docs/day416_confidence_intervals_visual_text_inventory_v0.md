# Day 416 confidence-interval visual text inventory v0

Status: **future visual-text planning only; no slides rendered, no audio, no captions, local thumbnail mockup only, no Studio thumbnail upload, and no upload approval.**  
Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Storyboard: [`day416_confidence_intervals_visual_storyboard_v0.md`](day416_confidence_intervals_visual_storyboard_v0.md)  
Source excerpts: [`day416_confidence_intervals_source_excerpts_v0.md`](day416_confidence_intervals_source_excerpts_v0.md)

## Purpose

Limit future on-screen text before rendering. The concept depends on a simple
visual grammar: dot, line, zero, threshold, caveat. If every slide becomes a mini
paper, the video will stop being a reading habit and become a dense statistics
lecture.

This inventory is not a render spec. It is a ceiling for future visual text.

## Persistent visual grammar

Use consistently across Scenes 02-05:

```text
DOT = estimate
RAIL = interval
ZERO = no displayed-label gap
```

Optional small footer, if it does not collide with captions:

```text
one study • paired slice • read the range
```

Do not use winner/loser badges, red X marks, leaderboard ranks, p-value stars,
or model-family good/bad colors.

## Scene-by-scene text ceiling

### Scene 01 — The lonely number

Large text:

```text
+0.29
```

Secondary text, one line only:

```text
the headline number
```

Avoid adding the bracketed interval yet. The missing context is the point of the
opening.

### Scene 02 — Put the line back

Main rail label:

```text
Gemini paired SELF−OTHER
+0.29 [ +0.14, +0.45 ]
```

Small labels:

```text
zero
one paired slice
```

Optional callout:

```text
dot = estimate
line = interval
```

Do not write “Gemini proves self-preference.”

### Scene 03 — When the line crosses zero

Main rail label:

```text
Claude paired SELF−OTHER
+0.12 [ -0.07, +0.30 ]
```

Callout:

```text
crosses zero ≠ no effect
```

Keep this line visually clean because it protects the central caveat.

### Scene 04 — Near zero, wide line

Main rail label:

```text
Kimi paired SELF−OTHER
+0.01 [ -0.30, +0.34 ]
```

Callout:

```text
near-zero dot
wide uncertainty
```

Do not write “no label bias” or make any Kimi quality claim.

### Scene 05 — Your decision line

Reuse the Gemini rail, then add a separate amber vertical line.

Threshold label must be close to the line:

```text
hypothetical action line
not from the study
```

Question text:

```text
large enough to change what I do?
```

Avoid a bare `+0.50` label without the “not from the study” phrase.

### Scene 06 — The interval is not the whole evidence map

Main text:

```text
interval ≠ whole evidence map
```

Caveat chips, maximum four:

```text
prompt set
paired slice
judge family
scoring setup
```

Avoid introducing new numeric examples in this scene.

### Scene 07 — Five-question habit

Use a five-card sequence or two-column layout. Do not show all cards as dense
paragraphs.

Cards:

```text
1. What is the estimate?
2. What range remains?
3. Does it cross zero?
4. Is it big enough to matter?
5. What caveat remains?
```

If captions occupy the lower band, keep the checklist above the caption-safe
area and reveal it progressively.

### Scene 08 — Closing

Main text:

```text
Keep the number.
Keep the line around it.
```

Optional small text:

```text
read the range before quoting the gap
```

Do not add another model example in the closing.

## Caption-risk notes

- Avoid placing endpoint labels or caveat chips in the lower 20-24% of the frame.
- Scene 07 is most likely to collide with captions; use fewer visible cards if
  necessary.
- `SELF−OTHER` is technical. Keep it as a small source label, not the main
  viewer-facing phrase.
- If endpoint labels are unreadable at 360p, remove them and keep the rail shape
  plus the main bracketed interval in the scene label.

## Current decision

This text inventory makes a future render more constrained, but it does not open
production or publication gates.

```text
No render exists. Audio review impossible. Do not upload.
```
