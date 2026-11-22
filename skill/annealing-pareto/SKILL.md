---
name: annealing-pareto
description: Run bounded independent AI design or review rounds, detect dry strikes, and return useful work to a human when the current grounding stops producing material movement. Use for long-tail non-Standard problems, repeated agent critique, architecture tradeoffs, or reviews that may churn. Do not use Pareto to declare legal, banking, financial, medical, regulatory, safety-critical, security-critical, or privacy-critical work complete.
compatibility: Requires two principal agent contexts when available, one coordinator, file hashing, and a separate Pareto evaluator. Python 3 runs the optional validators.
license: See bundled LICENSE
metadata:
  author: Todd Beckett
  version: "1.0.1"
---

# Annealing + Pareto

Use independent openings and alternating revision to change the artifact. Use Pareto to test whether another round has earned itself.

## Before any round

1. Read [`references/SAFETY-BOUNDARIES.md`](references/SAFETY-BOUNDARIES.md).
2. Classify the work before dispatch:
   - `ordinary`: Pareto may return work when movement dries.
   - `duty_bound`: legal, banking/financial, medical, regulatory, safety, security, privacy, or another required-completeness domain.
3. For `duty_bound`, Pareto may stop model churn only. It MUST preserve obligations and return to a qualified human or required control process. It MUST NOT declare completeness, approval, acceptance, compliance, or safety.
4. Freeze one byte-identical brief. Include outcome, evidence, revisions, constraints, non-goals, acceptance, effects, risks, falsifiers, and maximum rounds.
5. Hash the brief and every artifact. Record model family/build and role identity.
6. Name Principal A, Principal B, coordinator, Pareto evaluator, and human navigator. Different model families are preferred. Disclose if unavailable.
7. Keep both openings blind until each is frozen.

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

## Bounded rounds

1. Principal A and Principal B freeze independent openings.
2. The named lead writes a complete synthesis.
3. The partner critiques the exact artifact hash.
4. The partner writes the next complete revision.
5. The prior lead critiques that revision.
6. After each completed revision, Pareto evaluates movement. Pareto does not author the solution.
7. Continue only when the next pass names a specific expected change to a decision, boundary, dependency, assumption, evidence, risk/control, sequence, or verification method.

No permanent critic chair. No manufactured consensus. No unbounded “one more pass.”

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

This skill coordinates reasoning and bounded sandbox artifacts. It grants no permission to create agents, change workflow state, write Git, merge, deploy, access credentials, operate a provider, affect production, approve policy, accept risk, or perform legal, financial, medical, safety, security, privacy, or regulatory action.
