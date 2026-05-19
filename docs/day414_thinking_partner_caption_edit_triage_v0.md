# Day 414 thinking-partner caption edit triage v0

Status: **planning aid only — not a caption approval and not an upload approval**.

Current rough render:
`production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4`

Current draft captions:
- `docs/day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt`
- `docs/day413_caption_drafts/thinking_partner_v5_word_boundary_v3.srt`

This sheet exists to prevent rushed, ad-hoc edits if a real in-motion caption review flags one of the
known dense cues. It separates three edit types:

1. **Accept as-is** if the cue is readable in motion and the audio pacing feels natural.
2. **Caption-timing/grouping edit** if the spoken words are fine but the cue display needs a better
   split, a slightly longer on-screen duration, or a cleaner line break.
3. **Narration edit** if the words themselves feel rushed, list-like, or hard to follow; this requires
   rerendering the audio/video and regenerating captions.

Do not paraphrase captions away from the spoken audio. If narration changes, rerun the renderer and
caption generator instead of manually making captions say something different from the audio.

## Current structural caption state

From the current caption readability audit:

```text
Cue count: 106
No overlaps or nonpositive durations
Max line length: 43 characters
No cues above 21 characters/second
28 cues above 17 characters/second
Shortest cue: 0.935s
Longest cue: 5.779s
Max gap: 1.328s
Scene 04→05 gap: 1.299s
```

These numbers reduce technical risk but do not replace watching captions in motion.

## Decision labels for each flagged cue

Use exactly one label per cue during review:

```text
Accept as-is
Caption timing/grouping edit needed
Narration edit needed
Cannot assess without reliable playback
```

If the reviewer cannot hear audio or watch captions in motion, use:

```text
Cannot assess without reliable playback
```

and keep the upload gate closed.

## Known high-priority cues

### Cue 66 — relationship risks

Current text:

```text
and the relationship risks of each.
```

Current concern: highest CPS cue in the current draft, around 19.4 cps. It is short and plain, so it
may be acceptable if the surrounding prompt visual gives context.

Review question:

- Does the phrase land as a readable ending to the request, or does it flash by while the viewer is
  still reading the prompt card?

Possible outcomes:

- **Accept as-is** if it reads comfortably in motion.
- **Caption timing/grouping edit needed** if the surrounding cue split creates unnecessary pressure.
- **Narration edit needed** only if the line itself sounds rushed or too list-like.

Low-risk narration fallback if needed:

```text
Before drafting, list the possible goals of this message and the relationship risks.
```

This would remove “of each,” but it changes narration and therefore requires rerendering and caption
regeneration.

### Cue 93 — title-promise line

Current text:

```text
That is the difference between thinking with AI and letting it finish for you.
```

Current concern: around 19.0 cps and conceptually important because it connects to the title.

Review question:

- Does the line feel like the thesis landing, or does it pass too quickly before Scene 08 begins?

Possible outcomes:

- **Accept as-is** if the line is understandable and the following pause/transition gives it weight.
- **Caption timing/grouping edit needed** if the cue needs more breathing room but the narration sounds
  fine.
- **Narration edit needed** if the line still feels too compressed.

Narration fallback if needed:

```text
That is the difference between thinking with AI and handing it the ending.
```

This is shorter but slightly changes the title echo. Use only if the current line fails in a real
watch/listen pass.

### Cue 56 — different wording

Current text:

```text
Those goals can lead to different wording.
```

Current concern: around 18.6 cps at the end of Scene 05a.

Review question:

- Does the cue set up the gentle/direct/firm examples clearly, or is the transition too quick?

Possible outcomes:

- **Accept as-is** if the next visual beat clarifies the point.
- **Caption timing/grouping edit needed** if the transition to “Same facts” needs a cleaner hold.
- **Narration edit needed** only if the phrase itself sounds rushed.

Narration fallback if needed:

```text
Different goals lead to different wording.
```

This is shorter and keeps the meaning, but requires rerendering and caption regeneration.

### Cue 62 — firm version

Current text:

```text
A firm version might say, I cannot commit without a new date.
```

Current concern: around 17.7 cps and includes quoted example wording.

Review question:

- Can a viewer read the firm example before the next ownership sentence starts?

Possible outcomes:

- **Accept as-is** if the visual card reinforces the exact wording.
- **Caption timing/grouping edit needed** if the cue should hold longer around the quoted sentence.
- **Narration edit needed** only if the example sounds too abrupt.

Do not shorten this again without checking the ownership contrast. It was already reduced from a
longer version to improve caption readability.

### Cue 106 — final line

Current text:

```text
Keep your hands on the question.
```

Current concern: around 17.4 cps, but it is short, repeated visually, and appears at the end.

Review question:

- Does the final line land as a memorable close, or does the audio/caption cut off too quickly?

Possible outcomes:

- **Accept as-is** if the ending feels complete.
- **Caption timing/grouping edit needed** if the caption disappears too quickly near the end of the MP4.
- **Narration edit needed** only if the final line sounds clipped or unnatural.

If the line is clipped, first inspect the rendered audio/video tail and caption last-end timing before
changing the script.

## Scene-level checks before editing

### Scene 04→05 seam

Current gap is about 1.299 seconds after:

```text
before the advice feels settled.
```

and before:

```text
The third checkpoint is Ownership.
```

Decision:

```text
Helpful breath / Slight stall / Confusing transition / Cannot assess without reliable playback
```

A timing edit here should be based on listening, not just the numeric gap.

### Scene 05b emphasis

Current intended emphasis:

```text
Same facts.
Different posture.
Different risk.
```

Decision:

```text
Emphasis lands / Needs more breath / Feels too slow / Cannot assess without reliable playback
```

Do not collapse these cues unless the in-motion review finds them distracting; the separated display
is intentional.

### Scene 06 prompt listiness

The prompt is useful only if viewers can follow it without feeling buried by a list. During review,
separate visual density from narration density:

```text
Visual readable: yes / no / cannot assess
Narration paced: yes / no / cannot assess
Prompt worth keeping on screen: yes / no / cannot assess
```

## If edits are needed

Preferred order:

1. Caption timing/grouping edit when the audio and wording are good.
2. Micro narration edit only when the spoken phrase itself fails.
3. Full scene rewrite only if multiple nearby cues fail for the same structural reason.

After any narration edit:

```bash
python3 scripts/render_day413_thinking_partner_rough_v3.py
python3 scripts/generate_day413_v5_word_boundary_captions.py
python3 scripts/audit_channel_docs.py
git diff --check
```

Then repeat the relevant watch/listen and caption-in-motion checks. Do not treat regenerated captions
as final merely because the structural audit passes.
