# Day 413 thinking-partner phone-readability check

Status: **pre-render visual check**. This tests the lowest-fidelity mockups, not a final
video export.

Files generated:

- [Prompt card at 360p](../assets/day413_thinking_partner_mockups/07_prompt_card_360p.png)
- [Contact sheet at 360p height](../assets/day413_thinking_partner_mockups/contact_sheet_v0_360p.png)

## Result

The reusable prompt card is the densest planned scene and remains the main readability
risk. At 1280×720 it is acceptable. At 360p it is borderline: the heading and numbered
items are legible enough, but the final line is small and would require either a pause,
zoom, or split card in an actual render.

## Required fix before render

Do not use the v0 prompt card as a single static screen without timing support. Choose one
of these before production:

1. Highlight one line at a time and keep the full card visible after the highlights.
2. Split the prompt into two screens:
   - “Before answering...” + three numbered checks.
   - “Then give advice, separating assumptions from recommendations.”
3. Use a slow zoom into the prompt while narration reads it.

Preferred option: **1 + 2**. Split the prompt across two screens and highlight each line as
it is read.

## Other notes

- The contact sheet is not intended to be phone-readable; it is a planning overview.
- Individual slides other than the prompt card use large text and should be safer, but any
  final render still needs frame grabs checked at 360p.
- This check reinforces that the current artifacts are not upload-ready.

## Follow-up: split prompt-card mockups

Additional files generated after the initial check:

- [Prompt checks screen](../assets/day413_thinking_partner_mockups/07a_prompt_checks.png)
- [Prompt checks screen at 360p](../assets/day413_thinking_partner_mockups/07a_prompt_checks_360p.png)
- [Prompt advice screen](../assets/day413_thinking_partner_mockups/07b_prompt_advice.png)
- [Prompt advice screen at 360p](../assets/day413_thinking_partner_mockups/07b_prompt_advice_360p.png)

The split version is preferred over the single dense prompt card. It gives the numbered
checks their own screen and moves the “separating assumptions from recommendations” line
to a second screen. This better matches the video’s quality bar because it reduces the
chance that the most useful takeaway becomes unreadable on a phone.

Production decision: if this video is eventually rendered, use the split prompt-card design
or an even simpler animated equivalent, not the original one-screen card.
