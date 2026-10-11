# S-01 planning-only task records

Revision: 2026-10-11, reconciled with the user's allowed-domain update. Parent outcome: [S-01](slices/S-01.md). These are tracker-ready records kept in Markdown because this fixture has no external tracker. Publication status for every task: **draft, unpublished**. No task is dispatched or execution-ready. Actual module/file paths and implementer names require [U-01](decisions.md#u-01---actual-contract-and-repository) and implementation authorization. D-02 remains a product decision on the granted role; D-04 is a confirmed domain-policy input.

## T-01 - Persist invitation and atomic acceptance domain operation

- Objective/scope: add an invitation migration and domain operation for 24-hour expiry, token digest lookup, authoritative account-email match, current authoritative team-domain recheck, D-02 grant-role insert, one-use consumption, rollback, and concurrent requests. Domain-policy denial for unused older invitations must leave membership and consumption unchanged. Preserve existing membership uniqueness and team isolation; consume an already-member match without changing its role only when domain eligible.
- Acceptance: AC-03, AC-04, AC-06, AC-07, AC-08, AC-10, AC-12; prerequisite: U-01 identity, team-domain, normalization, and migration conventions.
- Evidence expected: migration review; PostgreSQL integration results for restart, expiry boundary, account created after invitation, changed/missing domain at acceptance, old invitation rows, concurrent configuration change, competing acceptance, pre-existing member, and rollback; security review of raw-token storage/logging.
- Owner: future server/data implementer, unassigned.
- `depends_on`: D-02 grant-role decision, U-01 identity/team-domain/migration contract, and implementation authority. D-01, surviving D-03, and D-04 are confirmed inputs.
- `touches`: database migration, invitation persistence/domain operation, authoritative team-domain read, membership unique constraint, token lifecycle.
- `conflicts_with`: T-02 while shared domain/API contract is unsettled; coordinate a single writer for schema and response semantics.
- `parallelizable`: limited. Can develop transaction boundary separately after agreeing internal contract with T-02; integrate before API acceptance checks.

## T-02 - Authenticated invitation API

- Objective/scope: expose creation and acceptance through existing HTTP/auth boundary. Enforce owner-only creation using persisted selected-team membership. Validate target email syntax, require a configured team allowed domain and exact normalized match, without requiring an account or rejecting an existing member. On acceptance, match the authenticated account's current email and recheck the team's current allowed domain for every unused invitation, including older rows. Return stable privacy-preserving denials; never expose boards in invite responses.
- Acceptance: AC-01, AC-02, AC-04, AC-05, AC-07, AC-10, AC-11, AC-12; prerequisites: D-02, U-01, T-01 contract.
- Evidence expected: API permission matrix for two teams and roles, creation for eligible absent account/existing member, missing/disallowed domain denial, normalized exact-match cases, old-link denial after domain change, target-match and wrong-account checks, response inspection, and integration results against PostgreSQL fixture.
- Owner: future server/API implementer, unassigned.
- `depends_on`: D-02, U-01, T-01 interface agreement, implementation authority. D-01, surviving D-03, and D-04 are confirmed inputs.
- `touches`: authenticated HTTP handlers, authorization, team-domain configuration read, normalization contract, invitation domain operation, response contract.
- `conflicts_with`: T-01 at domain boundary and T-03 at HTTP contract; settle contract once before parallel coding.
- `parallelizable`: only after T-01 interface and client contract are agreed; integrate with T-03 at web journey checks.

## T-03 - Web create, share, and accept journeys

- Objective/scope: use existing design system and authenticated client boundary for owner-only create form, copyable link, generic invitation entry, sign-in/account-switch guidance, acceptance, navigation after commit, and loading/error/retry/accessibility states. Show missing/disallowed domain creation errors and privacy-preserving rejection/recovery for older cross-domain links. Avoid account-existence or membership hints at creation. Domain configuration UI is out of scope.
- Acceptance: AC-01, AC-02, AC-03, AC-04, AC-05, AC-07, AC-08, AC-09, AC-10, AC-11, AC-12; prerequisites: U-01, T-02 contract.
- Evidence expected: web journey runner results for owner/member/nonmember, allowed/missing/disallowed domain, absent-account target later signing in, already-member target, reload, changed-domain old link, wrong account, expired/used links, keyboard and narrow viewport; UI inspection observations.
- Owner: future web implementer, unassigned.
- `depends_on`: U-01, T-02 response contract, implementation authority. D-01, surviving D-03, and D-04 are confirmed inputs; D-02 affects success content if the grant policy changes.
- `touches`: membership UI, invitation route, authenticated request client, sensitive link handling.
- `conflicts_with`: T-02 while contract is unsettled; single integration point is the agreed HTTP response/validation mapping.
- `parallelizable`: yes after contract agreement; integrated acceptance requires T-02 and T-01 running together.

## T-04 - Integrated verification and independent review

- Objective/scope: run the documented CI API integration and web journey checks against the complete flow, inspect token/privacy and allowed-domain behavior including unused older links, review migration recovery, and perform one independent review of this substantial security/concurrency change after required checks pass.
- Acceptance: AC-01 through AC-12; prerequisites: U-02 and completed T-01 through T-03.
- Evidence expected: check commands/environment/results, fixture description including mutable team domain and pre-existing invitation, review findings and resolutions, remaining release risks. No result exists in this planning fixture.
- Owner: future implementation owner plus independent reviewer, unassigned.
- `depends_on`: T-01, T-02, T-03, U-02, implementation authority.
- `touches`: CI fixture and results, review record; no production deployment.
- `conflicts_with`: none after integration; review requires stable changes and completed required checks.
- `parallelizable`: no for final integrated gate. API and web evidence may be gathered separately, then reviewed together.

## Dependency and traceability check

Order: confirmed D-01/surviving D-03/D-04 plus pending D-02, U-01, and implementation authority -> T-01 contract -> T-02 API contract -> T-03 client integration -> U-02 and T-04 integrated evidence/review. T-01 transaction development and T-03 UI preparation can overlap only after their shared contract is fixed. No task cycle is planned. All criteria AC-01 through AC-12 and requirements R-01 through R-09 map to at least one task; T-04 owns integrated evidence rather than a separate horizontal outcome.
