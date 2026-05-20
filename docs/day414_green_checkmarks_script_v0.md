# Day 414 script v0 — A Green Check Is a Receipt, Not a Verdict

Status: first script draft only. Not approved for rendering, upload, or publication.

Planning inputs:

- [`day414_green_checkmarks_creative_brief_v0.md`](day414_green_checkmarks_creative_brief_v0.md)
- [`day414_green_checkmarks_source_notes_v0.md`](day414_green_checkmarks_source_notes_v0.md)
- [`day414_green_checkmarks_outline_v0.md`](day414_green_checkmarks_outline_v0.md)

## Working title

A Green Check Is a Receipt, Not a Verdict

## Draft narration

A green checkmark is one of the most comforting shapes in software.

It says: the build passed. The tests passed. The robot is happy.

And if you are tired, or moving fast, it is easy to read that as a stronger sentence:

This is safe to merge.

But a green check usually means something narrower.

It means: this check passed, on this version, under these conditions.

That is useful. It is evidence.

But it is not a verdict.

By the end of this video, you will have three questions for reading an automated green light without asking it to do more than it can do:

Fresh base.

Right diff.

Uncovered risk.

First: what does the check actually prove?

Think of a passing check like a receipt.

A receipt does not say, "You made the best purchase."

It says: this item, at this time, under this transaction, went through.

A test result is similar.

It says: this command, against this commit, with this setup, returned success.

That specificity is why automated checks are valuable.

It is also why they have limits.

The mistake is not trusting the check.

The mistake is forgetting what question the check answered.

So the first question is: Fresh base.

Did the check run against the target you are about to merge or deploy into?

In a slow project, that may sound obvious.

In a fast-moving repository, the target branch can move while a pull request is waiting.

The check may have been true when main looked one way.

Then other work lands. The surrounding file changes. A validator appears. A slot that was empty becomes occupied.

Now the old green check is not useless.

But it is dated evidence.

In one exploratory AI Village pull-request study, local git reconstruction found six hundred and ten pull requests. One hundred forty-four pull-request heads were not descendants of their recorded base.

That does not prove that every one of those branches was unsafe.

It does mean the base relationship was a useful place to look.

A stale-base signal is a triage flag, not a final judgment.

It tells you to ask: did this pass against the code I am actually about to change?

The second question is: Right diff.

Did the check inspect the exact change that will land?

A file list is not the same as the diff you are about to ship.

A preview you remember is not the same as the current merge result.

In the PR-drift study's case-study appendix, one pull request is described as mechanically mergeable with passing checks. But a reviewer noted that its two-dot diff inserted new entries before an already-merged tail, shifting the intended numbering instead of appending after current main.

The issue was not that the code could not parse.

The issue was that the green signal was too narrow for the real review question.

The reviewer still had to ask: what change is actually landing, relative to the current target?

This is why "right diff" matters.

Do not only ask whether a check passed.

Ask what diff the check was attached to.

The green check may be attached to a real result. Just make sure it is attached to the result you are about to ship.

The third question is: Uncovered risk.

What important failure could still happen even if the check result is correct?

Some failures are easy for generic automation to see.

The file does not compile. The unit test fails. A required command exits with an error.

Other failures are about meaning.

Did this remove recent work?

Did it preserve the data shape the application expects?

Did it change permissions, user-visible wording, ordering, or a hidden invariant?

In another case from the same appendix, a pull request initially looked like a small append, but the entries used the wrong source layout: separate x, y, and z fields instead of the required position array.

That kind of problem is not solved by worshiping the green check or by ignoring it.

It is solved by naming what the check did not inspect.

The most useful question is not, "Did the robot approve?"

It is, "What would still worry me if the robot is right?"

This is also where the caveat matters.

Signals are not verdicts in either direction.

A stale branch is not automatically unsafe.

A large deletion count is not automatically a rollback risk.

A passing check is not automatically enough.

In the same exploratory trace, there was a merged pull request with more than fifteen hundred deletions in one file and no collected risk comment.

That does not mean big deletions are safe.

It means big deletions are something to inspect.

The lesson is not to replace one oracle with another.

The lesson is to keep every signal in its lane.

So before you treat a green check as approval, ask three things.

Fresh base: did the check run against the target I am about to merge or deploy into?

Right diff: did it inspect the exact change that will land?

Uncovered risk: what important failure could still happen even if this check result is correct?

If you are using an AI assistant during review, you can turn that into a prompt:

Before I treat this automated check as approval, help me verify three things.

What exact version, base branch, and diff did the check run on?

What files, behaviors, or risks did the check not inspect?

What human decision remains even if the check result is correct?

Then summarize whether the green check is strong evidence, weak evidence, or irrelevant evidence for the decision I am about to make.

That prompt will not make the decision safe by itself.

But it can slow the moment down just enough to keep the evidence visible.

Keep the green check.

It is useful.

Just read it like a receipt.

What version did it check?

What diff did it inspect?

What risk did it leave uncovered?

A passing check can help you move faster.

But the decision still belongs to the person who knows what failure would cost.

## Required description caveat if this becomes a video

This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

## Self-critique before v1

- The script may be too developer-specific for non-coders; consider adding one sentence that the same habit applies to benchmark dashboards and generated-code approvals.
- The PR #433 and wrong-layout examples are currently described without PR numbers, which may be better for viewers, but the description or notes should cite the source appendix.
- The ending is clear but could use a more memorable final line.
- Need a visual plan that prevents the middle from becoming abstract branch diagrams.
- No rendering should happen until source caveats, title, and visual proof are reviewed.
