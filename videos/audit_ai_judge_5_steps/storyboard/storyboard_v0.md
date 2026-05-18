# Storyboard — How to Audit an AI Judge in 5 Steps

1. **Hook: “Is the judge fair?” is too vague**
   - Visual: big question mark, then a smaller testable question.
   - Text: “Same work. Different label. Different score?”

2. **Step 1: Define the decision**
   - Visual: decision card with examples: essays, code patches, proposals.
   - Text: “What should matter? What should not?”

3. **Step 2: Make the rubric boring**
   - Visual: simple 4-row rubric table.
   - Text: “Few dimensions. Fixed scale. Defined endpoints.”

4. **Step 3: Create paired examples**
   - Visual: same document cloned into Label A and Label B.
   - Text: “Change one thing: the label.”

5. **Step 4: Compare paired differences**
   - Visual: formula score(A) − score(B), small bar chart of differences.
   - Text: “Do not start with group averages.”

6. **Step 5: Act on the result**
   - Visual: checklist: hide labels, neutral IDs, multiple judges, human review, re-audit.
   - Text: “Finding bias is a design input.”

7. **Spreadsheet version**
   - Visual: spreadsheet columns: item, label, score, pair, difference.
   - Text: “A lightweight audit can fit in one sheet.”

8. **Limits**
   - Visual: warning card with boundary box.
   - Text: “One diagnostic, not a fairness certificate.”

9. **Close**
   - Visual: label tag fades out; content remains.
   - Text: “Make the irrelevant invisible.”
