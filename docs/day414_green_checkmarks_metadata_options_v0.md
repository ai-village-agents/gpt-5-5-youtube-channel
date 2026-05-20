# Day 414 metadata options v0 — Green checkmarks candidate

Status: draft metadata only. Not final, not upload approval, and not evidence of a rendered video.

Active draft script: [`day414_green_checkmarks_script_v1.md`](day414_green_checkmarks_script_v1.md)

## Recommended title

A Green Check Is a Receipt, Not a Verdict

Why this is preferred:

- It is concrete and memorable.
- It does not sound anti-automation.
- It matches the script's opening and ending metaphor.
- It is less fear-based than "Why Green Checkmarks Can Still Hide Risky Changes."

Risk:

- Viewers unfamiliar with CI/code review may not immediately know this is about automated checks. The thumbnail or first description sentence should clarify.

## Alternate titles

1. What Did This Green Check Actually Prove?
2. Before You Trust a Passing Check, Ask These Three Questions
3. Green Checks, Stale Branches, and the Diff You Forgot to Read
4. Why Passing Tests Are Evidence, Not Approval
5. The Three Questions I Ask Before Trusting a Green Check

## Thumbnail concept

Primary text:

```text
GREEN CHECK ≠ VERDICT
```

Secondary text:

```text
fresh base • right diff • uncovered risk
```

Visual:

- Big green check on the left.
- Receipt card on the right with three fields:
  - version
  - diff
  - scope
- No real code, PR numbers, or agent names.

Caveat:

- Do not imply green checks are bad. The visual should make the check look useful but limited.

## Short description option

A green checkmark is useful evidence, but it is not a verdict. This video gives a three-question habit for reading automated checks without over-trusting them: Fresh base, Right diff, and Uncovered risk.

## Full description draft

A green checkmark feels like closure: the build passed, the tests passed, the robot is happy. But a passing automated check usually means something narrower: this check passed, on this version, under these conditions.

This video offers a practical three-question habit for reading automated green lights:

1. **Fresh base** — did the check run against the target you are about to merge or deploy into?
2. **Right diff** — did it inspect the exact change that will land?
3. **Uncovered risk** — what important failure could still happen even if the check result is correct?

The point is not to distrust automation. The point is to read the label on the signal before treating it as approval.

Source note: this video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

Draft prompt from the video:

```text
Before I treat this automated check as approval, help me verify three things.

1. What version, base branch, and diff did this check run on?
2. What files, behaviors, or risks did it not inspect?
3. What human decision remains even if the check result is correct?

Then summarize whether the green check is strong evidence, weak evidence, or irrelevant evidence for the decision I am about to make.
```

## Source links to include if published

- PR-drift study repository: `https://github.com/ai-village-agents/pr-drift-safety-study`
- Source notes for this video candidate in the channel repository, if public repository links are appropriate after publication: `docs/day414_green_checkmarks_source_notes_v0.md`

Before upload, replace repo-relative links with public GitHub URLs and verify they resolve.

## Chapter draft

These are provisional and must be recalculated against any final rendered MP4:

```text
0:00 A green check is not a verdict
0:38 Fresh base
1:45 Right diff
2:45 Uncovered risk
3:35 Signals are not verdicts
4:05 The three-question checklist
4:45 Let it speed up the review
```

Do not use these chapters without checking final render timings.

## Tags / topics draft

Potential tags, if useful in Studio:

```text
software testing, code review, CI/CD, pull requests, automated checks, AI coding, developer tools, software engineering, automation, git, continuous integration
```

## Metadata source-caveat checklist

Before any upload:

- [ ] Title does not imply green checks are useless or dangerous by default.
- [ ] Description says the PR-drift study is exploratory.
- [ ] Description says keyword labels are weak supervision.
- [ ] Description says stale/deletion-heavy diffs are triage signals, not automatic safety labels.
- [ ] Description says the checklist is a review habit, not a guarantee.
- [ ] Public links resolve to the intended source repository or docs.
- [ ] Chapters match the final rendered MP4, not this draft.
- [ ] Caption file is generated from final narration, not this draft by assumption.
- [ ] Full watch/listen and in-motion caption review have passed.
- [ ] Publish log, if used, distinguishes Studio-confirmed facts from public endpoint lag.

## Forbidden metadata claims

Do not say:

- green checks are dangerous;
- CI cannot catch semantic risk;
- stale branches are unsafe;
- the PR-drift model predicts unsafe PRs;
- the checklist prevents bad merges;
- the PR-drift study proves this happens in most AI coding projects;
- large deletion counts mean rollback risk.

## Gate state

No render exists for this candidate. No captions, watch/listen pass, or final metadata review exists.

Do not upload.
