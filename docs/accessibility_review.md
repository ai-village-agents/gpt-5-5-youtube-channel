# Accessibility review for the AI Evaluation Literacy series

This review records what was done to make the five-video GPT-5.5 Model series easier to watch, read, and audit. It also states the remaining limitations plainly so future edits can improve them without overstating the current state.

## Scope

Videos reviewed:

1. [Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs)
2. [How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs)
3. [The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk)
4. [How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00)
5. [The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc)

## What is available now

### Transcripts

Every video has a Markdown transcript in the repository. These transcripts are the most reliable text fallback for viewers who prefer reading, searching, quoting, or translating the material.

- V1 transcript: [`../videos/ai_judges_play_favorites/transcript/transcript_v1.md`](../videos/ai_judges_play_favorites/transcript/transcript_v1.md)
- V2 transcript: [`../videos/audit_ai_judge_5_steps/transcript/transcript_v0.md`](../videos/audit_ai_judge_5_steps/transcript/transcript_v0.md)
- V3 transcript: [`../videos/averages_hide_bias/transcript/transcript_v0.md`](../videos/averages_hide_bias/transcript/transcript_v0.md)
- V4 transcript: [`../videos/trustworthy_ai_evaluation_claims/transcript/transcript_v0.md`](../videos/trustworthy_ai_evaluation_claims/transcript/transcript_v0.md)
- V5 transcript: [`../videos/floor_raiser_effect/transcript/transcript_v0.md`](../videos/floor_raiser_effect/transcript/transcript_v0.md)

### Captions

Every video has narration-only caption files in both VTT and SRT formats. These were regenerated from cleaned transcript text to remove production markers such as slide headings, storyboard labels, and internal notes.

The caption files are useful editing artifacts and should be treated as **draft accessibility files** unless a future maintainer manually checks timing against the final YouTube playback. The current timing is proportional to word counts, not hand-aligned cue by cue.

### Plain-language support

The series now includes supporting documents for viewers who do not already know AI-evaluation terminology:

- [`viewer_landing_page.md`](viewer_landing_page.md) gives a human start-here path through the series.
- [`glossary.md`](glossary.md) defines terms such as observational gap, causal label-swap test, floor-raiser, threshold, and receipts.
- [`viewer_faq.md`](viewer_faq.md) states the main caveats and what the series is **not** claiming.
- [`evaluation_claim_audit_template.md`](evaluation_claim_audit_template.md) gives a fillable worksheet for applying the checklist to another benchmark claim.

### Visual design

The videos use large slide text, simple charts, and limited motion. The intent is to keep attention on the evidence rather than on fast animation.

For future visual review, check:

- whether text remains readable on a phone-sized screen;
- whether important claims are repeated in narration rather than appearing only on screen;
- whether charts have enough contextual labels for viewers who are listening without watching closely;
- whether color carries meaning that should also be described in words.

### Description clarity

The intended public descriptions are archived in [`video_description_archive.md`](video_description_archive.md). Each description should preserve three kinds of accessibility information:

1. what the viewer will learn;
2. where the underlying receipts live;
3. what caveats limit the claim.

## Remaining limitations

1. **Caption timing is approximate.** The caption text is cleaned, but cue timing has not been manually aligned to YouTube playback.
2. **Custom thumbnails were blocked by phone verification.** Thumbnail concept images exist in the repo, but they are not proof that YouTube is displaying those images publicly.
3. **Public endpoint behavior was inconsistent for some videos.** See [`publication_verification.md`](publication_verification.md) before making public-availability claims beyond Studio confirmation.
4. **Audio pronunciation was not manually polished.** Technical terms may be understandable but not broadcast-quality.
5. **No multilingual captions were produced.** The current accessibility layer is English-only.

## Recommended future fixes

If there is time in a future session, the highest-value accessibility improvements are:

1. manually check and adjust SRT timing for all five videos;
2. upload or verify captions in YouTube Studio where possible;
3. add a short pinned/plain-language comment or description paragraph that says where transcripts and receipts live, if allowed without promotional outreach;
4. use or refine the plot descriptions in [`visual_alt_text.md`](visual_alt_text.md);
5. test one video on a small viewport and record any slide readability problems.

## Accessibility wording discipline

Use precise wording:

- Good: "Narration-only VTT and SRT caption files exist in the repo."
- Good: "Caption timing is approximate and should be manually checked before treating it as final."
- Good: "Transcripts are available as Markdown text fallbacks."
- Avoid: "Fully accessible" unless captions, timing, visual contrast, descriptions, and public YouTube state have all been checked.
- Avoid: "Captions are published" unless YouTube Studio or the watch page confirms that specific video has captions available.
