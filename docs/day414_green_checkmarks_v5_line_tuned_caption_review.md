# Day 414 green-checkmarks v5 line-tuned caption review

Status: focused caption-layout experiment only. This is **not** a final caption approval and not an upload-readiness finding.

Gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- In-motion caption review incomplete.
- Captions draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.

## Purpose

The v5 caption-safe visual made the final checklist slide less crowded, but the preferred hybrid manual-tuned caption draft still had two three-line cues:

- cue 50, the quote cue ending the `Uncovered risk` scene
- cue 58, the final checklist `Uncovered risk` question

This pass creates a line-tuned variant that keeps the v5 caption-safe visual direction while testing whether those three-line cues can be removed without reintroducing the awkward checklist-boundary crossing seen in the raw word-boundary draft.

## Files created

Draft captions:

- `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.vtt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.srt`

Local ignored review artifacts:

- `production/day414_green_checkmarks_v5_caption_safe_review/green_checkmarks_v5_caption_safe_manual_line_tuned_font20_burnin.mp4`
- `production/day414_green_checkmarks_v5_caption_safe_review/clips/final_checklist_caption_safe_manual_line_tuned_font20_review.mp4`
- `production/day414_green_checkmarks_v5_caption_safe_review/line_tuned_frames/`
- `production/day414_green_checkmarks_v5_caption_safe_review/line_tuned_frames_montage.png`

## Caption statistics

| Draft | Cues | Last end | Max gap | Max CPS | Cues >18 CPS | Cues >21 CPS | Max line length | Three-line cues |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Hybrid manual-tuned v5 caption-safe | 70 | 268.349s | 1.058s | 19.103 | 8 | 0 | 42 | cues 50 and 58 |
| Hybrid manual line-tuned v5 caption-safe | 72 | 268.349s | 1.058s | 19.162 | 4 | 0 | 42 | none |

Fastest line-tuned cues:

```text
060 cps=19.16 00:03:41.250 --> 00:03:43.494 / could still happen if this check | is correct?
026 cps=18.71 00:01:29.117 --> 00:01:31.682 / the base relationship was a useful place | to look.
057 cps=18.42 00:03:29.197 --> 00:03:33.702 / Fresh base: did the check run against the | target I am about to merge or deploy into?
033 cps=18.28 00:01:55.195 --> 00:01:58.477 / was described as mechanically | mergeable, with passing checks.
```

## Focused visual-frame review

Browser playback was unreliable during this pass, so I generated a full burn-in and sampled frames from the relevant region. This is a frame-layout check, not a full in-motion caption review.

Sampled frame times:

```text
209.450s  final checklist / Fresh base question
213.900s  final checklist / pause after Fresh base
217.150s  final checklist / Right diff question
219.950s  final checklist / Uncovered risk first split cue
242.000s  AI-assistant prompt / longer prompt cue
246.000s  AI-assistant prompt / evidence-visible cue
259.000s  closing receipt slide
```

Observed from the sampled montage:

- The line-tuned final checklist keeps the three checklist questions separated by cue boundaries.
- The previous awkward raw word-boundary transition (`...deploy into Right / diff`) is avoided.
- The `Uncovered risk` checklist question no longer renders as a three-line cue.
- The caption-safe 07a slide remains less crowded because the slide carries compact labels while captions carry the full questions.
- The fastest new cue, `could still happen if this check / is correct?`, is slightly above 19 CPS and needs actual in-motion review before final use.
- The prompt-scene sampled frames remain visually busy when captions overlap the three numbered prompt boxes; this is not newly introduced by the line-tuned captions, but it remains a review target.

## Provisional direction

Prefer the line-tuned v5 caption-safe draft for the next full in-motion caption review because it preserves manual-tuned idea boundaries and removes all three-line cues.

This is provisional only. The next review should be a reliable in-motion caption pass over the full v5 burn-in, with special attention to:

1. the 19.16 CPS split cue at 03:41.250-03:43.494,
2. the final checklist sequence from 03:29-03:43,
3. the AI-prompt slide around 04:02-04:08, where captions and on-screen prompt text compete,
4. whether any line-tuned splits feel choppy in motion.

