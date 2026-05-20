# Day 414 green-checkmarks v6 line-tuned captions — static cue-midpoint review

This note records a static contact-sheet review of the v6 caption-safe rough with the line-tuned caption draft burned in at font size 20.

It is **not** a full in-motion caption review, not a reliable full watch/listen, and not upload approval.

## Assets inspected

Draft rough source:

```text
production/day414_green_checkmarks_rough_v6_caption_safe/green_checkmarks_rough_v6_caption_safe.mp4
```

Draft caption source:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v5_caption_safe_hybrid_manual_line_tuned.vtt
```

Ignored local review render:

```text
production/day414_green_checkmarks_v6_caption_safe_review/green_checkmarks_v6_caption_safe_manual_line_tuned_font20_burnin.mp4
```

Ignored local cue-midpoint contact sheets:

```text
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_01.png
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_02.png
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_03.png
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_04.png
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_05.png
production/day414_green_checkmarks_v6_caption_safe_review/full_cue_midpoint_pages/v6_line_tuned_cue_midpoints_page_06.png
```

Contact-sheet facts:

```text
cue_count: 72
pages: 6
layout: 12 cues per page except the final page if shorter
page size: 960 x 2040 px
```

## Static page observations

### Page 1 — cues 1–12

The opening and early checklist cues are generally separated from the main visual text. I did not see obvious three-line caption crowding in the static midpoint samples. The caption band sits low enough that the large title and three-question scaffold remain readable.

### Page 2 — cues 13–24

The fresh-base segment appears usable in static samples. Captions sit low and do not obviously obscure the key line/arrow relationship or the main stale-target explanation. The slide remains information-dense, so it still needs real playback review for reading-time pressure.

### Page 3 — cues 25–36

The right-diff samples are visually denser than the opening and fresh-base sections. However, the caption band appears below the main preview/current-diff boxes in the sampled frames. I did not see an immediate static overlap failure, but this remains a target for motion review because the viewer must parse both the diagram and the narration.

### Page 4 — cues 37–48

The uncovered-risk ledger is also dense. Static cue midpoints show captions remaining lower than the ledger rows, without obviously covering the row labels. The scene should still be checked in motion because the ledger asks the viewer to compare multiple rows while reading captions.

### Page 5 — cues 49–60

This page covers the end of uncovered-risk, the signals-not-verdicts slide, and the 07a review-checklist slide.

Observed static layout:

- The closing uncovered-risk question split avoids the earlier three-line caption problem.
- The signals-not-verdicts captions stay low relative to the three horizontal signal rows. I did not see the caption band cover the `stale base`, `large deletion`, or `green check` row labels at the sampled midpoints.
- The 07a caption-safe checklist slide is much less crowded than the earlier full-question checklist slide. The slide carries compact scaffold labels while captions carry the full spoken questions.
- The fastest checklist split, `could still happen if this check / is correct?`, remains visually legible in the static midpoint sample, but it should be checked in motion because it is one of the higher-CPS cues.

### Page 6 — cues 61–72

This page covers the 07b AI-prompt scaffold and the closing receipt slide.

Observed static layout:

- The v6 07b prompt scaffold is materially less crowded than the v5 prompt slide because it removes long duplicated prompt questions from the visual.
- Captions still sit across the lower prompt-card area and the footer line in several static midpoints. They sometimes overlap the lower `Human decision left` area or the green footer strip, so v6 is an improvement rather than a full solution.
- The overlap is less severe than v5 because the remaining on-slide prompt text is short scaffold text, not long sentence-level prompt questions.
- The closing receipt slide remains readable in the static samples. Captions overlap the low green footer strip but not the main `Keep the green check`, `It is useful`, or `Just read it like a receipt` lines.

## Review result

Static cue-midpoint review supports keeping the v6 prompt scaffold and the line-tuned caption draft as the next candidate for an actual in-motion caption review.

It does **not** establish that the video is upload-ready.

Current gate remains closed:

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

## Next action

Attempt a real in-motion caption review and reliable full watch/listen if feasible. If browser playback remains unreliable, continue improving review packets and avoid upgrading the caption status based only on static frames.
