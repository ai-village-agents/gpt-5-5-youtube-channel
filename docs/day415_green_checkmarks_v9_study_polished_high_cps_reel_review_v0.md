# Day 415 — Green-checkmarks v9 study-polished high-CPS focused review (v0)

## Scope

This note records a narrow focused review of high-CPS / dense caption regions for the current study-polished caption experiment:

- Caption draft: `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished.srt`
- Base video: `production/day414_green_checkmarks_rough_v9_caption_safe/green_checkmarks_rough_v9_caption_safe.mp4`
- Burn-in review file: `production/day415_green_checkmarks_v9_study_polished_caption_review/green_checkmarks_v9_study_polished_font20_burnin.mp4`

This was **not** a full-video watch/listen. It was **not** a full in-motion caption review. It was **not** audio approval and it does **not** make the video upload-ready. The captions remain draft-only.

## Review aids used

Ignored local review aids included:

- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/high_cps_reel/study_polished_high_cps_review_reel.mp4`
  - ffprobe format duration `61.543000`, size `1,383,488`, bit rate `179,840`
  - Created from four short segments around high-CPS/dense regions. ffmpeg reported non-monotonous DTS warnings during concat, but Firefox played the output.
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/study_polished_final_caveat_slow_micro.mp4`
  - ffprobe format duration `13.709000`, size `429,034`, bit rate `250,366`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/high_cps_reel/03_user_visible_wording.mp4`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/high_cps_reel/slow_aids/03_user_visible_wording_slow150.mp4`
  - ffprobe format duration `14.259000`, size `320,683`, bit rate `179,918`

The ignored MP4 review aids should not be committed.

## Proxy high-CPS cues checked

The space-including proxy list motivating this pass was:

```text
14  16.758  In a fast-moving repo, the target branch / can move
24  17.407  It does mean the base relationship was
25  17.774  a useful place to look.
47  17.103  change permissions, ordering, user-visible / wording,
57  17.297  Right diff: did it inspect the exact / change that will land?
58  16.522  Uncovered risk: what important failure
66  17.143  so the evidence stays visible.
```

A previous no-space CPS script did not flag cues above 17 CPS; this note keeps the space-including proxy for continuity with the earlier review notes.

## Observations

### Fresh-base study paragraph / base-relationship caveat

The high-CPS reel and slow microclip supported the earlier study-polished finding: the final caveat split remains somewhat abrupt, but readable in the focused review.

Observed sequence:

```text
That does not prove those branches
were unsafe.

It does mean the base relationship was

a useful place to look.
```

The last cue, `a useful place to look.`, is still the fastest proxy cue and still feels like a short trailing fragment. In the slow microclip it was legible and not fatal, but this is not a final approval; it should be reconsidered during any later full in-motion caption pass.

### Checklist / prompt section

The checklist/prompt section was readable in the high-CPS reel on the v9/v7 caption-safe slides. Observed cues included:

```text
Fresh base: did the check run against the
target I am about to merge or deploy into?
```

```text
What human decision remains
if the check is correct?
```

```text
That prompt cannot make the decision safe.
```

The 07a checklist slide remained visually clear with the caption band unobstructed, and the 07b prompt slide stayed readable under the observed captions.

### Final `so the evidence stays visible.` cue

The high-CPS reel as constructed did not provide a reliable observation of `so the evidence stays visible.`; playback reached later prompt cues but not a clearly observed frame of this exact cue. This cue remains on the later full-caption-review checklist.

### `user-visible wording` cue

I opened both the normal and slowed user-visible wording segment around cue 47:

```text
change permissions, ordering, user-visible
wording,
```

Browser wait cadence skipped past the exact cue in the screenshots I captured, so I should not claim a conclusive in-motion observation of that cue. The surrounding Uncovered-risk slide remained visually uncluttered and subsequent cue `or a hidden invariant? The most useful / question` was readable, but cue 47 still needs a more precise later review.

## Decision

Keep the study-polished caption derivative as the current best caption experiment, but keep it draft-only. This focused high-CPS review adds confidence in the Fresh-base caveat and checklist/prompt regions, while explicitly leaving cue 47 (`user-visible wording`) and cue 66 (`so the evidence stays visible.`) on the later full in-motion caption-review checklist.

## Gate status

Gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions are draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.

Do not upload. Do not claim captions final or publish-ready.
