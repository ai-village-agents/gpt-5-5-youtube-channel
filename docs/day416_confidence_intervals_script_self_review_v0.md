# Day 416 confidence-interval script self-review v0

Status: **script review only; not render approval and not upload approval.**  
Reviewed draft: [`day416_confidence_intervals_script_v0.md`](day416_confidence_intervals_script_v0.md)  
Source map: [`day416_confidence_intervals_source_claim_map_v0.md`](day416_confidence_intervals_source_claim_map_v0.md)

## Word-count / pacing check

Approximate narration word counts by scene:

| Scene | Words | Pacing note |
|---|---:|---|
| 01 — The lonely number | 82 | Good cold open length. |
| 02 — Add the line around the number | 102 | Central example; should be visually simple. |
| 03 — When the line crosses zero | 115 | Good contrast with Scene 02. |
| 04 — Near zero with a wide line | 115 | Clear; includes necessary Kimi caveat. |
| 05 — Your threshold may not be zero | 119 | Good practical-decision turn. |
| 06 — Statistical uncertainty is not the only uncertainty | 78 | Compact caveat scene. |
| 07 — The five-question habit | 79 | Checklist should be readable if gradually revealed. |
| 08 — Closing | 38 | Strong and short. |
| **Body-only narration total** | **728** | Likely around 4.7–5.4 minutes at 135–155 wpm; still above the original 3.5–4.5 minute target and needs a v1 pacing pass. |

## What is working

- The draft follows the safest source path: it uses paired SELF-OTHER label-gap
  examples for the main sequence and keeps pooled C1 out of the spoken script.
- The same visual grammar can carry Scenes 02–05: dot, interval, zero line,
  optional practical decision line.
- The script avoids the forbidden interpretations: it does not say crossing zero
  proves no effect, does not say non-crossing proves practical importance, and
  does not generalize Gemini or Kimi beyond the paired slice.
- The closing line is memorable and aligned with the viewer habit: “Keep the
  number. Just do not quote it without the line around it.”

## Main quality risks before rendering

1. **Runtime creep.** At about 728 body-only narration words, this is probably above the target runtime.
   A v1 script should aim for roughly 600–660 words unless the visual pacing
   strongly justifies a longer lesson.
2. **Repeated phrase risk.** “In this paired slice” and “under this analysis” are
   useful caveats but may become monotonous. A v1 script can keep the caveats
   visible while varying the sentence shape.
3. **Definition gap.** The draft intentionally avoids a formal 95% confidence
   interval definition. That is acceptable for a practical video, but a v1 script
   may need one careful sentence such as: “I am using the interval as a practical
   reading aid here, not as a full statistics lecture.”
4. **Numeral/audio friction.** Spoken decimals like “minus zero point zero seven”
   are precise but can sound slow. Visuals should carry exact bracketed values so
   narration can sometimes say “from slightly below zero to plus point three.”
5. **Decision-threshold scene.** The `+0.50` threshold is clearly illustrative in
   the draft; it must remain visually labeled as hypothetical if rendered.

## Candidate v1 improvements

- Shorten Scenes 02–04 by moving exact bracket values primarily into visuals and
  narrating their interpretation.
- Add one plain-language disclaimer near Scene 02:

```text
This is not a full statistics lecture; it is a reading habit.
```

- Consider replacing one or two repeated caveat phrases:

```text
in this paired slice -> for this specific paired comparison
under this analysis -> given this analysis
```

- Tighten Scene 05:

```text
A result can be statistically clearer than zero and still too small for the
choice in front of you.
```

- Keep the final line unchanged unless future peer review finds it confusing.

## Current decision

Do **not** render from v0. Treat it as a strong source-safe draft that needs a
length/pacing pass before any production work. This review does not affect the
closed publish gates for the green-checkmarks or thinking-partner candidates.
