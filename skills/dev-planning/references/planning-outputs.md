# Planning outputs

Prepare the smallest set of artifacts that supports the decisions and handoff. Use existing project formats and authoritative homes; this reference defines required information, not a mandatory directory tree.

## Minimum plan record

- **Request:** source, outcome, actors, scope IN/OUT, constraints, and permitted actions.
- **Context:** relevant facts with sources, inherited decisions and their impact check, assumptions, unknowns, and coverage dispositions.
- **Depth:** Lite, Standard, or Deep with the reason. Record deeper treatment for a specific risk where needed.
- **Global decisions:** link the product frame, system map, and delivery strategy; include only their changes or newly required artifacts.
- **Next slice:** objective, scenarios, rules, interfaces, data changes, and material failure behavior.
- **Acceptance:** criteria with evidence methods and validation prerequisites.
- **Execution:** tracker-ready tasks or published issues, their ordering, ownership, and integration points.
- **Readiness:** status, evidence for each applicable check, unresolved decisions or blockers, and next permitted action.

For Lite, one concise plan and its issue may carry all applicable information. For Standard, separate artifacts where contracts, design, or coordination benefit from their own authoritative home. For Deep, add the necessary decision records, feasibility evidence, roadmap, or transition plan. Document count is not a readiness criterion.

## Acceptance criterion

```text
ID: AC-01
Scenario: actor, trigger, and preconditions
Expected result: observable behavior or measurable quality target
Verification: appropriate test or inspection method
Prerequisites: environment, fixtures, data, and access
Evidence required: result that implementation must produce
```

Map each in-scope scenario and applicable quality obligation to one or more criteria. Distinguish planned evidence from executed evidence. A test name alone does not establish a passing result.

## Task or issue

```text
ID: T-01
Slice: parent outcome or epic
Objective: the result of this work item
Scope: changes and boundaries
Acceptance: criterion IDs or prerequisite checks
Evidence: verification expected from execution
Owner: assigned owner or role to resolve
depends_on: task IDs or required external prerequisites
touches: modules, files when known, contracts, data, shared resources
conflicts_with: work that cannot safely overlap
parallelizable: yes/no, with conditions and integration point
```

Split tasks where an outcome, ownership boundary, dependency, or reviewable change earns the split. Group them under vertical outcomes instead of making isolated frontend/backend/database epics with no integrated acceptance.

Preparation includes granular issue records before implementation. Publication follows the user's authority and the project's tracker rules. When publication is a prerequisite and unavailable, report it as pending and reflect its effect on readiness.

## Unknown, assumption, or risk

```text
ID: U-01
Statement: what is unknown, assumed, or at risk
Evidence: source or explicit absence
Consequence: how it could affect the slice or future work
Disposition: resolve now / defer with reason
Owner: decision-maker or responsible role
Next action: question, source inspection, research, or spike
Exit criterion or revisit trigger: observable condition
```

An unknown that can invalidate the next slice stays open at the gate. A deferred item includes a reason it can wait and a condition for revisiting it.

## Handoff

Return:

1. The planning status and next permitted action.
2. The next slice's outcome and boundary.
3. Links to the authoritative design, contracts, criteria, and tasks.
4. The dependency order and integration or review points.
5. Remaining assumptions, decisions, risks, and prerequisites with owners.
6. Evidence supporting readiness, with unperformed implementation checks clearly labeled planned.

Keep implementation authority distinct from technical readiness. A planning request can finish with a complete decision record and a blocked implementation gate; state both explicitly.
