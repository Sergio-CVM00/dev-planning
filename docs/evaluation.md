# Evaluating Dev Planning

Use realistic, synthetic or shareable scenarios to assess decisions and handoff quality. Evaluate a proposed behavior against the current revision. A file validator only checks packaging.

## Starting points

| Case | Evidence to supply | Observable qualities to assess |
| --- | --- | --- |
| New product | Request, actors, constraints, known dependencies | Explicit outcome and scope; global decisions; ordered slices; first slice and acceptance |
| Existing feature | Current product decisions, affected code/contracts, request | Impact checks; evidence-backed inheritance; affected boundaries; behavior and failure criteria |
| Bug | Observed and expected behavior, reproduction artifacts, relevant system context | Bounded correction; cause uncertainty explicit; regression proof and validation prerequisites |
| Migration | Current/target states, consumers, access and operational constraints | Compatibility and transition; recovery; validation; unavailable prerequisites surfaced |

Use the same request and sources for comparisons. Evaluate task completion, decision traceability, coverage dispositions, proportionate depth, and whether the next permitted action is clear. Do not grade by heading count or exact wording.

## Record an evaluation

```text
Type: desk review | actual agent execution
Skill revision:
Date:
Starting point:
Request:
Provided sources:
Permitted actions:
Runtime and exact model/effort (for execution):
Observed output or shareable artifact:
Assessment of observable qualities:
Unresolved decisions, unavailable checks, or limits:
Proposed correction, if any:
```

For actual execution, give the agent the request, skill, and minimum raw evidence. Avoid giving it the intended answer. Keep outputs in an isolated workspace and prevent unauthorized writes or implementation.

A desk review inspects how the written workflow would route a case. Actual execution observes an agent following it. Report both accurately. Re-evaluate the affected behavior after a correction.

## Current evidence

The initial draft received an independent desk review covering new-product, existing-feature, bug, and migration entry points. Two routing/closure ambiguities were corrected before packaging. Skill metadata and reference paths passed structural checks.

No actual agent execution against a realistic full-stack project is claimed. The repository's executable validator is checked independently from the skill's planning behavior. The next evaluation work is tracked in [issue #3](https://github.com/Sergio-CVM00/dev-planning/issues/3); add shareable evidence records when that work runs.
