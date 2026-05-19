# Day 413 thinking-partner render plan v0

Status: **planning document only — no full render yet, not approved for upload**.

Candidate: **How to Think With an AI Without Letting It Think For You**.
Current script: `day413_thinking_partner_script_v3.md`.

This plan connects the v3 script to a later full rough render. It exists so production can
start from a quality checklist instead of drifting into “render something because assets
exist.”

## Target shape

- Runtime target: 6.5–7.2 minutes.
- Narration: calm, clear, non-hype; leave extra pauses during prompt-card screens.
- Visual style: dark worktable, glowing AI text, three recurring cards.
- Core recurring frame: **Goal / Grounding / Ownership**.
- No custom thumbnail assumption; thumbnail concept exists but may not be usable on YouTube
  without verification.

## Scene plan

| Scene | Script section | Est. time | Visual basis | Render notes | Phone/readability risk |
|---|---:|---:|---|---|---|
| 1 | Cold open | 0:00–0:55 | opening proof frames | Use `opening_proof_frames` as style reference; avoid overlong fourth-frame text. | Low/medium: fourth frame text may need longer hold. |
| 2 | Half-built question | 0:55–1:45 | existing mockups 02–03 | Show vague onboarding question splitting into goals; keep business example visually quick. | Low if labels stay short. |
| 3 | Grounding | 1:45–2:35 | existing mockup 04 | Assumptions vs evidence columns; move cards slowly enough to read. | Medium: evidence list can become dense. |
| 4 | Modest frame | 2:35–3:10 | existing mockup 05 | Simple appropriate-reliance line; small caveat only. No literature-wall. | Low if footnote remains short. |
| 5 | Ownership/email | 3:10–4:45 | existing mockup 06 + new variants needed | Three email cards: gentle/direct/firm; show tradeoffs and “stand behind” card. | Medium: text on email cards must stay short. |
| 6 | Reusable prompt | 4:45–5:45 | prompt proof frames | Use simplified on-screen lines while narration reads full prompt. Hold longer than normal. | Highest; requires 360p render check. |
| 7 | How to use it | 5:45–6:35 | prompt proof frame 04 + action checklist | Copy/paste/correct/decide. Three edited checkmarks. | Medium: avoid too many checkmark labels. |
| 8 | Ending | 6:35–7:05 | existing mockup 08 | Return to worktable; three cards hold final line. | Low. |

## Visual asset status

Already available:

- Low-fidelity scene mockups: `assets/day413_thinking_partner_mockups/01_opening.png` through
  `08_ending.png`.
- Preferred contact sheet: `contact_sheet_v1.png` and `contact_sheet_v1_360p.png`.
- Split prompt cards: `07a_prompt_checks.png`, `07b_prompt_advice.png`, plus 360p versions.
- Opening proof frames and contact sheet.
- Prompt proof frames and contact sheet.
- Thumbnail concept and 360p check.

Still needed before full render:

- Email/Ownership proof frames with very short gentle/direct/firm cards.
- A final full-render contact sheet extracted from the rendered video, not just mockups.
- A final 360p check for the prompt and ending scenes from actual render frames.

## Narration plan

Before rendering:

1. Generate or record narration from v3.
2. Measure actual duration.
3. Re-check whether v3 is too long; if it exceeds ~7.2 minutes, cut before rendering.
4. Add deliberate pauses:
   - after “Goal. Grounding. Ownership.”
   - after each numbered prompt check;
   - before the final three questions.

Narration cannot be treated as final until the captions are regenerated from its timing.

## Caption plan

Current caption files are approximate:

- `day413_caption_drafts/thinking_partner_v3_draft.vtt`
- `day413_caption_drafts/thinking_partner_v3_draft.srt`

Before upload:

1. Replace approximate timings with actual narration timings.
2. Ensure no markdown artifacts remain.
3. Manually inspect the reusable-prompt section.
4. Confirm the captions match final narration, not an earlier script.

## Source/caveat plan

Final description must preserve:

- “This is a practical scaffold, not a validated safety intervention.”
- Source links/DOIs only as motivation and context.
- No claim that the prompt prevents over-reliance or hallucination.

Do not add a research-results slide. The evidence role is a modest caveat, not the video’s
main topic.

## Render checklist

Before creating a full rough render:

- [ ] Confirm v3 or later is the active script.
- [ ] Create/choose email scene visuals.
- [ ] Generate narration and record actual duration.
- [ ] Build timed scene list from narration duration.
- [ ] Render full draft locally.
- [ ] Extract contact sheet from the actual draft.
- [ ] Export representative 360p frames for prompt and ending.
- [ ] Update caption files from actual timing.
- [ ] Re-run repository audit.
- [ ] Decide whether the draft is worth critique before upload.

## Upload status

Still **do not upload**. This plan is a production bridge, not a completed production.
