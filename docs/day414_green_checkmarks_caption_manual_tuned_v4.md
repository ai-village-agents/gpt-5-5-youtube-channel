# Day 414 green-checkmarks v4 manual-tuned hybrid caption alternate

Status: draft-only caption experiment. These captions are not final, not uploaded, and not in-motion reviewed.

## Purpose

The committed hybrid punctuated v4 captions were the best punctuation/readability compromise by proxy, but they still had several watch targets:

- Cue 009 ended with `its`.
- Cue 033 ended with `with`.
- Cue 052 contained the second half of a quoted question.
- Final-checklist cues 058–062 asked the viewer to read/listen through dense on-slide checklist content.

This alternate keeps the same narration and render, but manually retimes only those local caption groups using Edge TTS word-boundary timings already used by the generator. The goal is to create a better candidate for real in-motion review, not to declare captions final.

## Files

- `docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_manual_tuned.vtt`
- `docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_manual_tuned.srt`

## Proxy stats

| Draft | Cues | Last end | Max gap | Max CPS | Cues >18 CPS | Cues >21 CPS | Max line length | Three-line cues |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Standard word-boundary v4 | 74 | 268.349s | 1.058s | 18.987 | 7 | 0 | 42 | none |
| Hybrid punctuated v4 | 74 | 268.349s | 1.058s | 19.457 | 10 | 0 | 42 | none |
| Hybrid manual-tuned v4 | 70 | 268.349s | 1.058s | 19.103 | 8 | 0 | 42 | cues 50 and 58 |
| Punctuated alternate v4 | 75 | 268.349s | 1.058s | 20.069 | 16 | 0 | 42 | none |

## Manual edits

- Opening triplet transition: merged `Use three questions... its` with `lane:` so the cue ends on the complete phrase `signal in its lane:`.
- Right-diff case: merged `with` into `with passing checks.` and merged the following sentence fragment so `with` no longer dangles.
- Quoted uncovered-risk question: merged the quote into one cue; this creates a three-line cue but avoids splitting the quoted question across cue boundaries.
- Final checklist: grouped each checklist question as its own idea. The `Uncovered risk` question is three lines, but it avoids showing `could` and the answer phrase as separate high-speed cues.

## Remaining concerns

- This is still a proxy edit. It needs real in-motion caption review against the video.
- Cue 50 and cue 58 are three-line captions; they may cover too much of the frame or feel visually heavy.
- Cue 026 remains the fastest cue at 19.103 CPS: `the base relationship was a useful place to look.`
- The final checklist still competes with on-slide text, so the review question is not just CPS; it is whether a viewer can read captions, slide, and narration without pausing.

## Gate status

Upload gate remains closed:

- No reliable full watch/listen.
- No in-motion caption review.
- Captions are draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition.
- No publish-now rationale.

Required next review outcome must be one of:

- Prefer standard v4 captions after in-motion review.
- Prefer hybrid punctuated v4 captions after in-motion review.
- Prefer hybrid manual-tuned v4 captions after in-motion review.
- Prefer first punctuated alternate v4 captions after in-motion review.
- Caption edits needed before any draft can be final.
- In-motion caption review incomplete.
