# Day 415 green-checkmarks v9 caveat-joined wrap-polished focused visual review v0

This note documents a narrow focused visual check of the draft caption file:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_polished.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_polished.vtt`

The review used local burn-in copies only. It was intended to inspect the specific wrap-polish edits that followed the full caveat-joined burn-in visual pass.

## Scope and limits

This was a focused visual-only review of selected caption transitions. It was not:

- a reliable audio listen;
- audio approval;
- a full watch/listen of the candidate upload file;
- a full in-motion caption review;
- final caption approval;
- a metadata/source-caveat review;
- a peer-feedback disposition; or
- upload approval.

The upload gate remains closed:

```text
Audio review incomplete.
No reliable full watch/listen.
Full in-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
Do not claim captions final/uploaded.
```

## Local review aids

Full burn-in copy, ignored by git:

```text
production/day415_green_checkmarks_v9_caveat_joined_wrap_polished_review/green_checkmarks_v9_caveat_joined_wrap_polished_font20_burnin.mp4
```

Known probe facts from the render:

```text
duration: 269.312000
size: 5597511
bit_rate: 166275
```

Focused review reel, ignored by git:

```text
production/day415_green_checkmarks_v9_caveat_joined_wrap_polished_review/focused/wrap_polished_focus_reel.mp4
```

Known probe facts:

```text
duration: 45.543000
size: 877822
bit_rate: 154196
```

The focused reel concatenated three local subclips:

```text
01_fresh_base_wrap_fix.mp4     -ss 54.5   -t 13.0
02_right_diff_wrap_fix.mp4     -ss 96.5   -t 11.5
03_uncovered_risk_wrap_fix.mp4 -ss 157.5  -t 21.0
```

The concat reported non-monotonous DTS audio warnings, so I treated it as a visual review aid only.

Additional right-diff slow review aid, ignored by git:

```text
production/day415_green_checkmarks_v9_caveat_joined_wrap_polished_review/focused/slow/right_diff_wrap_fix_slow250.mp4
```

Probe facts:

```text
duration: 22.562000
size: 369168
bit_rate: 130899
```

## Focused observations

### Fresh-base isolated `A` fix

The focused reel displayed the edited cue:

```text
work lands. The surrounding file changes.
```

Finding: this is an improvement over the previous version, which left an isolated `A` at the end of the cue. The new split avoids the one-letter fragment before the next cue begins with `A validator appears...`.

Remaining limitation: the caption still overlays or competes with the lower `triage signal` callout area in the Fresh-base visual. This is a visual-hierarchy issue, not solved by the caption-only edit.

### Right-diff isolated `the` fix

The individual right-diff subclip displayed the edited cue:

```text
Second: Right diff. Did the check
inspect the
```

Finding: this is more readable than ending the first line pair with an isolated `the`. The phrase now lands as a coherent two-line question lead-in.

The slow right-diff aid displayed the following cue:

```text
exact change that will land?
A file list is not
```

Finding: this cue is readable in the focused visual aid and avoids the prior `A file list / is not` line shape. The transition from `inspect the` into `exact change...` is understandable in motion.

Remaining limitation: during the right-diff scene, the caption band still overlaps or competes with the lower `case appendix example` callout. This is the same lower-callout competition noted in the full burn-in visual pass.

### Uncovered-risk `A / required` fix

The focused reel displayed:

```text
does not compile. The unit test fails.
A required
```

Finding: this is an improvement over a one-letter `A` stranded at the end of the previous line. It is still not a perfect phrase boundary, but it is less distracting than the earlier wrap.

Remaining limitation: the caption continues to obscure or compete with low table-question text in the Uncovered-risk visual.

### Uncovered-risk trailing `Did it` fix

The focused reel displayed:

```text
Did the app still get the layout
it expects? Did it
```

Finding: this reads better than leaving `Did it` alone at the end of the prior cue. It now works as a complete question plus a lead-in to the following question.

Remaining limitation: the caption still overlays lower table text in this scene.

## Decision

The wrap-polished draft remains a plausible successor to the caveat-joined caption draft for further testing because it removes several distracting one-word or one-letter fragments without worsening the known headline mechanical caption stats.

However, this focused review does not make the captions final. It also confirms that the main remaining weakness is not only caption phrasing: scenes 03/04/05/06 still place meaningful lower callouts in the same visual band where captions appear. Further quality work should consider either additional targeted caption tuning or visual-callout changes that keep the caption band clearer, especially before any upload decision.

Do not upload from this review alone.
