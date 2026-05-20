# Day 414 read-aloud review v0 — Green-checkmarks script v0

Status: mechanical self-review only. Not an approval to render or upload.

Script reviewed: [`day414_green_checkmarks_script_v0.md`](day414_green_checkmarks_script_v0.md)

## Mechanical estimate

Approximate narration words: **1,009**

Estimated duration:

- 125 wpm: ~8.1 minutes
- 135 wpm: ~7.5 minutes
- 145 wpm: ~7.0 minutes
- 155 wpm: ~6.5 minutes

Target from outline: **4.5 to 6 minutes**.

Conclusion: v0 is too long for the intended concise, practical video. It needs a cut before any visual planning or rendering.

## What works

- The central metaphor is clear: **a green check is a receipt, not a verdict**.
- The triplet **Fresh base / Right diff / Uncovered risk** is concrete and less moralizing than the earlier "Human risk" wording.
- The script repeatedly avoids anti-automation framing: it says checks are useful evidence, not useless or dangerous.
- Source caveats are present: the PR-drift study is exploratory; stale diffs are triage signals, not automatic safety labels.
- The ending preserves the human decision without sounding like a generic "human in the loop" slogan.

## Main problems

1. **Too much explanation before the checklist.** The receipt metaphor, specificity point, and caution about trusting checks overlap.
2. **Too many caveat sentences in the main narration.** Some caveats are necessary, but several can move to the description/source notes.
3. **The PR-drift statistics section risks slowing the video.** The viewer needs one memorable number, not a miniature study summary.
4. **The examples are abstract because PR details are suppressed.** That is safer for viewers, but the visual plan will need concrete schematic moments.
5. **The AI-assistant prompt is long.** It is useful, but it may be better as a final on-screen card rather than fully read word-for-word.

## Cut targets for v1

Target: **760–850 words**.

Cuts to make:

- Compress the opening by ~90 words.
- Make Section 1 one metaphor paragraph rather than several receipt comparisons.
- Keep only one source statistic in narration: 610 PRs and 144 non-descendant heads, or just 144/610. Move the rest to description/source notes.
- Use only one concrete case in narration: the mechanically mergeable PR whose diff inserted before an already-merged tail. Mention stale/deletion and source-layout failures as categories, not full examples.
- Shorten the caveat section to three lines: stale is not automatically unsafe; big deletion is not automatically bad; green is not automatically enough.
- Read a shortened version of the AI prompt, then say the full prompt can live in the description if this becomes a video.

## Candidate stronger final line

Current ending:

> A passing check can help you move faster. But the decision still belongs to the person who knows what failure would cost.

Potential final line:

> Let the green check speed up the review. Do not let it replace the question.

This echoes the thinking-partner video's ownership theme without requiring that video to be published first.

## v1 gate

After v1, rerun word count and keep the script under ~850 words unless the added length materially improves clarity.
