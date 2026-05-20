# Day 414 outline v0 — Why Green Checkmarks Can Still Hide Risky Changes

Status: outline only. Not a script, not a render plan, and not upload approval.

Planning inputs:

- [`day414_green_checkmarks_creative_brief_v0.md`](day414_green_checkmarks_creative_brief_v0.md)
- [`day414_green_checkmarks_source_notes_v0.md`](day414_green_checkmarks_source_notes_v0.md)

## Working title

Why Green Checkmarks Can Still Hide Risky Changes

Alternate titles:

1. A Green Check Is a Receipt, Not a Verdict
2. What Did This Green Check Actually Prove?
3. Before You Trust a Passing Check, Ask These Three Questions
4. Green Checks, Stale Branches, and the Diff You Forgot to Read

Current preference: **A Green Check Is a Receipt, Not a Verdict**. It is warmer and less fear-based than "hide risky changes," while keeping the core metaphor.

## Viewer promise

After this video, you will have a three-question habit for reading automated checks:

```text
Fresh base.
Right diff.
Uncovered risk.
```

A check can be correct and still too narrow for the decision you are about to make.

## Target length

4.5 to 6 minutes. This should be shorter than the thinking-partner candidate and more concrete.

## Tone

Calm, practical, non-cynical. The point is not "do not trust automation." The point is "read the label on the signal before treating it like approval."

## Cold open

Visual: a large green checkmark with the words:

```text
All checks passed.
Ready to merge?
```

Narration idea:

> A green checkmark is one of the most comforting shapes in software. It says: the build passed, the tests passed, the robot is happy.
>
> But it does not say: this is safe to merge.
>
> It says something narrower: this check passed, on this version, under these conditions.
>
> That difference matters.

Immediate title card:

```text
A green check is a receipt, not a verdict.
```

## Section 1 — What a green check actually proves

Goal: make the narrowness of the signal intuitive.

Visual: the green check expands into a receipt:

```text
Command: tests passed
Commit: abc123
Base: main at 10:14
Scope: files the test covered
```

Narration beats:

- A check result is valuable because it is specific.
- It is also limited because it is specific.
- The viewer should ask: what version, what diff, what test scope?

Key line:

> The mistake is not trusting the check. The mistake is forgetting what question the check answered.

## Section 2 — Fresh base

Question:

```text
Did the check run against the target I am about to merge or deploy into?
```

Visual: two branch lines. The check runs when `main` is at one point; then `main` moves forward before the merge decision.

Example source boundary:

- Use the PR-drift study as motivation: in the checked Universe sprint trace, local reconstruction found **144** PR heads that were not descendants of their recorded base.
- Explain that this is a triage signal, not proof that every such PR was unsafe.

Narration beats:

- In a fast-moving repo, the base branch can move after a check runs.
- A result can be true about yesterday's target and incomplete for today's target.
- This is why fresh fetch, rebase/merge-update checks, or explicit base confirmation matter.

Potential concrete case:

- PR #503 from the case-study appendix: reviewer-documented stale-branch risk where current main had moved far beyond the branch and the diff would delete newer content and a validator guard.
- Use only if the script needs one concrete stale-base example.

Key line:

> Green on an old base is not bad evidence. It is dated evidence.

## Section 3 — Right diff

Question:

```text
Did the check inspect the exact change that will land?
```

Visual: left panel "the diff I remember"; right panel "the diff that will merge." Highlight a shifted insertion or unexpected deletion.

Example source boundary:

- PR #433 from the case-study appendix: checks passed and the PR was mechanically mergeable, but a reviewer noted that the two-dot diff inserted new entries before an already-merged tail, shifting intended numbering rather than appending after current main.
- Say "the case-study appendix records" or "a reviewer noted," because these notes are illustrative, not final manual adjudications.

Narration beats:

- A file list is not the same as the actual change set.
- A small-looking PR can land in the wrong place if the surrounding file moved.
- Read the actual diff that corresponds to the merge decision, not a stale preview.

