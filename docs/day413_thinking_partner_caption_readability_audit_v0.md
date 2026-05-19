# Day 413 thinking-partner caption readability audit v0

Candidate: **How to Think With an AI Without Letting It Think For You**.

Status: **objective draft-caption audit only — not a manual caption approval and not upload approval**.

Input: `docs/day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt`.

## Summary

- Cue count: 106
- First cue start: 0.102s
- Last cue end: 414.583s
- Duration range: 0.935s to 5.779s
- Mean cue duration: 3.262s
- Median cue duration: 3.175s
- Maximum gap after a cue: 1.328s
- Mean characters per second: 14.87
- Median characters per second: 15.29
- Cues above 17 characters/second: 28
- Cues above 21 characters/second: 0
- Cues shorter than 0.75s: 0

Interpretation: the draft captions pass the structural checks, and the generator avoids the previously observed standalone 0.689s “behind.” cue. A targeted microcopy pass shortened three formerly flagged fast-caption moments: the Scene 04 caveat, the Scene 05b firm example, and the Scene 07 title-promise line. Several cues remain moderately fast by a 17 cps heuristic; none exceed 21 cps. The main human-review questions are whether those fast cues remain readable in motion and whether the pause structure feels natural against the actual narration.

## Approximate scene caption density

| Segment | Cues | Words | Words/minute over segment | Chars/second over segment |
|---|---:|---:|---:|---:|
| 01 | 15 | 133 | 127.9 | 11.7 |
| 02 | 15 | 132 | 130.4 | 12.2 |
| 03 | 11 | 94 | 133.5 | 13.4 |
| 04 | 6 | 60 | 127.3 | 12.9 |
| 05a | 9 | 82 | 129.8 | 12.7 |
| 05b | 8 | 65 | 136.2 | 11.8 |
| 05c | 8 | 56 | 116.8 | 11.6 |
| 06 | 11 | 104 | 142.3 | 13.5 |
| 07 | 10 | 76 | 118.4 | 11.4 |
| 08 | 13 | 98 | 128.4 | 12.1 |

## Gaps of at least 1.0s

- Cue 15: gap 1.328s after "But the worktable should not decide what the work is for." before "Start with a small example."
- Cue 30: gap 1.313s after "Once the target is visible, the model can help without inventing the game." before "The second checkpoint is Evidence."
- Cue 41: gap 1.308s after "That turns the answer into a checklist for reality." before "This is a small habit, not a safety guarantee."
- Cue 47: gap 1.299s after "before the advice feels settled." before "The third checkpoint is Ownership."
- Cue 56: gap 1.289s after "Those goals can lead to different wording." before "Same facts."
- Cue 64: gap 1.290s after "But you choose the posture, the risk, and the line you are willing to stand behind." before "A better request is: Before drafting, list the possible goals of this message"
- Cue 72: gap 1.309s after "You are still responsible for the decision." before "Here is the whole habit as one prompt: Before answering, help me keep ownership"
- Cue 83: gap 1.302s after "If the answer depends on values, stop pretending it is only a technical question." before "Try it on the next AI request that actually matters."
- Cue 93: gap 1.162s after "That is the difference between thinking with AI and letting it finish for you." before "The point is not to think alone."

Largest gap note: the largest caption gap is now 1.328s after the Scene 01 close. The former 2.001s Scene 04→05 gap is no longer present after the TTS cache fix and rerender; the Scene 04→05 gap is 1.299s. These gaps still require real listening review before any upload decision.

## High characters-per-second cues

- Cue 66 (264.088-265.889, 19.4 cps): and the relationship risks of each.
- Cue 93 (364.837-368.942, 19.0 cps): That is the difference between thinking with AI and letting it finish for you.
- Cue 56 (226.224-228.487, 18.6 cps): Those goals can lead to different wording.
- Cue 39 (155.219-157.001, 18.5 cps): would change your recommendation?
- Cue 40 (157.719-160.425, 18.5 cps): Separate what you know from what you are assuming.
- Cue 53 (215.182-217.680, 18.4 cps): But it does not know what you want to protect.
- Cue 87 (345.384-349.067, 18.2 cps): Then edit those three answers before you accept the recommendation.
- Cue 103 (404.768-406.562, 17.8 cps): What evidence would change this?
- Cue 49 (194.570-198.058, 17.8 cps): Some parts of a decision are not facts the model can discover.
- Cue 7 (27.617-31.785, 17.8 cps): By the end, you will have one prompt you can reuse before any important AI
- Cue 100 (393.635-398.030, 17.7 cps): But keep the purpose, the evidence standard, the risk tolerance, and the final
- Cue 76 (298.171-301.555, 17.7 cps): 2. List the facts or evidence that would change your answer.
- Cue 62 (243.880-247.333, 17.7 cps): A firm version might say, I cannot commit without a new date.
- Cue 54 (218.412-222.742, 17.6 cps): Is the email for repairing trust, setting a boundary, getting a new date, or
- Cue 20 (77.748-80.141, 17.6 cps): But it is answering a half-built question.
- Cue 33 (129.751-134.332, 17.5 cps): If the model recommends a redesign, what would make that recommendation stronger
- Cue 106 (412.749-414.583, 17.4 cps): Keep your hands on the question.
- Cue 74 (292.832-293.807, 17.4 cps): of this decision.
- Cue 48 (191.886-193.837, 17.4 cps): The third checkpoint is Ownership.
- Cue 61 (239.895-243.135, 17.3 cps): A direct version might say, I need a new date by Friday.
- Cue 85 (336.009-338.208, 17.3 cps): Paste the prompt before your question.
- Cue 35 (139.204-142.561, 17.3 cps): Maybe support tickets mention the same confusing sentence.
- Cue 43 (169.196-173.657, 17.3 cps): Here is the honest warning: people can lean too hard on automated advice, and
- Cue 21 (80.873-85.219, 17.3 cps): Does better mean more signups, fewer confused users, fewer support tickets,
- Cue 41 (161.157-164.136, 17.1 cps): That turns the answer into a checklist for reality.
- Cue 82 (321.804-325.544, 17.1 cps): If the evidence is missing, lower your confidence or go find it.
- Cue 80 (315.671-318.195, 17.0 cps): But it gives you three places to intervene.
- Cue 83 (326.101-330.864, 17.0 cps): If the answer depends on values, stop pretending it is only a technical question.

## Very short cues

- None below 0.75s.

## Next manual review targets

1. Scene 04→05: decide whether the 1.299s gap feels like a helpful breath or a stall.
2. High-cps cues: check especially Cue 66 at 19.4 cps, Cue 93 at 19.0 cps, and Cue 56 at 18.6 cps.
3. Scene 05b: confirm the short “Same facts / Different posture / Different risk” cues land with the intended emphasis, and confirm the merged “stand behind” cue remains readable.
4. Scene 06: confirm the numbered prompt remains readable and does not feel too list-heavy.
5. Scene 07→08: confirm the shortened title-promise line has enough time to land before the ending visual.
