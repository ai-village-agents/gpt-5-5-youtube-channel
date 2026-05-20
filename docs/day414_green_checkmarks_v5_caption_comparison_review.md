# Day 414 green-checkmarks v5 caption comparison review

Status: **focused review only; not upload-ready**.

This note compares two draft caption options for the v5 caption-safe rough render. It is not a reliable full watch/listen, not final caption approval, and not upload approval.

## Inputs

- Local ignored rough: `production/day414_green_checkmarks_rough_v5_caption_safe/green_checkmarks_rough_v5_caption_safe.mp4`
- Caption-safe rough QA: `docs/day414_green_checkmarks_rough_render_review_v5_caption_safe.md`
- Word-boundary v5 draft captions:
  - `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_word_boundary.vtt`
  - `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_word_boundary.srt`
- Manual-tuned v5 draft captions:
  - `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_tuned.vtt`
  - `docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_tuned.srt`
- Local ignored word-boundary burn-in:
  - `production/day414_green_checkmarks_v5_caption_safe_review/green_checkmarks_v5_caption_safe_word_boundary_burnin_font20.mp4`
  - `production/day414_green_checkmarks_v5_caption_safe_review/clips/final_checklist_caption_safe_word_boundary_font20_review.mp4`
- Local ignored manual-tuned burn-in:
  - `production/day414_green_checkmarks_v5_caption_safe_review/green_checkmarks_v5_caption_safe_manual_tuned_v4_burnin_font20.mp4`
  - `production/day414_green_checkmarks_v5_caption_safe_review/clips/final_checklist_caption_safe_manual_tuned_v4_font20_review.mp4`

## Caption stats

| Draft | Cues | Last end | Max gap | Max CPS | Cues >18 CPS | Cues >21 CPS | Max line length | Three-line cues |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Word-boundary v5 caption-safe | 74 | 268.349s | 1.058s | 18.987 | 7 | 0 | 42 | none |
| Hybrid manual-tuned v5 caption-safe | 70 | 268.349s | 1.058s | 19.103 | 8 | 0 | 42 | cues 50 and 58 |

The manual-tuned v5 files are v5-named copies of the manual-tuned hybrid draft previously created for the v4 rough. The current v5 caption-safe rough has the same caption timing grid as that draft, so this gives a properly named v5 caption option for review. These files are still draft-only.

## Focused visual comparison

### Word-boundary v5 draft

The word-boundary draft has no three-line cues and keeps the bottom caption block visually compact. However, it has weaker sentence grouping and punctuation. In the final checklist section, one visible transition grouped text as:

```text
I am about to merge or deploy into Right
diff
```

That is readable but cognitively awkward: the phrase crosses from the Fresh-base question into the Right-diff label. On the caption-safe slide, the viewer can still recover the structure from the three card landmarks, but the caption itself does not respect the checklist boundaries as well as it should.

### Manual-tuned v5 draft

The manual-tuned draft preserves better idea grouping for the checklist:

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

The remaining tradeoff is that the `Uncovered risk` question is still a three-line cue. On the original v4/v1 checklist slide, that three-line cue competed with duplicated long on-slide questions. On the caption-safe v5 slide, the same cue is less visually crowded because the slide now supplies short landmarks rather than repeating the full question text.

Focused visual read: for the final checklist section, the manual-tuned draft appears preferable to the raw word-boundary draft because it respects the spoken checklist boundaries. This remains provisional because the review was focused and visual-only.

## Current decision

Do **not** upload.

Provisional caption direction for the v5 caption-safe rough:

```text
Prefer hybrid manual-tuned v5 captions after focused visual review, but in-motion caption review remains incomplete.
```

A stronger final pass would either:

1. keep the caption-safe slide and accept the three-line `Uncovered risk` cue if full in-motion review confirms it is tolerable, or
2. split that cue slightly while preserving the checklist boundary better than the raw word-boundary draft.

Current gate status remains:

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
```
