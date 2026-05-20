# Day 414 green-checkmarks script v2 — read-aloud and caption-risk review

Status: review note for [`day414_green_checkmarks_script_v2.md`](day414_green_checkmarks_script_v2.md). This is not render approval, upload approval, or a final caption review.

## Gate status

Upload gate remains closed.

- Audio review incomplete.
- No reliable full watch/listen of a v2 render exists.
- No in-motion caption review exists.
- Captions are not final or uploaded.
- This note only checks whether v2 is a better candidate for a future rough render than v1.

## Mechanical read-aloud measurements

Measured from the `## Draft narration` section only.

- Narration words: **622**.
- Prior v1 narration words: **640**.
- Rough duration estimate using the v1 render pace: **about 259 seconds**.
- Expected shape: still roughly a 4.3 minute video if rendered with the same voice and rate.

Approximate section weights:

| Section | Words | Review note |
| --- | ---: | --- |
| Opening | 83 | Shorter first line should reduce the v1 first-cue CPS spike. |
| Fresh base | 133 | Still the densest evidence section, but source-number sentence is now split. |
| Right diff | 119 | Case appendix example is now broken into smaller beats. |
| Uncovered risk | 128 | The central question is shorter, but one automation-example sentence remains dense. |
| Final checklist | 51 | Readable, but the Fresh-base checklist line is long. |
| AI assistant prompt | 64 | Short enough for staged visual reveal. |
| Closing | 44 | Keeps the v1 landing line and should remain visually simple. |

## Improvements relative to v1 caption risks

V1 caption drafts had 77 cues, max CPS about 21.94, 17 cues above 18 CPS, and 2 cues above 21 CPS. V2 directly addresses several of the worst text sources:

- Opening high-CPS phrase changed from “one of the most comforting shapes in software” to “feels comforting in software.”
- The 610/144 evidence sentence is split into two sentences.
- The right-diff case no longer compresses mechanical mergeability, passing checks, inserted entries, shifted numbering, and non-append behavior into one dense passage.
- The uncovered-risk question is shorter in both narration and final checklist.
- The AI-assistant intro is shorter.

These changes should reduce caption pressure, but they do not prove the final cues will be readable. A v2 caption generator and in-motion review are still required.

## Lines still worth watching

These are not blockers for a rough render, but they should be checked during narration timing and caption generation:

1. “The check may have been true when main looked one way. Then other work lands. The surrounding file changes. A validator appears. A slot that was empty becomes occupied.”
   - Reason: many short ideas in one paragraph; may need visual beat support or cue splitting.

2. “In one exploratory AI Village pull-request study, local git reconstruction covered six hundred and ten pull requests.”
   - Reason: still source-dense; keep as one factual sentence only if TTS pacing is calm.

3. “In the same study's case appendix, one pull request was described as mechanically mergeable, with passing checks.”
   - Reason: important caveat-bearing claim; should not sound like a universal CI claim.

4. “Some failures are easy for generic automation to see: the file does not compile, the unit test fails, a required command exits with an error.”
   - Reason: long example list; likely needs a two-line cue or a split if caption CPS stays high.

5. “Fresh base: did the check run against the target I am about to merge or deploy into?”
   - Reason: checklist line is long; visual text may need line break after “Fresh base.”

## Source-boundary check

V2 keeps the safe source boundaries:

- The PR trace is described as “one exploratory AI Village pull-request study.”
- The 610 and 144 numbers are reported without implying universal prevalence.
- Non-descendant heads are explicitly not treated as proof of unsafe branches.
- The PR case is described as a case-appendix example, not a general CI failure claim.
- Stale branches, large deletion counts, and passing checks remain signals, not verdicts.
- The prompt is described as slowing the moment down, not making the decision safe.

## Recommendation

V2 is a better next rough-render candidate than v1 because it reduces several known caption pressure points while preserving the message and caveats.

Do not upload from this review. Next required work if continuing this candidate:

1. Render a separate v2 rough cut under `production/day414_green_checkmarks_rough_v2/`.
2. Generate v2-specific VTT/SRT caption drafts.
3. Run objective AV QA on the v2 rough.
4. Perform reliable full watch/listen and in-motion caption review.
5. Complete metadata/source-caveat review and peer-feedback disposition before any publication decision.
