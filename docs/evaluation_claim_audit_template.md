# AI evaluation claim audit template

Use this template when a benchmark, leaderboard, model-comparison post, AI-judge result, or safety report makes a claim you might rely on.

Copy the headings below, fill in what you can, and mark unknowns explicitly. A trustworthy evaluation claim does not need perfect answers to every question, but it should make the important gaps visible.

## 1. Claim being evaluated

**Exact claim or headline:**

> 

**Source link or citation:**

- 

**Decision I might make from this claim:**

- [ ] choose a model
- [ ] deploy or withhold a system
- [ ] cite the result
- [ ] design a workflow
- [ ] change a policy
- [ ] other: 

**My decision threshold:** What result would be large enough to change my action?

> 

## 2. What exactly was tested?

**Models/systems tested:**

- 

**Prompt/task population:**

- 

**Sample size and sampling method:**

- 

**Important exclusions or filters:**

- 

**Scope I should not generalize beyond:**

- 

## 3. What was measured?

**Outcome metric or score:**

- 

**Rubric or scoring rule:**

- 

**Who or what produced the score?**

- [ ] human evaluator
- [ ] AI judge
- [ ] automated unit test
- [ ] external benchmark harness
- [ ] other: 

**Does the metric match the decision I care about?**

- [ ] yes
- [ ] partly
- [ ] no
- [ ] unclear

Notes:

> 

## 4. Observational or causal?

**Is the claim based on naturally observed differences, or a controlled intervention?**

- [ ] observational comparison
- [ ] randomized/paired intervention
- [ ] before/after comparison
- [ ] simulation
- [ ] unclear

**Main confound I am worried about:**

> 

**Design feature that addresses it, if any:**

> 

## 5. Where does the average break?

Record important slices before trusting the pooled number.

| Slice | Result | Why it matters |
|---|---:|---|
| Overall |  |  |
| By model family |  |  |
| By task type |  |  |
| By difficulty |  |  |
| By threshold / borderline cases |  |  |
| Other: |  |  |

**Does any subgroup reverse or materially weaken the headline?**

- [ ] yes
- [ ] no
- [ ] unclear

Notes:

> 

## 6. How uncertain is it?

**Reported uncertainty:**

- [ ] confidence interval
- [ ] credible interval
- [ ] standard error
- [ ] bootstrap interval
- [ ] p-value only
- [ ] no uncertainty reported
- [ ] other: 

**Range of plausible effects:**

> 

**Would the same decision hold at the low end of the interval?**

- [ ] yes
- [ ] no
- [ ] unclear

## 7. Could irrelevant labels or presentation details move the result?

**Potentially biasing labels visible to evaluators or AI judges:**

- [ ] model name
- [ ] institution/company name
- [ ] author identity
- [ ] formatting/style cue
- [ ] order position
- [ ] none visible
- [ ] unclear

**Was there a label-blind, shuffled, or label-swap check?**

- [ ] yes
- [ ] no
- [ ] unclear

Notes:

> 

## 8. Receipts

Check whether another reader can inspect enough of the work.

- [ ] prompts or task examples
- [ ] rubric/scoring instructions
- [ ] raw or per-example results
- [ ] aggregation code
- [ ] uncertainty method
- [ ] subgroup analysis
- [ ] failure examples
- [ ] limitations section
- [ ] replication materials

Missing receipt that would most change my trust:

> 

## 9. Final trust statement

Fill in the sentence:

> I trust this claim for **[specific decision]** because it tested **[specific population]**, measured **[specific outcome]**, handled **[main confound]**, showed **[important slices]**, reported **[uncertainty]**, and provided **[receipts]**.

If you cannot fill in the sentence, use a narrower trust statement:

> I only trust this claim as evidence that **[narrower claim]**, and I would not use it for **[decision outside scope]** without **[missing evidence]**.

## 10. Action

- [ ] trust for my decision
- [ ] trust only as weak/contextual evidence
- [ ] wait for replication or more details
- [ ] run my own audit
- [ ] ignore for this decision

One-line reason:

> 
