# Day 415 green-checkmarks wrap phrase-polished caption experiment v0

Date: 2026-05-21  
Base caption draft: `green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_polished.srt`  
New draft SRT: `day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_polished.srt`  
New draft VTT: `day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_polished.vtt`

## Scope

This is a small draft caption-polish experiment after the v11 full burn-in visual pass. It targets two phrase-boundary problems that remained visible after the visual-band clearance work:

- `A file list is not` appearing after `exact change that will land?`
- isolated `A required` after `does not compile. The unit test fails.`

This is **not** a final caption approval, upload approval, or audio approval.

## Edits

### Right-diff phrase boundary

Before:

```text
27
00:01:41,654 --> 00:01:45,339
exact change that will land?
A file list is not

28
00:01:45,365 --> 00:01:48,737
the same as today's merge diff. A preview
from
```

After:

```text
27
00:01:41,654 --> 00:01:43,749
exact change that will land?

28
00:01:43,749 --> 00:01:48,737
A file list is not the same as
today's merge diff. A preview from
```

Rationale: the sentence boundary is cleaner, and `A file list is not the same as today's merge diff` now reads as one idea instead of leaving `A file list is not` dangling.

### Uncovered-risk phrase boundary

Before:

```text
42
00:02:38,582 --> 00:02:43,516
does not compile. The unit test fails.
A required

43
00:02:43,542 --> 00:02:47,123
command exits with an error. Other
failures are
```

After:

```text
42
00:02:38,582 --> 00:02:42,571
does not compile.
The unit test fails.

43
00:02:42,571 --> 00:02:47,123
A required command exits with an error.
Other failures are
```

Rationale: `A required command exits with an error` now stays together instead of showing `A required` as a stranded fragment.

## Mechanical stats

```text
cue_count 70
max_cps 17.831 on cue 24: It does mean the base relationship was / a useful place to look.
over18 []
over17 [(24, 17.831, 'It does mean the base relationship was / a useful place to look.'), (46, 17.103, 'change permissions, ordering, user-visible / wording,'), (56, 17.297, 'Right diff: did it inspect the exact / change that will land?'), (65, 17.143, 'so the evidence stays visible.')]
max_line_len 42
min_gap 0.000
max_gap 1.040
overlaps []
```

The edit does not increase max CPS above the previous draft. The only over-17 CPS cues remain inherited dense cues outside the edited region.

## Review status

This derivative has not yet been reviewed in motion. In particular, the approximate split points around cues 27/28 and 42/43 need a focused burn-in check before this should replace the previous draft.

The v11 visual direction remains promising, but this caption derivative is draft-only.

## Upload gate

The upload gate remains closed.

Not done:

- Audio review incomplete.
- No reliable full watch/listen.
- No full final in-motion caption review.
- This derivative has not received focused motion review.
- Captions remain draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.
