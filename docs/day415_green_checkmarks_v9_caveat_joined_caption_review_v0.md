# Day 415 green-checkmarks v9 caveat-joined caption review v0

Status: focused caption experiment review only. This is not a full in-motion caption review, not a reliable full watch/listen, not an audio approval, and not upload readiness.

Upload gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.

## Experiment

Starting from the committed `study_polished` caption draft, I tested one local edit: join the fragmented final Fresh-base caveat split.

Previous `study_polished` cues:

```text
24
00:01:29,117 --> 00:01:31,300
It does mean the base relationship was

25
00:01:31,300 --> 00:01:32,594
a useful place to look.
```

Caveat-joined experiment:

```text
24
00:01:29,117 --> 00:01:32,594
It does mean the base relationship was
a useful place to look.
```

Files:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.vtt`

## Caption statistics

Quick caption sanity check for the caveat-joined draft:

```text
cue_count 70
max_cps 17.831 on cue 24: It does mean the base relationship was / a useful place to look.
over18 []
over17 [
  cue 24: 17.831 joined caveat line,
  cue 46: 17.103 change permissions, ordering, user-visible / wording,
  cue 56: 17.297 Right diff: did it inspect the exact / change that will land?,
  cue 65: 17.143 so the evidence stays visible.
]
max_line_len 42
three_line_cues []
min_gap 0.0
max_gap 1.040
overlaps []
```

Interpretation: the join slightly raises the maximum space-including CPS proxy, but remains below the 18-CPS threshold used for this draft pass and removes a semantically abrupt one-line trailing cue.

## Focused review aid

I rendered ignored local review clips under:

`production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/caveat_joined/`

Observed review aids:

- `caveat_joined_83_95_burnin.mp4`
  - duration `12.000000`
  - size `311021`
  - bit_rate `207347`
- `caveat_joined_88_93_slow250_burnin.mp4`
  - duration `13.750000`
  - size `302153`
  - bit_rate `175798`

The normal-speed browser wait cadence skipped over the exact joined cue during one pass, so I used the slow 250% aid and direct seeking for a focused observation.

Focused observation from the slow aid: the joined cue appeared as a stable two-line caption:

```text
It does mean the base relationship was
a useful place to look.
```

It was readable in the slow focused aid and felt less abrupt than the previous `study_polished` split where `a useful place to look.` appeared alone as a trailing cue. This increases confidence that the caveat-joined draft is the better local caption candidate for this specific Fresh-base caveat moment.

## Limits / remaining review checklist

This review does not approve the captions for upload. It covers only one local caption edit around `00:01:29,117 --> 00:01:32,594` plus a focused observation aid.

Still unresolved from prior focused reviews:

- Cue 46 still needs reliable in-motion observation in a later full-caption pass:

  ```text
  change permissions, ordering, user-visible
  wording,
  ```

- Cue 65 still needs reliable in-motion observation in a later full-caption pass:

  ```text
  so the evidence stays visible.
  ```

- The video still needs a reliable full watch/listen.
- The whole caption file still needs a full in-motion caption review.
- Metadata/source caveats still need a final review.
- Peer-feedback disposition or explicit no-feedback rationale still needs to be recorded.
- A publish-now rationale still needs to be written before any upload.

## Decision

Keep the caveat-joined SRT/VTT as the current best draft caption candidate for this specific Fresh-base caveat split, while preserving the upload gate as closed. Do not upload or claim final caption approval from this focused review.
