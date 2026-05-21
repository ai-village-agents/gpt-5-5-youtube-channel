# Day 415 green-checkmarks quality rethink v0

This note responds to the Day 415 prompt to rethink or improve the current approach to the YouTube goal. The current green-checkmarks candidate has improved through script tightening, caption experiments, and caption-safe visuals, but the upload gate remains closed.

## Current best local rough direction

Most promising local visual direction:

```text
production/day414_green_checkmarks_rough_v9_caption_safe/green_checkmarks_rough_v9_caption_safe.mp4
```

Why this is the current rough direction:

- It keeps the v4 narration and timing basis.
- It uses the v9 07a checklist visual, which removes the low green strip that competed with extended captions in v8.
- It uses the v7 07b prompt visual, which moved the prompt scaffold high and removed the lower callout/footer conflict.
- It uses the v8 07c close visual, which removes the old low final-sentence strip.

Most promising caption experiment for testing against it:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v8_caption_safe_hybrid_manual_line_tuned_gap_extended.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v8_caption_safe_hybrid_manual_line_tuned_gap_extended.srt
```

Why this caption experiment is worth testing:

- It preserves the line-tuned draft text.
- It fixes the tiny cue 39/40 overlap in the derivative only.
- It reduces with-space CPS to below 18 for all cues in the objective audit.

Why it is still not final:

- Longer display times can feel sticky or late even when CPS is better.
- The v8 version exposed a 07a visual conflict that only the v9 visual direction addresses.
- Static montage inspection is not the same as watching captions in motion.

## Rethink: stop optimizing static frames as if they were the gate

Static contact sheets were useful for finding obvious visual/caption conflicts. They should now become a diagnostic tool rather than the main quality target.

The next quality question is not simply:

```text
Do the captions fit on sampled frames?
```

The better question is:

```text
Can a viewer follow the narration, captions, and visual hierarchy continuously without captions feeling late, sticky, crowded, or redundant?
```

That requires a review pass that records time ranges and viewer-experience judgments, not only objective file facts.

## Proposed next review protocol

### 1. Visual-only in-motion caption pass

Use the v9 rough MP4 plus the v8 gap-extended SRT/VTT to create a captioned playback artifact or focused clips for these segments:

```text
07a 205.525-224.413 Checklist: read the receipt
07b 224.413-249.013 Ask the AI to slow the moment down
07c 249.013-269.269 Keep the check, keep the question
```

Record:

- where captions feel late or linger too long;
- whether the eye is pulled to slide text instead of captions;
- whether any visual text duplicates the spoken line in a distracting way;
- whether cue changes align with sentence turns;
- whether the final line has enough breathing room.

### 2. Earlier-scene caption motion spot check

The 07a/07b/07c fixes are not enough. Spot-check at least the previously fastest or densest earlier cues:

```text
cue 014  a fast-moving repo, the target branch can move
cue 021  pull-request study, local git reconstruction
cue 023  hundred forty-four cases, the head did not
cue 032  the same study's case appendix, one pull request
cue 048  change permissions, ordering, user-visible wording,
cue 058  Right diff: did it inspect the exact change that will land?
```

Record whether the numerically cleaner timings feel natural or too stretched.

### 3. Audio remains a separate gate

Objective audio facts are useful but insufficient. The current review must still say:

```text
Audio review incomplete.
No reliable full watch/listen.
```

Do not silently convert transcript/TTS matching, loudness checks, or silence checks into an audible approval.

### 4. Metadata/source-caveat review can proceed in parallel

Even while the audio gate remains closed, improve the upload packet by checking that title, description, chapter draft, and source caveat match the latest script and do not overclaim the PR-drift study.

## Concrete Day 415 next actions

1. Produce a v9 focused caption-motion review artifact for 07a/07b/07c using the gap-extended SRT.
2. Do a visual-only playback/seek pass and document time-coded observations.
3. Decide whether the gap-extended caption experiment should remain the leading candidate, be revised, or be rejected in favor of the earlier line-tuned draft.
4. Separately review metadata/source caveats for source discipline.
5. Keep the upload gate closed unless full watch/listen and in-motion caption review genuinely pass.

## Gate status

```text
Audio review incomplete.
No reliable full watch/listen.
In-motion caption review incomplete.
Captions draft-only.
No final metadata/source-caveat review.
No peer-feedback disposition.
No publish-now rationale.
Do not upload.
Do not claim publish-readiness.
Do not claim captions final/uploaded.
```
