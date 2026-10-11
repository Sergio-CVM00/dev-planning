# Decisions, prerequisites, and risks

Sources: [project.md](../../evaluation-fixtures/team-invitations/project.md), supplied 2026-10-11, the user's continuation request, and the subsequent 2026-10-11 allowed-domain change request. Status labels follow the [dev-planning decision policy](../../../skills/dev-planning/references/decision-policy.md).

## D-01 - Invitation sender role

- Question: may only team owners create invitations, or may owners and members both create them?
- Status: **confirmed for S-01: only a current team owner may create**.
- Owner and authority: product owner / user, explicit continuation request on 2026-10-11. This resolves the fixture's undecided choice for the first feature.
- Options: **Owner-only** fits the current owner-mediated support workflow and limits who can grant team access. **Owner and member** allows broader self-service but increases access-granting authority and changes the server check, create UI visibility, and permission tests.
- Resolution and rationale: owner-only as explicitly chosen. The server checks current membership role on every creation request; UI hiding alone is insufficient. A later role change takes effect on subsequent requests.
- Consequence: member and nonmember creation is denied even if the client presents an owner UI or another selected team ID. Revisit if the product owner broadens sender permissions in a later feature.
- Depends on: none. Affects: R-01, SC-01, SC-02, AC-01, AC-02, T-02, T-03, and the planning review.
- Resolution action: complete; the affected records and review use owner-only behavior.

## D-03 - Target email eligibility and acceptance identity

