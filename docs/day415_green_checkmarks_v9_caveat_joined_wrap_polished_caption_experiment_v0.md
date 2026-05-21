# Day 415 green-checkmarks v9 caveat-joined wrap-polished caption experiment v0

This note records a small caption-only derivative after the full burn-in visual pass identified several readable but awkward cue wraps.

## Status

This is a draft caption experiment only.

It is not a full in-motion caption review, not a reliable audio listen, not a metadata/source-caveat review, and not upload approval.

Standing gate status remains:

```text
Audio review incomplete.
No reliable full watch/listen.
Full in-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
```

## Files

Source draft used as base:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.vtt`

New wrap-polished draft:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_polished.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_polished.vtt`

## Motivation

The full burn-in visual review found the current caveat-joined captions generally readable, but it also identified a few awkward fragments:

- Fresh-base cue with isolated `A` after `The surrounding file changes.`
- Right-diff transition cue with isolated `the`.
- Uncovered-risk cue split as `A / required`.
- Uncovered-risk cue with trailing `Did it`.

This derivative is a minimal caption-only reflow. It does not change scene visuals or audio.

## Edits

### Cue 17 / 18 — Fresh-base isolated `A`

Before:

```text
17
00:00:56,682 --> 00:01:01,162
work lands. The surrounding file changes.
A

18
00:01:01,188 --> 00:01:05,700
validator appears. A slot that was empty
becomes occupied.
```

After:

```text
17
00:00:56,682 --> 00:01:01,162
work lands. The surrounding file changes.

18
00:01:01,188 --> 00:01:05,700
A validator appears. A slot that was empty
becomes occupied.
```

Reason: removes a one-letter trailing line while preserving the sentence.

### Cue 26 / 27 — Right-diff transition isolated `the`

Before:

```text
26
00:01:38,162 --> 00:01:41,630
Second: Right diff. Did the check inspect
the

27
00:01:41,654 --> 00:01:45,339
exact change that will land? A file list
is not
```

After:

```text
26
00:01:38,162 --> 00:01:41,630
Second: Right diff. Did the check
inspect the

27
00:01:41,654 --> 00:01:45,339
exact change that will land?
A file list is not
```

Reason: removes the isolated `the` line without changing timing.

### Cue 42 — Uncovered-risk `A / required`

Before:

```text
42
00:02:38,582 --> 00:02:43,516
does not compile. The unit test fails. A
required
```

After:

```text
42
00:02:38,582 --> 00:02:43,516
does not compile. The unit test fails.
A required
```

Reason: keeps the next phrase together enough to avoid the especially awkward `A` line, while avoiding a large retiming change.

### Cue 44 / 45 — trailing `Did it`

Before:

```text
44
00:02:47,149 --> 00:02:51,576
about meaning. Did this remove recent
work? Did

45
00:02:51,602 --> 00:02:55,027
the app still get the layout it expects?
Did it
```

After:

```text
44
00:02:47,149 --> 00:02:51,576
about meaning. Did this remove recent
work?

45
00:02:51,602 --> 00:02:55,027
Did the app still get the layout
it expects? Did it
```

Reason: avoids ending cue 44 on a stranded `Did`, and makes cue 45 read as a complete question plus the start of the next question.

## Mechanical stats

For the wrap-polished draft:

```text
cue_count: 70
max_cps: 17.831 on cue 24
max_cue_text: It does mean the base relationship was / a useful place to look.
over18: []
over17:
  - cue 24: 17.831 — It does mean the base relationship was / a useful place to look.
  - cue 56: 17.297 — Right diff: did it inspect the exact / change that will land?
  - cue 65: 17.143 — so the evidence stays visible.
  - cue 46: 17.103 — change permissions, ordering, user-visible / wording,
max_line_len: 42
three_line_cues: []
min_gap: 0.000
max_gap: 1.040
```

The experiment preserves the same max-CPS cue as the prior caveat-joined draft and does not create any cue above the 18 CPS proxy threshold used in this caption pass.

## Decision for now

This wrap-polished draft is a plausible successor to the caveat-joined draft for further visual testing because it removes several awkward line breaks without worsening the headline mechanical stats.

It still needs an in-motion review. It also does not solve the lower-callout visual competition noted in the full burn-in review; that may require visual-callout changes rather than caption-only edits.

Do not upload based on this experiment.
