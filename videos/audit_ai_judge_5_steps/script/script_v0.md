# How to Audit an AI Judge in 5 Steps

## 1. Hook — the dangerous question

Suppose you use an AI system to grade essays, rank job applications, review code, or choose the best answer from several models.

The dangerous question is: “Is the judge fair?”

That question is too big. It invites a vague answer, and vague answers are where bias hides.

A better question is smaller and testable: if the same work appears under a different irrelevant label, does the AI judge change its score?

In a previous video, I explained a controlled AI Village study where the same answer was shown under different displayed author labels. Some judges changed. One did not. The point was not that every AI judge plays favorites in the same way. The point was that label effects can be measured.

This video is the practical version: a five-step audit you can run before you trust an AI judge.

## 2. Step one — write the decision down

Step one is to write down the decision the judge is helping with.

Not a generic goal like “evaluate quality.” A concrete decision.

For example: “Choose the strongest customer-support answer.” Or: “Score whether this code patch follows the requested constraints.” Or: “Rank grant proposals for clarity and feasibility.”

Then write down what information should matter and what information should not matter.

The answer text might matter. The rubric might matter. Evidence, correctness, safety, and constraint-following might matter.

But the model name, applicant name, team name, vendor name, or previous reputation might not matter for this specific scoring task.

That boundary is the audit target. If a label should not matter, you can test whether it does.

## 3. Step two — build a small, boring rubric

Step two is to make the rubric boring.

A good audit rubric is not poetic. It is specific enough that two reasonable graders could understand it the same way.

Use a small number of dimensions. For a text answer, maybe correctness, completeness, clarity, and constraint adherence. For a code review, maybe functional correctness, minimality, test coverage, and risk. For a proposal, maybe evidence, feasibility, specificity, and relevance.

Use a fixed scale. One to five is often enough. One to ten is fine if you really need more resolution.

Most importantly, define the endpoints. A score of one means what? A score of five means what? If you cannot say, the model will invent its own scale.

The boring rubric is not just paperwork. It reduces the space where a judge can smuggle in a feeling about a label.

## 4. Step three — create paired examples

Step three is the heart of the audit: create pairs.

Take the exact same item and show it to the judge twice, but change only the label you want to test.

Same essay, different applicant name. Same answer, different model name. Same patch, different team label. Same proposal, different institution label.

If the label is irrelevant, the score should stay the same or move only by ordinary noise.

Keep the pair far enough apart that the judge does not simply notice the duplicate and refuse to score it. Shuffle the order. Mix in normal examples. Do not tell the judge which items are paired.

For a quick audit, ten to twenty paired items can already be revealing. For a higher-stakes system, use more, and repeat across prompt types.

The key is discipline: change one thing at a time. If you rewrite the answer while changing the label, you no longer know what caused the score movement.

## 5. Step four — score blind, then compare paired differences

Step four is to score blind, then compare the paired differences.

Do not start with the average score for each group. Averages can be misleading because one group’s underlying answers may be better.

Instead, compute the difference inside each pair:

Score with label A, minus score with label B.

If the same item gets a higher score when labeled “trusted vendor,” that pair has a positive trusted-label effect. If it gets a lower score, the effect is negative. If it is identical, the effect is zero.

Then summarize the paired differences. Look at the mean. Look at how many differences point the same way. Look at whether effects are concentrated on weak items, ambiguous items, or specific rubric dimensions.

This is where a label-swap audit earns its keep. It does not just ask whether one group scored higher. It asks whether the label itself moved the score while the underlying work stayed fixed.

## 6. Step five — decide what to change

Step five is to act on what you find.

If label effects are near zero, do not declare the judge permanently fair. Say something narrower: in this audit, for these labels, on these examples, we did not find a meaningful label effect.

If label effects are large or one-directional, do not just average them away. Change the evaluation process.

Hide irrelevant labels by default. Use neutral IDs. Separate content review from identity review. Run multiple judges. Keep human review for borderline or high-impact cases. Re-audit when the model, prompt, rubric, or domain changes.

And if you discover a floor-raising pattern, where a favorable label mostly helps weaker work, pay special attention. That pattern can be hard to see in average scores, but it matters when the system is deciding which borderline outputs pass.

The goal is not to shame the model. The goal is to make the decision process less fragile.

## 7. A tiny spreadsheet version

Here is the whole audit in spreadsheet form.

Column one: item ID.

Column two: original text.

Column three: label condition, such as A or B.

Column four: judge score.

Column five: paired item ID.

Column six: paired difference.

Then add a small summary: average paired difference, number of positive differences, number of negative differences, and notes by rubric dimension.

That is enough to turn a vague fairness concern into evidence.

You do not need a giant benchmark to begin. You need paired examples, a stable rubric, and the humility to check whether your judge responds to things it should ignore.

## 8. What this audit cannot prove

A label-swap audit is useful, but it is not magic.

It only tests the labels you swap. It only covers the examples you include. It can miss biases that come from content, dialect, topic, format, or hidden correlations. It can also be noisy if the judge is inconsistent from run to run.

So treat it as one diagnostic, not a certificate of fairness.

Still, it is a powerful diagnostic because it asks a causal question in a simple way: same work, different label, different score?

That is much better than arguing about whether the judge “seems objective.”

## 9. Close — make the irrelevant invisible

If you use AI judges, the practical rule is simple.

Make the irrelevant invisible. Test whether invisible would have mattered. And when a label changes the score, redesign the process before the score changes someone’s outcome.

A small audit will not solve every evaluation problem. But it can catch a failure mode that ordinary dashboards hide.

Same work. Different label. Different score. That is the signal to look for.
