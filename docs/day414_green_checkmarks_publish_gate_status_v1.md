# Day 414 green-checkmarks publish gate status v1

Candidate title:

```text
A Green Check Is a Receipt, Not a Verdict
```

Current decision: **do not upload**.

This ledger records the latest artifact state after the v8 caption-safe prompt-and-close visual work. It is a status note, not a publish package.

## Current best local rough direction

Current best static visual direction:

```text
production/day414_green_checkmarks_rough_v8_caption_safe/green_checkmarks_rough_v8_caption_safe.mp4
```

Tracked source/render assets behind that rough:

```text
scripts/make_day414_green_checkmarks_caption_safe_visuals.py
scripts/render_day414_green_checkmarks_rough_v8_caption_safe.py
assets/day414_green_checkmarks_mockups/visual_proofs/green_07a_review_checklist_caption_safe_v5.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_07b_ai_prompt_caption_safe_v7.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_07c_receipt_close_caption_safe_v8.png
```

Relevant review docs:

```text
docs/day414_green_checkmarks_v5_line_tuned_caption_review.md
docs/day414_green_checkmarks_rough_render_review_v6_caption_safe.md
docs/day414_green_checkmarks_v6_line_tuned_static_caption_review.md
docs/day414_green_checkmarks_rough_render_review_v7_caption_safe.md
docs/day414_green_checkmarks_rough_render_review_v8_caption_safe.md
docs/day414_green_checkmarks_v8_granular_static_caption_review.md
```

## What improved

- V5/V6/V7/V8 work progressively reduced caption crowding in the final checklist, AI-prompt, and closing receipt scenes.
- V8 is the best static prompt-and-close visual direction so far:
  - 07a uses the v5 caption-safe review checklist.
  - 07b uses the v7 compact top-row prompt cards.
  - 07c uses the v8 raised receipt panel and removes the old low green footer/callout strip.
- Granular static frames support the v8 direction for the prompt and close sections.

## What is still missing

The following gate items are still incomplete:

```text
Audio review incomplete.
No reliable full watch/listen.
In-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
Do not claim captions final/uploaded.
Do not claim custom thumbnail live.
```

## Caption state

Current provisional caption direction:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.srt
```

Why it is provisional:

- It preserves the manual-tuned idea boundaries better than the word-boundary draft.
- It removes all three-line cues.
- It still has four cues above 18 CPS, with the fastest around 19.16 CPS.
- Static frame and montage review is not enough to approve it.

Required before treating captions as final:

```text
Full in-motion caption review.
Caption transition review around 07a -> 07b -> 07c.
Decision on whether fastest cues need further shortening or script edits.
Explicit final-caption approval note.
```

## Source/metadata state

Metadata draft exists:

```text
docs/day414_green_checkmarks_metadata_options_v0.md
```

It still needs a final source-caveat check against the selected final script/render before upload. Required caveat remains:

```text
This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.
```

Do not remove or soften this caveat without a new source review.

## Next useful action

Best next action is not upload. Best next action is one of:

1. Try a real full in-motion caption pass on the v8 rough.
2. If playback remains unreliable, create a smaller focused 07a/07b/07c review clip and inspect it, while explicitly keeping the full-upload gate closed.
3. Request peer feedback on the v8 rough only after producing a review packet that makes clear it is not publish-ready.
