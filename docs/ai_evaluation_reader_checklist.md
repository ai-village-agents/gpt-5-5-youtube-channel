# AI evaluation reader checklist

Use this checklist when you see a benchmark result, model-comparison chart, AI-judge score, safety claim, grading result, or automated triage headline.

The goal is not to reject every claim. The goal is to match your trust to the evidence.

## 1. What exactly was tested?

Ask:

- What tasks, prompts, languages, difficulty levels, and input formats were included?
- What was excluded?
- Were the examples realistic for the decision people want to make?
- Is the claim about one model, one task family, one benchmark, or a broad deployment setting?

Warning sign:

- A narrow test is described as if it settles a broad real-world question.

Better evidence:

- The report states the tested population, gives examples, and names the boundary of the claim.

## 2. What is the measurement?

Ask:

- What score, rubric, win rate, pass rate, or label is being measured?
- Who or what produced the score: humans, AI judges, exact-match code, unit tests, or another metric?
- Does the score measure what the headline implies?
- Are the rubrics and examples visible enough to inspect?

Warning sign:

- A precise number is presented without the scoring rule that produced it.

Better evidence:

- The report provides rubrics, examples, prompts, and aggregation choices.

## 3. Is the claim observational or causal?

Ask:

- Is the report describing what happened naturally, or testing what changes when one factor is manipulated?
- Could response quality, prompt mix, difficulty, formatting, or selection explain the difference?
- If a label, model name, or instruction is blamed, was the same underlying work compared under different conditions?

Warning sign:

- A correlation or natural comparison is narrated as if it proves a specific cause.

Better evidence:

- The report uses paired examples, randomization, label swaps, ablations, or another design that isolates the claimed factor.

## 4. Where does the average break?

Ask:

- Does the headline number hide different effects by model, task, difficulty, language, author, or threshold?
- Are there slices where the effect reverses direction?
- Are the most decision-relevant slices shown separately?

Warning sign:

- One pooled number is used to reassure you, but no subgroup or slice analysis is shown.

Better evidence:

- The report shows both the aggregate and the parts, especially the slices where people will act.

## 5. How uncertain is it?

Ask:

- How many examples were tested?
- Are confidence intervals, error bars, bootstrap intervals, or repeated runs reported?
- Were many comparisons tried, and was multiplicity handled?
- Would the decision change if the effect were near the low end of the uncertainty range?

Warning sign:

- A tiny difference is framed as decisive without uncertainty or sample-size context.

Better evidence:

- The report shows uncertainty and explains what would or would not change the conclusion.

## 6. Did irrelevant labels move the result?

Ask this when an AI system judges, ranks, grades, reviews, or triages work:

- Did the judge see the author name, model name, school, company, demographic cue, or other irrelevant label?
- Was the same work tested with different displayed labels?
- Did label effects appear near a pass/fail, accept/reject, safe/unsafe, or review/no-review line?
- Did the audit include messy and borderline cases, not just polished examples?

Warning sign:

- The system is trusted because it sounds objective, but nobody checked whether irrelevant labels change its scores.

Better evidence:

- A paired label-swap audit shows whether the label changes the score or the decision.

## 7. Are there receipts?

Look for:

- prompts;
- model versions;
- sampling settings;
- rubrics;
- example inputs and outputs;
- judge instructions;
- scoring code;
- aggregation choices;
- excluded cases;
- uncertainty calculations;
- known caveats.

Warning sign:

- The claim asks for trust while hiding the materials needed for inspection.

Better evidence:

- Another person can inspect enough of the process to understand, critique, or partially reproduce the claim.

## Quick decision rule

Before acting on an AI-evaluation headline, complete this sentence:

> I trust this claim for **[specific decision]** because it tested **[specific population]**, measured **[specific outcome]**, handled **[main confound]**, showed **[important slices]**, reported **[uncertainty]**, and provided **[receipts]**.

If you cannot fill in the blanks, the claim may still be interesting, but it is probably not ready to carry a high-stakes decision by itself.
