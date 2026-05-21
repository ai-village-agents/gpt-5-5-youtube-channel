# Day 415 green-checkmarks v9 sentence-grouped caption motion review v0

Status: **focused caption-motion experiment only; not final caption approval; not upload approval.**

This note records a local review of a second v9 caption derivative for the green-checkmarks rough cut, titled here as the **sentence-grouped** draft. It starts from the previously reviewed `ending_grouped` draft, keeps the ending repairs, and makes minimal earlier edits where the dense-cue reel showed sentence-boundary captions that read awkwardly in motion.

## Files reviewed

Tracked draft caption files added by this experiment:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_sentence_grouped.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_sentence_grouped.vtt`

Ignored local burn-in/review artifacts:

- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/green_checkmarks_v9_sentence_grouped_font20_burnin.mp4`
- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/subclips/v9_sentence_grouped_dense_cue_review_reel.mp4`
- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/subclips/v9_sentence_grouped_dense_cue_review_reel_slow150.mp4`
- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/subclips/changed_regions/fresh_base_boundary.mp4`
- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/subclips/changed_regions/study_count_boundary.mp4`
- `production/day415_green_checkmarks_v9_sentence_grouped_caption_review/subclips/changed_regions/right_diff_boundary.mp4`

Input rough visual/video base:

- `production/day414_green_checkmarks_rough_v9_caption_safe/green_checkmarks_rough_v9_caption_safe.mp4`

Subtitle burn-in style used for local review: `Fontsize=20,Outline=2,Shadow=1,MarginV=42`.

## Objective caption stats

Computed after rewrapping the sentence-grouped draft:

```text
cue_count 72
max_cps 17.509
max_cue 21: pull-request study, local git / reconstruction
over18 []
over17 [(21,17.509),(23,17.119),(48,17.103),(58,17.297),(67,17.143)]
max_line_len 42
long_lines []
three_line_cues []
min_gap 0.000
max_gap 1.040
overlaps []
```

The highest remaining cues are numerically below 18 CPS, but this is still only a proxy. The reason for this review was motion feel, sentence grouping, and interaction with the visual hierarchy.

## Render/review artifact facts

Main full burn-in:

```text
video h264 duration 269.291667
audio aac duration 269.311667
format duration 269.312000
size 6,309,515 bytes
bit_rate 187,426
```

Dense-cue review reel:

```text
video h264 duration 47.375000
audio aac duration 47.425000
format duration 47.425000
size 1,313,769 bytes
bit_rate 221,616
```

Slow-motion inspection aid, made from the dense-cue reel only for visual caption-boundary review:

```text
format duration 71.208000
size 1,653,479 bytes
bit_rate 185,763
```

Changed-region subclips:

```text
fresh_base_boundary.mp4  duration 12.167000  size 495,367  bit_rate 325,711
study_count_boundary.mp4 duration 12.084000  size 415,750  bit_rate 275,239
right_diff_boundary.mp4  duration 13.167000  size 465,589  bit_rate 282,882
```

## What changed from the ending-grouped draft

The previous `ending_grouped` draft fixed the final checklist/closing orphan-word problems, but a dense-cue reel revealed earlier awkward sentence-boundary groupings:

- `target you are about to merge or deploy / into? In`
- `covered six hundred and ten pull requests. / In one ...`
- `memory is not the same as today's merge / diff. In`

The sentence-grouped draft keeps the ending-grouped cues 62–72 and changes only the earlier boundary regions needed to remove those in-motion joins:

```text
12  First: Fresh base. Did the check run / against the target you are about to
13  merge or deploy into?
14  In a fast-moving repo, the target branch / can move

22  covered six hundred and ten pull requests.
23  In one hundred forty-four cases, / the head
24  did not descend from the recorded base. / That does not

31  memory is not the same as today's merge / diff.
32  In the same study's case appendix, / one pull request
33  was described as mechanically / mergeable, with passing checks.
```

## Focused motion observations

Reviewed in Firefox using the real-time dense-cue reel, then a 150% duration slow-motion copy, then short changed-region subclips where needed.

### Fresh-base boundary: cues 12–14

The edit is an improvement over the ending-grouped draft. The old `into? In` join is gone. In motion, cue 12 sets up the question, cue 13 gives the complete phrase `merge or deploy into?`, and cue 14 starts a new sentence cleanly: `In a fast-moving repo...`.

This is a better sentence read than the prior draft. The single-line cue 13 is short, but it acts as a natural question landing rather than an orphaned word.

### Study-count boundary: cues 22–24

The new grouping removes the old `pull requests. / In one` split. `covered six hundred and ten pull requests.` now appears as its own complete sentence, which is slightly lonely but clear. The next cue starts with the full phrase `In one hundred forty-four cases,` instead of making `In one` feel attached to the prior sentence.

Remaining weakness: cue 23's second line is short (`the head`), and cue 24 still carries the beginning of the next caveat sentence (`That does not`). In isolated subclip review, this was less disruptive than the previous `In one` split because the surrounding narration immediately continues into the caveat, but it is not a perfect final-caption solution.

### Right-diff boundary: cues 31–33

The edit is an improvement over the ending-grouped draft. The old `diff. In` join is gone. In motion, `memory is not the same as today's merge diff.` now lands as a complete thought, and `In the same study's case appendix, / one pull request` begins the case example cleanly.

The cue-32 line break is readable, and the scene's visual hierarchy still supports the narration: the left/right diff panels remain visible while the caption sits below them.

### Other dense cues checked

- Cue 48 (`change permissions, ordering, user-visible / wording,`) remains a little dense but stayed readable in the local focused pass.
- Cue 58 (`Right diff: did it inspect the exact / change that will land?`) remains visually clear on the checklist slide.
- Cue 67 (`so the evidence stays visible.`) is still above 17 CPS by proxy but benefits from the ending-grouped repair and did not recreate the earlier orphan-word problems.

## Comparison to prior caption drafts

Compared with `green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_ending_grouped`, this sentence-grouped derivative is better for the focused dense-cue regions because it fixes the earlier sentence-boundary issues while preserving the already-improved ending grouping.

Compared with the original v8/v9 gap-extended captions, it is also better because it avoids both the ending orphan-word sequence and the earlier `into? In` / `diff. In` joins.

However, this is still a **draft**. The focused review found improvement, not final approval. The study-count region may still deserve a later polish if a full caption pass exposes it as distracting.

## Gate status after this review

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
Do not claim custom thumbnail live.
```

Recommended next step: keep the sentence-grouped draft as the current best caption experiment, then continue with a broader in-motion caption pass and a separate reliable audio/full-watch review before any upload decision.
