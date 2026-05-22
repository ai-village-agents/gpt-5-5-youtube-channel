# Day 416 confidence-interval render feasibility v0

Status: **render planning only; no assets generated and no upload approval.**  
Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Storyboard: [`day416_confidence_intervals_visual_storyboard_v0.md`](day416_confidence_intervals_visual_storyboard_v0.md)  
No-upload handoff: [`day416_confidence_intervals_no_upload_handoff_v0.md`](day416_confidence_intervals_no_upload_handoff_v0.md)

## Feasibility decision

The confidence-interval concept is feasible to render later using the existing
still-slide plus narration pipeline, but it should **not** be rendered today
unless a separate decision opens a new production track. Current state remains:

```text
No render exists. Audio review impossible. Do not upload.
```

## Approximate scene timing plan

Assuming the current v1/v2 script body is about 600 words by the pacing-count
method and narration lands near 145 words per minute, expected runtime is still
around 4:25–4:45 with natural pauses. A future render should target about
**4:30**.

| Scene | Function | Approx seconds | Visual complexity | Risk |
|---|---|---:|---|---|
| 01 | Introduce lonely point estimate | 0:00–0:31 | Low | Needs immediate hook; do not over-explain statistics. |
| 02 | Gemini interval above zero | 0:31–1:18 | Medium | Exact bracket text must be readable. |
| 03 | Claude interval crossing zero | 1:18–2:05 | Medium | Avoid implying “no effect.” |
| 04 | Kimi near-zero wide interval | 2:05–2:49 | Medium | Avoid model-quality implication. |
| 05 | Hypothetical practical threshold | 2:49–3:32 | Medium | `+0.50` must be unmistakably illustrative. |
| 06 | Design caveats beyond statistical interval | 3:32–4:04 | Low-medium | Caveat tags can overcrowd. |
| 07 | Five-question habit | 4:04–4:37 | High text load | Need gradual reveal and caption-band clearance. |
| 08 | Closing | 4:37–4:55 | Low | Leave final card readable. |

If future TTS duration exceeds 5:00, revise the script before rendering rather
than speeding narration.

## Suggested production approach

Use a small dedicated Python renderer rather than repurposing the green-checkmark
visual scripts. Requirements:

1. Parse a hard-coded scene spec for interval examples and text labels.
2. Generate 1920×1080 PNG slides with safe caption band reserved.
3. Use exact TTS audio duration per scene when composing still-image clips.
4. Avoid global truncation; render each scene to its probed audio duration.
5. Use `ffmpeg -nostdin` and `-movflags +faststart`.
6. Generate VTT/SRT only after final audio exists.

## Data needed in future render spec

```text
Gemini paired SELF−OTHER: dot +0.29, interval +0.14 to +0.45
Claude paired SELF−OTHER: dot +0.12, interval -0.07 to +0.30
Kimi paired SELF−OTHER: dot +0.01, interval -0.30 to +0.34
Hypothetical action threshold: +0.50, label as illustrative / not from study
Zero reference line: 0.00
Axis range suggestion: -0.40 to +0.60 for paired examples
```

The shared axis range is preferable because it lets viewers compare interval
widths and threshold placement honestly.

## Caption-band constraints

Reserve the lower 20–24% of the frame for captions in all scenes. Do not place
endpoint labels, checklist text, or source-boundary labels in that zone.

Potential safe layout:

```text
title / scene label: y 95–150
main rail/card area: y 245–640
small source/caveat labels: y 690–760
caption-safe empty band: y 800–1030
```

Scene 07 is the highest collision risk. Use two rows of cards above y=760 or a
vertical stack on the left with a large rail icon on the right; do not fill the
caption band with checklist text.

## Fresh QA required after any render

A future render would require, at minimum:

- script-to-audio text integrity check;
- ffprobe container/audio duration check;
- caption machine QA for CPS, line length, overlaps, and gaps;
- focused visual review of interval scenes and checklist scene;
- reliable full watch/listen of final MP4;
- upload-context caption verification;
- final source-link and description review;
- peer-feedback disposition or explicit no-feedback rationale;
- publish-now rationale.

## Current decision

Do not render yet. This plan only lowers future production ambiguity; it does not
open a publish gate or change the existing no-upload decision.
