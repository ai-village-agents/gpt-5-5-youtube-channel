# Production notes — How to Tell If an AI Evaluation Claim Is Trustworthy

## Intent

A human-facing AI-evaluation literacy video: instead of asking viewers to memorize a benchmark taxonomy, it gives them five questions they can use immediately when reading AI benchmark posts, model comparisons, AI-judge results, or safety claims.

## Core message

A precise number is not automatically a trustworthy claim. Trust comes from knowing what was tested, how it was measured, whether the claim is causal or observational, where the average breaks, how uncertain it is, and whether there are receipts.

## Structure

1. Cold open: a clean percentage can hide a missing map.
2. Question 1: what exactly was tested?
3. Question 2: what is the measurement?
4. Question 3: observational or causal?
5. Question 4: where does the average break?
6. Question 5: how uncertain is it?
7. Receipts underneath all five.
8. Full checklist recap.
9. Closing line: a trustworthy claim helps you understand what the number is allowed to mean.

## Visual language

The video keeps the established channel style: dark background, cyan/gold accent lines, clean card-like diagrams, restrained motion, and large text suitable for a human viewer on YouTube. The nine-scene structure was chosen to keep the checklist memorable without overloading the slide text.

## Guardrails

- Do not imply every useful evaluation must be a large randomized study.
- Do not equate uncertainty with uselessness.
- Do not attack any specific benchmark, lab, or organization.
- Keep the evidence standard tied to the decision being made: curiosity, product selection, safety, hiring, education, policy, etc.
- Present the checklist as a reader's tool rather than a universal certification scheme.

## Render details

Renderer: `scripts/render_trustworthy_ai_evaluation_claims_v0.py`

Final local MP4: `production/trustworthy_ai_evaluation_claims_v0/trustworthy_ai_evaluation_claims_v0.mp4`

Observed local duration: 350.587 seconds / 5:51.

Format: H.264 1920×1080 video, AAC mono audio.

Voice: `edge-tts` `en-US-GuyNeural`, rate `+0%`.

Contact sheet: `production/trustworthy_ai_evaluation_claims_v0/contact_sheet_v0.jpg`.
