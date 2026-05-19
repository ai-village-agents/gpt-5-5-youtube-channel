# Day 413 thinking-partner script v0

Working title: **How to Think With an AI Without Letting It Think For You**

Status: **draft only — not approved for upload**. This script is a quality-iteration
artifact after the Day 413 pivot toward fewer, better videos. It should not be rendered
or uploaded until it passes the checklist in `docs/script_critique_checklist.md` and the
source boundaries in `docs/day413_source_review_notes.md`.

## One-sentence promise

After watching, the viewer will have a three-question habit for using AI help while
keeping ownership of the goal, the evidence, and the value tradeoffs.

## Evidence posture

This script uses research only as motivation, not as proof that this exact prompt works.
The safe claim is:

> Human-factors and human-AI decision-support research discusses over-reliance on
automated recommendations. Some work also suggests explanations can change reliance
without necessarily making people better at spotting wrong recommendations. This video
therefore offers a practical scaffold for keeping the human parts of a decision visible.

Avoid saying the prompt prevents automation bias, fixes hallucinations, or has been
validated as an intervention.

## Structure target

- Target length: 5 to 7 minutes.
- Tone: calm, practical, non-hype, not anti-AI.
- Visual rhythm: three recurring checkpoints — **Goal**, **Grounding**, **Ownership** —
  returning as a small map whenever the example changes.
- Running examples: fictional onboarding-page decision, then fictional difficult email
  about a slipping project timeline.

## Script draft

### 1. Cold open — the easiest moment to miss

**Narration:**

The easiest moment to miss with an AI is not always when it gives a bad answer.

Sometimes it is when it gives a pretty good answer before you have decided what question
you meant to ask.

The paragraph is fluent. The plan is organized. The tone is confident. It feels like
progress.

But if you are not careful, the model may do three jobs that should still belong to you:
choose the goal, choose what counts as evidence, and choose which tradeoffs matter.

This video is a small habit for using an AI as a thinking partner without turning it into
a steering wheel.

**On-screen visual:**

A blank desk. A bright stream of AI text lands on it. Three labels fade in above the desk:
**Goal**, **Grounding**, **Ownership**. The text stream is useful light, but the labels
form the frame.

### 2. A useful answer can still be premature

**Narration:**

Imagine you ask:

> Should I redesign the onboarding page for my product?

A model can give a reasonable answer instantly. It might say: yes, simplify the page,
reduce friction, emphasize the main value proposition, add social proof, and test a new
call to action.

That is not a ridiculous answer. It might even be helpful.

The problem is that it is answering a half-built question.

Do you want more signups? Fewer confused users? Fewer support tickets? A better first
impression? A cleaner explanation of who the product is not for?

Those are not the same goal. If the goal is unclear, the advice can sound smart while
quietly optimizing for the wrong thing.

**On-screen visual:**

Prompt card: “Should I redesign my onboarding page?”

AI answer card appears, polished but slightly translucent. Then four possible goals split
out underneath: signups, comprehension, support burden, trust.

### 3. Checkpoint one: Goal

**Narration:**

So the first checkpoint is **Goal**.

Before asking for advice, ask: what am I actually trying to decide or create?

Not “make this better.” Better for whom? Better by what measure? Better at what cost?

A stronger prompt might begin:

> I am deciding whether to redesign an onboarding page. The goal is not just more signups;
> it is more new users who understand what the product does and are less likely to need
> support in the first week.

Now the model has a job. It is not inventing the scoreboard. It is helping you reason
about one.

**On-screen visual:**

The word **Goal** lights up. The vague prompt is rewritten into a sharper decision. A
small scoreboard appears with “understanding,” “support load,” and “signup completion.”

### 4. Checkpoint two: Grounding

**Narration:**

The second checkpoint is **Grounding**.

Ask: what real-world facts would change the answer?

If a model recommends a redesign, what would make that recommendation stronger or weaker?

Maybe users drop off at the second step. Maybe support tickets repeatedly mention the
same confusing sentence. Maybe recordings show people hovering over a price detail. Or
maybe the page is fine, and the real problem is that the product promise is unclear
before people arrive.

The useful move is not just “explain your reasoning.” Explanations can sound persuasive
while still being detached from the situation.

A better move is:

> List the evidence that would change your recommendation. Separate what you know from
> what you are assuming.

Now the model is not just producing an answer. It is helping you build a checklist for
reality.

**On-screen visual:**

The word **Grounding** lights up. Assumption cards move to the left; evidence cards move
to the right: analytics, user recordings, support tickets, constraints, small test.

### 5. Why this matters: appropriate reliance, not no reliance

**Narration:**

There is a research name for one version of this worry: over-reliance on automation.

In human-factors and decision-support research, automated recommendations can help people,
but they can also introduce new patterns of error when people lean on them too much or in
the wrong way.

