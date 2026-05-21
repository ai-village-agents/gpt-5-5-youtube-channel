# Day 415 green-checkmarks wrap phrase-polished end-to-end visual review v0

## Scope

This note records a conservative browser review of the current V11 visual render with the wrap phrase-polished caption draft burned in.

Reviewed file, ignored production artifact:

```text
production/day415_green_checkmarks_rough_v11_caption_band_clearance/green_checkmarks_rough_v11_caption_band_clearance_wrap_phrase_polished_burnin.mp4
```

Review method:

- Opened the full burn-in MP4 in Firefox from a local `file://` URL.
- Played from the beginning and confirmed playback reached the final frame at `4:29 / 4:29`.
- Took visual/caption observations at representative points across the video, with special attention to the phrase-polished regions previously reviewed in focused clips.

Important limitation: this was an end-to-end browser visual/caption spot pass, not a reliable audio listen and not final caption approval. It should not be treated as upload readiness.

## Observations

### Opening / receipt framing

At the opening scene, the large checkmark and receipt card remained clear. Captions were readable in the lower caption band, including:

```text
A green checkmark feels comforting in
software.
```

Later in the same opening, the caption band remained readable around:

```text
robot is happy. And when you are tired, it
is easy
```

and:

```text
this version, under these conditions. That
is
```

No new visual collision was observed in the opening.

### Fresh base

The V11 Fresh-base layout kept the compact `triage signal / not failure label` badge and the `144 / 610 PR heads` card away from the caption band. At about `1:18 / 4:29`, the visible caption was readable:

```text
local git reconstruction covered
six hundred and ten pull requests.
```

The timeline, badge, and stat card were legible; the caption sat below them without blocking the main visual content.

### Right diff

The earlier focused review already checked the phrase-polished Right-diff split from a corrected full-burn-in cut. That corrected focused clip showed the improved cue:

```text
A file list is not the same as
today's merge diff. A preview from
```

and the following cue:

```text
memory is not the same as today's merge
diff.
```

In the end-to-end browser pass, playback advanced through the Right-diff section without an obvious layout regression being observed. The V11 top `case appendix example` badge remains the preferred visual direction because it keeps the lower caption band cleaner than the older v9 layout.

### Uncovered risk

The V11 Uncovered-risk table remained higher/shorter, leaving more lower-band clearance than the earlier layouts. At about `2:52 / 4:29`, the caption was readable:

```text
Did the app still get the layout
it expects? Did it
```

The earlier corrected focused clip also confirmed the phrase-polished required-command split:

```text
does not compile.
The unit test fails.
```

followed by:

```text
A required command exits with an error.
Other failures are
```

This fixes the prior stranded `A required` phrase. No new caption-band collision was observed around the V11 table during the end-to-end pass.

### Review checklist / final prompt / ending

At about `3:42 / 4:29`, the `Review checklist` scene was visible with three clear cards. The caption remained below the explanatory line and did not block the cards:

```text
could still happen if this check
is correct?
```

The video reached the final frame at `4:29 / 4:29`. The final card was clear:

```text
Keep the green check.
It is useful.
Read it like a receipt.
```

The ending frame displayed cleanly.

## Decision

The V11 visual direction plus the wrap phrase-polished caption draft remains the best current green-checkmarks candidate observed so far. Compared with the prior wrap-polished draft, the phrase-polished version improves the two known awkward boundaries:

- `A file list is not` is no longer stranded after `exact change that will land?`.
- `A required` is no longer stranded after `The unit test fails.`

The V11 scene revisions also continue to reduce lower-callout/caption-band conflict in the Fresh-base, Right-diff, Uncovered-risk, and Signals/review sections.

## Gate status

Gate remains closed.

This review does **not** establish upload readiness. Remaining blockers include:

- Audio review incomplete.
- No reliable full watch/listen.
- Full final in-motion caption review incomplete.
- Captions remain draft-only.
- No final metadata/source-caveat review.
- No peer-feedback disposition or explicit no-feedback rationale.
- No publish-now rationale.

Do not upload from this review alone.
