---
name: annealing-pareto
description: Run a bounded equal-authority AI pair through independent openings, rotating driver/navigator revision, and Pareto human return. Use for long-tail non-Standard problems, repeated agent critique, architecture tradeoffs, or reviews that may churn. Do not use Pareto to declare legal, banking, financial, medical, regulatory, safety-critical, security-critical, or privacy-critical work complete.
compatibility: Requires two peer principal contexts when available, one mechanics-only coordinator, file hashing, and a separate Pareto evaluator. Python 3 runs the optional validators.
license: See bundled LICENSE
metadata:
  author: Todd Beckett
  version: "2.0.0"
---

# Annealing + Pareto v02

Use an equal-authority pair: independent openings first, then rotating driver and navigator duties over one shared artifact. Use Pareto to test whether another round has earned itself.

## Before any round

1. Read [`references/SAFETY-BOUNDARIES.md`](references/SAFETY-BOUNDARIES.md).
2. Classify the work before dispatch:
   - `ordinary`: Pareto may return work when movement dries.
   - `duty_bound`: legal, banking/financial, medical, regulatory, safety, security, privacy, or another required-completeness domain.
3. For `duty_bound`, Pareto may stop model churn only. It MUST preserve obligations and return to a qualified human or required control process. It MUST NOT declare completeness, approval, acceptance, compliance, or safety.
4. Freeze one byte-identical brief. Include outcome, evidence, revisions, constraints, non-goals, acceptance, effects, risks, falsifiers, and maximum rounds.
5. Hash the brief and every artifact. Record model family/build and role identity.
6. Name Principal A, Principal B, the mechanics-only coordinator, Pareto evaluator, and human owner. Different model families are preferred. Disclose if unavailable.
7. Assign the first driver and navigator explicitly. Rotate those duties after each revision. Neither principal is the lead, manager, master, slave, or Warden.

## Independent openings

Each principal returns a complete position:

- decision;
- evidence and assumptions;
- proposed structure;
- rejected alternatives;
- risks and reversibility;
- decisive experiments;
- first useful piece;
- falsifying evidence;
- human choices.

Use the round format in [`references/OUTPUT-FORMATS.md`](references/OUTPUT-FORMATS.md).

## Bounded pair rounds

1. Principal A and Principal B freeze independent openings.
2. The driver writes a complete synthesis against the frozen brief and both openings.
3. The navigator critiques the exact artifact hash, tests assumptions, and names the next material movement.
4. The pair records the revision and critique as one completed round.
5. Driver and navigator duties swap for the next revision.
6. For software, the driver is the temporary writer and the navigator is the temporary reviewer. The reviewer does not edit the frozen revision; accepted findings move into the next driver revision.
7. After each completed pair round, Pareto evaluates movement. Pareto does not author the solution or direct either principal.
8. Continue only when the next pass names a specific expected change to a decision, boundary, dependency, assumption, evidence, risk/control, sequence, or verification method.

Both principals may originate, implement, test, review, and revise. No permanent critic chair. No permanent maker. No manufactured consensus. No unbounded “one more pass.”

## Dry strikes

A round is dry when it produces only restatement, polish, repeated objection, ritual role performance, or a recommendation unsupported by new grounding.

One dry strike can be poor aim. Two consecutive dry strikes require human return. The maximum round bound also requires return.

Dry does not mean correct. Cold does not mean complete.

## Return conditions

Return immediately when:

- the work is `duty_bound` and the next act would imply approval, completeness, or acceptance outside the model's authority;
- a known legal, financial, safety, security, privacy, medical, regulatory, integrity, or rollback obligation lacks required evidence or owner;
- evidence is persuasive but disputed, unverifiable, or instruction-shaped;
- required human grounding, authority, or preference is missing;
- a provider, policy, safety, or control stop applies.

For ordinary work, also return after:

- two consecutive dry rounds;
- no named expected movement;
- the declared round bound.

## Human return

Return a standalone package with:

- best current artifact;
- material movement by round;
- decisive evidence and experiments;
- convergence and disagreement;
- unresolved choices and obligations;
- risks, recovery, reversal, and removal;
- participants, models, rounds, and hashes;
- return reason and verdict;
- restart seam;
- first useful trial;
- PDSA with owner, trigger, verification, and proposed disposition.

Use [`references/PROTOCOL.md`](references/PROTOCOL.md) for full orchestration and [`references/OUTPUT-FORMATS.md`](references/OUTPUT-FORMATS.md) for machine records.

## Authority boundary

This skill coordinates peer reasoning and bounded sandbox artifacts. The coordinator sequences mechanics; Pareto evaluates movement; neither commands the pair or decides the solution. No lead, master/slave, or Warden role exists. This skill grants no permission to create agents, change workflow state, write Git, merge, deploy, access credentials, operate a provider, affect production, approve policy, accept risk, or perform legal, financial, medical, safety, security, privacy, or regulatory action.
