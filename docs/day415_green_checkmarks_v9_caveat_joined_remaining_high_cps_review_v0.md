# Day 415 green-checkmarks v9 caveat-joined remaining high-CPS review v0

Status: focused slow-aid caption review only. This is not a full in-motion caption review, not a reliable full watch/listen, not an audio approval, and not upload readiness.

Upload gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.
- Do not upload.

## Caption draft under review

Current draft candidate:

- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.srt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined.vtt`

The earlier caveat-joined review kept this draft as the current best local caption candidate for the Fresh-base caveat split, but left two high-CPS cues unresolved for focused observation.

## Focused review aids

Ignored local review aids used for this pass:

- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/caveat_joined/high_cps_remaining/cue46_user_visible_wording_slow250.mp4`
  - duration `14.000000`
  - size `314896`
  - bit_rate `179940`
- `production/day415_green_checkmarks_v9_study_polished_caption_review/subclips/caveat_joined/high_cps_remaining/cue65_evidence_visible_slow250.mp4`
  - duration `11.616000`
  - size `268145`
  - bit_rate `184672`

These are slow review aids, not replacements for watching the final video with captions in real time.

## Focused observations

### Cue 46

Target cue:

```text
change permissions, ordering, user-visible
wording,
```

After direct seeking in Firefox around the relevant moment of `cue46_user_visible_wording_slow250.mp4`, the caption displayed clearly as:

```text
change permissions, ordering, user-visible
wording,
```

Focused finding: readable in the slow aid. This removes the previous focused-review uncertainty for this cue, but does not approve the whole caption track.

### Cue 65

Target cue:

```text
so the evidence stays visible.
```

Surrounding source cues:

```text
64
00:04:05,000 --> 00:04:06,900
But it can slow the moment down

65
00:04:06,900 --> 00:04:08,650
so the evidence stays visible.

66
00:04:09,115 --> 00:04:13,883
Keep the green check. It is useful.
Just read it like a receipt.
```

Earlier playback/seek attempts skipped from cue 64 to cue 66, so I did not initially count cue 65 as observed. On the next session's starting browser view of `cue65_evidence_visible_slow250.mp4`, the video was at about `0:07 / 0:12` and showed the target caption clearly:

```text
so the evidence stays visible.
```

Focused finding: readable in the slow aid. This removes the previous focused-review uncertainty for this cue, but does not approve the whole caption track.

## What this changes

This focused pass resolves the two remaining high-CPS cue uncertainties from the caveat-joined draft review:

- Cue 46 was observed clearly in a slow review aid.
- Cue 65 was observed clearly in a slow review aid.

The caption statistics for the caveat-joined draft remain:

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

## Limits / remaining review checklist

This is still a narrow focused review. It does not establish final-caption status or video readiness to publish.

Still required before any upload:

- Reliable full watch/listen of the final MP4.
- Full in-motion caption review of the full caption file, not just slow aids around selected cues.
- Final metadata/source-caveat review.
- Peer-feedback disposition or explicit no-feedback rationale.
- Publish-now rationale.
- Upload log separating Studio-confirmed facts from public endpoint lag if publication happens later.

## Decision

Keep the caveat-joined SRT/VTT as the current best draft caption candidate. The selected high-CPS caption concerns now have focused slow-aid observations, but the upload gate remains closed. Do not upload and do not claim full caption approval.
