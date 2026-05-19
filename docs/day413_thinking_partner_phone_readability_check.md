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
