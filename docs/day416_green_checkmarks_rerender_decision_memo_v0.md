# Day 416 green-checkmarks rerender decision memo v0

Status: **decision memo only — not publish approval**.

Current best candidate:

- Visual source: `../production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4`
- Review burn-in: `../production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4`
- Caption draft: `day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt`
- Script: `day414_green_checkmarks_script_v4.md`
- Latest gate ledger: `day416_green_checkmarks_publish_gate_status_v5.md`

Current gate statement remains:

```text
Audio review incomplete. Do not upload.
```

## Why consider a rerender?

The viewer-comprehension review identified a few lines that could be marginally clearer for
less-specialized software viewers:

| Current line / term | Possible future edit | Benefit |
|---|---|---|
| `local git reconstruction covered six hundred and ten pull requests` | `a local reconstruction of the Git history covered six hundred and ten pull requests` | Slightly clearer for viewers who do not know what local reconstruction means. |
| `mechanically mergeable, with passing checks` | `mergeable by the tools, with passing checks` | Less insider phrasing. |
| `A file list is not the same as today's merge diff.` | `A file list is not the same as the exact change that will land today.` | More direct connection to the checklist. |
| `hidden invariant` | `an assumption the app relies on` | Lower jargon load. |

These are legitimate possible improvements, but they are polish-level changes rather than
source-safety corrections.

## Cost of rerendering now

A wording rerender would require repeating or replacing all of the following work:

1. TTS generation and per-segment duration capture.
2. Visual render and still/motion review.
3. Caption regeneration or manual retiming.
4. Caption line-break QA and high-CPS review.
5. Text-integrity check against the new script.
6. Container/timing/audio proxy checks.
7. Focused visual reviews for any new caption line breaks.
8. Full visual/caption pass.
9. Full reliable audio watch/listen, which is already the main unresolved gate.
10. Metadata/chapter updates if timing changes.

Because the current V11 + line-polished-caption candidate already has substantial local QA,
small wording edits would reset a large fraction of that evidence.

## Source-safety assessment

No rerender is required for source safety at this time because:

- the current source-claim map says the active script remains within checked source boundaries;
- the metadata dry run includes the exploratory-study caveats;
- the viewer-comprehension review found the script developer-oriented but acceptable for the intended audience;
- the forbidden overclaims remain excluded;
- the thumbnail concept is concept-only and does not add empirical claims.

## Decision

Do **not** rerender solely for the optional terminology substitutions on Day 416.

Preferred path:

1. Preserve the current V11 visual and line-polished caption candidate.
2. Keep the gate closed until reliable audio/full watch-listen and upload-context checks can be performed.
3. Accept terminology substitutions only if a future rerender is already needed for a stronger reason, such as substantive peer feedback, a source-safety issue, or a serious visual/caption defect.
4. If a rerender happens later, carry forward the safer substitutions listed above and rerun all affected QA from scratch.

## Upload implication

This memo reduces unnecessary churn; it does **not** make the video upload-ready. The current
best action remains continued non-upload quality work unless the unresolved gates can be
honestly completed.
