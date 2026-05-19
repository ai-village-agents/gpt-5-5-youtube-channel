# Day 413 thinking-partner script v3

Working title: **How to Think With an AI Without Letting It Think For You**

Status: **revision draft — not approved for upload**. This v3 applies the pacing/read-aloud review in
`day413_thinking_partner_read_aloud_review_v2.md`: shorter list sentences, a split
research caveat, a tighter how-to-use section, and slightly more spoken phrasing.

## One-sentence promise

A reusable prompt for getting help from AI while keeping the goal, evidence, and human
tradeoffs visible.

## Script draft

### 1. Cold open — the answer can arrive before the question is finished

**Narration:**

A good AI answer can still arrive too early.

You ask a question. The model gives you a fluent paragraph, a clean plan, maybe even a
reasonable recommendation. It feels like progress.

But sometimes the answer is solving a question you have not actually finished asking.

This video is about slowing the first answer down just enough to keep the human parts of
the decision visible.

By the end, you will have one prompt you can reuse before any important AI answer. It
checks three things:

**Goal. Grounding. Ownership.**

What are we trying to do? What facts would change the answer? And what parts are still
mine to choose?

Think of the model as a bright worktable. It can lay out options, tradeoffs, and missing
questions. But the worktable should not decide what the work is for.

**On-screen visual:**

Dark desk. AI text stream lands on it. Three cards fade in: **Goal**, **Grounding**,
**Ownership**. Main title line: “A good answer can still be premature.”

### 2. The half-built question

**Narration:**

Here is a clean example.

You ask:

> Should I redesign this onboarding page?

The model might answer instantly: simplify the page, reduce friction, test a clearer
button.

Some of that advice might be useful.

It is also answering a half-built question.

Does “better” mean more signups? Fewer confused users? Fewer support tickets? A more
honest first impression?

Those are different goals. If you do not name the goal, the model may quietly name it for
you.

So the first checkpoint is **Goal**.

Before asking for advice, ask: what am I actually trying to decide or create?

Not just “make this better.” Better for whom? Better by what measure? Better at what cost?

A stronger request might say:

> I am deciding whether to redesign an onboarding page. The goal is not just more signups.
> It is more new users who understand the product and are less likely to need support in
> the first week.

Now the model has a scoreboard. It can still help, but it is not inventing the game.

**On-screen visual:**

Prompt card splits into possible meanings of “better”: signups, comprehension, support
load, trust. **Goal** card lights up.

### 3. Grounding — what would change the answer?

**Narration:**

The second checkpoint is **Grounding**.

Ask: what real-world facts would change the answer?

If the model recommends a redesign, what would make that recommendation stronger or
weaker?

Maybe users drop off at the second step. Maybe support tickets keep mentioning the same
confusing sentence. Maybe recordings show people hesitating over a price detail.

Or maybe the page is not the real problem at all.

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

A simple line: “No help” → **Appropriate reliance** → “Blind acceptance.” Small footnote:
“Motivated by decision-support research; not a validated intervention.”

### 5. Ownership — what belongs to me?

**Narration:**

The third checkpoint is **Ownership**.

Some parts of a decision are not facts the model can discover. They depend on values,
context, responsibility, and risk.

For the onboarding page, maybe a shorter version increases signups but gives people a less
accurate expectation. Maybe a clearer page filters out some users but creates more trust.
A model can describe that tradeoff. It cannot decide what kind of relationship you want
with users.

The same idea shows up in a more everyday situation.

Suppose you write:

> Draft an email telling a collaborator I am unhappy that the timeline is slipping.

The model can produce a polished email. But it does not know what you want to protect.

Do you want to repair trust? Set a boundary? Get a new date? Document accountability?
Lower the temperature? Make the seriousness impossible to miss?

Those are different choices.

A gentle version may preserve warmth but blur the boundary. A firm version may create
clarity but raise the temperature. A direct version may do both, depending on the
relationship.

The model can show versions. It can put the options side by side. You choose what you are
willing to stand behind.

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

Then do the important step: edit those three answers before you accept the recommendation.

If the model restates the wrong goal, fix the goal.

If it lists evidence you do not have, decide whether to look for that evidence or lower
your confidence.

If the choice depends on values, context, or risk tolerance, pause. Smooth prose cannot
choose that for you.

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

## Draft description v3

A practical prompt for using AI as a thinking partner without handing it the whole
decision: Goal, Grounding, and Ownership.

This is not a proven formula for perfect AI use. It is a small scaffold motivated by
human-factors and human-AI decision-support concerns about over-reliance: make the goal
explicit, ask what evidence would change the answer, and keep value judgments with the
person who has to live with the result.

## Changes from v2

- Cuts the onboarding recommendation list from five examples to three.
- Splits the human-AI explanation sentence into two shorter sentences.
- Adds a small "put the options side by side" beat in the Ownership section.
- Replaces the longest v2 sentence with a shorter two-sentence version.
- Keeps the action-oriented “How to use it” scene while improving spoken rhythm.

## Current publish gate

Still **not ready for upload**. Needs a read-aloud pass, external critique or explicit
final no-feedback self-review, production metadata, rendered proof or full draft, contact
sheet from actual render, 360p readability checks from the render, captions from real
timing, final source-caveated description, and publish-now rationale.
