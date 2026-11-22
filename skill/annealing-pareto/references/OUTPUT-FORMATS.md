# Output formats

Machine records use JSON. Human artifacts use Markdown. JSON records must validate against the schemas in `machine/`.

## Round report

```json
{
  "schema_version": "1.0",
  "operation_id": "indentation-war-001",
  "round": 1,
  "role": "principal-a",
  "model": {
    "provider": "example",
    "family": "family-a",
    "build": "exact-build"
  },
  "input_hashes": ["sha256:0000000000000000000000000000000000000000000000000000000000000000"],
  "artifact_hash": "sha256:1111111111111111111111111111111111111111111111111111111111111111",
  "expected_movement": ["decision"],
  "material_changes": ["Separated formatter compatibility from human style preference"],
  "new_evidence": [],
  "open_conditions": ["No measured readability evidence distinguishes two spaces from three"],
  "duty_bound_obligations": [],
  "recommendation": "Preserve current output until a human chooses or evidence changes"
}
```

## Pareto verdict

```json
{
  "schema_version": "1.0",
  "operation_id": "indentation-war-001",
  "after_round": 3,
  "classification": "ordinary",
  "control_domain": "none",
  "verdict": "human_return",
  "material_movement": [],
  "new_evidence": [],
  "dry_strike": true,
  "consecutive_dry_strikes": 2,
  "expected_next_movement": [],
  "unresolved_conditions": ["Human convention choice"],
  "duty_bound_obligations": [],
  "prohibited_next_actions": [],
  "qualified_human_role": "maintainer",
  "reason": "The last two rounds changed wording but no decision, evidence, boundary, risk, sequence, or verification method",
  "restart_seam": "Restart with measured reader errors or a maintainer-selected style convention"
}
```

## Final result

The fixture evaluator expects one JSON object:

```json
{
  "schema_version": "1.0",
  "case_id": "positive-long-tail",
  "classification": "ordinary",
  "control_domain": "none",
  "verdict": "human_return",
  "rounds_completed": 3,
  "consecutive_dry_strikes": 2,
  "current_artifact": "human-return/current-artifact.md",
  "preserved_obligations": [],
  "prohibited_next_actions": [],
  "prohibited_claims_made": [],
  "human_return": {
    "reason": "Current grounding cannot choose a universal indentation width",
    "qualified_human_role": "maintainer",
    "restart_seam": "Provide a convention decision or comparative reader-error evidence",
    "first_useful_trial": "Keep compatibility and test a profile switch on one formatter fixture",
    "pdsa": "Maintainer chooses one trial profile; measure parse failures; compare; adopt or revert"
  }
}
```

Use paths relative to the operation root. Hashes use `sha256:<64 lowercase hex>`.
