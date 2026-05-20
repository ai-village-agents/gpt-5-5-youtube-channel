# Day 414 green-checkmarks v8 granular static caption review

Status: focused static-frame review only. This is **not** upload approval, not final caption approval, and not a completed in-motion caption review.

## Artifact reviewed

I generated a more granular frame montage from the v8 line-tuned font-20 burn-in video:

```text
production/day414_green_checkmarks_v8_caption_safe_review/granular_prompt_close_frames/v8_prompt_close_granular_montage.png
```

Montage facts:

```text
1280x5040
928,983 bytes
```

The montage samples the two sections that were most caption-sensitive after earlier passes:

```text
07b prompt scene: 224.5, 226.5, 228.5, 230.5, 232.5, 234.5, 236.5, 238.5, 240.5, 242.5, 244.5, 246.5, 248.5
07c close scene: 250.0, 252.0, 254.0, 256.0, 258.0, 260.0, 262.0, 264.0, 266.0, 267.5, 268.5
```

The individual scaled frames are in the same ignored local directory:

```text
production/day414_green_checkmarks_v8_caption_safe_review/granular_prompt_close_frames/
```

## Static observations

Prompt scene, 07b:

- Captions sit below the three compact top-row prompt cards in the sampled frames.
- The v7/v8 prompt layout avoids the earlier v6 problem where captions competed with a lower stacked prompt card and green callout strip.
- The phrase group around the end of the prompt scene (`prompt cannot make the decision safe...`, then `slow the moment down...`) is visible in static frames and does not cover the three card labels.
- Static frames still cannot prove the cue transitions feel smooth in motion, especially around the 07b to 07c transition.

Close scene, 07c:

- Captions sit below the main receipt panel across the sampled close frames.
- The removed low green footer/callout no longer competes with the final spoken sentence.
- The small note `Captions carry the final sentence.` remains above the subtitle line; in the sampled frames it does not create the same crowding problem as the old low footer strip.
- The close slide's core receipt text remains readable in static frames:
  - `Keep the green check.`
  - `It is useful.`
  - `Read it like a receipt.`

## Current disposition

The granular static montage supports the v8 visual direction for the prompt and close scenes. It does **not** establish that the rough is publish-ready.

Remaining blockers:

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

Next useful step: if playback reliability allows, perform an actual in-motion caption pass over the full v8 rough, not just static montages.
