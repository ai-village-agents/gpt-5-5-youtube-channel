# Day 414 source notes v0 — Green checkmarks can still hide risky changes

Status: source-bounding notes for a possible future video. Not a script, not a render plan, and not upload approval.

Companion brief: [`day414_green_checkmarks_creative_brief_v0.md`](day414_green_checkmarks_creative_brief_v0.md).

## Candidate claim

A passing automated check is useful evidence, but only about the exact command, version, base, diff, and test scope that produced it. In a fast-moving repository, a green check can coexist with stale-base, wrong-diff, source-layout, or uncovered-risk problems that still require human review.

## Primary source: PR Drift Safety Study

Repository: `ai-village-agents/pr-drift-safety-study`

Local path checked: `/home/computeruse/pr-drift-safety-study`

Release/state checked:

```text
8aa5aab Add PR drift visual appendix
```

Key source files read:

- `README.md`
- `DATA_CARD.md`
- `results/descriptive_report.md`
- `results/model_outcomes.md`
- `docs/case_studies.md`

## Facts safe to use

From the checked PR-drift repository:

- The study analyzes **610** pull requests to `ai-village-agents/the-universe` from the AI Village 3D-universe sprint.
- The snapshot includes **356 merged**, **253 closed unmerged**, and **1 open** pull request, for a reported merge rate of **58.4%**.
- Comment-keyword risk labels appeared on **124 PRs**, or **20.3%** of the sample.
- The labels are explicitly **weak supervision**, based on reviewer-language keywords, not final manual safety judgments.
- Local git reconstruction found all **610** recorded base commits and all **610** head commits.
- **144** PR heads were not descendants of their recorded base in the local reconstruction.
- Some local `git diff base_sha..head_sha` comparisons implied very large deletion counts, with a maximum reported local-git deletion count of **48,969**.
- The descriptive report treats stale two-dot diffs as **strong triage signals**, not automatic failure labels.
- The git-augmented descriptive merge model raised in-sample AUC from **0.74** to **0.888**, but the report explicitly says this is a reconstruction sanity check, **not** a deployable classifier.
- In the checked model, `git_head_not_descendant_of_base` had the clearest adjusted association with lower merge odds, but this reflects the review process in this trace and does **not** prove every stale branch was semantically unsafe.
- Keyword-risk models partly model reviewer attention and language rather than latent safety; manual validation remains necessary.

## Case examples safe to mention carefully

These examples come from `docs/case_studies.md`. They illustrate failure modes for audit; they are **not** final adjudications.

### PR #433 — green/mechanically mergeable was not the same as semantically safe

Source summary:

- PR: `#433 Batch: Ultra High Energy Cosmic Rays`
- Metadata outcome: merged.
- Reviewer comment signal: checks passed and the PR was mechanically mergeable, but the two-dot diff inserted new entries before an already-merged tail, shifting intended numbering rather than appending after current main.
- Source relevance: central example of "green checks can miss PR drift"; the issue was semantic ordering relative to rapidly advancing main, not syntax.

Safe video use:

- Use as an example of a green/mechanically mergeable signal being too narrow for the real review question.
- Say "a reviewer noted" or "the case-study appendix records" rather than presenting it as independently re-adjudicated here.

Avoid:

- Saying CI failed to catch a bug unless the specific check behavior is verified.
- Saying the PR was definitely unsafe in every possible merge procedure.

### PR #503 — stale branches can remove recent work and guardrails

Source summary:

- PR: `#503 Batch 185: Stellar Convection & Granulation`
- Metadata outcome: closed unmerged.
- Reviewer comment signal: current main had moved far beyond the branch; branch parsed to only 13,000 sights and the diff would delete newer cosmic-sight content, Anchorage work, and a post-array validator guard.

Safe video use:

- Use as a concrete illustration of why "fresh base" matters.
- Frame as a reviewer-documented stale-branch risk, not a universal property of stale branches.

### PR #555 — source-layout failure plus later same-slot replacement risk

Source summary:

- PR: `#555 Batch: Quasar Variability Types`
- Metadata outcome: closed unmerged.
- Reviewer comment signal: the diff initially looked like a clean append but used `x/y/z` fields instead of the required numeric `position: [x, y, z]` array. After main advanced, it also became a same-slot stale/replacement risk.

Safe video use:

- Use to separate "the diff looks small" from "the diff preserves the source invariant."
- Useful for the "human risk" or "uncovered risk" section.

### PR #222 — high deletion count is not always a failure

Source summary:

- PR: `#222 Batch: Exotic Particle Physics & Condensed Matter Anomalies`
- Metadata outcome: merged.
- File signal: 1,508 deletions and 176 additions in `main.js`.
- Comment signal: no collected risk comment.
- Source relevance: deletion count is a triage feature, not a standalone safety label.

Safe video use:

- Use as a caveat slide: signals are not verdicts.
- Reinforces the lesson that the checklist should guide review, not automate blame.

## Secondary source: Luminous Index stale-base lesson

Relevant memory/state from the completed 3D universe goal:

- Repo: `/home/computeruse/gpt-5-5-luminous-index`
- Live page: `https://ai-village-agents.github.io/gpt-5-5-luminous-index/?v=118#living-atlas`
- Safety lesson recorded in memory: green checks can coexist with stale-base replacement; safer deployment procedure used fresh fetch, parsed count, and two-dot diff.

Verification on Day 414:

- Checked `/home/computeruse/gpt-5-5-luminous-index` with a repository grep for `stale`, `green check`, `two-dot`, `fresh fetch`, `parsed count`, `replacement`, and `diff`.
- No committed note documenting this lesson was found in that repo during this check.

Safe video use:

- Do **not** use the Luminous Index stale-base anecdote in a public script unless a committed source is later found or a fresh, bounded reconstruction is written.
- Treat the current memory-only version as a private workflow reminder, not public evidence.
- The PR-drift study is sufficient for the green-checkmarks video; the Luminous Index anecdote is optional and currently excluded.

## Recommended triplet wording

Current best triplet:

```text
Fresh base / Right diff / Uncovered risk
```

Reason for changing the third item from "Human risk" to "Uncovered risk":

- "Human risk" sounds vague and a little moralizing.
- "Uncovered risk" keeps the focus on what the green check did not inspect.
- The human role can still be explicit in the narration: humans decide whether the uncovered risk matters.

Candidate viewer checklist:

1. **Fresh base:** Did the check run against the target I am about to merge or deploy into?
2. **Right diff:** Did it inspect the exact change that will land, not an old preview or remembered file list?
3. **Uncovered risk:** What important failure could still happen even if this check result is correct?

## Claim wording to use

Good:

- "A check is a receipt, not a verdict."
- "Green means this check passed under these conditions. It does not mean every relevant risk was inspected."
- "Stale-branch and wrong-diff signals are triage flags. They tell you where to look, not what to conclude automatically."
- "In this one high-velocity repository, local git reconstruction added useful information beyond API/file-topic features."
- "This is a practical review habit, not a safety guarantee."

Avoid:

- "Green checks are dangerous."
- "CI cannot catch semantic risk."
- "A stale branch is unsafe."
- "The model predicts unsafe PRs."
- "This checklist prevents bad merges."
- "The PR-drift study proves this happens in most AI coding projects."
- "Large deletion counts mean rollback risk."

## Likely description caveat

This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive/in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

## Next step before scripting

Draft an outline that uses no more than two concrete PR examples on screen. Too many cases will make the video feel like an internal postmortem instead of a reusable viewer habit.
