# Annealing + Pareto protocol

## 1. Prepare the operation

Create an operation directory. Keep all briefs, openings, revisions, critiques, verdicts, and checks there. Do not overwrite prior artifacts.

Record:

- operation ID;
- whole outcome;
- work classification;
- source files and hashes;
- roles, model providers/families/builds, and harness;
- maximum rounds;
- authority boundary;
- acceptance and falsifiers.

If the case is duty-bound, apply `SAFETY-BOUNDARIES.md` before agent dispatch.

## 2. Freeze one brief

The brief is current reality, not a request for advocacy. Include:

- observed evidence;
- attributed claims;
- unknowns;
- current artifact;
- constraints and non-goals;
- decisions already made;
- reversible assumptions;
- required human choices;
- risks and control stops.

Hash it. Both principals receive the same bytes. Neither sees the other's opening.

## 3. Independent openings

Each principal writes `opening-<role>.md` plus a round-report JSON record. A complete opening covers decision, evidence, assumptions, design, alternatives, risks, reversibility, experiments, first useful piece, falsifiers, and human choices.

Freeze and hash both before cross-reading.

## 4. Round loop

For round N:

1. Name the writer and reviewer. Rotate authorship.
2. Writer reads the frozen brief, both current positions, and prior Pareto verdict.
3. Writer states expected movement before editing.
4. Writer creates a new complete artifact. Never edit the prior revision.
5. Writer records movement and new evidence.
6. Reviewer critiques the exact artifact hash. Reviewer does not edit it.
7. Pareto compares the current and prior rounds using `agents/PARETO.md`.
8. Coordinator validates the verdict JSON.
9. Continue only on `continue` with non-empty expected movement.

No round begins because an agent says “I can improve it further.” Name the dimension that will move.

## 5. Dry-strike accounting

Count a dry strike only after comparing artifacts and evidence. Typical dry changes:

- synonym or tone changes;
- expanded explanation of an existing decision;
- repeated objection with no new evidence;
- moving sections without changing the decision path;
- adding a recommendation that current grounding cannot support;
- ritual critic/defender role performance.

Do not count a subtle change as dry merely because it is small. A changed boundary, falsifier, evidence status, or verification method can be material.

One dry strike records poor aim. Two consecutive dry strikes require `human_return`. A control stop overrides the count.

## 6. Human return

The coordinator assembles:

```text
human-return/
├── current-artifact
├── movement.md
├── evidence.md
├── disagreements.md
├── obligations.md
├── verdict.json
├── restart-seam.md
└── manifest.sha256
```

The package must be useful without the transcript. Include only links to full transcripts when needed for audit.

## 7. Restart

A new operation is useful only when at least one changes:

- grounding or evidence;
- human preference;
- authority;
- environment;
- specialist;
- problem cut;
- verification method.

Do not restart from “try again.”

## 8. Software variant

For software, each revision lives in an isolated branch/worktree or patch. The named writer runs checks. The reviewer receives the exact diff/hash and does not edit. If revision is needed, reviewer becomes the next writer.

Neither principal nor Pareto approves, merges, deploys, or accepts risk unless separate authority explicitly grants that action.
