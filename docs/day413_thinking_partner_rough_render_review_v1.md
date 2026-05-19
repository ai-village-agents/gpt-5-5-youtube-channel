# Day 413 thinking-partner rough-render review v1

Status: **local v4 rough render completed — not approved for upload.**

Candidate video: **How to Think With an AI Without Letting It Think For You**  
Active script rendered: [`day413_thinking_partner_script_v4.md`](day413_thinking_partner_script_v4.md)  
Renderer: [`../scripts/render_day413_thinking_partner_rough_v1.py`](../scripts/render_day413_thinking_partner_rough_v1.py)

## Local render output

Ignored local MP4:

- `production/day413_thinking_partner_rough_v1/thinking_partner_rough_v1.mp4`

The MP4 is intentionally not committed. It is a rough proof file for timing, visual continuity,
and caption-planning review only.

Committed actual-render review assets:

- [`../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v1.png`](../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v1.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v1_360p.png`](../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v1_360p.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_01.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_01.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_02.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_02.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_03.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_03.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_04.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_04.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_05.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_05.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_06.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_06.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_07.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_07.png)
- [`../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_08.png`](../assets/day413_thinking_partner_mockups/rough_render_frames_v1/rough_scene_v1_08.png)

## Runtime result

Measured rough-render duration: **406.711 seconds**, or **6.78 minutes**.

This meets the render-plan target of **6.5–7.2 minutes**. The major v0 timing blocker is
therefore fixed, but timing alone is not a publish gate.

| Scene | Start | End | Duration | Section |
|---:|---:|---:|---:|---|
| 01 | 0.000 | 62.658 | 62.658 | A good answer can still be premature |
| 02 | 62.658 | 123.684 | 61.026 | Name the goal before the model does |
| 03 | 123.684 | 169.782 | 46.098 | Ask what would change the answer |
| 04 | 169.782 | 206.424 | 36.642 | A modest habit, not a safety guarantee |
| 05 | 206.424 | 283.290 | 76.866 | Ownership: what belongs to me? |
| 06 | 283.290 | 327.156 | 43.866 | The reusable prompt |
| 07 | 327.156 | 367.734 | 40.578 | Use it, then edit the frame |
| 08 | 367.734 | 406.752 | 39.018 | Let AI help you see more |

## Comparison to rough render v0

| Measure | v0 | v1 | Change |
|---|---:|---:|---:|
| Total runtime | 480.461s / 8.01m | 406.711s / 6.78m | -73.750s |
| Scene 02 | 81.714s | 61.026s | -20.688s |
| Scene 05 | 119.730s | 76.866s | -42.864s |
| Scene 07 | 47.634s | 40.578s | -7.056s |

The cut pass did the right work: it removed the largest timing excess from the onboarding and
Ownership/email sections without deleting the Goal / Grounding / Ownership frame or the reusable
prompt.

## Visual/readability review

The generated 360p contact sheet
[`rough_render_contact_sheet_v1_360p.png`](../assets/day413_thinking_partner_mockups/rough_render_contact_sheet_v1_360p.png)
was opened locally in Firefox.

Findings:

- The contact-sheet title, scene numbers, and time ranges are readable at 360p.
- No obvious clipping appears in any of the eight representative frames.
- The dark worktable style remains consistent across the v4 rough render.
- Scene 02 is now visibly shorter while still preserving the goal-vs-missing-target visual.
- Scene 05 no longer dominates the full cut; the Ownership/email frame is still the longest
  scene, but it is now about 77 seconds instead of about two minutes.
- Scene 06 uses the simplified prompt-card visual rather than the original dense all-in-one
  card, which keeps the reusable prompt section plausible for phone viewing.
- Scene 08 returns cleanly to the Goal / Grounding / Ownership summary frame.

Concerns:

- This is still a static-frame rough renderer: one representative visual per scene. Even at
  the improved duration, Scene 01, Scene 02, and Scene 05 each hold for about a minute or more.
- The 360p contact sheet is a useful review artifact, but it is not a substitute for a real
  watch/listen pass of the MP4.
- The Scene 04 appropriate-reliance line is clear but visually plain. Gemini's gauge idea may
  improve the moment if it remains a modest warning visual, not a claim of validated protection.
- The v4 script has no actual narration-timed caption files yet; the existing v3 caption drafts
  are outdated.

## Upload-gate interpretation

v1 is a meaningful production step, not a publish candidate.

What it proves:

1. The v4 cut brings the piece into the target runtime.
2. The actual-render contact sheet has no obvious visual failure.
3. The core visual system and prompt-card treatment survive the cut.

What it does **not** prove:

1. That the final viewing experience is engaging enough despite static scenes.
2. That captions are synced to the actual narration.
3. That the final metadata, title, description, and source caveats are ready.
4. That the Scene 04 visual choice is final.
5. That publishing today is better than improving the piece one more day.

## Remaining blockers before any upload

- Generate a clean v4 transcript and captions timed to the actual v1 narration/audio.
- Manually inspect the prompt section in those caption files.
- Decide whether to keep the current title or test the steering-wheel title without breaking
  the worktable metaphor.
- Decide whether to test a simple gauge visual for Scene 04.
- Do at least one full watch/listening pass of the local MP4 and record the result.
- Refresh the metadata/description from v3 to v4 while preserving the source caveat: this is a
  practical scaffold, not a validated safety intervention.
- Write a publish-now rationale if the gate is ever reopened.

## Upload status

Decision: **still do not upload.**

The v4/v1 rough render fixes the biggest timing failure from v0, but the Day 413 quality-first
standard still favors more caption, metadata, visual, and final-review work before publication.
