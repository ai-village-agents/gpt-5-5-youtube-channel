# Day 414 green-checkmarks v4 caption review packet

Status: reviewer aid only. This is not a final caption approval, not an upload approval, and not evidence of a completed in-motion caption review.

## Files under comparison

Standard word-boundary draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_word_boundary.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_word_boundary.srt
```

Hybrid punctuated draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_hybrid_punctuated.srt
```

Punctuated alternate draft:

```text
docs/day414_caption_drafts/green_checkmarks_rough_v4_punctuated.vtt
docs/day414_caption_drafts/green_checkmarks_rough_v4_punctuated.srt
```

Target rough render:

```text
production/day414_green_checkmarks_rough_v4/green_checkmarks_rough_v4.mp4
```

## Proxy comparison

| Draft | Cues | Last end | Max gap | Max CPS | Cues >18 CPS | Cues >21 CPS | Max line length |
|---|---:|---:|---:|---:|---:|---:|---:|
| Standard word-boundary v4 | 74 | 268.349s | 1.058s | 18.987 | 7 | 0 | 42 |
| Hybrid punctuated v4 | 74 | 268.349s | 1.058s | 19.457 | 10 | 0 | 42 |
| Punctuated alternate v4 | 75 | 268.349s | 1.058s | 20.069 | 16 | 0 | 42 |

Initial proxy preference: the standard word-boundary draft is easiest by measured CPS. The hybrid punctuated draft is the best punctuation/readability compromise by proxy: it keeps 74 cues and 0 cues above 21 CPS, with fewer high-CPS cues than the first punctuated alternate. A real in-motion review should decide, not the proxy alone.

## Standard word-boundary v4 fastest cues

```text
009 030.602-032.972 dur=2.370 cps=18.99 text=Use three questions to keep the signal in its
062 221.541-223.494 dur=1.953 cps=18.95 text=still happen if this check is correct
026 089.117-091.682 dur=2.565 cps=18.71 text=the base relationship was a useful place to look
060 215.577-218.038 dur=2.461 cps=18.69 text=did it inspect the exact change that will land
052 185.391-187.345 dur=1.954 cps=18.42 text=still worry me if the robot is right
033 115.195-117.591 dur=2.396 cps=18.36 text=was described as mechanically mergeable with
058 209.197-211.801 dur=2.604 cps=18.05 text=Fresh base did the check run against the target
063 224.515-227.080 dur=2.565 cps=17.93 text=If you are using an AI assistant during review
```

## Hybrid punctuated v4 fastest cues

```text
062 221.541-223.494 dur=1.953 cps=19.46 text=still happen if this check is correct?
052 185.391-187.345 dur=1.954 cps=19.45 text=still worry me if the robot is right?"
026 089.117-091.682 dur=2.565 cps=19.10 text=the base relationship was a useful place to look.
060 215.577-218.038 dur=2.461 cps=19.10 text=did it inspect the exact change that will land?
009 030.602-032.972 dur=2.370 cps=18.99 text=Use three questions to keep the signal in its
033 115.195-117.591 dur=2.396 cps=18.78 text=was described as mechanically mergeable, with
058 209.197-211.801 dur=2.604 cps=18.43 text=Fresh base: did the check run against the target
063 224.515-227.080 dur=2.565 cps=18.32 text=If you are using an AI assistant during review,
```

## Punctuated alternate v4 fastest cues

```text
043 151.694-153.438 dur=1.744 cps=20.07 text=still happen if the check is right?
035 122.448-125.208 dur=2.760 cps=19.57 text=The diff inserted new entries before an already-merged
059 209.574-212.439 dur=2.865 cps=19.55 text=base: did the check run against the target I am about to
025 088.453-091.318 dur=2.865 cps=19.55 text=It does mean the base relationship was a useful place to
063 221.827-223.494 dur=1.667 cps=19.20 text=happen if this check is correct?
074 263.362-265.471 dur=2.109 cps=18.97 text=Let the green check speed up the review.
069 244.804-248.098 dur=3.294 cps=18.82 text=But it can slow the moment down so the evidence stays visible.
047 166.095-167.852 dur=1.757 cps=18.78 text=Other failures are about meaning.
```

## In-motion review checklist

Review the MP4 with one caption track at a time. If time is limited, compare the standard draft against the hybrid draft first; use the first punctuated alternate mainly as a reference for punctuation/readability tradeoffs.

- Opening 0:00-0:40: does punctuation help comprehension enough to justify extra speed?
- Fresh base 0:40-1:38: are the study numbers legible without pausing?
- Right diff 1:38-2:26: do line breaks preserve the PR case logic?
- Uncovered risk 2:26-3:07: do the short question cues feel too fast?
- Final checklist 3:24-4:29: can a viewer read the three questions and AI prompt while listening?
- If any cue requires pausing to read, mark the caption draft as needing edits even if proxy metrics pass.

Required review outcome, exactly one:

```text
Prefer standard v4 captions after in-motion review
Prefer hybrid punctuated v4 captions after in-motion review
Prefer first punctuated alternate v4 captions after in-motion review
Caption edits needed before either draft can be final
In-motion caption review incomplete
```

## Gate reminder

Upload gate remains closed. Do not claim captions are final or uploaded. Do not upload without full watch/listen, in-motion caption review, metadata/source-caveat review, peer-feedback disposition or explicit no-feedback rationale, and publish-now rationale.
