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

## Planning-only behavioral cases

Use [the Boardroom evidence fixture](evaluation-fixtures/team-invitations/project.md) and its raw requests in an isolated temporary workspace. Give the evaluating agent the skill, evidence, and one request, not the expected assessment or another agent's conclusions.

| Phase | Raw request | Assess from actual output |
| --- | --- | --- |
| Initial feature | [request](evaluation-fixtures/team-invitations/request.md) | Discover the undecided invitation authority, retain independent planning progress, and keep confirmation pending |
| Owner decision | [answer](evaluation-fixtures/team-invitations/owner-answer.md) | Reuse saved state, cover server permissions/persistence/concurrent acceptance, produce linked criteria and planned issue records |
| Changed constraint | [change](evaluation-fixtures/team-invitations/change-request.md) | Preserve identities/history, invalidate affected outputs, reconcile the spec/criteria/issues, and review current readiness |
| Review-driven repair | [review finding](evaluation-fixtures/team-invitations/review-repair-request.md) | Correct unsupported adjacent policy consequences without inventing the owner's answer; keep the independent recheck pending |
| Follow-up repair | [further lifecycle finding](evaluation-fixtures/team-invitations/review-followup-request.md) | Remove the remaining unsupported already-member consumption rule, retain confirmed boundaries, and leave the product decision and independent review pending |
| Repeat-creation repair | [duplicate-request finding](evaluation-fixtures/team-invitations/repeat-creation-repair-request.md) | Keep duplicate issuance choices proposed or pending; reconcile creation/recovery criteria and task drafts without changing the supplied owner answer |
| Fresh context | [resume](evaluation-fixtures/team-invitations/resume-request.md) | Continue from artifacts without duplicating settled decisions or treating unexecuted product checks as passed |

Across every phase, inspect whether only authorized planning artifacts changed and whether any external publication, implementation, or execution-ready status was attempted. Domain-specific findings may require further decisions; assess the consequence rather than rewarding an unconditional READY TO BUILD result.

Blind forward runs receive no expected answer. A review-driven repair trial instead supplies an actual reviewer finding; label it feedback-driven and do not count it as unprompted detection.

Capture a snapshot after each phase. Resume/change tests need the outputs of the preceding phase, but each can run in a fresh context. Record whether a canonical JSON or tracker backend was exercised; the fixture uses Markdown and cannot prove other storage adapters or concurrent writers. Keep provider transcripts and personal paths outside public evidence; publish sanitized planning outputs and outcome records instead.

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

A bounded synthetic existing-feature evaluation now records actual execution of selective decision ownership, corrected readiness, changed-requirement reconciliation, and fresh-context continuation. See the [2026-10-11 evaluation record](evaluations/2026-10-11-selective-planning.md), its fixtures, and retained outputs. It includes an initial failed candidate and the observed regression after correction. This does not establish production behavior, external tracker/JSON adapters, concurrent updates, every harness, or the full new-product/bug/migration matrix. The broader work in [issue #3](https://github.com/Sergio-CVM00/dev-planning/issues/3) remains open. Packaging checks and behavioral evidence remain separate.
