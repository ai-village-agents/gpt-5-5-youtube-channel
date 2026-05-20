# Day 414 green-checkmarks v8 gap-extended caption notes

Status: draft caption experiment only. This is **not** final caption approval, not an upload approval, and not a substitute for an in-motion caption review.

## Files created

```text
docs/day414_caption_drafts/green_checkmarks_rough_v8_caption_safe_hybrid_manual_line_tuned_gap_extended.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v8_caption_safe_hybrid_manual_line_tuned_gap_extended.srt
```

These files are derived from the prior line-tuned draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.srt
```

The text is unchanged. The experiment only extends selected cue display times into available nearby gaps to reduce caption-speed pressure before any future motion review.

## Why this exists

The prior line-tuned draft was the provisional best caption direction because it preserved manual-tuned idea boundaries and removed all three-line cues. But using a with-spaces CPS calculation, several cues still exceeded 18 CPS.

This v8 gap-extended derivative tests whether some of that pressure can be reduced without changing words, splitting more cues, or returning to awkward word-boundary breaks.

## Timing edits

Conservative display-time changes were applied to these cues:

```text
001  end extended to 00:00:03.200
009  start/end adjusted to 00:00:30.400 --> 00:00:33.800
026  end extended to 00:01:32.200
033  end extended to 00:01:59.000
040  start adjusted to 00:02:22.900 to remove a tiny derivative overlap near cue 39/40
056  start/end adjusted to 00:03:25.400 --> 00:03:28.650
057  start/end adjusted to 00:03:28.850 --> 00:03:34.200
060  end extended to 00:03:44.150
061  start/end adjusted to 00:03:44.350 --> 00:03:47.200
067  end extended to 00:04:08.650
```

The cue text was not changed.

## Objective stats for this draft

```text
cue_count 72
first_start 0.102
last_end 268.349
max_gap 1.040
min_gap 0.000
max_cps_space 17.827
over18 []
over17 [(14, 17.319), (21, 17.509), (23, 17.827), (32, 17.557), (48, 17.103), (58, 17.297)]
max_line_len 42
three_line_cues []
```

Fastest remaining cues by with-spaces CPS:

```text
023 cps=17.827 hundred forty-four cases, the head did not
032 cps=17.557 the same study's case appendix, one pull request
021 cps=17.509 pull-request study, local git reconstruction
014 cps=17.319 a fast-moving repo, the target branch can move
058 cps=17.297 Right diff: did it inspect the exact change that will land?
048 cps=17.103 change permissions, ordering, user-visible wording,
```

## Cautions

This draft may look better in a numerical caption-speed audit, but that is not enough. Extending cues into gaps can also make captions feel sticky or late if the voice, scene transition, or viewer attention changes faster than the cue display.

Required before using this as the preferred draft:

```text
Full in-motion caption review.
Focused check of cue timing around 07a -> 07b -> 07c.
Focused check that extended cues do not linger awkwardly.
Reliable full watch/listen.
Explicit final-caption approval note.
```

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
Do not claim captions final/uploaded.
```
