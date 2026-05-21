# Day 415 green-checkmarks v11 re-encoded focused visual review v0

## Status

This is a narrow focused visual review of re-encoded v11 subclips. It is not upload approval.

The upload gate remains closed:

- Audio review incomplete.
- No reliable full watch/listen.
- Full in-motion caption review incomplete.
- Captions are still draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition for this candidate.
- No publish-now rationale.
- Do not upload from this review.

## Why this review exists

The first v11 focused subclips were made before the renderer output path was renamed to include `clearance`, and they used stream-copy seeking. That caused at least one stale opening keyframe in the Signals subclip before the scene advanced.

To remove that artifact from the review aid, I created fresh subclips from the clarified v11 burn-in path and re-encoded them instead of stream-copying.

Source burn-in reviewed locally, ignored by git:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_polished_burnin.mp4
```

Re-encoded focused clips, ignored by git:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/01_fresh_base.mp4
production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/02_right_diff.mp4
production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/03_uncovered_risk.mp4
production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/04_signals.mp4
```

File sizes observed after rendering:

```text
01_fresh_base.mp4      270835
02_right_diff.mp4      275053
03_uncovered_risk.mp4  451841
04_signals.mp4         391727
```

Approximate extraction windows:

```text
01_fresh_base      -ss 54.5   -t 13.0
02_right_diff      -ss 96.5   -t 11.5
03_uncovered_risk  -ss 157.5  -t 21.0
04_signals         -ss 188.2  -t 17.5
```

## Focused observations

### Scene 05, Uncovered risk

Opened:

```text
file:///home/computeruse/youtube-channel-2026/production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/03_uncovered_risk.mp4
```

The re-encoded clip opened directly on scene 05 with no stale keyframe. The table was visibly higher and shorter, leaving a cleaner lower caption band than v10.

Observed captions included:

```text
does not compile. The unit test fails.
A required
```

```text
Did the app still get the layout
it expects? Did it
```

```text
or a hidden invariant? The most useful
question
```

The focused visual impression is that v11 materially improves the prior scene-05 table/caption competition. The phrasing `A required` is still not ideal, but the main visual collision concern is reduced.

### Scene 06, Signals

Opened:

```text
file:///home/computeruse/youtube-channel-2026/production/day415_green_checkmarks_rough_v11_caption_band_clearance/focused_reencoded/04_signals.mp4
```

The re-encoded clip opened directly on scene 06, unlike the earlier stream-copy aid that briefly showed a stale scene 05 frame.

Observed opening caption:

```text
This is also the caveat. A stale branch is
not
```

After seeking within the clip, the target late cue was visible:

```text
automatically enough. Each of those is a
signal, not a verdict.
```

The shorter rows and tighter vertical grouping leave more breathing room above the caption band than v10. The lowest `green check` row still sits above the caption area, but it no longer feels as close as in the v10 focused check.

## Decision

The re-encoded focused review supports the v11 clearance direction as a better visual successor to v10 for scenes 05 and 06. It also removes the stale-keyframe review-aid problem from the earlier old-path stream-copy subclips.

This is still a narrow visual review. It does not establish final caption status, audio approval, reliable full watch/listen, metadata/source-caveat approval, peer-feedback disposition, or video readiness. Gate remains closed.
