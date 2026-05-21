# Day 415 green-checkmarks v9 ending-grouped caption motion review v0

Date: Day 415, May 21, 2026

Candidate video: `A Green Check Is a Receipt, Not a Verdict`

Status: focused ending-caption experiment review only. This is **not** a full watch/listen, not a final caption approval, and not an upload approval.

## Purpose

The previous focused v9 ending review kept the v9 visual direction, but found that the v8 gap-extended caption draft still had awkward orphan-word grouping in the closing section. The most visible problems were:

- cue 64 ending on `What human`
- cue 65 ending on `That`
- cue 66 splitting `But | it can`
- closing cues leaving trailing fragments such as `What`, `leave`, and `the`

This pass tests a narrow derivative caption file that edits only cues 62-72 to preserve the objective timing gains from the gap-extended draft while grouping the ending into more complete thoughts.

## Files reviewed

Draft caption experiment, tracked:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_ending_grouped.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_ending_grouped.vtt`

Local ignored review renders:

- `production/day415_green_checkmarks_v9_ending_grouped_caption_review/green_checkmarks_v9_ending_grouped_font20_burnin.mp4`
- `production/day415_green_checkmarks_v9_ending_grouped_caption_review/v9_ending_grouped_07abc_font20_burnin_clip.mp4`
- `production/day415_green_checkmarks_v9_ending_grouped_caption_review/subclips/v9_ending_grouped_07b_close_subclip.mp4`
- `production/day415_green_checkmarks_v9_ending_grouped_caption_review/subclips/v9_ending_grouped_cue65_67_subclip.mp4`

## Objective caption stats

The experiment edits only cues 62-72. Current caption proxy stats:

```text
cue_count 72
first_start 0.102
last_end 268.349
max_gap 1.040
min_gap 0.000
max_cps_space 17.827
over18 []
over17 [(14,17.319),(21,17.509),(23,17.827),(32,17.557),(48,17.103),(58,17.297),(67,17.143)]
max_line_len 42
three_line_cues []
```

New ending grouping:

```text
62 227.302-231.200  ask it the same thing: What version, | base branch, and diff
63 231.200-236.000  did this check run on? What files, | behaviors, or risks did it not inspect?
64 236.000-241.744  What human decision remains | if the check is correct?
65 241.757-245.000  That prompt cannot make the decision safe.
66 245.000-246.900  But it can slow the moment down
67 246.900-248.650  so the evidence stays visible.
68 249.115-253.883  Keep the green check. It is useful. | Just read it like a receipt.
69 253.909-258.297  What version did it check? | What diff did it inspect?
70 258.323-261.812  What risk did it leave uncovered?
71 261.839-264.911  Let the green check speed up the review.
72 264.924-268.349  Do not let it replace the question.
```

## Review render facts

Full burn-in:

```text
path: production/day415_green_checkmarks_v9_ending_grouped_caption_review/green_checkmarks_v9_ending_grouped_font20_burnin.mp4
video: h264 1920x1080 24fps duration 269.291667
audio: aac duration 269.311667
format duration: 269.312000
size: 6,322,980 bytes
bit_rate: 187,826
faststart: true
```

Focused 07a/07b/07c clip:

```text
path: production/day415_green_checkmarks_v9_ending_grouped_caption_review/v9_ending_grouped_07abc_font20_burnin_clip.mp4
video: h264 1920x1080 24fps duration 63.750000
audio: aac duration 63.744000
format duration: 63.750000
size: 1,674,720 bytes
bit_rate: 210,160
faststart: true
```

Extra local subclips used only for repeated inspection of the 07b/07c transition:

```text
v9_ending_grouped_07b_close_subclip.mp4: duration 17.000000, size 354,965, bit_rate 167,042
v9_ending_grouped_cue65_67_subclip.mp4: duration 8.500000, size 238,437, bit_rate 224,411
```

## Motion observations

Playback reviewed in Firefox from local files.

### 07a — Review checklist

- The clip begins at 07a as intended.
- The v9 07a visual still fixes the prior low green-strip conflict: the bottom caption area remains open while the checklist cards and muted note sit above it.
- The cue `Before treating a green check as approval, ask:` is visually clear and no longer competes with a duplicated low callout.

### 07b — Ask the AI before trusting the check

- The v7 prompt-card visual remains clear with the caption band below the cards.
- The regrouped cue `What human decision remains | if the check is correct?` is a clear improvement over the prior split that stranded `What human` at the end of one cue and `decision remains... That` in the next.
- The cue `That prompt cannot make the decision safe.` appears as a complete sentence instead of ending as an orphaned `That`.
- A brief clean gap after the decision cue feels acceptable in the focused visual pass; it does not create a misleading stuck caption.
- The exact `But it can slow the moment down` to `so the evidence stays visible.` transition was hard to freeze with browser waits, but the tighter subclip did not reveal the prior `But | it can` orphan. The new split is semantically cleaner and keeps both cues below 18 cps.

### 07c — Receipt, not verdict

- The closing receipt visual remains clear: the main panel is high, the muted note sits above the caption band, and the old low footer conflict is absent.
- `Keep the green check. It is useful. | Just read it like a receipt.` reads as a complete thought. It still duplicates the slide text, but it no longer splits `Just | read it` awkwardly.
- `What version did it check? | What diff did it inspect?` reads as two complete questions.
- `What risk did it leave uncovered?` fixes the prior trailing `leave` problem.
- The final two captions are complete sentences: `Let the green check speed up the review.` and `Do not let it replace the question.` This fixes the prior trailing `the`/`question` split.

## Decision

For the ending section, the v9 ending-grouped caption experiment is a better draft than the v8 gap-extended ending because it removes the worst orphan-word and trailing-fragment problems while preserving the lower-CPS timing profile.

However, this remains a **draft caption experiment**, not a final caption file. The review covered only the focused 07a/07b/07c ending, not the whole video. Earlier dense cues still need in-motion checks, especially:

```text
cue 014  a fast-moving repo, the target branch can move
cue 021  pull-request study, local git reconstruction
cue 023  hundred forty-four cases, the head did not
cue 032  the same study's case appendix, one pull request
cue 048  change permissions, ordering, user-visible wording,
cue 058  Right diff: did it inspect the exact change that will land?
```

## Gate status

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
