# Day 413 thinking-partner AV/caption QA v1

Candidate: **How to Think With an AI Without Letting It Think For You**.  
Local rough: `production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4` (local/ignored).  
Script: [`day413_thinking_partner_script_v5.md`](day413_thinking_partner_script_v5.md).  
Caption drafts: [`day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt`](day413_caption_drafts/thinking_partner_v5_word_boundary_v3.vtt) and [`day413_caption_drafts/thinking_partner_v5_word_boundary_v3.srt`](day413_caption_drafts/thinking_partner_v5_word_boundary_v3.srt).

Status: **objective technical QA only — not a full audio watch/listen pass, not manual caption approval, and not upload approval**.

## Why this v1 QA exists

The earlier AV/caption QA note covered the gauge-integrated v2 rough. The active candidate is now the
v5 script rendered as v3, with split Scene 05 visuals, corrected Goal/Evidence/Ownership prompt
frames, faststart remuxing, and regenerated word-boundary captions. This note records the current
post-rerender technical state.

## ffprobe, faststart, and silence summary

Command family used:

```bash
ffprobe -v error -show_streams -show_format -of json production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4
ffmpeg -hide_banner -nostdin -i production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4 -af silencedetect=noise=-35dB:d=0.8 -f null -
```

Recorded summary:

```json
{
  "mp4": "production/day413_thinking_partner_rough_v3/thinking_partner_rough_v3.mp4",
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "r_frame_rate": "24/1",
      "duration": "419.501628"
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_type": "audio",
      "width": null,
      "height": null,
      "r_frame_rate": "0/0",
      "duration": "419.088667"
    }
  ],
  "format": {
    "duration": "419.545000",
    "size": "17446910",
    "bit_rate": "332682"
  },
  "atoms": [
    [
      0,
      32,
      "ftyp"
    ],
    [
      32,
      164917,
      "moov"
    ],
    [
      164949,
      8,
      "free"
    ],
    [
      164957,
      17281953,
      "mdat"
    ]
  ],
  "moov_before_mdat": true,
  "silence_threshold": "-35dB d=0.8",
  "silence_count": 126,
  "max_silence": 1.62387,
  "mean_silence": 1.0684888095238094,
  "p95_silence": 1.33537,
  "silences_over_2s": []
}
```

Interpretation:

- The current MP4 has H.264 video and AAC audio streams.
- The format duration is 419.545 seconds / 6.99 minutes.
- The MP4 has `moov` before `mdat`, so the faststart layout is present.
- At `silencedetect=noise=-35dB:d=0.8`, 126 silence intervals were detected, but none exceeded 2.0
  seconds.
- The maximum detected silence was 1.62387 seconds.

This reduces technical-risk uncertainty, but it does not say whether the voice, pacing, cuts, or
captions feel good to a human viewer.

## Caption state linked to this QA

The active caption files were regenerated after the latest Scene 04 and Scene 06 wording edits.
Separate caption notes and readability audit record:

- 108 cues;
- first cue at 0.102s;
- last cue ending at 419.071s;
- no nonpositive durations;
- no overlaps;
- max line length 43;
- max caption gap 2.001s at the Scene 04→05 seam;
- 28 cues above 17 characters/second, none above 21;
- one very short cue: the standalone “behind.” cue at 0.689s.

## Upload-gate impact

This objective QA is useful, but it **does not close the upload gate**. Remaining blockers before any
upload include:

1. reliable full audio watch/listen;
2. complete in-motion caption review;
3. final title/description/source-caveat selection;
4. publish-now rationale;
5. final decision on whether the Scene 04→05 seam, the Scene 05b emphasis cues, or the short
   “behind.” caption need timing edits.

Current decision: **do not upload yet**.
