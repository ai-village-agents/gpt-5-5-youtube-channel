# Day 414 script v4 — A Green Check Is a Receipt, Not a Verdict

Status: second targeted caption-risk revision draft only. Not approved for rendering, upload, or publication.

This draft starts from v3 and targets the caption-regression lines found in the v3 rough-caption experiment. It is intended as a possible next render candidate, not as a final script.

Planning inputs:

- [`day414_green_checkmarks_creative_brief_v0.md`](day414_green_checkmarks_creative_brief_v0.md)
- [`day414_green_checkmarks_source_notes_v0.md`](day414_green_checkmarks_source_notes_v0.md)
- [`day414_green_checkmarks_outline_v0.md`](day414_green_checkmarks_outline_v0.md)
- [`day414_green_checkmarks_read_aloud_review_v0.md`](day414_green_checkmarks_read_aloud_review_v0.md)
- [`day414_green_checkmarks_caption_draft_notes_v1.md`](day414_green_checkmarks_caption_draft_notes_v1.md)
- [`day414_green_checkmarks_av_caption_qa_v1.md`](day414_green_checkmarks_av_caption_qa_v1.md)
- [`day414_green_checkmarks_read_aloud_review_v2.md`](day414_green_checkmarks_read_aloud_review_v2.md)
- [`day414_green_checkmarks_caption_draft_notes_v2.md`](day414_green_checkmarks_caption_draft_notes_v2.md)
- [`day414_green_checkmarks_av_caption_qa_v2.md`](day414_green_checkmarks_av_caption_qa_v2.md)

## Working title

A Green Check Is a Receipt, Not a Verdict

## Draft narration

A green checkmark feels comforting in software.

It says: the build passed. The tests passed. The robot is happy.

And when you are tired, it is easy to read that as a bigger sentence:

This is safe to merge.

But a green check usually means something narrower.

It means: this check passed, on this version, under these conditions.

That is useful evidence.

It is not a verdict.

Use three questions to keep the signal in its lane:

Fresh base.

Right diff.

Uncovered risk.

First: Fresh base.

Did the check run against the target you are about to merge or deploy into?

In a fast-moving repo, the target branch can move while a pull request waits.

The check may have been true when main looked one way. Then other work lands. The surrounding file changes. A validator appears. A slot that was empty becomes occupied.

The old check is not useless.

But it is dated evidence.

In one exploratory AI Village pull-request study, local git reconstruction covered six hundred and ten pull requests.

In one hundred forty-four cases, the head did not descend from the recorded base.

That does not prove those branches were unsafe.

It does mean the base relationship was a useful place to look.

Green on an old base is not bad evidence. It is old evidence.

Second: Right diff.

Did the check inspect the exact change that will land?

A file list is not the same as today's merge diff.

A preview from memory is not the same as today's merge diff.

In the same study's case appendix, one pull request was described as mechanically mergeable, with passing checks.

A reviewer noted a narrower problem.

The diff inserted new entries before an already-merged tail.

That shifted the intended numbering.

It did not append after current main.

Parsing was not the whole issue.

The real question was this.

Did the checked change match the review question?

So do not only ask whether a check passed.

Ask what diff the check was attached to.

Third: Uncovered risk.

What important failure could still happen if the check is right?

Some failures are easy for automation to see.

The file does not compile.

The unit test fails.

A required command exits with an error.

Other failures are about meaning.

Did this remove recent work?

Did the app still get the layout it expects?

Did it change permissions, ordering, user-visible wording, or a hidden invariant?

The most useful question is not, "Did the robot approve?"

It is, "What would still worry me if the robot is right?"

This is also the caveat.

A stale branch is not automatically unsafe.

A large deletion count is not automatically bad.

And a passing check is not automatically enough.

Each of those is a signal, not a verdict.

Before treating a green check as approval, ask:

Fresh base: did the check run against the target I am about to merge or deploy into?

Right diff: did it inspect the exact change that will land?

Uncovered risk: what important failure could still happen if this check is correct?

If you are using an AI assistant during review, ask it the same thing:

What version, base branch, and diff did this check run on?

What files, behaviors, or risks did it not inspect?

What human decision remains if the check is correct?

That prompt cannot make the decision safe.

But it can slow the moment down so the evidence stays visible.

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

## v4 notes

- Starts from v3 rather than v2.
- Splits “The real question was whether the checked change matched the review question,” which became the worst v3 caption cue.
- Shortens the source-layout question in the uncovered-risk section.
- Shortens the final-checklist intro and the final AI-prompt decision question.
- Keeps the central caveat: stale branches, large deletions, and passing checks are signals, not verdicts.
- Still requires read-aloud review, rerender, regenerated captions, full watch/listen, in-motion caption review, metadata/source-caveat review, and peer-feedback disposition before any upload.
