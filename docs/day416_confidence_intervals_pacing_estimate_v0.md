# Day 416 confidence-interval pacing estimate v0

Status: **script pacing estimate only; no audio generated, no captions generated, no render, no Studio upload, and no upload approval.**

Script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)

Current decision:

```text
No render exists. Audio review impossible. Do not upload.
```

## Purpose

Estimate scene density before any future text-to-speech or rendering work. This helps identify where pacing, caption load, and visual load may become tight.

This is not an audio review. No narration file exists, and no scene duration is final.

## Method

Words were counted from the body text under each `###` scene heading in script v1. Durations are simple estimates at 130, 145, and 160 words per minute, with no extra pause budget. Future TTS will need measured audio durations.

## Scene estimates

| Scene | Words | @130 wpm | @145 wpm | @160 wpm | Pacing note |
|---|---:|---:|---:|---:|---|
| 01 — The lonely number | 71 | 32.8s | 29.4s | 26.6s | comfortable |
| 02 — Put the line back | 101 | 46.6s | 41.8s | 37.9s | dense; protect visual/caption breathing room |
| 03 — If the line crosses zero | 89 | 41.1s | 36.8s | 33.4s | moderate-dense; avoid visual clutter |
| 04 — If the dot is near zero | 84 | 38.8s | 34.8s | 31.5s | moderate-dense; avoid visual clutter |
| 05 — Your decision line may be somewhere else | 89 | 41.1s | 36.8s | 33.4s | moderate-dense; avoid visual clutter |
| 06 — The interval is not the whole evidence map | 57 | 26.3s | 23.6s | 21.4s | comfortable |
| 07 — The five-question habit | 69 | 31.8s | 28.6s | 25.9s | comfortable |
| 08 — Closing | 38 | 17.5s | 15.7s | 14.2s | short; likely needs pause/hold time |

## Totals

Body narration words counted: **598**

- At 130 wpm without added pauses: **276.0s**
- At 145 wpm without added pauses: **247.4s**
- At 160 wpm without added pauses: **224.2s**

Practical expectation: with pauses for interval reveals, threshold labeling, and final-card hold time, script v1 likely wants roughly 4:30–5:10 rather than a compressed three-minute treatment.

## Scene-level cautions

- Scene 02 is the densest: it introduces paired slice, Gemini, point estimate, interval endpoints, confidence interval, dot, line, zero, and source scope. Let the visual carry bracket values and keep captions short.
- Scene 03 needs a pause after “But the line crosses zero” and after “Crossing zero does not prove there is no effect.”
- Scene 05 must keep “That threshold is illustrative, not from the study” close to the threshold visual.
- Scene 07 can become list-heavy; reveal the five questions progressively and avoid putting all of them on screen while dense captions are active.
- Scene 08 is short; hold the final card long enough for “Keep the number / keep the line around it” to register.

## Future use

If a future TTS pass makes any scene substantially faster than the @160 wpm estimate, revise timing or script rather than relying on fast captions. If total measured runtime exceeds about 5:15, cut repeated setup before speeding narration.

## Current decision

```text
No render exists. Audio review impossible. Do not upload.
```
