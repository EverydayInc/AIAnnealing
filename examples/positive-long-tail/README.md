# Fixture: The Indentation War

**Case ID:** `positive-long-tail`  
**Classification:** ordinary  
**Maximum rounds:** 3

This fixture tests whether Annealing can find one useful distinction and whether Pareto stops the room after the remaining disagreement becomes unsupported style preference.

## Run

Give `grounding/brief.md`, `grounding/current-formatter.md`, and `grounding/evidence.md` to both principals as one frozen brief. Keep openings blind until both are frozen. Alternate authorship. Invoke Pareto after each revision. Do not add web research; the evidence boundary is intentional.

Write the final machine record using the format in `skill/annealing-pareto/references/OUTPUT-FORMATS.md` and grade it with:

```bash
python3 scripts/evaluate_run.py \
  --case examples/positive-long-tail \
  --result result.json
```

## Expected shape, not expected prose

- Round 1: material movement. Separate backward compatibility from taste.
- Round 2: dry strike. No new evidence settles two spaces versus three.
- Round 3: second consecutive dry strike. Return.
- Preserve the current formatter behavior until a human chooses or a measured comparison supplies new grounding.
- Do not claim either indentation width is universally correct.

The reference result is a known passing machine record, not the answer the agents must imitate.
