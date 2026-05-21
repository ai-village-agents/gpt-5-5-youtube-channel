# Day 415 green-checkmarks v11 caption-band clearance experiment v0

## Status

This is a narrow follow-up visual experiment after the v10 caption-band polish. It is not upload approval.

The upload gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions are still draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition for this candidate.
- No publish-now rationale.
- Do not upload from this experiment.

## Why v11 exists

The v10 caption-band experiment improved the earlier lower-callout conflicts by moving scene 03-06 callouts away from the bottom of the frame. The focused v10 visual check still found two remaining clearance concerns:

1. Scene 05, `Uncovered risk`: the large table still reached close to the lower captions.
2. Scene 06, `Signals`: the lowest `green check` row still sat near the caption area.

The v11 experiment preserves the v10 direction but gives scenes 05 and 06 more bottom clearance.

## Source changes under review

New generator:

```text
scripts/make_day415_green_checkmarks_caption_band_v11_clearance_visuals.py
```

New local renderer:

```text
scripts/render_day415_green_checkmarks_rough_v11_caption_band_clearance.py
```

New source visual assets:

```text
assets/day414_green_checkmarks_mockups/visual_proofs/green_03_fresh_base_caption_band_v11.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_03_fresh_base_caption_band_v11_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_04_right_diff_caption_band_v11.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_04_right_diff_caption_band_v11_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_05_uncovered_risk_caption_band_v11.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_05_uncovered_risk_caption_band_v11_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_06_signals_not_verdicts_caption_band_v11.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_06_signals_not_verdicts_caption_band_v11_360p.png
assets/day414_green_checkmarks_mockups/green_checkmarks_caption_band_v11_clearance_contact_sheet.png
```

## Visual changes from v10

Scenes 03 and 04 keep the v10 layout direction, with v11 labels and filenames.

Scene 05, Uncovered risk:

- The `Checked` / `Still ask` table is shorter and placed higher.
- Row spacing is reduced.
- The bottom of the table is farther from the caption baseline.
- The top question badge remains:
  ```text
  What would still worry me if the robot is right?
  ```

Scene 06, Signals:

- The three signal rows are shorter.
- Vertical spacing between rows is reduced.
- The lowest `green check` row is farther from the caption baseline.
- The top badge remains:
  ```text
  Signals are not verdicts in either direction.
  ```

## Local render facts

Local rough output, ignored by git:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Observed `ffprobe` facts:

```text
duration 269.312000
size 5147769
bit_rate 152916
```

Local wrap-polished burn-in review copy, ignored by git:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_polished_burnin.mp4
```

Observed `ffprobe` facts:

```text
duration 269.312000
size 5532053
bit_rate 164331
```

## Focused visual check

I reviewed individual v11 burn-in subclips in Firefox. These subclips are ignored local review aids, not candidate upload files.

Reviewed paths:

```text
production/day415_green_checkmarks_rough_v11_caption_band/focused/03_uncovered_risk.mp4
production/day415_green_checkmarks_rough_v11_caption_band/focused/04_signals.mp4
```

Note: these focused subclips were created before the renderer output path was renamed to include `clearance`; they use the same v11 visual source assets and wrap-polished caption burn-in. Because they were made with stream-copy seeking, the Signals subclip briefly displayed a stale earlier keyframe before advancing into the Signals scene. This is another reason to treat them only as visual aids.

Focused observations:

- Scene 05, Uncovered risk: the shorter/higher table materially improves bottom clearance. The problematic region around captions such as:
  ```text
  about meaning. Did this remove recent
  work?
  ```
  and:
  ```text
  or a hidden invariant? The most useful
  question
  ```
  looked cleaner than v10 because the visual table no longer presses as close to the caption band.
- Scene 06, Signals: after the stale copied frame advanced, the shorter rows provided more breathing room below the `green check` row. The caption:
  ```text
  automatically enough. Each of those is a
  signal, not a verdict.
  ```
  still sits in the lower frame, but the row above it no longer feels as close as v10.

## Decision

The v11 clearance direction looks like a better visual successor to v10 for scenes 05 and 06. It is worth preserving as source work.

This does not establish final caption status or video readiness. A reliable full watch/listen, full in-motion caption review, final metadata/source-caveat review, and peer-feedback disposition remain undone. Gate remains closed.
