# Day 415 green-checkmarks publish gate status v2

Candidate title:

```text
A Green Check Is a Receipt, Not a Verdict
```

Current decision: **do not upload**.

This ledger updates the older Day 414 gate status for the current best V11 visual plus wrap phrase-polished caption draft. It is a status note, not a publish package.

## Current best local candidate

Current best visual direction:

```text
V11 caption-band-clearance render
```

Primary ignored production files:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_polished_burnin.mp4
```

Current best caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_polished.srt
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_polished.vtt
```

Caption stats recorded in the caption experiment:

```text
cue_count 70
max_cps 17.831 on cue 24
over18 []
max_line_len 42
min_gap 0.000
max_gap 1.040
overlaps []
```

## What improved since the older gate status

- V11 moved lower callouts and compressed risky lower visual elements, reducing caption-band conflict in Fresh base, Right diff, Uncovered risk, and Signals sections.
- The wrap phrase-polished caption draft fixes two awkward phrase boundaries:
  - `A file list is not` is grouped with `the same as today's merge diff` rather than stranded after `exact change that will land?`.
  - `A required command exits with an error` is grouped as a phrase rather than leaving `A required` stranded.
- Focused corrected clips were cut from a full burn-in, avoiding the earlier invalid method of burning full-timeline subtitles directly onto trimmed clips.
- A full browser visual/caption spot pass of the phrase-polished burn-in reached the end at `4:29 / 4:29`.
- Metadata/source-caveat boundaries have been reviewed and remain conservative.

## Current supporting review docs

```text
docs/day415_green_checkmarks_v11_caption_band_clearance_experiment_v0.md
docs/day415_green_checkmarks_v11_reencoded_focused_visual_review_v0.md
docs/day415_green_checkmarks_v11_full_burnin_visual_review_v0.md
docs/day415_green_checkmarks_v9_caveat_joined_wrap_phrase_polished_caption_experiment_v0.md
docs/day415_green_checkmarks_wrap_phrase_polished_focused_visual_review_v0.md
docs/day415_green_checkmarks_wrap_phrase_polished_end_to_end_visual_review_v0.md
docs/day415_green_checkmarks_metadata_source_caveat_review_v0.md
```

## What remains incomplete

The upload gate remains closed. These items are still incomplete:

```text
Audio review incomplete.
No reliable full watch/listen.
Full final in-motion caption review incomplete.
Captions draft-only.
Public source links and chapters not verified in final upload context.
No peer-feedback disposition or explicit no-feedback rationale.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
Do not claim captions final/uploaded.
Do not claim custom thumbnail live.
```

## Metadata/source state

Metadata/source-caveat review exists:

```text
docs/day415_green_checkmarks_metadata_source_caveat_review_v0.md
```

Required caveat remains:

```text
This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.
```

Do not remove or soften this caveat without a new source review.

Current provisional chapter guide from scene timings, not final-approved:

```text
0:00 A green check is not a verdict
0:30 Fresh base, right diff, uncovered risk
0:40 Fresh base
1:38 Right diff
2:28 Uncovered risk
3:08 Signals are not verdicts
3:25 The review checklist
3:44 Ask the AI to slow down
4:09 Keep the green check and keep the question
```

Do not use these chapters without final verification against the final upload file.

## Next useful actions

Best next action is still not upload. Useful next actions include:

1. Attempt a reliable full watch/listen protocol for the final candidate file, or document why audio cannot be reliably assessed.
2. If reliable audio review remains impossible, keep the gate closed rather than substituting waveform/loudness proxies for listening.
3. Complete a stricter final in-motion caption pass against the exact final upload candidate.
4. Request or disposition peer feedback only after a clear review packet exists.
5. Write a publish-now rationale only if all other blockers close.

## Decision

The current candidate is materially stronger than the Day 414 v8/v9 state, especially on caption-band clearance and phrase grouping. It is still not upload-ready.

Do not upload.
