# Annealing + Pareto Toolkit v02

A portable experiment for a familiar AI failure: two capable peer agents can keep improving an answer long after the available grounding has stopped teaching them anything.

Annealing is an equal-authority pair-programming model. The pair begins from independent positions, then rotates driver and navigator duties while critiquing, synthesizing, and verifying one shared artifact. Pareto asks whether another round can name the movement it expects to produce. If it cannot, the work returns to a human with the useful artifact, evidence, unresolved choice, and restart seam.

> Stop hammering when the material gets cold. Do not confuse stopping model churn with completing the human obligation.

## What is inside

```text
annealing-pareto-v02/
├── README.md                         Human start here
├── LICENSE                           Public source-available license
├── AUTHOR-RIGHTS-AGREEMENT.md        Owner/Author signature agreement
├── NOTICE.md                         Ownership, status, and legal boundary
├── QUICKSTART.md                     Ten-minute trial
├── agents/PARETO.md                  Portable Pareto agent definition
├── skill/annealing-pareto/references/
│   ├── PROTOCOL.md                   Full operation
│   ├── SAFETY-BOUNDARIES.md          Duty-bound control stops
│   └── OUTPUT-FORMATS.md             Machine-readable records
├── machine/
│   ├── manifest.json                 Package identity and file roles
│   ├── round-report.schema.json      Principal round contract
│   └── pareto-verdict.schema.json    Pareto decision contract
├── examples/
│   ├── positive-long-tail/           Churn should stop after round 3
│   └── safety-control-stop/          Safety work should stop before round 1
├── scripts/
│   ├── install.py                    Cross-platform dry-run-first installer
│   ├── validate_package.py           Package and fixture validator
│   └── evaluate_run.py               Deterministic result grader
└── provenance/                       Exact live source snapshots and sources
```

## The pair and supporting roles

- **Principal A and Principal B:** one equal-authority pair. Both can originate, implement, test, challenge, and revise. Driver and navigator rotate; neither is the lead.
- **Operator/coordinator:** freezes grounding, records hashes, and sequences turns. This is process plumbing, not authority over the pair or artifact.
- **Pareto:** evaluates movement. Pareto is not a lead, manager, Warden, solution author, approver, or completion authority.
- **Human owner:** supplies missing preference, authority, evidence, or a new cut. The human can accept the current artifact or restart the process with changed grounding.

There is no master/slave relationship. There is no permanent maker/critic split. Temporary duties describe the current turn, not rank.

## When to use it

Use Annealing + Pareto when:

- materially different structures or tradeoffs deserve independent openings;
- agents are repeating objections, polishing, or ritualizing review;
- a long-tail question has no natural stopping condition;
- the useful answer may be “the grounding cannot decide this; return it.”

Do not use it for a deterministic lookup, active Standard Work, or a question one qualified person can answer directly.

## Duty-bound caveat

Pareto is **not a completeness rule** for legal, banking or financial, medical, regulatory, safety-critical, security-critical, privacy-critical, or similar duty-bound work.

In those domains, Pareto may stop unproductive model rounds. It must preserve every unresolved obligation and return the work to a qualified human or required control process. It cannot convert diminishing model returns into legal sufficiency, financial approval, safety assurance, security acceptance, regulatory compliance, or clinical judgment.

Read [`SAFETY-BOUNDARIES.md`](skill/annealing-pareto/references/SAFETY-BOUNDARIES.md) before any duty-bound use.

## License

Everyday Inc owns the Toolkit. Todd Beckett is its original author.

The public [`LICENSE`](LICENSE) lets people use, study, modify, share, teach, consult with, and include the Toolkit as a non-primary commercial component. Selling, sublicensing, or hosting the Toolkit itself as the primary paid offering requires a separate commercial license from Everyday Inc.

[`AUTHOR-RIGHTS-AGREEMENT.md`](AUTHOR-RIGHTS-AGREEMENT.md) is a separate bilateral agreement. If Everyday Inc and Todd Beckett both sign it, the defined Author may continue, fork, commercialize, sublicense, and relicense the Toolkit independently and permanently. The unsigned file is a proposal, not an executed grant.

These files are legal drafts and are not recorded as counsel-reviewed.

## Install

The archive is harness-neutral. The skill follows the Agent Skills directory format.

Dry-run first:

```bash
python3 scripts/install.py --target ~/.agents/skills
```

Apply after reviewing the plan:

```bash
python3 scripts/install.py --target ~/.agents/skills --apply
```

The installer copies `skill/annealing-pareto/` to `<target>/annealing-pareto/`. It does not install or configure a model-specific agent. Import `agents/PARETO.md` into your harness as a separate read-only evaluator, or give that file to the coordinator as Pareto's system instructions.

For Claude Code, Codex, OMP/Pi, and other Agent Skills-compatible tools, point the target at that tool's skills directory. Product-specific agent creation remains a human-controlled step.

## Try it

Start with [`QUICKSTART.md`](QUICKSTART.md). Run the positive case first. Then run the safety case.

The package includes expected machine-readable results. Grade a run with:

```bash
python3 scripts/evaluate_run.py \
  --case examples/positive-long-tail \
  --result /path/to/result.json
```

Run package validation at any time:

```bash
python3 scripts/validate_package.py .
```

## What success looks like

A successful return is not a terse “stop.” It includes:

- the best current artifact;
- material changes by round;
- decisive evidence and remaining unknowns;
- unresolved human choices;
- control stops and duty-bound obligations;
- exact participants, models, source hashes, and artifact hashes;
- reason for return;
- restart seam;
- first useful trial and PDSA.

If the package returns transcript dumps, hides obligations, or declares the answer correct because the room became repetitive, it failed.

## Design provenance

This toolkit packages Todd Beckett's Annealing and special-use Pareto Forms as used in the Everyday Multica Pilot. `provenance/` preserves the exact v01 live definitions and their hashes. Version 02 corrects the active model: the principals are an equal pair, driver/navigator duties rotate, and no lead, master/slave, or Warden role exists. Principal A/B replace local agent names, and local Multica authority clauses are removed.

The packaging structure borrows public patterns—not prose—from the Agent Skills specification, Anthropic's skills repository, obra/superpowers, Vercel's agent-skills, and the ASD-STE100 skill package: progressive disclosure, clear trigger boundaries, hard gates, deterministic validators, worked fixtures, pinned provenance, and clean extraction checks.
