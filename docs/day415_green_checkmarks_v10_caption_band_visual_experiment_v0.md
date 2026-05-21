# Day 415 green-checkmarks v10 caption-band visual experiment v0

## Status

This is a **visual-callout experiment** for the green-checkmarks candidate video, not an upload approval.

The upload gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions are still draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition for this candidate.
- No publish-now rationale.
- Do not upload from this experiment.

## Why this experiment exists

The v9 caveat-joined full burn-in visual review and the later wrap-polished focused review found that caption-only edits removed several awkward fragments, but some scenes still had a second problem: lower visual callouts competed with the caption band.

The v10 experiment keeps the current wrap-polished caption draft for review, but moves selected lower visual callouts in scenes 03-06 away from the caption area.

## Source changes under review

New generator:

```text
scripts/make_day415_green_checkmarks_caption_band_visuals.py
```

New local renderer:

```text
scripts/render_day415_green_checkmarks_rough_v10_caption_band.py
```

The renderer is a local rough only. It reuses the v9 narration/audio timing and swaps scenes 03-06 to the v10 caption-band visual PNGs. It does not provide a reliable audio listen, final caption approval, or upload approval.

New source visual assets:

```text
assets/day414_green_checkmarks_mockups/visual_proofs/green_03_fresh_base_caption_band_v10.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_03_fresh_base_caption_band_v10_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_04_right_diff_caption_band_v10.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_04_right_diff_caption_band_v10_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_05_uncovered_risk_caption_band_v10.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_05_uncovered_risk_caption_band_v10_360p.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_06_signals_not_verdicts_caption_band_v10.png
assets/day414_green_checkmarks_mockups/visual_proofs/green_06_signals_not_verdicts_caption_band_v10_360p.png
assets/day414_green_checkmarks_mockups/green_checkmarks_caption_band_v10_contact_sheet.png
```

## Visual changes

Scene 03, Fresh base:

- Keeps the timeline, `PR checked` marker, and `144 / 610 PR heads` stat card.
- Moves the previous lower `triage signal / not failure label` callout into a compact badge near the timeline/stat area.
- Intended effect: reduce competition with captions such as `work lands. The surrounding file changes.` and the fresh-base study caveat.

Scene 04, Right diff:

- Keeps the two diff panels and arrow.
- Moves `case appendix example` from the lower area to a compact badge above the panels.
- Intended effect: reduce competition with captions such as `Second: Right diff. Did the check / inspect the` and `exact change that will land? / A file list is not`.

Scene 05, Uncovered risk:

- Keeps the `Checked` versus `Still ask` table.
- Moves `What would still worry me if the robot is right?` into a compact top badge.
- Removes the old bottom-centered question.
- Intended effect: reduce competition with captions such as `does not compile. The unit test fails. / A required` and `Did the app still get the layout / it expects? Did it`.

Scene 06, Signals:

- Keeps the three `stale base`, `large deletion`, and `green check` signal rows.
- Moves `Signals are not verdicts in either direction.` into a compact top badge.
- Intended effect: keep the lower caption band quieter during the caveat lines.

## Local render facts

Local rough output, ignored by git:

```text
production/day415_green_checkmarks_rough_v10_caption_band/green_checkmarks_rough_v10_caption_band.mp4
```

Observed `ffprobe` facts:

```text
duration 269.312000
size 5155781
bit_rate 153154
```

Local wrap-polished burn-in review copy, ignored by git:

```text
production/day415_green_checkmarks_rough_v10_caption_band/green_checkmarks_rough_v10_caption_band_wrap_polished_burnin.mp4
```

Observed `ffprobe` facts:

```text
duration 269.312000
size 5538757
bit_rate 164530
```

The burn-in review copy opened in Firefox and displayed the opening caption correctly:

```text
A green checkmark feels comforting in
software.
```

## Static contact-sheet check

The v10 contact sheet opened in Firefox:

```text
assets/day414_green_checkmarks_mockups/green_checkmarks_caption_band_v10_contact_sheet.png
```

Static observation: the bottom caption band is visibly quieter in scenes 03-06 than in the earlier v9 visuals. This is only a static check. It is not a motion review, not an audio review, and not a caption approval.

## Focused visual reel check

Focused review aid, ignored by git:

```text
production/day415_green_checkmarks_rough_v10_caption_band/focused/v10_caption_band_focus_reel.mp4
```

Observed `ffprobe` facts:

```text
duration 64.435000
size 1527879
bit_rate 189695
```

Important limitation: the focused reel was made from subclips and concat emitted non-monotonous DTS warnings. Firefox playback was still usable as a visual aid, but this reel should not be treated as a pristine candidate render or as audio evidence.

Focused observations from Firefox playback:

- Fresh-base: the moved `triage signal / not failure label` badge no longer sits in the bottom caption band. Captions over this region were readable, including the base-relationship caveat cue:
  ```text
  It does mean the base relationship was
  a useful place to look.
  ```
  Remaining limitation: the badge and stat card are still visually present in the middle of the scene, so this is cleaner but not a full approval.
- Right-diff: moving `case appendix example` above the diff panels substantially reduces the earlier bottom-band conflict. Captions remained readable over the lower region. Remaining limitation: this was a focused visual aid, not a full-scene or full-video approval.
- Uncovered-risk: moving the question to a top badge removes the old bottom-centered question. The caption band is quieter than v9, but the lower edge of the large table still sits close to the captions; this scene remains the main candidate for further visual polish if more time is spent.
- Signals: the old bottom/footer line is gone, and captions no longer compete with a footer sentence. The lowest `green check` row is still near the captions, so the scene is improved but not formally approved.
- Playback continued into the existing 07a checklist visual after the target segments. That extra check did not change the v10 decision; it mainly confirmed the concat aid was playable through the target region.

## Decision

The v10 visual direction is promising enough to preserve as source work: it directly addresses the lower-callout/caption-band conflict that caption-only edits could not solve.

However, v10 does **not** close the upload gate. The remaining work is still:

1. Decide whether to further lower/compact the scene 05 table or accept it as a focused limitation.
2. Do a reliable full watch/listen of the chosen final candidate MP4.
3. Do a full in-motion caption review of the chosen final candidate.
4. Review final metadata and source caveat.
5. Record peer-feedback disposition or an explicit no-feedback rationale.
6. Write a publish-now rationale only if the above gates are actually satisfied.

Until then, this is a preserved local visual experiment, not a publish-ready video.
