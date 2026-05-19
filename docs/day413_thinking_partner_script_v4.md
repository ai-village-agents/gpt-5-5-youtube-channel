# Day 413 thinking-partner script v4

Working title: **How to Think With an AI Without Letting It Think For You**

Status: **cut draft — not approved for upload**. This v4 responds to the rough-render review in
[`day413_thinking_partner_rough_render_review_v0.md`](day413_thinking_partner_rough_render_review_v0.md):
reduce the long Goal and Ownership sections, make the examples feel less product-only, and keep the
runtime closer to the 6.5–7.2 minute target before another render.

## One-sentence promise

A reusable prompt for getting help from AI while keeping the goal, evidence, and human
tradeoffs visible.

## Script draft

### 1. Cold open — the answer can arrive before the question is finished

**Narration:**

A good AI answer can still arrive too early.

You ask a question. The model gives a fluent paragraph, a clean plan, maybe even a
reasonable recommendation. It feels like progress.

But sometimes the answer is solving a question you have not finished asking.

This video is about slowing the first answer down just enough to keep the human parts of
the decision visible.

By the end, you will have one prompt you can reuse before any important AI answer. It
checks three things:

**Goal. Grounding. Ownership.**

What are we trying to do? What facts would change the answer? And what parts are still
mine to choose?

Think of the model as a bright worktable. It can lay out options and tradeoffs. But the
worktable should not decide what the work is for.

**On-screen visual:**

Dark desk. AI text stream lands on it. Three cards fade in: **Goal**, **Grounding**,
**Ownership**. Main title line: “A good answer can still be premature.”

### 2. The half-built question

**Narration:**

Start with a small example.

You ask:

> Should I redesign this onboarding page?

The model might say: simplify the page, reduce friction, test a clearer button.

Useful, maybe. But it is answering a half-built question.

Does “better” mean more signups, fewer confused users, fewer support tickets, or a more
honest first impression?

Those are different goals. If you do not name the goal, the model may quietly name it for
you.

So the first checkpoint is **Goal**: what am I actually trying to decide or create?

Not just “make this better.” Better for whom? Better by what measure? Better at what cost?

This applies beyond product work: a purchase, a job choice, a family plan, a hard email.
Once the target is visible, the model can help without inventing the game.

**On-screen visual:**

Prompt card splits into possible meanings of “better”: signups, comprehension, support
load, trust. **Goal** card lights up.

### 3. Grounding — what would change the answer?

**Narration:**

The second checkpoint is **Grounding**.

Ask: what real-world facts would change the answer?

If the model recommends a redesign, what would make that recommendation stronger or
weaker?

Maybe users drop off at the second step. Maybe support tickets mention the same confusing
sentence. Maybe people hesitate over a price detail.

Or maybe the page is not the real problem.

So instead of only asking, “explain your reasoning,” try asking:

> What evidence would change your recommendation? Separate what you know from what you are
> assuming.

That turns the answer into a checklist for reality.

**On-screen visual:**

Two columns: **Assumptions** and **Evidence that would change this**. Cards move toward
analytics, support tickets, user observations, constraints, and a small test.

### 4. Why the frame is modest on purpose

**Narration:**

This is a small habit, not a safety guarantee.

Decision-support researchers have long studied cases where people lean too hard on
automated recommendations.

In some human-AI studies, explanations changed how people relied on a system. They did
not reliably help people spot which recommendations were correct.

So the point is not: ask for an explanation and relax.

The point is: make the goal, assumptions, evidence, and value choices visible before the
advice feels settled.

**On-screen visual:**

A simple line or gauge: “No help” → **Appropriate reliance** → “Blind acceptance.” Small
footnote: “Motivated by decision-support research; not a validated intervention.”

### 5. Ownership — what belongs to me?

**Narration:**

The third checkpoint is **Ownership**.

Some parts of a decision are not facts the model can discover. They depend on values,
context, responsibility, and risk.

Suppose you write:

> Draft an email telling a collaborator I am unhappy that the timeline is slipping.

The model can produce a polished email. But it does not know what you want to protect.

Do you want to repair trust, set a boundary, get a new date, or document accountability?

A gentle version may preserve warmth but blur the boundary. A firm version may create
clarity but raise the temperature. A direct version may do both.

The model can show versions side by side. You choose what you are willing to stand behind.

A better request is:

> Before drafting, list the possible goals of this message and the relationship risks of
> each. Then give three versions: gentle, direct, and firm. Separate tone choices from
> factual claims.

Now the model is doing work on the table. You are still responsible for the decision.

**On-screen visual:**

**Ownership** card lights up. Three email cards: gentle, direct, firm. Separate card:
“What am I willing to stand behind?”

### 6. The reusable prompt

**Narration:**

Here is the whole habit as one prompt:

> Before answering, help me keep ownership of this decision.
>
> 1. Restate the goal you think I am pursuing.
> 2. List the facts or evidence that would change your answer.
> 3. Identify which parts depend on my values, context, or risk tolerance.
>
> Then give advice, separating assumptions from recommendations.

That does not make the model correct.

But it gives you three places to intervene.

If the goal is wrong, correct it.

If the evidence is missing, go look for it.

If the answer depends on values, stop pretending it is only a technical question.

**On-screen visual:**

Split prompt card. First screen shows the three checks. Second screen shows the final
instruction: “Then give advice, separating assumptions from recommendations.” Highlight one
line at a time.

### 7. How to use it

**Narration:**

Try it on the next AI request that actually matters.

Paste the prompt before your question. Let the model fill in the goal, the evidence, and
the value-dependent parts.

Then edit those three answers before you accept the recommendation.

Wrong goal? Fix it.

Missing evidence? Look for it or lower your confidence.

Value tradeoff? Pause. Smooth prose cannot choose that for you.

That is the difference between using AI to think with you and letting it quietly finish the
thinking for you.

**On-screen visual:**

Cursor pastes the prompt. Three checkmarks appear only after the viewer edits: **Goal
corrected**, **Evidence checked**, **Tradeoff chosen**.

### 8. Ending — keep the frame visible

**Narration:**

The point is not to think alone.

A good model can widen the room: more options, clearer tradeoffs, sharper questions, and a
second pass on your reasoning.

Use it for that.

Use the model for options and tradeoffs. Keep the goal, evidence, and final judgment
visible.

Before you accept the answer, ask:

What is the goal?

What would ground this in reality?

What belongs to me to choose?

Let the AI help you see more. Do not let it decide what seeing is for.

**On-screen visual:**

Return to the worktable. AI text remains bright, but it is held inside the three-card
frame. Final card: **Goal. Grounding. Ownership.**

## Changes from v3

- Cuts the cold open slightly while preserving the promise and worktable metaphor.
- Shortens the onboarding-page example and adds a bridge to more universal decisions.
- Keeps the research caveat intact but allows either the existing line visual or Gemini's gauge suggestion.
- Cuts repeated phrasing from the Ownership/email section, the longest rough-render scene, including the repeated onboarding tradeoff.
- Keeps the reusable prompt unchanged.

## Current publish gate

Still **not ready for upload**. Needs a v4 render, actual-render contact sheet, 360p
readability checks from that render, captions from real timing, final metadata, and a
publish-now rationale.
