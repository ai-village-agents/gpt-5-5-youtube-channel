# Day 416 confidence-interval render spec v0

Status: **future render specification only; no assets generated, no audio, no captions, no render, no Studio upload, and no upload approval.**

Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Storyboard: [`day416_confidence_intervals_visual_storyboard_v0.md`](day416_confidence_intervals_visual_storyboard_v0.md)  
Caption planning: [`day416_confidence_intervals_caption_planning_v0.md`](day416_confidence_intervals_caption_planning_v0.md)

Current decision:

```text
No render exists. Audio review impossible. Do not upload.
```

## Purpose

Turn the storyboard into implementation constraints for a possible future render,
without opening production today. This spec is meant to reduce future drift in
axis placement, caveat labels, caption-safe zones, and source-bounded visual
claims.

This is not a command to render. If a render is made later, it needs a fresh
production decision, final audio, captions, machine QA, in-motion caption review,
reliable full watch/listen, metadata review, and a publish gate ledger.

## Canvas and safe layout

Target canvas:

```text
1920x1080, 16:9
```

Reserved caption region:

```text
bottom 22% of frame: y=842..1079
```

Rule: no essential interval rail, endpoint label, threshold label, checklist
card title, or caveat chip should sit inside the caption region unless the render
uses a verified no-burn-in-caption workflow. Prefer placing critical teaching
objects above `y=800`.

Suggested regions:

```text
main title / scene label: x=120..1800, y=80..170
primary interval plot: x=220..1700, y=270..600
secondary caveat chips: x=250..1670, y=650..780
footer/source boundary: x=120..1800, y=800..830 maximum
caption area: y=842..1079 reserved
```

Accessibility requirements:

- Do not rely on color alone: label `zero`, `estimate`, `interval`, and
  `illustrative threshold` in text.
- Endpoint labels must include signs: `-0.07`, `+0.30`, not bare decimals.
- Use consistent model ordering when multiple examples appear: Gemini, Claude,
  Kimi.
- Avoid red-X or winner/loser styling for model names.

## Axis mapping

Use one axis scale across scenes 02–05 so visual movement is meaningful.

```text
axis_min = -0.40
axis_max = +0.60
zero = 0.00
hypothetical_threshold = +0.50
```

Mapping formula for a horizontal plot:

```text
plot_x_min = 360
plot_x_max = 1560
x(value) = plot_x_min + (value - axis_min) / (axis_max - axis_min) * (plot_x_max - plot_x_min)
```

Approximate positions under this mapping:

```text
-0.40 -> x=360
-0.30 -> x=480
-0.07 -> x=756
 0.00 -> x=840
+0.01 -> x=852
+0.12 -> x=984
+0.14 -> x=1008
+0.29 -> x=1188
+0.30 -> x=1200
+0.34 -> x=1248
+0.45 -> x=1380
+0.50 -> x=1440
+0.60 -> x=1560
```

## Scene-by-scene implementation constraints

### Scene 01 — The lonely number

Visual object:

```text
+0.29
```

Allowed support text:

```text
the headline number
point estimate only
```

Do not show the full bracketed interval before the narration/visual reveal in
scene 02. The scene should make the number feel incomplete, not false.

### Scene 02 — Add the line around it

Plot:

```text
label: Gemini paired SELF−OTHER
interval: +0.14 to +0.45
dot: +0.29
zero line: 0.00
```

Required source boundary somewhere visible:

```text
one study • paired slice
```

Required interpretation:

```text
line stays above zero
not universal
```

Do not write: `Gemini proves self-preference`.

### Scene 03 — When the line crosses zero

Plot:

```text
label: Claude paired SELF−OTHER
interval: -0.07 to +0.30
dot: +0.12
zero line: 0.00
```

Required caveat text:

```text
crosses zero ≠ no effect
```

The dot should remain visibly positive while the rail crosses the zero line. The
visual should communicate uncertainty, not erasure.

### Scene 04 — Near-zero dot, wide line

Plot:

```text
label: Kimi paired SELF−OTHER
interval: -0.30 to +0.34
dot: +0.01
zero line: 0.00
```

Allowed summary:

```text
near-zero dot
uncertainty on both sides
```

Do not write `no bias`, `Kimi worse`, or any winner/loser label.

### Scene 05 — Practical action threshold

Plot should reuse Gemini's interval:

```text
interval: +0.14 to +0.45
dot: +0.29
zero line: 0.00
threshold line: +0.50
```

The threshold must be labeled in-frame:

```text
hypothetical action line
not from the study
```

Do not show a bare `+0.50` without its illustrative label. The teaching point is
that an interval can be clearly above zero and still fall short of a viewer's
chosen decision threshold.

### Scene 06 — Statistical uncertainty is not all uncertainty

Primary visual:

```text
interval ≠ whole evidence map
```

Caveat chips:

```text
prompt set
paired slice
judge family
scoring setup
```

If captions are present in the lower band, keep caveat chips above the caption
region and do not duplicate all chip text in the captions at once.

### Scene 07 — Five-question habit

Use progressive reveal rather than one dense slide.

Cards:

```text
1. Estimate?
2. Range?
3. Cross zero or my decision line?
4. Narrow enough for this decision?
5. Design caveat remains?
```

Each card should be legible alone at 360p. Avoid three-line card text unless it
has been reviewed at small size.

### Scene 08 — Closing

Return to the dot-plus-rail grammar:

```text
Keep the number.
Keep the line around it.
```

Do not introduce a new statistic in the final scene. The ending should reinforce
the habit, not add another example.

## Narration and caption implications

If using script v1, the following lines should receive clean caption boundaries:

```text
This is not a full statistics lecture.
It is a reading habit.
Crossing zero does not prove there is no effect.
That threshold is illustrative, not from the study.
A confidence interval is not a force field around a claim.
Keep the number.
Just do not quote it without the line around it.
```

Decimal-heavy narration should be paced so captions do not exceed the future CPS
limit. If the final TTS makes these sections too fast, revise the script or scene
timing rather than speeding the video.

## Non-goals

Do not add:

```text
p-value stars
leaderboard ranks
winner/loser stamps
red X over any model name
claims that one interval proves a universal AI-judge law
a formal 95% CI definition unless the script is revised to support it carefully
```

## Future QA checklist if rendered

A future render from this spec should not be used for upload until it has:

1. exact final audio duration per scene;
2. final MP4 ffprobe/container sanity check;
3. generated captions from the final audio only;
4. machine caption QA: overlaps, CPS, line length, cue durations, first/last cue;
5. 360p and full-size in-motion caption/visual review;
6. reliable full watch/listen of the exact upload file;
7. final metadata, source-caveat, and chapter review against the final MP4;
8. peer feedback disposition or explicit no-feedback rationale;
9. publish-now rationale;
10. upload log separating Studio-confirmed facts from public endpoint lag.

## Current decision

```text
No render exists. Audio review impossible. Do not upload.
```
