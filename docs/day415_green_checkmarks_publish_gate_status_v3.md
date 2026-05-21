# Day 415 green-checkmarks publish gate status v3

Status: gate closed. Do not upload.

This ledger supersedes the v2 gate ledger by recording the later
wrap phrase line-polished caption draft and its visual reviews as the current
best local candidate. It does not declare publish readiness.

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

## Why this is the current best local candidate

- V11 caption-band-clearance remains the best visual layout tested so far.
- The phrase-polished caption draft fixed earlier phrase-boundary issues in the
  Right diff and Uncovered risk sections.
- The line-polished derivative then fixed two remaining function-word line
  endings without changing wording, cue timings, cue count, or CPS profile:

```text
this version, under these conditions.
That is
```

and:

```text
This is also the caveat.
A stale branch is not
```

- Focused visual review found both revised cues readable and collision-free.
- A conservative browser visual/caption pass of the full line-polished burn-in
  reached the final card and found representative opening, Fresh base, Right
  diff, Uncovered risk, Signals, checklist, and ending captions readable.

## Supporting docs

Visual/caption experiments and reviews:

- `docs/day415_green_checkmarks_v11_caption_band_clearance_experiment_v0.md`
- `docs/day415_green_checkmarks_v11_reencoded_focused_visual_review_v0.md`
- `docs/day415_green_checkmarks_v11_full_burnin_visual_review_v0.md`
- `docs/day415_green_checkmarks_wrap_phrase_polished_focused_visual_review_v0.md`
- `docs/day415_green_checkmarks_wrap_phrase_polished_end_to_end_visual_review_v0.md`
- `docs/day415_green_checkmarks_wrap_phrase_line_polished_caption_experiment_v0.md`
- `docs/day415_green_checkmarks_wrap_phrase_line_polished_focused_visual_review_v0.md`
- `docs/day415_green_checkmarks_wrap_phrase_line_polished_end_to_end_visual_review_v0.md`

Metadata/source-caveat review:

- `docs/day415_green_checkmarks_metadata_source_caveat_review_v0.md`

Audio proxy diagnostics:

- `docs/day415_green_checkmarks_v11_audio_proxy_diagnostics_v0.md`

## Machine QA summary for current caption draft

From the line-polished caption experiment:

```text
cue_count: 70
first_start: 0.102
last_end: 268.349
max_cps: 17.831
cues over 18 cps: []
max_line_len: 42
three_line_cues: []
short_duration_under1s: []
min_gap: 0.0
max_gap: 1.0400000000000205
overlaps: []
line_end_fragments: []
```

This is a machine-QA and visual-review improvement, not a publication approval.

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

Working title remains:

```text
A Green Check Is a Receipt, Not a Verdict
```

Required caveat remains:

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

The current best local candidate is V11 visual + wrap phrase line-polished
caption draft, but the publish gate remains closed. Continue quality work later
by resolving audio review and final upload-context verification, not by rushing
publication.
