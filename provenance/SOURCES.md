# Sources and provenance

## Local method sources

The portable package was built from live definitions in the Everyday Multica workspace, captured on 2026-11-22.

| Source | Local snapshot | SHA-256 | Treatment |
|---|---|---|---|
| `annealing-v01` skill, Multica ID `2bd13745-4659-48e7-b4d4-5161e3990c40`, updated 2026-11-06 | `annealing-v01-live.md` | `a2c092cd733e62363f5e417ce979f9a643873f206398986e7169fffc45ee416e` | Exact live skill content |
| `Pareto` agent, Multica ID `9e0ba338-f709-4cbd-b5f4-011dc03d66ad`, updated 2026-11-20 | `pareto-live.md` | `eeb8fec58616d0b980bffa9e4610a783a496febec42d41c55d1950a6b4ce8665` | Exact live instructions, including local authority clauses not carried into the portable agent |
| AIRetool Notebook entry, “Pareto Takes the Hammer Away (The Material Stopped Moving),” 2026-10-28 | Not redistributed | — | Source framing and special-use caveat |
| AIRetool Notebook entry, “The Art of the Subtle Movement,” 2026-11-13 | Not redistributed | — | Source field observation; no text copied into package except the method's own phrase “subtle movement” |

The portable adaptation replaces local participant names with Principal A/B, removes Multica-specific status authority, and adds explicit duty-bound circuit breakers, machine schemas, install tooling, and fixtures.

Version 02 applies Todd Beckett's 2026-11-22 correction to the active package: Annealing is a pair-programming model with equal principals and rotating driver/navigator duties. No lead, master/slave, or Warden role exists. The v01 snapshot remains unchanged as provenance rather than current instruction.

## Public packaging references

These sources informed package shape only. No code, templates, or prose from them is bundled.

| Source | Pinned revision | Pattern inspected |
|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) / [`agentskills/agentskills`](https://github.com/agentskills/agentskills) | `83021e2be457a9b6679148719c1f6074f0ad975e` | Required frontmatter, skill directory layout, progressive disclosure, validation |
| [`anthropics/skills`](https://github.com/anthropics/skills) | `e4bb5d960d87126ff3b3a8af1a104b7db67560ba` | Minimal skill template, self-contained package boundary |
| [`obra/superpowers`](https://github.com/obra/superpowers) | `22f0b463e7a5e579904dd6211a520321035526f7` | Trigger boundaries, hard gates, explicit handoff, multi-harness installation |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | `5a37a6329fbad3666c3207392a6a7c0110e92efb` | Pinned rule provenance, deterministic checks, compact audit skills |
| [`danyuchn/asd-ste100-skill`](https://github.com/danyuchn/asd-ste100-skill) | `65c8ab6ef5fcb3619c8e6daca43e68627f3d7b4a` | Full skill package, fixtures, stdlib-only linter, byte-verifiable distribution |

## Claims not made

- The public projects endorse this toolkit.
- Popularity establishes fitness for this method.
- The package complies with ASD-STE100.
- A passing fixture establishes professional completeness or safety.
- The portable adaptation is byte-identical to the live Multica operation; the exact sources are preserved separately so the delta remains inspectable.
