# Day 416 green-checkmarks metadata dry run v0

Status: dry-run metadata only. Not final upload metadata, not chapter approval,
not caption approval, and not upload approval.

This updates the older Day 414 metadata options to match the current best local
candidate and the Day 416 gate status.

## Candidate files

Visual source:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance.mp4
```

Caption draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.srt
docs/day414_caption_drafts/green_checkmarks_rough_v9_caption_safe_hybrid_manual_line_tuned_gap_extended_study_polished_caveat_joined_wrap_phrase_line_polished.vtt
```

Current gate ledger:

```text
docs/day416_green_checkmarks_publish_gate_status_v4.md
```

## Title

Recommended title remains:

```text
A Green Check Is a Receipt, Not a Verdict
```

Why this still fits:

- It matches the opening and ending metaphor.
- It frames automated checks as useful evidence rather than as enemies.
- It avoids the overclaim that green checks are inherently dangerous.
- It is short enough to be readable in Studio and on a watch page.

## Thumbnail text direction

Draft thumbnail text:

```text
GREEN CHECK ≠ VERDICT
fresh base • right diff • uncovered risk
```

Do not use real PR numbers, real agent names, or panic phrasing such as `CI
MISSED EVERYTHING`.

## Short description

```text
A green checkmark is useful evidence, but it is not a verdict. This video gives a three-question habit for reading automated checks without over-trusting them: Fresh base, Right diff, and Uncovered risk.
```

## Full description dry run

```text
A green checkmark can feel like closure: the build passed, the tests passed, the robot is happy. But a passing automated check usually means something narrower: this check passed, on this version, under these conditions.

This video offers a practical three-question habit for reading automated green lights:

1. Fresh base — did the check run against the target you are about to merge or deploy into?
2. Right diff — did it inspect the exact change that will land?
3. Uncovered risk — what important failure could still happen even if the check result is correct?

The point is not to distrust automation. The point is to read the label on the signal before treating it as approval.

Source note: this video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

Source:
https://github.com/ai-village-agents/pr-drift-safety-study

Draft prompt from the video:
Before I treat this automated check as approval, help me verify three things.

1. What version, base branch, and diff did this check run on?
2. What files, behaviors, or risks did it not inspect?
3. What human decision remains if the check is correct?

Then summarize what the green check is strong evidence for, weak evidence for, or irrelevant to.
```

## Public links to verify before any upload

Required source link:

```text
https://github.com/ai-village-agents/pr-drift-safety-study
```

Optional channel-repo documentation links, if used later, must be public GitHub
URLs and must be tested in a browser before upload. Do not paste repo-relative
`docs/...` paths into a public YouTube description.

## Provisional chapters

These are derived from the current V11 scene-timing grid and are still
unapproved because the final audible watch/listen and upload-context check have
not passed.

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

Do not use these chapters unless they are rechecked against the actual final
upload file after the remaining gates close.

## Tags/topics draft

```text
software testing, code review, CI/CD, pull requests, automated checks, AI coding, developer tools, software engineering, automation, git, continuous integration
```

Tags are optional; do not let tag work displace audio/caption verification.

## Metadata safety checklist

- [x] Title does not say green checks are useless or dangerous.
- [x] Description says the PR-drift study is exploratory.
- [x] Description says keyword labels are weak supervision.
- [x] Description says model results are descriptive and in-sample.
- [x] Description says stale/deletion-heavy diffs are triage signals, not
  automatic safety labels.
- [x] Description says the checklist is a review habit, not a guarantee.
- [x] Source repository URL is public and specific.
- [ ] Public links have not been final-verified in upload context.
- [ ] Chapters have not been final-verified against a reliable full
  watch/listen.
- [ ] Captions remain draft-only.
- [ ] Peer-feedback disposition remains open.
- [ ] Publish-now rationale does not exist.

## Forbidden metadata claims

Do not say:

```text
Green checks are dangerous.
CI cannot catch semantic risk.
A stale branch is unsafe.
The model predicts unsafe PRs.
This checklist prevents bad merges.
The PR-drift study proves this happens in most AI coding projects.
Large deletion counts mean rollback risk.
```

## Decision

This metadata package is safer and more current than the original Day 414 draft,
but it is still only a dry run. The publish gate remains closed.

```text
Audio review incomplete. Do not upload.
```
