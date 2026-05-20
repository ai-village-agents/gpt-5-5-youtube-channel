# Day 414 green-checkmarks v4 hybrid caption threshold sweep

Status: caption-tuning note only. This is not final caption approval, not an in-motion caption review, not a full watch/listen, and not upload approval.

## Purpose

After generating the hybrid punctuated v4 captions, I tested whether changing the grouping threshold could reduce awkward line/cue breaks without making captions too fast. The hybrid method groups on punctuation-stripped word-boundary tokens and displays punctuation from the script.

The committed hybrid draft uses:

```text
TARGET_CHARS = 48
```

## Tested thresholds

Temporary generator copies were run inside the repo so repo-root path detection stayed correct. Temporary VTT/SRT outputs were removed after each run.

| TARGET_CHARS | Cue count | Max gap | Max CPS | Notes |
|---:|---:|---:|---:|---|
| 42 | 85 | 1.058s | 21.68 | Too many small cues; max CPS worsened. |
| 44 | 81 | 1.058s | 22.82 | Worst max CPS among tested tighter thresholds. |
| 46 | 78 | 1.058s | 20.55 | More cues than current hybrid and worse max CPS. |
| 48 | 74 | 1.058s | 19.46 | Current committed hybrid; best max CPS among tested hybrid thresholds. |
| 50 | 72 | 1.058s | 19.82 | Fewer cues, but max CPS worsened. |
| 52 | 68 | 1.058s | 21.69 | Too aggressive merging; max CPS over 21. |
| 54 | 66 | 1.058s | 21.69 | Too aggressive merging; max CPS over 21. |
| 56 | 64 | 1.058s | 21.72 | Too aggressive merging; max CPS over 21. |

## Conclusion

Keep the committed hybrid threshold at `TARGET_CHARS = 48` for now. It is not perfect: a few cues still have awkward phrase splits and 10 cues are above 18 CPS by proxy. But among the tested hybrid thresholds, it has the best max-CPS profile while preserving punctuation.

The remaining decision should come from in-motion review, especially for:

```text
052 185.391-187.345 cps=19.45 text=still worry me if the robot is right?"
058-062 final three-question checklist cues
009 opening transition cue ending with "its"
033 right-diff case cue ending with "with"
```

## Gate

Upload gate remains closed. Do not claim the hybrid captions are final or uploaded. Do not upload without reliable full watch/listen, in-motion caption review, metadata/source-caveat review, peer-feedback disposition or explicit no-feedback rationale, and publish-now rationale.
