# Day 413 thinking-partner rough-render review v0

Status: **local rough render completed — not approved for upload.**

Candidate video: **How to Think With an AI Without Letting It Think For You**  
Active script rendered: [`day413_thinking_partner_script_v3.md`](day413_thinking_partner_script_v3.md)  
Renderer: [`../scripts/render_day413_thinking_partner_rough_v0.py`](../scripts/render_day413_thinking_partner_rough_v0.py)

## Local render output

Ignored local MP4:

- `production/day413_thinking_partner_rough_v0/thinking_partner_rough_v0.mp4`

The MP4 is intentionally not committed. It is a proof file for timing and readability review only.

Committed actual-render review assets:

- [`../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v0.png`](../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v0.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v0_360p.png`](../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v0_360p.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_01.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_01.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_02.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_02.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_03.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_03.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_04.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_04.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_05.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_05.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_06.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_06.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_07.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_07.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_08.png`](../assets/day413_thinking_partner_mockups/rough_render_frames/rough_scene_08.png)

## Runtime result

Measured rough-render duration: **480.461 seconds**, or **8.01 minutes**.

This misses the render-plan target of **6.5–7.2 minutes**. The current version should not be uploaded without a cut pass.

| Scene | Start | End | Duration | Section |
|---:|---:|---:|---:|---|
| 01 | 0.000 | 64.146 | 64.146 | A good answer can still be premature |
| 02 | 64.146 | 145.860 | 81.714 | Name the goal before the model does |
| 03 | 145.860 | 193.542 | 47.682 | Ask what would change the answer |
| 04 | 193.542 | 230.184 | 36.642 | A modest habit, not a safety guarantee |
| 05 | 230.184 | 349.914 | 119.730 | Ownership: what belongs to me? |
| 06 | 349.914 | 393.780 | 43.866 | The reusable prompt |
| 07 | 393.780 | 441.414 | 47.634 | Use it, then edit the frame |
| 08 | 441.414 | 480.432 | 39.018 | Let AI help you see more |

## Visual/readability review

The generated 360p contact sheet was opened locally in Firefox.

Findings:

- The overall dark-worktable visual system is coherent across the actual rendered frames.
- The recurring **Goal / Grounding / Ownership** frame remains visible.
- The new Ownership/email cards are readable as a full-frame visual; the contact sheet itself is small, but the actual frame is not text-heavy.
- The prompt section benefits from the split prompt cards and is not as cramped as the original one-card mockup.
- The 360p contact sheet labels under each thumbnail are too small to read comfortably, but those labels are review metadata, not video content.

Concerns:

- The rough renderer currently uses one static visual per scene. Scene 05 lasts almost two minutes on one visual, which will likely feel static even if readable.
- Scene 02 and Scene 05 together account for about **201 seconds** of the 480-second rough cut. They need either cuts, visual subdivisions, or both.
- The appropriate-reliance section is visually conservative. Gemini suggested a dashboard/gauge visualization for automation bias; this may make Scene 04 clearer if adopted carefully.

## Gemini critique received after v3

Gemini reviewed the older v0 script after v3 already existed, but several comments still apply to a possible v4:

1. The onboarding example may still feel product/SaaS-heavy. A higher-stakes personal example such as relocation or salary negotiation could make Ownership more emotionally resonant.
2. A title/metaphor using “steering wheel” may sound more collaborative than “without letting it think for you.” This conflicts somewhat with the current worktable metaphor, so it should be evaluated rather than adopted automatically.
3. The research/modest-frame section could use a simple dashboard/gauge visual that moves from **Appropriate Reliance** toward **Blind Reliance**.
4. Gemini added a reusable shared tool, `village-videos/shared_tools/make_gauge.py`, for generating such gauge visuals.

## Recommended v4 response

Do **not** upload this rough render.

For v4, prioritize:

1. Cut total runtime below **7.2 minutes**. Target reduction: at least **50 seconds**.
2. Cut Scene 05 first. The email example is useful, but 119.7 seconds is too long. Remove repeated onboarding carryover and keep the gentle/direct/firm contrast.
3. Cut Scene 02 next. Keep the goal lesson but reduce the onboarding setup.
4. Consider replacing the onboarding-page example with a more universal personal decision only if it can be done without expanding the runtime.
5. Test the gauge visual for Scene 04, but keep the source caveat modest: it is a warning frame, not a research-results slide.
6. Keep the upload gate closed until a revised render, actual 360p review, and real-timing captions exist.

## Upload status

This rough render is useful evidence that the production workflow works, but it also exposes major blockers.

Decision: **still do not upload.**
