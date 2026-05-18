# Mobile readability review

The GPT-5.5 Model videos are slide-based explainers. A slide that looks clear on a desktop preview can be difficult to read on a phone. This checklist records what to inspect before future edits or new videos.

## Review setup

For each video, check at least three moments:

1. the opening title or promise;
2. the densest evidence slide;
3. the final takeaway or checklist slide.

If direct public playback is unavailable or inconsistent, use the local rendered MP4 or contact-sheet images. Record which source was inspected so the result is not confused with public YouTube verification.

## Readability checks

A slide is phone-readable if a viewer can understand the main point without pausing for a long time.

Check:

- title text is large enough to read at a glance;
- body text is short enough for one screen;
- numbers are not crowded together;
- chart labels are not essential if they are too small;
- the narration repeats the most important visual claim;
- color is not the only way to understand the contrast;
- caveats are not hidden in tiny text.

## Series-specific risk areas

The highest-risk slides are likely to be:

- V1 method/evidence overview slides with multiple study terms;
- V2 checklist slides if all five steps appear at once;
- V3 average-versus-slices examples if numbers are too dense;
- V4 receipts/checklist slides if the prompt/rubric/code/examples list is crowded;
- V5 threshold examples where a small numeric change carries the lesson.

## Improvement rules for future videos

Prefer:

- one claim per slide;
- one key number per visual beat;
- short labels such as "observational" and "causal" with narration explaining the difference;
- repeated verbal summaries of any chart pattern;
- a companion transcript or support doc for dense details.

Avoid:

- putting a full paragraph on screen when narration already says it;
- shrinking caveats to make room for a cleaner headline;
- relying on color-only distinctions;
- using a chart whose labels are necessary but unreadable on mobile;
- declaring a slide "accessible" because it passed only desktop inspection.

## Suggested log entry

When a future maintainer performs a mobile readability pass, use this format:

```text
Mobile readability check, YYYY-MM-DD: Inspected [video/source] at [opening/dense/final moments]. Main text readable: [yes/no]. Dense numbers readable: [yes/no]. Narration covers visual-only claims: [yes/no]. Fixes made: [summary]. Remaining caveat: [summary].
```

## Relationship to other docs

- Use [`accessibility_review.md`](accessibility_review.md) for the broader accessibility state.
- Use [`visual_alt_text.md`](visual_alt_text.md) when a chart needs a text fallback.
- Use [`caption_workflow.md`](caption_workflow.md) when transcript or caption text changes.
- Use [`publication_verification.md`](publication_verification.md) before describing a public YouTube watch-page result.
