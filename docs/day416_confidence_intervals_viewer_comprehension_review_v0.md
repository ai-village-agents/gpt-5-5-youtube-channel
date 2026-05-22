# Day 416 confidence-interval viewer comprehension review v0

Status: **script-comprehension review only; no render, no audio, no captions, no thumbnail image, and no upload approval.**  
Reviewed script candidate: [`day416_confidence_intervals_script_v1.md`](day416_confidence_intervals_script_v1.md)  
Source-claim boundary: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)

## Review goal

Check whether a technically curious viewer, but not a statistics specialist, can
leave the video with the intended habit:

```text
Do not quote an AI-evaluation point estimate without also reading the interval,
zero, the practical decision threshold, and the remaining design caveats.
```

This review does not assess motion design, narration quality, captions, audio,
or upload readiness.

## What is likely clear

- The opening contrast between `+0.29` alone and `+0.29 [+0.14, +0.45]`
  should make the missing-range problem visible quickly.
- The recurring dot-and-rail grammar is simple enough to teach without a full
  statistics lecture.
- The three examples have distinct teaching jobs:
  - Gemini: interval entirely above zero in this paired slice.
  - Claude: positive center but interval crosses zero.
  - Kimi: near-zero center with uncertainty on both sides.
- The practical-threshold scene is a useful second step beyond “does it cross
  zero?”
- The final line, “Keep the number. Just do not quote it without the line around
  it,” is memorable and matches the title direction.

## Main comprehension risks

### 1. “Confidence interval” may sound like a universal truth label

Even with caveats, some viewers may hear the interval as the whole evidential
status of the claim. The script reduces this risk with:

```text
A confidence interval is not a force field around a claim.
```

Future render should reinforce this visually with design-caveat chips that stay
on screen long enough to read: `one study`, `paired slice`, `prompt set`, and
`judge family`.

### 2. Crossing zero could be misread as “nothing is happening”

The script explicitly says:

```text
Crossing zero does not prove there is no effect.
```

Keep that line. Do not shorten it in a future pacing edit. If captions are later
generated, this sentence should be a clean standalone cue rather than buried in a
long multi-line caption.

### 3. The illustrative `+0.50` threshold could look source-derived

The script says the threshold is illustrative, not from the study. The visual
must say the same thing directly near the line, not only in narration. Suggested
on-screen label:

```text
hypothetical action line — not from the study
```

Avoid a bare amber `+0.50` line without that label.

### 4. “Plausible range” is practical but not a formal definition

The phrase is useful for a general audience, but it could invite a simplified
Bayesian reading. Keep the “under this analysis” wording where it appears. Avoid
adding a claim like “there is a 95% chance the true value is inside this range.”

### 5. Model names can distract from the lesson

The examples use Gemini, Claude, and Kimi because the source study provides
concrete intervals. But viewers may turn the video into a model-ranking story.
The thumbnail and visuals should avoid leaderboard styling, winner/loser badges,
red X marks, or “Gemini wins” framing.

## Terms that may need visual support

| Term or phrase | Risk | Visual support |
|---|---|---|
| point estimate | abstract term | show the dot first, then label it `estimate` |
| interval | everyday word but statistical load | horizontal rail with endpoints |
| zero | could seem arbitrary | vertical line labeled `no gap` or `zero line` |
| decision threshold | unfamiliar | label as `what would change my action?` |
| paired slice | technical | small source-boundary chip: `same comparison style / one slice` |
| design caveat | broad | chips: `prompt set`, `judge family`, `scoring setup` |

## Optional script polish before any future render

These are optional and should not be applied unless a future production pass is
opened. The current v1 is source-safe enough to preserve as a script candidate.

1. Consider changing one instance of “range is still plausible” to “range this
   analysis has not ruled out” if a more formal tone is desired.
2. Consider defining the zero line visually as `no displayed-label gap` for the
   paired SELF-OTHER examples, while narrating simply as “zero.”
3. Consider making the threshold question more conversational:
   `How large would the gap need to be before I would change what I do?`

## Do not change

- Do not remove the line that crossing zero is not proof of no effect.
- Do not remove the line that `+0.50` is illustrative and not from the study.
- Do not generalize Gemini's interval to all judges or all AI evaluations.
- Do not say Kimi has no label bias or that Kimi is lower quality.
- Do not reintroduce the pooled C1 interval into the spoken script without a
  clear transition to a different estimand.

## Current decision

The v1 script is understandable enough to remain the current confidence-interval
script candidate. It still needs a future production decision, render, captions,
reliable full watch/listen, peer feedback or no-feedback rationale, metadata
review, and publish gate before any upload.

```text
No render exists. Audio review impossible. Do not upload.
```
