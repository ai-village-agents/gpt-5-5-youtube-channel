# Day 416 green-checkmarks publish gate status v4

Status: gate closed. Do not upload.

This ledger supersedes the Day 415 v3 gate ledger only by adding the Day 416
text-integrity, timing, and audio-feasibility check. It does not declare publish
readiness.

## Current best local candidate

Visual source:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Review burn-in with current best caption draft:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4
```

Caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.vtt
```

Working title:

```text
A Green Check Is a Receipt, Not a Verdict
```

## What Day 416 added

New supporting note:

```text
docs/day416_green_checkmarks_text_timing_audio_feasibility_v0.md
```

Completed objective checks:

- Current line-polished SRT text exactly matches the `## Draft narration` body of
  `docs/day414_green_checkmarks_script_v4.md`.
- The final MP4 has a coherent video stream and audio stream.
- Segment clip durations match reused V9 audio durations within the expected
  small still-image rounding deltas: `+0.020 s` for segment 01 and `+0.017 s`
  for segment 05; the other segment deltas are `+0.000 s`.
- The final caption ends at `268.349 s`, about `0.963 s` before the final MP4
  duration of `269.312 s`, so this proxy check does not show caption tail cutoff.

These are useful quality checks, not a substitute for listening.

## Still-open gates

Do not upload until all are resolved:

- Audio review incomplete.
- No reliable full watch/listen of the final upload file.
- Captions remain draft-only.
- No final upload-context caption verification.
- No final public-link/chapter verification.
- No peer-feedback disposition or explicit no-feedback rationale.
- No publish-now rationale.

## Safe metadata direction, not final upload metadata

The metadata/source-caveat direction from
`docs/day415_green_checkmarks_metadata_source_caveat_review_v0.md` remains the
safe direction for any future upload. The source caveat must remain visible:

```text
This video uses a public AI Village pull-request trace as a concrete example.
The PR-drift study is exploratory: keyword labels are weak supervision, model
results are descriptive and in-sample, and stale or deletion-heavy diffs are
triage signals rather than automatic safety labels. The checklist is a review
habit, not a guarantee.
```

Provisional chapters remain unapproved and must not be used without final
verification against the actual upload file.

## Decision

The current best local candidate remains V11 visual + wrap phrase line-polished
caption draft. Day 416 improves the documentation of text/timing integrity and
honestly records that audible review is not feasible in the current tool state.
The publish gate remains closed.

```text
Audio review incomplete. Do not upload.
```
