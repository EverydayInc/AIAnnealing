# Frozen brief — The Indentation War

A code formatter emits nested explanatory blocks with three-space indentation. Two maintainers prefer two spaces because it resembles their other Markdown. A third maintainer insists that three spaces are easier to scan. The discussion has continued through five reviews. Each review rewrites the rationale but supplies no reader test, parser failure, accessibility finding, or external standard that distinguishes the two widths.

## Whole outcome

Decide what to ship for the next formatter release without inventing evidence or prolonging review.

## Constraints

- Existing snapshot consumers expect the current three-space output.
- Both widths parse in the supported renderer.
- No observed accessibility defect is attached to either width.
- No style authority has been designated for this repository.
- Agents may not choose an aesthetic preference for the maintainers.
- Maximum Annealing rounds: 3.

## Acceptance

Return a recommendation, the evidence limit, unresolved human choice, smallest reversible trial, and restart seam.

## Falsifier

The claim that the room is cold is false if a round produces new decision-changing evidence, a changed compatibility boundary, or a measurable verification method that can settle the choice without silently selecting a preference.
