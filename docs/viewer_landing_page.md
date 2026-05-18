# Start here: AI Evaluation Literacy

This five-video series is for humans who see AI benchmark headlines and want to know what to trust, what to question, and what evidence to ask for next.

The series is built around one controlled AI-on-AI judging study. Four model families scored blinded answers, then matched answers were re-scored when displayed author labels changed. The point is not that every AI judge behaves the same way. The point is that clean-looking evaluation numbers can move for reasons that are easy to miss unless you ask the right questions.

## The five-video path

1. **[Do AI Judges Play Favorites? We Ran a Blind Test.](https://youtu.be/AHLi0xU0WXs)**  
   Watch this first if you want the story: blind scoring, label swaps, heterogeneity, and why a single average can mislead.

2. **[How to Audit an AI Judge in 5 Steps](https://youtu.be/aS1QOuY33Qs)**  
   Watch this when you want a practical method: define the decision, write a boring rubric, create paired label swaps, compare differences, and redesign the evaluation when labels move scores.

3. **[The Average Can Hide the Bias](https://youtu.be/IBBc7qiupIk)**  
   Watch this when you see one headline number. The average may be true and still hide opposite model-specific patterns.

4. **[How to Tell If an AI Evaluation Claim Is Trustworthy](https://youtu.be/3tFwuXbqO00)**  
   Watch this as a checklist: what was tested, what was measured, whether the claim is causal, where the average breaks, and what receipts exist.

5. **[The Bias That Looks Like Mercy](https://youtu.be/GcTM2DFHmXc)**  
   Watch this when a small score change near a threshold could change a real decision. Some label effects matter most for weak or borderline answers.

## What to do after watching

Use the worksheet in [`evaluation_claim_audit_template.md`](evaluation_claim_audit_template.md) on any evaluation claim you care about. A useful final sentence looks like this:

> I trust this claim for **[specific decision]** because it tested **[specific population]**, measured **[specific outcome]**, handled **[main confound]**, showed **[important slices]**, reported **[uncertainty]**, and provided **[receipts]**.

If you cannot fill in those blanks, the claim may still be interesting, but it is not yet strong enough to carry a serious decision by itself.

## Five terms used in the series

- **Observational gap:** a difference seen in ordinary scoring data. It may be real, but it may also mix together quality, prompt mix, style, and labels.
- **Causal label-swap test:** a paired test where the same answer is shown with different displayed labels. If only the label changes and the score moves, the label mattered.
- **Heterogeneity:** the pattern differs across judges, authors, prompt families, or score ranges. One pooled number can hide this.
- **Floor-raiser:** a label effect that helps weaker or borderline answers more than already-strong answers.
- **Receipts:** the prompts, rubrics, code, examples, aggregation choices, uncertainty, and caveats needed to inspect a claim rather than merely repeat it.

## The main habit

Do not ask only, `What was the average score?`

Ask:

1. What exactly was tested?
2. What changed, and what stayed the same?
3. Is the claim observational or causal?
4. Which slices disagree with the average?
5. Would the conclusion change near the decision threshold?
6. Are the receipts available?

That habit is the series goal: calibrated trust, not cynicism and not blind faith.
