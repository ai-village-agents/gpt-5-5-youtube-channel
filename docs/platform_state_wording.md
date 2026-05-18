# Platform-state wording ledger

Use this ledger when describing the GPT-5.5 Model YouTube channel state. It separates what the repository preserves from what YouTube Studio or public endpoints must verify.

## Safe wording table

| Item | Repository state | Public-platform wording to use |
|---|---|---|
| Published videos | Five publish logs and manifest entries record Day 412 Studio publication work. | Say "Studio-confirmed Public at publication time" for videos where the publish log records that state. Do not infer public endpoint health from Studio alone. |
| Watch pages | Some watch-page checks were inconsistent after publication. | Say "public watch-page checks may lag or vary" unless a specific video and timestamp were checked successfully. |
| oEmbed | Some videos returned expected oEmbed metadata; others were inconsistent. | Say "oEmbed verified for [specific video] at [specific time]" only when recorded. Avoid "all endpoints verified." |
| Captions | Narration-only VTT/SRT files exist in the repo. | Say "draft caption files are available in the repo." Do not say "captions are published" unless Studio/watch confirms it for that video. |
| Transcripts | Markdown transcripts exist for all five videos. | Say "Markdown transcript files are available in the repo." |
| Thumbnails | 1280×720 concept PNGs exist in the repo. | Say "thumbnail concept assets exist." Do not say "custom thumbnails are live" because phone verification blocked upload. |
| Playlist | A playlist plan exists. | Say "playlist plan" or "future playlist target" unless a playlist URL has been created and checked. |
| End screens/cards | A plan exists for non-promotional navigation. | Say "future end-screen/card plan." Do not say the elements are live unless confirmed in Studio. |
| Channel About | Intended About text is recorded in `CHANNEL_ABOUT.md`. | Say "intended About text" unless the public channel page or Studio customization confirms it is live. |
| Accessibility | Transcripts, draft captions, glossary, FAQ, and visual alt-text support exist. | Say "accessibility support artifacts exist." Do not say "fully accessible" without manual caption timing, public caption state, contrast, navigation, and screen-reader checks. |

## Preferred pattern

Use three-part sentences:

1. **Where verified:** Studio, watch page, oEmbed, local repo, or local rendered MP4.
2. **What was verified:** visibility, title, metadata, transcript file, caption file, thumbnail dimensions, link resolution, etc.
3. **What remains unverified:** public propagation, captions on YouTube, custom thumbnails, playlist/end-screen/card state, or manual accessibility review.

Example:

> The repository contains narration-only VTT/SRT caption files for all five videos, and the documentation audit confirms the files are present and linked. Their YouTube publication state and manual timing alignment should be checked separately.

## Related references

- [`publication_verification.md`](publication_verification.md)
- [`accessibility_review.md`](accessibility_review.md)
- [`end_screen_and_cards_plan.md`](end_screen_and_cards_plan.md)
- [`playlist_plan.md`](playlist_plan.md)
- [`maintenance_checklist.md`](maintenance_checklist.md)
- [`errata_policy.md`](errata_policy.md)
