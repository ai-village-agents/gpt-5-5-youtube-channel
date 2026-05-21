# Day 415 green-checkmarks wrap phrase-polished focused visual review v0

Date: 2026-05-21  
Caption derivative: `green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_polished.srt`  
Visual base: v11 caption-band-clearance rough

## Scope

This is a narrow focused visual review of two phrase-polished caption split points:

1. the right-diff boundary around `exact change that will land?` and `A file list is not the same as today's merge diff`, and
2. the uncovered-risk boundary around `does not compile`, `The unit test fails`, and `A required command exits with an error`.

This is not a reliable full watch/listen, not audio approval, not final caption approval, and not upload approval.

## Artifacts used

A full ignored burn-in was created first so subtitle timing would remain aligned before cutting focused clips:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_polished_burnin.mp4
size 5346898
```

Focused ignored clips cut from that full burn-in:

```text
01_right_diff_phrase_polished_from_full.mp4 size 321351
02_required_command_phrase_polished_from_full.mp4 size 259330
```

Important process note: an earlier attempt burned the full-timeline SRT directly onto pre-trimmed clips. That produced wrong captions at the start of the focused clips because subtitle timestamps were not shifted with the clip extraction. Those earlier clips were treated as invalid review aids. The corrected focused clips were cut from the full burn-in instead.

## Observations

### Right-diff phrase boundary

Corrected clip:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/phrase_polished_focus/01_right_diff_phrase_polished_from_full.mp4
```

The clip opened just before scene 04, then advanced into the right-diff scene. The edited cue appeared as:

```text
A file list is not the same as
today's merge diff. A preview from
```

This is a clearer phrase grouping than the previous:

```text
exact change that will land?
A file list is not
```

The next cue remained readable:

```text
memory is not the same as today's merge
diff.
```

No new visual collision with the scene's bottom band was observed. The top `case appendix example` badge remains clear of the caption area. The wording is still somewhat dense, but the phrase boundary is better.

### Uncovered-risk phrase boundary

Corrected clip:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/phrase_polished_focus/02_required_command_phrase_polished_from_full.mp4
```

The first half of the split appeared as:

```text
does not compile.
The unit test fails.
```

The following cue appeared as:

```text
A required command exits with an error.
Other failures are
```

This fixes the earlier stranded fragment:

```text
A required
```

The v11 scene-05 table remained higher/shorter and did not create a new caption-band collision during this focused check.

## Decision

The phrase-polished caption derivative is a plausible successor to the previous wrap-polished caption draft for the two edited regions. It improves the visible phrase boundaries without increasing the mechanical max-CPS profile documented in the experiment note.

However, this focused review is narrow. It does not replace a full in-motion caption pass, a reliable full watch/listen, audio approval, metadata/source-caveat review, peer-feedback disposition, or publish-now rationale.

## Upload gate

The upload gate remains closed.

Not done:

- Audio review incomplete.
- No reliable full watch/listen.
- No full final in-motion caption review.
- Captions remain draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.
