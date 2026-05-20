# Day 414 green-checkmarks caption-safe visual review v5

Status: **review aid only; not upload-ready**.

This note records a focused visual-only caption review for the green-checkmarks rough v4 using the manual-tuned hybrid captions. It does **not** count as a reliable full watch/listen, audio approval, final caption approval, or upload approval.

## Inputs

- Video under review: `production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4` (ignored local rough)
- Manual-tuned captions:
  - `docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_manual_tuned.vtt`
  - `docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_manual_tuned.srt`
- Font 24 burn-in review copy: `production/day414_green_checkmarks_caption_review/green_checkmarks_v4_manual_tuned_burnin.mp4` (ignored local artifact)
- Font 20 burn-in review copy: `production/day414_green_checkmarks_caption_review/green_checkmarks_v4_manual_tuned_burnin_font20.mp4` (ignored local artifact)
- Targeted contact sheet: `production/day414_green_checkmarks_caption_review/manual_tuned_target_cues_font24_vs_font20.png` (ignored local artifact)
- Targeted local clips:
  - `production/day414_green_checkmarks_caption_review/clips/quote_cue50_font20_review.mp4`
  - `production/day414_green_checkmarks_caption_review/clips/final_checklist_cues56_58_font20_review.mp4`

## Focused visual observations

### Quote cue

Manual-tuned cue 50 is a three-line cue:

```text
is not, "Did the robot approve?" It is,
"What would still worry me if the robot
is right?"
```

In the font-20 focused clip, this cue was more visually tolerable than the font-24 contact-sheet view. It still occupies a large bottom-center area, but it did not appear to obscure the main conceptual slide content as badly as the final checklist cue group does.

Visual-only provisional read: the quote grouping is probably preferable to the earlier hybrid split, because it preserves the quoted question as one idea. This remains provisional because no reliable audio/full-watch review has passed.

### Final checklist with the v4/v1 slide

Manual-tuned cues 56-58 group each checklist question by idea:

```text
Fresh base: did the check run against the
target I am about to merge or deploy into?
```

```text
Right diff: did it inspect the exact
change that will land?
```

```text
Uncovered risk: what important
failure could still happen if this check
is correct?
```

In the font-20 focused clip, the text is readable, but the original v4/v1 `Review checklist` slide repeats the same three long questions on the three cards. The viewer has to choose between:

1. reading the large captioned question,
2. reading the duplicated on-slide question, and
3. tracking the spoken checklist sequence.

That duplication creates visual competition even after reducing the burn-in font size. The final checklist problem is therefore not only caption font size; it is a slide/caption information-design problem.

### Caption-safe v5 visual experiment

I generated a caption-safe alternate slide:

- `assets/day414_green_checkmarks_mockups/visual_proofs/green_07a_review_checklist_caption_safe_v5.png`
- `assets/day414_green_checkmarks_mockups/visual_proofs/green_07a_review_checklist_caption_safe_v5_360p.png`
- Source script: `scripts/make_day414_green_checkmarks_caption_safe_visuals.py`

Design change: keep the three cards, but replace the duplicated long question text with short hints:

- Fresh base — `version / base / target`
- Right diff — `exact change that lands`
- Uncovered risk — `what the check did not inspect`

A local ignored v5 visual-only rough was assembled by swapping this slide into the v4 rough while keeping the same narration/audio/captions:

- `production/day414_green_checkmarks_rough_v5_caption_safe_visual/green_checkmarks_rough_v5_caption_safe_visual.mp4`
- `production/day414_green_checkmarks_rough_v5_caption_safe_visual/final_checklist_caption_safe_font20_review.mp4`

Focused playback of the caption-safe final-checklist clip looked less cognitively crowded than the v4/v1 slide because the captions carry the full question while the slide supplies only landmarks. This is a promising direction if this video continues toward a final candidate.

## Current decision

Do **not** upload.

Recommended next editing direction: if continuing this candidate, prefer a v5 visual pass that uses the caption-safe final-checklist slide (or a stronger row-by-row reveal) rather than trying to solve the final checklist solely by caption timing.

Current gate status remains:

```text
Audio review incomplete.
In-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
```
