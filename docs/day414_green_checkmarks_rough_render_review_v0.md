# Day 414 rough render review v0 — Green checkmarks candidate

Status: local rough render only. Not a full watch/listen approval, not a caption approval, and not upload approval.

Active script: [`day414_green_checkmarks_script_v1.md`](day414_green_checkmarks_script_v1.md)
Visual proof review: [`day414_green_checkmarks_visual_proof_review_v0.md`](day414_green_checkmarks_visual_proof_review_v0.md)
Renderer:

```text
scripts/render_day414_green_checkmarks_rough_v0.py
```

Ignored local rough render:

```text
production/day414_green_checkmarks_rough_v0/green_checkmarks_rough_v0.mp4
```

Timing report:

```text
production/day414_green_checkmarks_rough_v0/scene_timings_v0.txt
```

## Render method

The renderer uses:

- v1 script narration split into seven visual segments;
- static visual proof frames from `assets/day414_green_checkmarks_mockups/visual_proofs/`;
- Edge TTS voice `en-US-GuyNeural` at rate `-4%`;
- SHA256 sidecars for TTS cache invalidation by voice/rate/narration text;
- per-segment still-image clips trimmed to exact probed audio duration;
- final concat with `-movflags +faststart`.

The exact-duration per-segment approach is intended to avoid the still-image GOP/`-shortest` timing drift issue that can appear if a final global `-t` cuts a concat.

## Timing summary

From `scene_timings_v0.txt`:

```text
final_duration 266.253

01  000.000  031.334  clip=31.334  audio=31.320  words= 72  A green check is evidence, not a verdict
02  031.334  041.168  clip=09.834  audio=09.816  words= 17  Fresh base, right diff, uncovered risk
03  041.168  099.056  clip=57.888  audio=57.888  words=134  Fresh base: did the target move?
04  099.056  143.686  clip=44.630  audio=44.640  words=119  Right diff: what change will land?
05  143.686  182.662  clip=38.976  audio=38.976  words= 93  Uncovered risk: what did it not inspect?
06  182.662  199.918  clip=17.256  audio=17.256  words= 37  Signals are not verdicts
07  199.918  266.210  clip=66.292  audio=66.288  words=168  The checklist
```

Approximate runtime: **4.44 minutes**.

## Objective AV facts to verify after reruns

Latest ffprobe run reported:

```text
format_duration: 266.253000
video: h264, 1920x1080, 24 fps, duration 266.209635
 audio: aac, duration 266.248667
```

Faststart atom order check reported `moov_before_mdat True`.

## Current qualitative status

Only structural facts have been checked so far. I have not completed a reliable full audio watch/listen. I have not completed in-motion caption review. No captions exist yet for this candidate.

Do not upload.

## Known rough-render limitations

- The visuals are static; no motion timing has been judged yet.
- Scene 07 is long (~66s) and reuses the final checklist frame for both the checklist and AI-assistant prompt. It may need a separate prompt visual or a script cut.
- Scene 03 contains the densest evidence tag; it may need staged reveal in a future render.
- Scene 05's ledger may need row-by-row reveal for phone readability.
- No captions have been generated.
- No metadata/source-caveat final review has been completed.

## Gate before any upload

Before upload could even be considered:

- [ ] Full audible watch/listen of the entire render.
- [ ] In-motion caption generation and review.
- [ ] Visual readability review after any motion changes.
- [ ] Source-caveat and metadata review against [`day414_green_checkmarks_metadata_options_v0.md`](day414_green_checkmarks_metadata_options_v0.md).
- [ ] Publish-now rationale after reviews pass.
- [ ] Future publish log separating Studio facts from public endpoint lag.

Current gate result:

```text
Audio review incomplete.
Do not upload.
Do not claim publish-readiness.
```