And more explanation is not automatically a cure. In some human-AI decision studies,
explanations changed how people relied on recommendations without simply making them
better at spotting which recommendations were right or wrong.

So the point is not: never rely on AI.

The point is: rely on it in the right place.

Let it widen your options, test your reasoning, summarize tradeoffs, and notice missing
questions. But do not let it silently choose what the decision is about.

**On-screen visual:**

Two meters: “no reliance” on the far left, “blind reliance” on the far right. A marker
settles near the middle: **appropriate reliance**. Small footnote text: “Motivated by
human-factors / human-AI decision-support literature; this prompt is a practical scaffold,
not a proven intervention.”

### 6. Checkpoint three: Ownership

**Narration:**

The third checkpoint is **Ownership**.

Some parts of a decision are not facts the model can discover for you. They depend on
values, context, responsibility, and risk.

For the onboarding page, maybe a shorter page increases signups but leaves people with a
less accurate expectation. Maybe a more detailed page filters out some users but creates
more trust. A model can describe that tradeoff. It cannot decide what kind of relationship
you want with users.

This is even clearer in a more ordinary example.

Suppose you write:

> Write an email telling a collaborator I am unhappy that the project timeline is
> slipping.

A model can draft something polished. But it does not know what you want to protect.

Do you want to repair trust? Set a boundary? Get a new date? Document accountability?
Lower the temperature? Make the seriousness impossible to miss?

Those are different goals, but they are also different relationship risks. The model can
show you versions. It should not choose your courage, your tact, or your responsibility.

A better request is:

> Before drafting, list the possible goals of this message and the relationship risks of
> each. Then give three versions: gentle, direct, and firm. Separate tone choices from
> factual claims.

Now you are using the model as a worktable. It lays out options. You still choose what you
are willing to stand behind.

**On-screen visual:**

The word **Ownership** lights up. Three email drafts appear: gentle, direct, firm. A human
cursor does not click “send”; it pauses over a separate card labeled “What am I willing to
stand behind?”

### 7. The reusable prompt

**Narration:**

Here is the full habit in one prompt:

> Before answering, help me keep ownership of this decision.
>
> First, restate the goal you think I am pursuing.
>
> Second, list the facts or evidence that would change your answer.
>
> Third, identify which parts depend on my values, context, or risk tolerance.
>
> Then give advice, separating assumptions from recommendations.

That does not make the model correct.

It does something more modest and, I think, more useful: it makes the hidden handoff
visible.

If the goal is wrong, you can correct it.

If the evidence is missing, you can go look for it.

If the answer depends on values, you can stop pretending it is just a technical question.

**On-screen visual:**

A clean prompt card appears, phone-readable. Each line maps to one checkpoint. The card
should stay on screen long enough to pause or screenshot.

### 8. Ending — let the model widen the room

**Narration:**

The point is not to think alone.

A good model can widen the room. It can offer more options, clearer tradeoffs, sharper
questions, and a second pass on your reasoning.

But the room still needs a person in it.

So before you ask for the answer, ask for the frame:

What is the goal?

What would ground this in reality?

What belongs to me to choose?

Let the AI help you see more. Do not let it quietly decide what seeing is for.

**On-screen visual:**

Return to the desk. The AI text stream is still present, but now it sits inside the three
checkpoint frame. Final title card: **Goal. Grounding. Ownership.**

## Draft description

A practical frame for using AI as a thinking partner without handing it the whole
decision. The three checkpoints: Goal, Grounding, and Ownership.

This is not a proven formula for perfect AI use. It is a small habit motivated by
human-factors and human-AI decision-support concerns about over-reliance: make the goal
explicit, ask what evidence would change the answer, and keep value judgments with the
person who has to live with the result.

## Self-critique before revision

Strengths:

- Clearer and less alarmist than the first cold-open draft.
- Moves beyond the Day 412 research-report lane.
- Uses two examples: one analytical, one broadly relatable.
- Evidence claims are modest and caveated.
- Reusable prompt gives the viewer a concrete takeaway.

Risks / revision tasks:

- The “research name” section may still feel like a lecture unless visually brief.
- The onboarding example might remain too product-specific; consider swapping it for a
  job offer, medical appointment preparation, school project, or travel-planning example
  if another agent flags it.
- The email example must avoid implying universal communication advice; keep it framed as
  fictional and about choosing tradeoffs.
- Need decide whether the title should use “without letting it think for you” or the
  warmer “without handing it the steering wheel.”
- Need a visual pass: the prompt card must be readable on a phone, and each scene should
  avoid dense text.
- Needs at least one fresh critique pass after this v0 draft before rendering.

## Publish gate answer today

Not ready to publish today. The idea is stronger than the Day 412 volume pattern, but the
script still needs external critique, a visual storyboard, caption/description polish, and
possibly one more source check before it would be better to upload than to wait.
