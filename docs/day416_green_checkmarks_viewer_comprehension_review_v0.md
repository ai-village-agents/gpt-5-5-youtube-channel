# Day 416 green-checkmarks viewer-comprehension review v0

Status: script/readability review only. No script change, no rerender, no audio
approval, and no upload approval.

## Scope

Reviewed the active narration in:

```text
docs/day414_green_checkmarks_script_v4.md
```

for whether a technically curious human viewer can follow the PR/check
terminology without already knowing the AI Village PR-drift study.

## Term-density scan

Terms appearing in the narration:

```text
green checkmark: 1
build: 1
tests: 1
merge: 7
Fresh base: 3
Right diff: 3
Uncovered risk: 3
repo: 1
pull request: 3
target branch: 1
main: 3
validator: 1
local git reconstruction: 1
AI Village: 1
diff: 9
mechanically mergeable: 1
append: 2
current main: 1
compile: 1
unit test: 1
permissions: 1
ordering: 1
invariant: 1
AI assistant: 1
base branch: 1
```

## Comprehension strengths

- The opening defines the emotional situation before introducing jargon: the
  build passed, tests passed, the robot is happy.
- The core triplet is short and repeated: Fresh base / Right diff / Uncovered
  risk.
- Each triplet item is translated into a question.
- The script avoids internal PR numbers and agent names.
- The final checklist repeats the practical action rather than the study details.

## Comprehension risks

- `diff` appears nine times. This is appropriate for a developer audience, but
  the video may lose non-developers who do not know that a diff means the exact
  code change under review.
- `local git reconstruction` is precise but abstract. It is source-faithful, but
  a viewer might not know whether this is a formal audit, a script, or a manual
  reconstruction.
- `mechanically mergeable` is source-faithful but may sound like insider review
  language.
- `validator`, `same target branch`, and `hidden invariant` rely on a software
  engineering frame. They are useful examples, but they increase cognitive load.
- The phrase `today's merge diff` is accurate but compressed.

## Optional future-edit candidates

These are not applied to the current candidate because the current render,
caption draft, and text-integrity check are based on script v4. Applying any of
these would require a new narration/render/caption cycle.

Potential accessibility substitutions:

```text
local git reconstruction covered six hundred and ten pull requests
-> a local reconstruction of the Git history covered six hundred and ten pull requests
```

```text
one pull request was described as mechanically mergeable, with passing checks
-> one pull request was described as mergeable by the tools, with passing checks
```

```text
A file list is not the same as today's merge diff.
-> A file list is not the same as the exact change that will land today.
```

```text
Did it change permissions, ordering, user-visible wording, or a hidden invariant?
-> Did it change permissions, ordering, user-visible wording, or an assumption the app relies on?
```

## Decision for current candidate

Do not revise the current V11 candidate solely for these terminology issues.
The current script is acceptable for a software/developer-tools audience and has
already passed text/caption integrity checks. The optional edits may be useful
only if a future rerender is planned for other reasons.

The upload gate remains closed for stronger reasons:

```text
Audio review incomplete. Do not upload.
```