Key line:

> The green check may be attached to a real diff. Just make sure it is the diff you are about to ship.

## Section 4 — Uncovered risk

Question:

```text
What important failure could still happen even if this check result is correct?
```

Visual: risk ledger with three columns:

```text
Checked                Not checked                 Human decision
syntax/test command    domain invariant             does this matter?
changed files          recent surrounding work       is the risk acceptable?
mechanical merge       user-visible effect           should we wait or inspect?
```

Example source boundary:

- PR #555 illustrates a source-layout invariant issue: `x/y/z` fields instead of required `position: [x, y, z]`, later compounded by same-slot stale/replacement risk.
- Use only as a compact example. Avoid a long internal postmortem.

Narration beats:

- Many important risks are outside generic tests: permissions, deletion, ordering, user-visible language, data migration, hidden invariants.
- The reviewer does not need to distrust the check. The reviewer needs to name what the check did not inspect.
- This is where human judgment belongs.

Key line:

> The most useful question is not, "Did the robot approve?" It is, "What would still worry me if the robot is right?"

## Section 5 — Signals are not verdicts

Purpose: prevent overclaiming and avoid making viewers afraid of every green check.

Visual: two examples on a balance:

```text
Triage signal ≠ failure label
Passing test ≠ safety proof
```

Source caveat:

- The PR-drift study explicitly treats stale diffs, non-descendant heads, deletion counts, and keyword labels as triage signals.
- High deletion counts are not automatically failures; PR #222 had 1,508 deletions in `main.js`, merged, and had no collected risk comment.

Narration beats:

- A stale signal tells you where to look.
- A large deletion count tells you to ask what changed and why.
- A passing check tells you a specific automated question got a positive answer.
- None of these should replace review.

Key line:

> The answer is not to ignore green checks. The answer is to stop asking them to be oracles.

## Section 6 — The checklist

Visual: final three-card checklist.

```text
Fresh base
Did the check run against the target I am about to merge or deploy into?

Right diff
Did it inspect the exact change that will land?

Uncovered risk
What important failure could still happen even if this check result is correct?
```

Optional AI-assistant prompt:

```text
Before I treat this automated check as approval, help me verify three things:

1. What exact version, base branch, and diff did the check run on?
2. What files, behaviors, or risks did the check not inspect?
3. What human decision remains even if the check result is correct?

Then summarize whether the green check is strong evidence, weak evidence, or irrelevant evidence for the decision I am about to make.
```

Narration beats:

- You can use this with code review, generated code, benchmark dashboards, document approvals, or any automated green light.
- It slows you down just enough to keep the signal in its lane.

## Ending

Visual: green check remains, now labeled:

```text
Useful signal.
Limited scope.
Human decision.
```

Narration idea:

> Keep the green check. It is useful.
>
> Just read it like a receipt.
>
> What version did it check? What diff did it inspect? What risk did it leave uncovered?
>
> A passing check can help you move faster. But the decision still belongs to the person who knows what failure would cost.

## Source caveat for description

This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

## Production notes for a future script

- Keep on-screen numbers minimal: 610 PRs, 144 non-descendant heads, maybe 20.3% keyword-risk labels.
- Avoid showing many PR numbers in the main video. One or two examples are enough.
- Use schematics over terminal dumps.
- If citing the Luminous Index lesson, inspect the repo first and use exact wording from a committed note.
- Do not claim the PR-drift model predicts safety. It predicts observed outcomes/comment labels in this trace.

## Gate before rendering

Before any render work:

- [ ] Choose final title.
- [ ] Decide whether to include PR #433, PR #503, or both.
- [ ] Verify the Luminous Index stale-base lesson from committed files if used.
- [ ] Draft a script that preserves the source caveat.
- [ ] Produce at least one visual proof for phone readability.
- [ ] Generate captions from the final narration and run structural audits.
- [ ] Require full watch/listen and in-motion caption review before upload.
