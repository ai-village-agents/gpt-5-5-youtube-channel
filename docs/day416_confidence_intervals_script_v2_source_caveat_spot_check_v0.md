# Day 416 confidence-interval script v2 source/caveat spot-check v0

Status: **script-source spot-check only; not a render, caption, audio, thumbnail,
Studio, peer-review, publish-gate, or upload approval.**

Script checked:
[`day416_confidence_intervals_script_v2.md`](day416_confidence_intervals_script_v2.md)

Source/control files checked against:

- [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)
- [`day416_confidence_intervals_source_excerpts_v0.md`](day416_confidence_intervals_source_excerpts_v0.md)
- [`day416_confidence_intervals_number_validation_v0.md`](day416_confidence_intervals_number_validation_v0.md)
- [`day416_confidence_intervals_render_spec_v0.md`](day416_confidence_intervals_render_spec_v0.md)

## Result

No v2 script line was found that changes the approved source boundary from the
source-claim map. The v2 wording changes are confined to the final checklist and
do not alter the Gemini, Claude, or Kimi example numbers.

## Spot-check table

| v2 script element | Spot-check decision | Notes |
|---|---|---|
| Gemini example `+0.29`, interval `+0.14` to `+0.45` | Source-bounded | Matches the paired SELF-OTHER label-gap example in the source map. The script says `one paired slice` and `specific paired comparison`, and it does not generalize to all judges. |
| Claude example `+0.12`, interval from slightly below zero to `+0.30` | Source-bounded | Matches the source-map row. The script explicitly says crossing zero does not prove no effect. |
| Kimi example about `+0.01` with negative and positive interval values | Source-bounded | Matches the source-map row. The script explicitly avoids the forbidden claim `Kimi has no label bias`. |
| Hypothetical `+0.50` action threshold | Properly labeled | The script immediately says the threshold is illustrative and not from the study. |
| Design-caveat scene | Properly bounded | The script says the interval does not remove questions about prompt set, paired slice, judge family, scoring rubric, or decision context. |
| Scene 07 checklist wording | Improved but still needs future review | `What range has this analysis not ruled out?` is safer than a bare formal-probability reading. `action line` is more conversational than `decision threshold`, but future visuals should still label it as a threshold/line so the concept is clear. |

## Remaining risks for any future render

- Keep the `+0.50` line visibly labeled as hypothetical / not from the study.
- Do not let visual labels imply Gemini proves universal self-preference.
- Do not let the Kimi scene imply no bias, lower quality, or a model ranking.
- Do not shorten the description in a way that drops the one-study / one-slice
  caveat.
- Re-run number validation after any source-number, render-spec, or visual-axis
  change.

## Gate reminder

The current confidence-interval packet remains a future concept only:

```text
No render exists. Audio review impossible. Do not upload.
```
