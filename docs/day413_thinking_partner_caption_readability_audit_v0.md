# Day 413 thinking-partner caption readability audit v0

Candidate: **How to Think With an AI Without Letting It Think For You**.

Status: **objective draft-caption audit only — not a manual caption approval and not upload approval**.

Input: `docs/day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt`.

## Summary

- Cue count: 108
- First cue start: 0.102s
- Last cue end: 419.071s
- Duration range: 0.689s to 5.714s
- Mean cue duration: 3.250s
- Median cue duration: 3.175s
- Maximum gap after a cue: 2.001s
- Mean characters per second: 14.80
- Median characters per second: 15.18
- Cues above 17 characters/second: 28
- Cues above 21 characters/second: 0
- Cues shorter than 0.75s: 1

Interpretation: the draft captions pass the structural checks, but this readability audit identifies concrete targets for the manual pass. Several cues are moderately fast by a 17 cps heuristic; none exceed 21 cps. The main human-review questions are whether those fast cues remain readable in motion and whether the pause structure feels natural against the actual narration.

## Approximate scene caption density

| Segment | Cues | Words | Words/minute over segment | Chars/second over segment |
|---|---:|---:|---:|---:|
| 01 | 15 | 133 | 127.9 | 11.7 |
| 02 | 15 | 132 | 130.4 | 12.2 |
| 03 | 11 | 94 | 133.5 | 13.4 |
| 04 | 6 | 60 | 127.3 | 12.9 |
| 05a | 9 | 82 | 129.8 | 12.7 |
| 05b | 9 | 69 | 139.0 | 12.4 |
| 05c | 8 | 56 | 116.8 | 11.6 |
| 06 | 11 | 104 | 142.3 | 13.5 |
| 07 | 11 | 83 | 122.8 | 11.7 |
| 08 | 13 | 98 | 128.4 | 12.1 |

## Gaps of at least 1.0s

- Cue 47: gap 2.001s after “before the advice feels settled.” before “The third checkpoint is Ownership.”
- Cue 15: gap 1.328s after “But the worktable should not decide what the work is for.” before “Start with a small example.”
- Cue 30: gap 1.313s after “Once the target is visible, the model can help without inventing the game.” before “The second checkpoint is Evidence.”
- Cue 73: gap 1.309s after “You are still responsible for the decision.” before “Here is the whole habit as one prompt: Before answering, help me keep ownership”
- Cue 41: gap 1.308s after “That turns the answer into a checklist for reality.” before “This is a small habit, not a safety guarantee.”
- Cue 56: gap 1.289s after “Those goals can lead to different wording.” before “Same facts.”
- Cue 95: gap 1.278s after “finish the thinking for you.” before “The point is not to think alone.”
- Cue 65: gap 1.275s after “behind.” before “A better request is: Before drafting, list the possible goals of this message”

Largest gap note: the 2.001s gap after Scene 04 is intentional enough to preserve for listening review, but not accepted as final without a reliable full audio pass.

## High characters-per-second cues

- Cue 94 (366.709-370.542, 20.9 cps): “That is the difference between using AI to think with you and letting it quietly”
- Cue 67 (266.872-268.673, 19.4 cps): “and the relationship risks of each.”
- Cue 62 (245.728-249.759, 19.1 cps): “A firm version might say, I cannot commit to the next milestone without a new”
- Cue 56 (228.072-230.335, 18.6 cps): “Those goals can lead to different wording.”
- Cue 39 (155.219-157.001, 18.5 cps): “would change your recommendation?”
- Cue 40 (157.719-160.425, 18.5 cps): “Separate what you know from what you are assuming.”
- Cue 53 (217.030-219.528, 18.4 cps): “But it does not know what you want to protect.”
- Cue 88 (347.256-350.939, 18.2 cps): “Then edit those three answers before you accept the recommendation.”
- Cue 43 (169.196-173.758, 18.0 cps): “Here is the honest warning: people can lean too hard on automated recommendations,”
- Cue 105 (409.256-411.050, 17.8 cps): “What evidence would change this?”
- Cue 49 (196.418-199.906, 17.8 cps): “Some parts of a decision are not facts the model can discover.”
- Cue 7 (27.617-31.785, 17.8 cps): “By the end, you will have one prompt you can reuse before any important AI”
- Cue 102 (398.123-402.518, 17.7 cps): “But keep the purpose, the evidence standard, the risk tolerance, and the final”
- Cue 77 (300.955-304.339, 17.7 cps): “2. List the facts or evidence that would change your answer.”
- Cue 54 (220.260-224.590, 17.6 cps): “Is the email for repairing trust, setting a boundary, getting a new date, or”
- Cue 20 (77.748-80.141, 17.6 cps): “But it is answering a half-built question.”
- Cue 33 (129.751-134.332, 17.5 cps): “If the model recommends a redesign, what would make that recommendation stronger”
- Cue 108 (417.237-419.071, 17.4 cps): “Keep your hands on the question.”
- Cue 75 (295.616-296.591, 17.4 cps): “of this decision.”
- Cue 48 (193.734-195.685, 17.4 cps): “The third checkpoint is Ownership.”
- Cue 61 (241.743-244.983, 17.3 cps): “A direct version might say, I need a new date by Friday.”
- Cue 86 (337.881-340.080, 17.3 cps): “Paste the prompt before your question.”
- Cue 35 (139.204-142.561, 17.3 cps): “Maybe support tickets mention the same confusing sentence.”
- Cue 21 (80.873-85.219, 17.3 cps): “Does better mean more signups, fewer confused users, fewer support tickets,”
- Cue 41 (161.157-164.136, 17.1 cps): “That turns the answer into a checklist for reality.”
- Cue 83 (324.588-328.328, 17.1 cps): “If the evidence is missing, lower your confidence or go find it.”
- Cue 81 (318.455-320.979, 17.0 cps): “But it gives you three places to intervene.”
- Cue 84 (328.885-333.648, 17.0 cps): “If the answer depends on values, stop pretending it is only a technical question.”

## Very short cues

- Cue 65 (0.689s): “behind.”

## Next manual review targets

1. Scene 04→05: decide whether the 2.001s gap feels like a helpful breath or a stall.
2. High-cps cues: check especially Cue 94 at 20.9 cps, Cue 62 at 19.1 cps, and Cue 43 at 18.0 cps.
3. Cue 65: decide whether the standalone 0.689s “behind.” cue is acceptable or should be merged/retimed.
4. Scene 05b: confirm the short “Same facts / Different posture / Different risk” cues land with the intended emphasis.
5. Scene 06: confirm the numbered prompt remains readable and does not feel too list-heavy.
6. Scene 07→08: confirm the title-promise line has enough time to land before the ending visual.
