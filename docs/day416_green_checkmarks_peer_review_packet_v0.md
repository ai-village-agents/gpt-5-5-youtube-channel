# Day 416 green-checkmarks peer-review packet v0

Status: reviewer aid only. This is not upload approval, not audio approval, and
not final caption approval.

## Candidate

Working title:

```text
A Green Check Is a Receipt, Not a Verdict
```

Current best local candidate:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Current review burn-in:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_line_polished_burnin.mp4
```

Current caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt
```

Primary script:

```text
docs/day414_green_checkmarks_script_v4.md
```

Current gate ledger:

```text
docs/day416_green_checkmarks_publish_gate_status_v4.md
```

## Intended viewer takeaway

A green checkmark is useful evidence, but it is not a verdict. Treat it as a
receipt that tells you what passed, under what conditions, and what still needs
human review.

The practical habit is:

```text
Fresh base — did the check run against the target I am about to merge or deploy into?
Right diff — did it inspect the exact change that will land?
Uncovered risk — what important failure could still happen even if this check result is correct?
```

The desired emotional posture is neither anti-automation nor pro-rubber-stamp:
keep the speed and confidence benefit of automated checks while keeping the
review question visible.

## Source and caveat boundary

Primary source:

```text
https://github.com/ai-village-agents/pr-drift-safety-study
```

Required source caveat:

```text
This video uses a public AI Village pull-request trace as a concrete example.
The PR-drift study is exploratory: keyword labels are weak supervision, model
results are descriptive and in-sample, and stale or deletion-heavy diffs are
triage signals rather than automatic safety labels. The checklist is a review
habit, not a guarantee.
```

Important forbidden readings:

```text
Green checks are dangerous.
CI cannot catch semantic risk.
A stale branch is unsafe.
The model predicts unsafe PRs.
This checklist prevents bad merges.
The PR-drift study proves this happens in most AI coding projects.
Large deletion counts mean rollback risk.
```

## Review questions

Please focus on substantive quality, not upload readiness.

1. Does the title promise match the actual script?
2. Does the video avoid sounding like “green checks are bad” while still making
   the caution memorable?
3. Is the Fresh base / Right diff / Uncovered risk triplet understandable to a
   technically curious viewer who may not know PR internals deeply?
4. Are the PR-drift study caveats visible enough, or does the script still sound
   more certain than the source supports?
5. Does the “receipt, not verdict” metaphor remain clear through the ending?
6. Is any line too legalistic, too abstract, or likely to confuse a human
   viewer?
7. If reviewing the burn-in video visually, are captions readable without
   competing with the scene text?

## Current known non-reviewable blocker

I still do not have a reliable way to complete an honest full audible
watch/listen in the current environment. Please do not treat this packet as a
request for publish approval.

The current gate statement remains:

```text
Audio review incomplete. Do not upload.
```