- Question: may creation target an email with no account or an existing membership, and who may accept?
- Status: **partly superseded for S-01 by [D-04](#d-04---team-allowed-domain-policy)**. The matching signed-in account rule and account/membership independence remain confirmed; the former any-valid-email eligibility rule does not.
- Owner and authority: product owner / user, explicit continuation request on 2026-10-11.
- Original resolution: an owner could create an invitation for any syntactically valid target email, whether or not an account or membership currently existed. Creation did not perform account or membership eligibility lookup. This email eligibility is superseded by D-04. The still-confirmed rule requires a signed-in account whose authoritative current email matches the stored target email to accept before expiry; an unauthenticated or different account cannot consume the token or gain membership. [U-01](#u-01---actual-contract-and-repository) must establish account-email comparison semantics.
- Retained consequence: creation does not reject an absent account or existing membership when the email passes D-04. A target without an account may accept if a matching account exists and is signed in before expiry. A matching account already in the team receives an already-member terminal outcome without a duplicate membership or role change. A new invitation to the same eligible email is allowed and has its own token and 24-hour lifetime.
- Depends on: none. Retained identity and account/membership rules affect R-04/R-07, SC-04/07, AC-04/07, T-01/T-02/T-03, and review. Former any-email eligibility in R-01/SC-01/AC-01 is superseded by D-04.
- Revisit trigger: a future product request changes eligible targets or account-email identity rules.

## D-04 - Team allowed-domain policy

- Status: **confirmed for S-01** by the user's 2026-10-11 allowed-domain change request; supersedes only D-03's any-valid-email target eligibility.
- Owner and authority: product owner / user. Only current owners may create invitations, and only for an email whose normalized domain exactly matches the selected team's configured allowed domain. A team without an allowed domain rejects creation until configured. An existing unused invitation to another domain is rejected on acceptance. Domain configuration is outside S-01.
- Planning interpretation: read the authoritative current team allowed domain at both creation and acceptance. Compare normalized domains for equality, not suffix or subdomain containment. If the current allowed domain is absent or differs, reject creation or acceptance and grant no membership. This covers an allowed-domain change after creation and prevents an old link from bypassing current policy at the time of an acceptance attempt. D-04 does **not** decide whether a rejected unused token remains pending, is invalidated, or can later become eligible after policy changes; [D-05](#d-05---rejected-invitation-token-lifecycle) owns that choice. The product repository must establish the authoritative field and normalization rules through U-01; no configuration UI or write path is included.
- Consequence: sender permission and domain eligibility are separate server-side checks. Existing-account and already-member behavior from D-03 remains applicable only for eligible domains. Acceptance checks the current team policy in a serialization strategy compatible with domain updates, so a concurrent domain change cannot make a mismatched invitation grant access. Any token-state transition on rejection awaits D-05.
- Depends on: none. Affects: R-01/R-04/R-07/R-08/R-09, SC-01/04/07/08/09, AC-01/04/07/08/11/12, T-01/T-02/T-03/T-04, and review. The former no-consumption/retry interpretation is superseded, not confirmed.
- Revisit trigger: a later product decision changes the domain policy or domain configuration ownership.

## D-02 - Member-role target for S-01

- Status: **proposed scope boundary**, not a confirmed product-wide invitation policy.
- Source: project.md names owner/member roles but requests a team invitation without role selection. The saved S-01 plan proposes member-role grants; the continuation request does not explicitly settle the granted role.
- Proposal: S-01 creates only member-role memberships. It never grants owner. This is the least-privilege way to deliver the stated join outcome and avoids expanding the feature into role administration.
- Owner: product owner / user for confirmation. Planning authority does not independently settle a user-visible access grant.
- Consequence of waiting: the role inserted by acceptance and its criteria remain provisional, so S-01 cannot pass READY TO BUILD. Owner invitations would require revised authorization and security review.
- Resolution action: confirm member-only grants for S-01 or choose a different grant policy; then reconcile R-04, SC-04/07, AC-04/07, T-01/T-02, and review.
- Affects: R-04, AC-07, T-01, T-02.

## D-05 - Rejected invitation token lifecycle

- Status: **needs product-owner decision for S-01**. The separate plan reviewer found that the earlier D-04 interpretation and AC-12 asserted non-consumption and later retry after a cross-domain rejection without owner authority. Those assertions are superseded; this record does not assign the owner an answer.
- Confirmed boundary: [D-04](#d-04---team-allowed-domain-policy) requires rejection of an unused invitation when its target domain differs from the team's current configured allowed domain. That attempt grants no membership or board access. Single-use and 24-hour expiry from project.md still apply to successful acceptance; they do not settle the state of a policy-rejected token.
- Choice for product owner / user: **terminal invalidation** marks a rejected token unusable for future acceptance, including if the domain policy later changes; **retain pending** permits a later attempt before expiry if the current policy then matches. Either choice must define the response and recovery guidance without disclosing team-private data. Terminal invalidation is the security-conservative proposal, not a confirmed requirement. The owner may choose another explicit lifecycle rule.
- Consequence of waiting: the invitation state model, transaction write on policy rejection, later retry behavior, stale-link UI, and AC-12 state assertions cannot be finalized. S-01 is not READY TO BUILD. Keep failed transaction retry semantics in R-08 separate from this policy rejection.
- Depends on: D-04. Affects: R-03/R-04/R-07/R-08/R-09, SC-03/04/07/08/09, AC-03/04/07/08/12, T-01/T-02/T-03/T-04, and review.
- Resolution action: ask the product owner which fate a policy-rejected unused token has, including after a later domain-policy change; then reconcile the state model, responses, criteria, tasks, and review. Do not treat silence or this recommendation as confirmation.

## U-01 - Actual contract and repository

- Type/status: **prerequisite; unavailable in this fixture**.
- Evidence: project.md describes the authenticated HTTP boundary and PostgreSQL but supplies no product code, API schema, account email semantics, migration framework, or live app.
- Consequence: route names, field names, exact response codes, authoritative account-email comparison and change semantics, the team allowed-domain source and normalization rules, concurrency with domain updates, and migration mechanics cannot be validated. The matching account email must come from authenticated identity, not client input; allowed domain must come from authoritative team configuration. If existing semantics cannot safely support either check, the contract needs a new decision before building.
- Owner: future implementation owner. Next action: inspect the owning repository's auth, team authorization, allowed-domain configuration and update path, response conventions, migration tooling, and tests before finalizing contracts or writing code. Stop when the path, normalization, identity, and serialized policy guarantees are evidenced; revise [S-01](slices/S-01.md) and [review](review.md) if they differ.
- Depends on: access to the actual repository. Affects: R-01 to R-09, T-01 to T-04. This is a limit on implementation readiness, not permission to access services during this exercise.

## U-02 - Validation access

- Type/status: **prerequisite; unavailable in this fixture**.
- Evidence: project.md documents API integration checks with a disposable PostgreSQL fixture and a web journey runner, but no executable harness or runtime access is supplied and product test execution is forbidden here.
- Consequence: acceptance methods are planned, not executed; any environment-specific fixture gap may change the evidence plan.
- Owner: future implementation owner. Next action: after implementation authorization, confirm harness access and fixture support; run API and web checks at the required gate. Stop when recorded results cover [S-01 criteria](slices/S-01.md#acceptance-and-planned-evidence).

## U-03 - Registered product execution host and authority

- Type/status: **prerequisite; unavailable in this fixture**. The synthetic project has no registered execution host or product delivery owner. This planning evaluation runs on Lenovo, but that host and the global coordination rule do not register it as Boardroom's implementation environment or grant implementation permission.
- Owner: product/project owner through the project's registry or instructions. Next action: identify the owning repository, registered execution host and delivery path, then obtain separate implementation authority before assigning or running T-01 through T-04. Preserve Lenovo as the global planning/coordination owner under the host instructions; do not infer a product execution route from it.
- Depends on: project registry/instructions supplied outside this fixture. Affects: task assignment, U-01/U-02 access, implementation and validation execution, and readiness review.

## RISK-01 - Link disclosure

Possession of a link must not bypass signed-in target-email matching. Treat the opaque token as sensitive: do not put it in server logs, analytics, or outbound referrers; avoid showing team or board metadata to an unauthenticated or wrong-account visitor. A fragment-based share URL with client submission to an authenticated API is proposed to reduce routine server/referrer exposure, subject to U-01. Planned API and web checks cover the boundary. Revisit if actual routing or observability behavior differs.

## RISK-02 - Duplicate membership and partial consumption

The existing `(team_id, user_id)` uniqueness constraint is necessary but not sufficient to define a clean invitation outcome. One transaction must coordinate membership and consumed state. Concurrent requests, retries, and a pre-existing membership need deterministic terminal results. Planned integration checks use the disposable PostgreSQL fixture. Revisit if current persistence abstractions cannot supply row-level locking or equivalent atomicity.

## RISK-03 - Retention and operational scale

Expired and consumed invitation records have no supplied retention policy. S-01 checks expiry at request time and does not require cleanup for correctness. Retention, list-management UX, analytics, and volume objectives are deferred to an operational/product decision when measured usage or a release plan requires them. They cannot invalidate the first bounded outcome.
