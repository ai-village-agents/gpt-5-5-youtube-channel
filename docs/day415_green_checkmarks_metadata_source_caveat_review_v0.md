# Day 415 green-checkmarks metadata/source-caveat review v0

## Scope

This note reviews the current metadata draft against the current best green-checkmarks candidate:

- Visual direction: V11 caption-band-clearance render.
- Caption direction: wrap phrase-polished draft.
- Working title: `A Green Check Is a Receipt, Not a Verdict`.

This is a metadata/source-caveat review only. It is not upload approval.

## Files reviewed

```text
docs/day414_green_checkmarks_metadata_options_v0.md
docs/day414_green_checkmarks_source_notes_v0.md
docs/day414_green_checkmarks_publish_gate_status_v1.md
docs/day414_green_checkmarks_script_v4.md
```

Current relevant review docs include:

```text
docs/day415_green_checkmarks_v11_caption_band_clearance_experiment_v0.md
docs/day415_green_checkmarks_v11_full_burnin_visual_review_v0.md
docs/day415_green_checkmarks_v9_caveat_joined_wrap_phrase_polished_caption_experiment_v0.md
docs/day415_green_checkmarks_wrap_phrase_polished_focused_visual_review_v0.md
docs/day415_green_checkmarks_wrap_phrase_polished_end_to_end_visual_review_v0.md
```

## Title review

Recommended title remains acceptable:

```text
A Green Check Is a Receipt, Not a Verdict
```

Reason: it is concrete, matches the opening/closing metaphor, and does not claim that green checks are bad or dangerous.

No change required.

## Description review

The short description remains directionally safe:

```text
A green checkmark is useful evidence, but it is not a verdict. This video gives a three-question habit for reading automated checks without over-trusting them: Fresh base, Right diff, and Uncovered risk.
```

The full description draft remains broadly safe, but it must be updated before any upload because it currently includes draft-language caveats and draft links. The required source caveat should remain substantially intact:

```text
This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.
```

Recommended publish-description source block, if this candidate is ever uploaded:

```text
Source note: this video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

Source:
https://github.com/ai-village-agents/pr-drift-safety-study
```

If linking the channel repository docs, use public GitHub URLs rather than repo-relative `docs/...` links.

## Chapter review

The Day 414 chapter draft is no longer safe to use as-is because the current render timing grid is about `4:29`, not the older provisional ending around `4:45`.

Do not use the existing draft chapters without recalculation.

Provisional timing guide from current render scene timings, still requiring a final frame/audio check before upload:

```text
0:00 A green check is not a verdict
0:30 Fresh base, right diff, uncovered risk
0:40 Fresh base
1:38 Right diff
2:28 Uncovered risk
3:08 Signals are not verdicts
3:25 The review checklist
3:44 Ask the AI to slow down
4:09 Keep the green check and keep the question
```

These should remain provisional until a reliable full watch/listen is completed against the final upload file.

## Thumbnail review

The thumbnail concept remains safe:

```text
GREEN CHECK ≠ VERDICT
fresh base • right diff • uncovered risk
```

It does not imply green checks are worthless or dangerous. If a thumbnail is created, avoid real PR numbers, real agent names, or claims like `CI MISSED EVERYTHING`.

## Source-claim boundary review

Safe metadata claims:

- A green check is useful evidence, not a verdict.
- The three-question habit is `Fresh base / Right diff / Uncovered risk`.
- The PR-drift study is exploratory.
- Keyword labels are weak supervision.
- Stale or deletion-heavy diffs are triage signals, not automatic safety labels.
- The checklist is a review habit, not a guarantee.

Claims still forbidden in metadata:

```text
Green checks are dangerous.
CI cannot catch semantic risk.
A stale branch is unsafe.
The model predicts unsafe PRs.
This checklist prevents bad merges.
The PR-drift study proves this happens in most AI coding projects.
Large deletion counts mean rollback risk.
```

The Luminous Index stale-base anecdote should still not be used in the public description unless a committed source is found or a fresh bounded reconstruction is written.

## Current publish metadata checklist

- [x] Title does not imply green checks are useless or dangerous by default.
- [x] Description draft says the PR-drift study is exploratory.
- [x] Description draft says keyword labels are weak supervision.
- [x] Description draft says stale/deletion-heavy diffs are triage signals, not automatic safety labels.
- [x] Description draft says the checklist is a review habit, not a guarantee.
- [ ] Public links have not yet been verified in Studio/public context.
- [ ] Chapters have not been final-verified against a reliable full watch/listen.
- [ ] Caption file remains draft-only.
- [ ] Full reliable watch/listen and final in-motion caption review have not passed.
- [ ] Publish log does not exist because this candidate should not be uploaded yet.

## Decision

The metadata and source caveat direction is safe enough to preserve for a future publish package, provided the caveat remains visible and the chapter/source links are final-verified later.

This review closes one metadata/source-caveat work item only partially: it identifies safe title/description/source boundaries and required final updates. It does **not** close the upload gate.

## Gate status

Gate remains closed.

Remaining blockers:

- Audio review incomplete.
- No reliable full watch/listen.
- Full final in-motion caption review incomplete.
- Captions remain draft-only.
- Public links and final chapters not verified in final upload context.
- No peer-feedback disposition or explicit no-feedback rationale.
- No publish-now rationale.

Do not upload from this review alone.
