# Selective planning behavioral evaluation

Type: actual agent execution (blind forward runs and a separately labelled feedback-driven repair), with independent review and repair recheck.
Date: 2026-10-11.
Starting point: the synthetic existing-product [Boardroom fixture](../evaluation-fixtures/team-invitations/project.md).
Runtime: native Codex CLI 0.160.0 on Linux (Lenovo), OpenAI Codex `gpt-6-sol`, reasoning effort `high`, workspace-write sandbox, ephemeral contexts, user configuration ignored. The authenticated catalog route and fresh quota were checked before dispatch. No model substitution was used.
Permitted actions: read the supplied skill/evidence and write synthetic planning documents only. No product implementation, test execution, external tracker, installation, or service contact.

## Initial candidate and correction

Instruction revision `c6dbfeb636502d70b3d268aba862a833f9ce0c42` was exercised in two completed fresh-context runs. The first created seven planning documents, identified the undecided invitation sender role, recommended owner-only without treating the recommendation as consent, and returned NEEDS DECISION. Server authorization, durable persistence, wrong-account rejection, and concurrent acceptance were included in planned evidence.

The second run applied the owner answer and prepared four unpublished issue records. It exposed two readiness defects: the unconfirmed member-role target became an agent-delegated choice without a source, and the review used READY TO BUILD as a specification while required repository/verification prerequisites remained unavailable. Those results are retained as failures, not counted as passed behavior. A third downstream run was interrupted after this finding; it supplies no completed evaluation result.

Correction revision `e06bf650df1c38ba90e68e2f1246dbd6eeb5a4b0` requires a scoped authority source for delegated product/access choices and separates completed specification documents from a blocked implementation-readiness gate. The regression starts from the saved first-run artifacts, uses the unchanged owner-answer request, and does not receive the evaluator's expected answer.

## Corrected regression

The repeated owner-answer run on `e06bf650df1c38ba90e68e2f1246dbd6eeb5a4b0` keeps D-01 confirmed from the supplied answer, D-02 proposed pending its decision-maker, and U-01/U-02 unavailable. It returns NEEDS DECISION instead of the previous qualified READY TO BUILD. Specification and draft issue records are updated, while implementation, product tests, and publication remain unperformed. This is an observed regression result, not an assertion inferred from instruction wording.

The completed changed-constraint run preserves D-01, partially supersedes D-03, and introduces D-04 with source and affected records. Requirement/scenario/criterion IDs remain stable where behavior is retained; added domain checks include absent configuration, exact domain equality, and rejection of previously unused cross-domain invitations. The slice and four draft issue records are reconciled; domain configuration remains out of scope. The review stays NEEDS DECISION for D-02 and retains unavailable U-01/U-02. The agent performed documentary link/ID checks, not product tests.

The completed fresh-context run loads the saved records and reconciles the superseded/current decisions without changing any planning file: all seven files are byte-identical to the phase-three snapshot. It returns the same NEEDS DECISION handoff, identifies D-02 as unresolved rather than reopening D-01/D-04, and keeps U-01/U-02 as prerequisites. It does not create duplicate questions/issues or claim product-test results.

## Independent-review finding and second correction

A separate native Codex `gpt-6-sol/high` read-only review of `4807bf1341708e93c96716e964f61c01de39faf5` checked new-product, existing-feature, bug, and migration entry points at desk-review level. It verified the retained resume snapshots and passed the packaging validator, but found a remaining access-policy attribution error: D-04 and AC-12 treated a rejected cross-domain token as unconsumed even though the request did not decide its later retry eligibility. It also identified an unsupported future execution-host claim in the synthetic output. The earlier changed-constraint result therefore establishes reconciliation, not complete decision attribution.

Correction revision `cf12948327b305ab55a6df3e144636bc4420583b` keeps unspecified adjacent access/lifecycle/recovery consequences proposed and separates the planning host from future product ownership. Its blind regression uses the unchanged domain-change request from the pre-change saved state, with no expected answer supplied. That run still retained the unsupported lifecycle interpretation; this is a failed attribution result, not a passing regression.

Revision `c872357407c2872ae74da39b68f6fe9fcde675fd` makes independent contextual review a gate for consequential plans and splits confirmed boundaries from adjacent consequences. A feedback-driven repair run then receives the actual reviewer finding. It moves rejected-token lifecycle/retry behavior into proposed D-05, reconciles R/SC/AC-12 and the draft tasks, and records unavailable product execution ownership in U-03. D-04 retains only the confirmed domain gate. The result stays NEEDS DECISION for D-02/D-05 with implementation prerequisites and independent recheck pending. This proves response to review feedback; it does not prove unprompted detection of that gap by the drafting agent.

The final fresh-context continuation on `c872357407c2872ae74da39b68f6fe9fcde675fd` reads the repaired records and retains D-02/D-05, U-01/U-02/U-03, and independent rereview as pending. It does not reopen confirmed D-01/D-04 or infer retry eligibility. All seven planning files are byte-identical to the feedback-repaired snapshot. This is a completed persistence/authority observation on the final instruction revision.

## Retained evidence

The [observed final index](selective-planning-output/index.md), [decision records](selective-planning-output/decisions.md), [slice](selective-planning-output/slices/S-01.md), [issue drafts](selective-planning-output/tasks.md), and [review](selective-planning-output/review.md) retain the shareable final artifacts. Only relative file links were normalized to this repository; [the manifest](selective-planning-output-manifest.json) records hashes before and after that transformation. These are historical evaluation outputs, not normative product requirements or another editable source for the skill.

Eight planning runs are covered by the final record: two initial-candidate runs, three first-correction runs, the second blind changed-constraint run, a feedback-driven review repair, and continuation from the repaired state. Failed attribution candidates are distinguished from successful repair/persistence observations. One initial-candidate downstream run was interrupted and is not counted as complete. File-change events in the completed runs stay under the allowed planning directory. Input skill/project files match their supplied snapshots; the tool-event audit found no product implementation, product test execution, or tracker/service calls. Both fresh-context resume phases made no writes. The final source inputs match the supplied instruction tree; the intermediate failed blind run is retained through its source revision and tool events rather than counted as passed. These checks verify this bounded exercise, not sandbox containment or all future agent behavior.

## Assessment protocol

Inspect the source records and observable outputs for decision attribution, relevant coverage, normal/negative acceptance, requirement-to-issue traceability, dependency ordering, changed-requirement invalidation, fresh-context continuation, and the planning-only exit. Verify input files remain unchanged and inspect tool events for unauthorized side effects. Product tests mentioned in artifacts are planned evidence, not executed tests.

## Limits

This is a bounded synthetic feature evaluation, not a comparative benchmark or proof of completeness. It does not execute a product, a production deployment, native GUI QA, external tracker publication, concurrent writers, a canonical JSON backend, or automatic activation in every harness. The broader new-product/bug/migration execution matrix in issue #3 remains open. Structural validation checks packaging separately from observed agent behavior.
