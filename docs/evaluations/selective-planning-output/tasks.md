# S-01 planning-only task records

Revision: 2026-10-11, repaired after separate plan-review feedback. Parent outcome: [S-01](slices/S-01.md). These are tracker-ready records kept in Markdown because this fixture has no external tracker. Publication status for every task: **draft, unpublished**. No task is dispatched or execution-ready. Actual module/file paths and implementer names require [U-01](decisions.md#u-01---actual-contract-and-repository), a registered product execution host under [U-03](decisions.md#u-03---registered-product-execution-host-and-authority), and separate implementation authorization. D-02 remains a product decision on the granted role; D-05 remains a product decision on policy-rejected token fate; D-04 confirms only the allowed-domain rejection.

## T-01 - Persist invitation and atomic acceptance domain operation

- Objective/scope: add an invitation migration and domain operation for 24-hour expiry, token digest lookup, authoritative account-email match, current configured team-domain check at creation and acceptance, D-02 grant-role insert, one-use successful consumption, rollback, and concurrent requests. Require exact normalized domain equality without account or membership lookup at creation; reject missing configuration. Recheck current policy under serialization with domain updates before accepting even a legacy unused link. Reject mismatched links without membership changes; implement their token-state transition only after D-05. Preserve membership uniqueness and team isolation; consume an eligible already-member match without changing its role.
- Acceptance: AC-01, AC-03, AC-04, AC-06, AC-07, AC-08, AC-10, AC-11, AC-12; prerequisite: U-01 identity, allowed-domain source/normalization/update semantics, and migration conventions.
- Evidence expected: migration review; PostgreSQL integration results for restart, expiry boundary, account created after invitation, competing acceptance and domain update, old out-of-domain pending link, pre-existing member, and rollback; after D-05, token state and later policy-change outcome; security review of raw-token storage/logging.
- Owner: future server/data implementer, unassigned.
- `depends_on`: D-02 grant-role decision, D-05 rejected-token lifecycle decision, U-01 identity/domain/migration contract, U-03 registered execution host, and implementation authority. D-01, retained D-03, and D-04 are confirmed inputs.
- `touches`: database migration, invitation persistence/domain operation, team allowed-domain read/serialization boundary, membership unique constraint, token lifecycle. No domain configuration write path.
- `conflicts_with`: T-02 while shared domain/API contract is unsettled; coordinate a single writer for schema and response semantics.
- `parallelizable`: limited. Can develop transaction boundary separately after agreeing internal contract with T-02; integrate before API acceptance checks.

## T-02 - Authenticated invitation API

- Objective/scope: expose creation and acceptance through existing HTTP/auth boundary. Enforce owner-only creation using persisted selected-team membership and require the target's normalized domain to equal the team's current configured allowed domain; reject missing configuration. Validate target email syntax without requiring an account or rejecting an existing member. On acceptance, match the authenticated account's current email and recheck current domain policy for unused links; return privacy-preserving ineligible outcomes without membership changes or board exposure. Finalize token state and later retry response only after D-05.
- Acceptance: AC-01, AC-02, AC-04, AC-05, AC-07, AC-10, AC-11, AC-12; prerequisites: D-02, D-05, U-01, T-01 contract.
- Evidence expected: API permission/domain matrix for two teams and roles, missing configuration, exact/equivalent/subdomain/suffix domains, creation for absent account and existing member, legacy out-of-domain pending link, target-match and wrong-account checks, response inspection, chosen D-05 token-state and later policy-change response, and integration results against PostgreSQL fixture.
- Owner: future server/API implementer, unassigned.
- `depends_on`: D-02, D-05, U-01, U-03, T-01 interface agreement, implementation authority. D-01, retained D-03, and D-04 are confirmed inputs.
- `touches`: authenticated HTTP handlers, authorization, current team-domain check, invitation domain operation, response contract.
- `conflicts_with`: T-01 at domain boundary and T-03 at HTTP contract; settle contract once before parallel coding.
- `parallelizable`: only after T-01 interface and client contract are agreed; integrate with T-03 at web journey checks.

## T-03 - Web create, share, and accept journeys

- Objective/scope: use existing design system and authenticated client boundary for owner-only create form, copyable link, generic invitation entry, sign-in/account-switch guidance, acceptance, navigation after commit, and loading/error/retry/accessibility states. Show actionable missing/mismatched-domain feedback to the owner and privacy-preserving stale-link recovery to the recipient; finalize whether guidance may suggest later retry only after D-05. Avoid account-existence or membership hints at creation; do not add a domain configuration UI.
- Acceptance: AC-01, AC-02, AC-03, AC-04, AC-05, AC-07, AC-08, AC-09, AC-10, AC-11, AC-12; prerequisites: U-01, T-02 contract.
- Evidence expected: web journey runner results for owner/member/nonmember, configured/missing/mismatched domains, absent-account target later signing in, already-member target, reload, wrong account, stale out-of-domain and expired/used links, chosen D-05 recovery, keyboard and narrow viewport; UI inspection observations.
- Owner: future web implementer, unassigned.
- `depends_on`: D-05, U-01, U-03, T-02 response contract, implementation authority. D-01, retained D-03, and D-04 are confirmed inputs; D-02 affects success content if the grant policy changes.
- `touches`: membership UI, invitation route, authenticated request client, sensitive link handling.
- `conflicts_with`: T-02 while contract is unsettled; single integration point is the agreed HTTP response/validation mapping.
- `parallelizable`: yes after contract agreement; integrated acceptance requires T-02 and T-01 running together.

## T-04 - Integrated verification and independent review

- Objective/scope: run the documented CI API integration and web journey checks against the complete flow, inspect token/privacy behavior, current-domain enforcement including legacy invitations and races, and migration recovery, then perform one independent review of this substantial security/concurrency change after required checks pass.
- Acceptance: AC-01 through AC-12; prerequisites: U-02 and completed T-01 through T-03.
- Evidence expected: check commands/environment/results, fixture description, D-05 policy-change scenario results, review findings and resolutions, remaining release risks. No result exists in this planning fixture.
- Owner: future implementation owner plus independent reviewer, unassigned.
- `depends_on`: T-01, T-02, T-03, U-02, U-03, implementation authority.
- `touches`: CI fixture and results, review record; no production deployment.
- `conflicts_with`: none after integration; review requires stable changes and completed required checks.
- `parallelizable`: no for final integrated gate. API and web evidence may be gathered separately, then reviewed together.

## Dependency and traceability check

Order: confirmed D-01/retained D-03/D-04 plus pending D-02/D-05, U-01/U-03, and separate implementation authority -> T-01 contract -> T-02 API contract -> T-03 client integration -> U-02 and T-04 integrated evidence/review. T-01 transaction development and T-03 UI preparation can overlap only after their shared contract is fixed. No task cycle is planned. All criteria AC-01 through AC-12 and requirements R-01 through R-09 map to at least one task; T-04 owns integrated evidence rather than a separate horizontal outcome.
