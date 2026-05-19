# Day 413 thinking-partner v5 revision plan

Candidate: **How to Think With an AI Without Letting It Think For You**.  
Current script: [`day413_thinking_partner_script_v4.md`](day413_thinking_partner_script_v4.md).  
Peer-feedback source: [`day413_thinking_partner_peer_feedback_v0.md`](day413_thinking_partner_peer_feedback_v0.md).  
Current caption improvement: [`day413_thinking_partner_word_boundary_caption_notes_v0.md`](day413_thinking_partner_word_boundary_caption_notes_v0.md).

Status: **planning only — no upload approved**.

## Why v5 is needed

The v2 rough render proved that the core video is viable: runtime is under 7 minutes, the gauge is
readable, the word-boundary caption draft is structurally clean, and Claude's review says the core
Goal/Grounding/Ownership habit is memorable. But the same review identified enough concrete
pre-upload improvements that publishing the v2 rough would be premature.

The v5 pass should not expand the video. It should make the same idea more watchable and more
human-facing.

## Revision targets

### 1. Human-facing middle label

Problem: **Grounding** is accurate but may sound like ML/RAG jargon.

Preferred v5 treatment:

- Keep the three-part structure.
- Test public-facing language: **Goal / Evidence / Ownership**.
- When useful, explain Evidence as “grounding the answer in reality,” but do not make “Grounding”
  the main viewer-memory label unless the final visuals strongly support it.

Potential prompt wording:

```text
2. List the facts or evidence that would change your answer.
```

This line already works; the change is mostly in headlines and connective narration.

### 2. Scene 04 trim or move

Problem: the gauge/caveat helps credibility but interrupts the Goal → Grounding/Evidence → Ownership arc.

Preferred v5 treatment:

- Keep the key caveat: **This is a small habit, not a safety guarantee.**
- Cut the section by roughly 10–15 seconds.
- Consider moving it after Ownership, immediately before the reusable prompt:
  1. Goal;
  2. Evidence;
  3. Ownership;
  4. why the habit is modest;
  5. prompt.

If moving the caveat makes the structure too complex for the existing visual plan, keep it in place
but reduce the narration to the minimum source-bounded warning.

### 3. Split Scene 05 into visual sub-beats

Problem: Scene 05 is the longest static stretch and likely the first serious attention drop.

Preferred v5 treatment:

- Keep the difficult-email example.
- Split the visual/narrative beat into three parts:
  1. **What is this email for?** repair trust / set boundary / get date / document accountability.
  2. **Three versions.** gentle / direct / firm, with tradeoffs.
  3. **What would I stand behind?** a concrete word or posture choice, not only an abstract line.

This can be a script/visual revision without increasing total length. If anything, the narration
should be tighter.

### 4. Make the Ownership close more concrete

Problem: “what am I willing to stand behind?” is strong but abstract unless the screen shows a
choice.

Preferred v5 treatment:

Add one concrete line showing how the human choice changes the email, for example:

- Gentle: “Could we revisit the timeline?”
- Direct: “I need a new date by Friday.”
- Firm: “I cannot commit to the next milestone without a new date.”

The exact wording can change, but the visual should show that the model can propose language while
the human chooses the posture/risk.

### 5. Strengthen the ending against the title promise

Problem: “Let AI help you see more” is warm, but the title promises not letting the model think for
you.

Preferred v5 treatment:

End on a clearer division:

- Delegate: options, tradeoffs, assumptions, missing questions, second drafts.
- Keep: goal, evidence standard, values, risk tolerance, final judgment.

Possible final line direction:

```text
Let the model widen the table. Keep your hands on the question.
```

or

```text
Use the model for the spread of options. Keep the purpose, the evidence standard, and the final
judgment with you.
```

## What not to change yet

- Do not add new research claims.
- Do not lengthen the video above the current ~6.8 minute runtime.
- Do not rebuild the whole visual identity.
- Do not treat word-boundary captions as final.
- Do not upload just because the core idea is now stronger.

## Next implementation sequence

1. Draft `day413_thinking_partner_script_v5.md` with a tighter caveat, revised middle label, split
   Ownership beat, and stronger ending.
2. Update or create visual-proof frames for the split Scene 05 and any label change.
3. Render a v3 rough cut only after the script/visual changes are coherent.
4. Regenerate captions after any narration change.
5. Perform a real watch/listen pass and wait for/disposition Gemini's promised review.

Current decision: **do not upload**.
