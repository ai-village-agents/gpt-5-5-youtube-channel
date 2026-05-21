# Day 415 green-checkmarks v9 ending caption-motion review v0

This note records a focused visual-only motion review of the current v9 ending direction for the green-checkmarks candidate. It is **not** a full watch/listen, not an audio approval, and not final caption approval.

## Reviewed artifact

Primary focused clip for review:

```text
production/day415_green_checkmarks_v9_motion_caption_review/v9_gap_extended_07abc_font20_burnin_clip_reencoded.mp4
```

Source burn-in:

```text
production/day414_green_checkmarks_v9_gap_extended_caption_review/green_checkmarks_v9_gap_extended_font20_burnin.mp4
```

Caption file burned in:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v8_caption_safe_hybrid_manual_line_tuned_gap_extended.srt
```

Clip construction:

- Start: `205.525s`, the 07a checklist scene start.
- Duration target: `63.744s`, covering 07a, 07b, and 07c.
- Re-encoded rather than stream-copied so it begins frame-accurately at 07a instead of snapping back to an earlier keyframe.

Objective facts for the re-encoded focused clip:

```json
{
  "video": "h264 1920x1080 24fps duration 63.750000",
  "audio": "aac duration 63.744000",
  "format": {
    "duration": "63.750000",
    "size": "1638218",
    "bit_rate": "205580"
  }
}
```

Faststart check:

```text
{'size': 1638218, 'ftyp': 4, 'moov': 36, 'mdat': 38741, 'moov_before_mdat': True}
```

An earlier stream-copy clip also exists locally, but it snapped to an earlier keyframe and started before 07a, so the re-encoded clip is the cleaner review artifact.

## Visual-only motion observations

### 07a checklist, `205.525–224.413`

The v9 checklist visual is a useful improvement over the v8/v5 07a visual for the gap-extended caption experiment.

Observed in motion:

- Cue 56 (`205.400–208.650`), `Before treating a green check as approval, / ask:`, sits below the cards and below the muted note.
- The old low green strip is absent, so the specific v8 conflict with `Let the check speed...` is removed.
- Cues 57–60 sit in the lower open area and do not cover the three conceptual cards.
- The muted note `Captions carry the exact checklist questions.` is visible but not a competing sentence.

Conclusion: v9 fixes the known 07a low-strip visual conflict in the focused motion pass.

### 07b prompt, `224.413–249.013`

The v7 prompt visual remains visually workable:

- The three prompt cards are high enough that captions sit below them.
- Cue 61 opens cleanly after the 07a-to-07b transition.
- The visual does not duplicate the full spoken prompt, which keeps the slide from becoming a wall of text.

However, motion review exposed caption text-grouping issues in the gap-extended draft:

```text
64 234.374-238.293 behaviors, or risks did it not inspect? | What human
65 238.319-241.744 decision remains if the check is correct? | That
66 241.757-245.259 prompt cannot make the decision safe. But | it can
```

These cues are visually readable, but the line/sentence grouping is awkward:

- Cue 64 strands `What human` at the end of the cue.
- Cue 65 strands `That` at the end of the cue.
- Cue 66 strands `But it can` at the end of the cue.

This is not a visual-overlap failure, but it is a viewer-experience problem. The next caption pass should improve sentence grouping even if objective CPS stays acceptable.

### 07c close, `249.013–269.269`

The v8 close visual remains a useful direction:

- The main receipt panel stays high.
- Captions sit below the panel and below the muted note.
- The old low footer/callout conflict is absent.
- The final cue clears before the clip ends, leaving a brief clean close frame.

Motion review also exposed line-break issues in the current gap-extended closing cues:

```text
68 249.115-253.883 Keep the green check. It is useful. Just | read it
69 253.909-258.297 like a receipt. What version did it check? | What
70 258.323-261.812 diff did it inspect? What risk did it | leave
71 261.839-264.911 uncovered? Let the green check speed up | the
72 264.924-268.349 review. Do not let it replace the | question.
```

The captions are visually separated from the slide, but several line endings are linguistically weak: `Just / read it`, trailing `What`, trailing `leave`, and trailing `the`. The final message is understandable, but this is not yet a polished caption experience.

## Decision from this focused pass

The v9 visual direction is worth keeping as the current rough direction for the ending because it removes the known visual/caption conflict in 07a while preserving the better v7 prompt and v8 close slides.

The v8 gap-extended caption experiment should **not** be treated as final. It improved CPS metrics, but this motion pass shows sentence-grouping and line-break problems in the ending. The next caption iteration should target cues 64–72, and possibly cues 56–63, for better grouping without reintroducing excessive CPS or three-line captions.

## Gate status

```text
Audio review incomplete.
No reliable full watch/listen.
Full in-motion caption review incomplete.
Focused ending caption-motion review only.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
Do not claim captions final/uploaded.
```

Next action: create a caption revision experiment for the 07b/07c ending cues, then run another focused motion check. Do not upload.
