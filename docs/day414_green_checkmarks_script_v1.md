# Day 414 script v1 — A Green Check Is a Receipt, Not a Verdict

Status: tighter script draft only. Not approved for rendering, upload, or publication.

Planning inputs:

- [`day414_green_checkmarks_creative_brief_v0.md`](day414_green_checkmarks_creative_brief_v0.md)
- [`day414_green_checkmarks_source_notes_v0.md`](day414_green_checkmarks_source_notes_v0.md)
- [`day414_green_checkmarks_outline_v0.md`](day414_green_checkmarks_outline_v0.md)
- [`day414_green_checkmarks_read_aloud_review_v0.md`](day414_green_checkmarks_read_aloud_review_v0.md)

## Working title

A Green Check Is a Receipt, Not a Verdict

## Draft narration

A green checkmark is one of the most comforting shapes in software.

It says: the build passed. The tests passed. The robot is happy.

And when you are tired, it is easy to read that as a bigger sentence:

This is safe to merge.

But a green check usually means something narrower.

It means: this check passed, on this version, under these conditions.

That is useful evidence.

It is not a verdict.

Here are three questions that keep the signal in its lane:

Fresh base.

Right diff.

Uncovered risk.

First: Fresh base.

Did the check run against the target you are about to merge or deploy into?

In a fast-moving repo, the target branch can move while a pull request waits.

The check may have been true when main looked one way. Then other work lands. The surrounding file changes. A validator appears. A slot that was empty becomes occupied.

The old check is not useless.

But it is dated evidence.

In one exploratory AI Village pull-request study, local git reconstruction found six hundred and ten pull requests. One hundred forty-four pull-request heads were not descendants of their recorded base.

That does not prove those branches were unsafe.

It does mean the base relationship was a useful place to look.

Green on an old base is not bad evidence. It is old evidence.

Second: Right diff.

Did the check inspect the exact change that will land?

A file list is not the same as the current merge diff.

A preview you remember is not the same as the change that will ship.

In the same study's case appendix, one pull request is described as mechanically mergeable with passing checks. But a reviewer noted that its diff inserted new entries before an already-merged tail, shifting the intended numbering instead of appending after current main.

The issue was not simply whether the code could parse.

The issue was whether the checked change matched the real review question.

So do not only ask whether a check passed.

Ask what diff the check was attached to.

Third: Uncovered risk.

What important failure could still happen even if the check result is correct?

Some failures are easy for generic automation to see: the file does not compile, the unit test fails, a required command exits with an error.

Other failures are about meaning.

Did this remove recent work?

Did it preserve the source layout the application expects?

Did it change permissions, ordering, user-visible wording, or a hidden invariant?

The most useful question is not, "Did the robot approve?"

It is, "What would still worry me if the robot is right?"

This is also the caveat.

A stale branch is not automatically unsafe.

A large deletion count is not automatically bad.

And a passing check is not automatically enough.

Each of those is a signal, not a verdict.

So before you treat a green check as approval, ask:

Fresh base: did the check run against the target I am about to merge or deploy into?

Right diff: did it inspect the exact change that will land?

Uncovered risk: what important failure could still happen even if this check result is correct?

If you are using an AI assistant during review, you can ask it the same thing:

What version, base branch, and diff did this check run on?

What files, behaviors, or risks did it not inspect?

What human decision remains even if the check result is correct?

That prompt will not make the decision safe by itself.

But it can slow the moment down just enough to keep the evidence visible.

Keep the green check.

It is useful.

Just read it like a receipt.

What version did it check?

What diff did it inspect?

What risk did it leave uncovered?

Let the green check speed up the review.

Do not let it replace the question.

## Required description caveat if this becomes a video

This video uses a public AI Village pull-request trace as a concrete example. The PR-drift study is exploratory: keyword labels are weak supervision, model results are descriptive and in-sample, and stale or deletion-heavy diffs are triage signals rather than automatic safety labels. The checklist is a review habit, not a guarantee.

## v1 notes

- Cut from 1,009 narration words in v0 to a shorter target range.
- Preserves the strongest source number: 144 non-descendant heads out of 610 pull requests.
- Keeps one concrete case from the source appendix without overloading the viewer with PR numbers.
- Changes the ending to: "Let the green check speed up the review. Do not let it replace the question."
- Still needs source-caveat review, visual storyboard, and external critique before any rendering.
