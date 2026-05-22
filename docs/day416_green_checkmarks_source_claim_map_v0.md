# Day 416 green-checkmarks source-claim map v0

Status: source-bounding review only. Not upload approval, not audio approval, and
not final metadata approval.

## Scope

Mapped the active script:

```text
docs/day414_green_checkmarks_script_v4.md
```

against the primary source repository:

```text
/home/computeruse/pr-drift-safety-study
https://github.com/ai-village-agents/pr-drift-safety-study
```

Checked source state:

```text
8aa5aab Add PR drift visual appendix
```

Files checked:

```text
README.md
DATA_CARD.md
results/descriptive_report.md
results/model_outcomes.md
docs/case_studies.md
```

## Source snippets reverified on Day 416

The checked source includes:

- `README.md`: exploratory status, weak-supervision warning, 610 PR records,
  356 merged / 253 closed unmerged / 1 open, 58.4% merge rate, 144 PR heads not
  descendants of recorded base, stale two-dot diffs as triage signals rather
  than automatic failure labels, and git-augmented in-sample AUC as a
  reconstruction sanity check rather than a deployable classifier.
- `DATA_CARD.md`: 610-PR snapshot and weak-supervision caveat.
- `results/descriptive_report.md`: local git metrics, 144 non-descendant heads,
  maximum local-git deletion count 48,969, and repeated triage-not-label caveat.
- `docs/case_studies.md`: PR #433 case-study note that checks passed and the PR
  was mechanically mergeable, but the two-dot diff inserted new entries before
  an already-merged tail; also a deletion-count caveat.

## Claim map

| Script claim or implication | Source basis | Status |
|---|---|---|
| A green check is useful evidence, not a verdict. | Practical framing derived from CI/check semantics plus PR-drift examples. | Safe as a metaphor, not a measured empirical claim. |
| A check usually means this check passed, on this version, under these conditions. | General interpretation of automated check results; consistent with PR-drift stale-base examples. | Safe if phrased as “usually” and “this check,” as in the script. |
| Fresh base matters because a target branch can move while a PR waits. | `README.md` and `results/descriptive_report.md` discuss stale two-dot diffs and non-descendant PR heads in a high-velocity repo. | Safe with caveat that stale is a triage signal, not automatic failure. |
| The study covered 610 pull requests. | `README.md`, `DATA_CARD.md`, and `results/descriptive_report.md`. | Directly sourced. |
| In 144 cases, the head did not descend from the recorded base. | `README.md` and `results/descriptive_report.md`. | Directly sourced. |
| That does not prove those branches were unsafe. | Source caveat: stale/two-dot diffs are triage signals, not automatic failure labels. | Required caveat; keep. |
| The base relationship was a useful place to look. | Source frames local git metrics as sharpening stale-branch picture and as triage signals. | Safe as “place to look,” not “proof.” |
| Right diff matters; a file list or memory preview is not today's merge diff. | Practical conclusion from stale-base/diff reconstruction and case-study framing. | Safe as review advice, not a measured claim. |
| One case appendix PR was mechanically mergeable with passing checks but had a narrower ordering problem. | `docs/case_studies.md` PR #433. | Safe if attributed as case-study/reviewer note; do not claim CI failed unless verified. |
| The diff inserted entries before an already-merged tail, shifting intended numbering rather than appending after current main. | `docs/case_studies.md` PR #433. | Directly sourced as a case-study summary. |
| Some failures are easy for automation to see; others are about meaning. | Conceptual review distinction illustrated by PR #433 and related source-layout/stale cases. | Safe as explanatory framing, not a universal theorem about CI. |
| Stale branch, large deletion count, and passing check are signals, not verdicts. | `README.md`, `results/descriptive_report.md`, and `docs/case_studies.md` caveats. | Directly aligned with source caveats. |
| The three-question checklist is useful review habit. | Authorial synthesis from source examples. | Safe only as habit/advice; not a guarantee. |
| Asking an AI assistant about version, base branch, diff, uninspected risks, and remaining human decision can slow the moment down. | Practical workflow recommendation; not tested by the PR-drift study. | Safe if not presented as proven to prevent errors. |

## Claims deliberately excluded

The current script does not use:

- the memory-only Luminous Index stale-base anecdote;
- deployable model-prediction claims;
- universal claims about all stale branches being unsafe;
- claims that CI cannot catch semantic risk;
- claims that this checklist prevents bad merges.

## Metadata implication

The required source caveat remains necessary in any future public description:

```text
This video uses a public AI Village pull-request trace as a concrete example.
The PR-drift study is exploratory: keyword labels are weak supervision, model
results are descriptive and in-sample, and stale or deletion-heavy diffs are
triage signals rather than automatic safety labels. The checklist is a review
habit, not a guarantee.
```

## Decision

The active script remains within the checked source boundaries if the caveats
stay visible and the excluded claims stay excluded. This source-claim map does
not close the upload gate.

```text
Audio review incomplete. Do not upload.
```
