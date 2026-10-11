# Decisions, prerequisites, and risks

Sources: [project.md](../../evaluation-fixtures/team-invitations/project.md), supplied 2026-10-11, the earlier 2026-10-11 continuation request, and the user's 2026-10-11 domain-policy update. Status labels follow the [dev-planning decision policy](../../../skills/dev-planning/references/decision-policy.md).

## D-01 - Invitation sender role

- Question: may only team owners create invitations, or may owners and members both create them?
- Status: **confirmed for S-01: only a current team owner may create**.
- Owner and authority: product owner / user, explicit continuation request on 2026-10-11. This resolves the fixture's undecided choice for the first feature.
- Options: **Owner-only** fits the current owner-mediated support workflow and limits who can grant team access. **Owner and member** allows broader self-service but increases access-granting authority and changes the server check, create UI visibility, and permission tests.
- Resolution and rationale: owner-only as explicitly chosen. The server checks current membership role on every creation request; UI hiding alone is insufficient. A later role change takes effect on subsequent requests.
- Consequence: member and nonmember creation is denied even if the client presents an owner UI or another selected team ID. Revisit if the product owner broadens sender permissions in a later feature.
- Depends on: none. Affects: R-01, SC-01, SC-02, AC-01, AC-02, T-02, T-03, and the planning review.
- Resolution action: complete; the affected records and review use owner-only behavior.

## D-03 - Target account eligibility and acceptance identity

- Question: may creation target an email with no account or an existing membership, and who may accept?
- Status: **partly superseded by [D-04](#d-04---team-allowed-domain-policy)**. The no-account/no-membership lookup and matching signed-in identity rules remain confirmed; the earlier any-valid-domain creation rule is superseded.
- Owner and authority: product owner / user, explicit continuation request on 2026-10-11.
- Original resolution: an owner could create an invitation for any syntactically valid target email, whether or not an account or membership currently existed. **Superseded for domain eligibility by D-04:** creation now also requires a configured team allowed domain and an exact match of normalized domains. Creation still performs no account or membership eligibility lookup. Only a signed-in account whose authoritative current email matches the stored target email may accept before expiry, subject also to D-04's acceptance check. An unauthenticated or different account cannot consume the token or gain membership. Matching uses the product's authoritative account-email comparison semantics; [U-01](#u-01---actual-contract-and-repository) must establish those semantics before implementation.
- Consequence: the previous proposal to reject creation for an existing member is superseded. An in-domain target without an account may accept if a matching account exists and is signed in before expiry and the team's current allowed domain still matches. A matching account already in the team receives an already-member terminal outcome without a duplicate membership or role change. A new invitation to the same eligible email is allowed and has its own token and 24-hour lifetime.
- Depends on: none. Affects: R-03/R-04/R-07, SC-01/04/07, AC-01/04/07, T-01/T-02/T-03, and review.
- Revisit trigger: a future product request changes account or membership eligibility or account-email identity rules. Domain eligibility is owned by D-04.

## D-04 - Team allowed domain policy

- Question: which target domains permit creation, and what happens to unused invitations after the team's allowed domain changes?
- Status: **confirmed for S-01** by the user's 2026-10-11 domain-policy update.
- Resolution: a current owner may create an invitation only when the selected team has a configured allowed domain and the normalized domain of the target email exactly equals that configured allowed domain after normalization. A team with no allowed domain rejects creation until configured. Acceptance rechecks the invitation target's normalized domain against the team's current configured allowed domain; an existing unused invitation to another domain is rejected without membership creation or token consumption. An absent allowed domain also fails this acceptance check. The current domain check applies even when the invitation was created before this policy or before a domain change.
- Scope: domain configuration and its UI/API are outside S-01. D-03's any-valid-domain creation permission is superseded; its absence-of-account, existing-member, and matching-identity rules remain in force for eligible domains. D-01 owner-only creation and D-02's provisional member grant are unchanged.
- Rationale/consequence: current team configuration is the authority at both creation and acceptance, so old links cannot bypass a changed domain policy. A domain-policy denial exposes no team-private data and follows the saved plan's rejected-attempt behavior by leaving the invitation unused. The client gives an actionable generic explanation without disclosing the configured domain to an unauthorized visitor.
- Depends on: none. Affects: R-01/R-04/R-07/R-08/R-09, SC-01/04/07/08/09, AC-01/04/07/08/11/12, T-01/T-02/T-03/T-04, and review.
- Implementation prerequisite: [U-01](#u-01---actual-contract-and-repository) must identify the authoritative team setting and normalization contract. Revisit if the product owner changes the policy or the owning contract cannot express exact normalized comparison.

## D-02 - Member-role target for S-01

- Status: **proposed scope boundary**, not a confirmed product-wide invitation policy.
- Source: project.md names owner/member roles but requests a team invitation without role selection. The saved S-01 plan proposes member-role grants; the continuation request does not explicitly settle the granted role.
- Proposal: S-01 creates only member-role memberships. It never grants owner. This is the least-privilege way to deliver the stated join outcome and avoids expanding the feature into role administration.
- Owner: product owner / user for confirmation. Planning authority does not independently settle a user-visible access grant.
- Consequence of waiting: the role inserted by acceptance and its criteria remain provisional, so S-01 cannot pass READY TO BUILD. Owner invitations would require revised authorization and security review.
- Resolution action: confirm member-only grants for S-01 or choose a different grant policy; then reconcile R-04, SC-04/07, AC-04/07, T-01/T-02, and review.
- Affects: R-04, AC-07, T-01, T-02.

## U-01 - Actual contract and repository

- Type/status: **prerequisite; unavailable in this fixture**.
- Evidence: project.md describes the authenticated HTTP boundary and PostgreSQL but supplies no product code, API schema, account email semantics, team-domain setting contract, migration framework, or live app. The allowed-domain requirement comes from the user's update, not from observed product code.
- Consequence: route names, field names, exact response codes, authoritative account-email comparison and change semantics, location of the team allowed-domain setting, domain normalization semantics, and migration mechanics cannot be validated. In particular, the matching email must come from authenticated account identity, not a client-supplied email; the allowed domain must come from current authoritative team configuration, not a request field. If the existing contracts cannot safely support either match, the plan needs revision before building.
- Owner: future implementation owner. Next action: inspect the owning repository's auth, team authorization and configuration, email/domain normalization, response conventions, migration tooling, and tests before finalizing contracts or writing code. Stop when the source, normalization, and identity guarantees are evidenced; revise [S-01](slices/S-01.md) and [review](review.md) if they differ.
- Depends on: access to the actual repository. Affects: R-01 to R-09, T-01 to T-04. This is a limit on implementation readiness, not permission to access services during this exercise.

## U-02 - Validation access

- Type/status: **prerequisite; unavailable in this fixture**.
- Evidence: project.md documents API integration checks with a disposable PostgreSQL fixture and a web journey runner, but no executable harness or runtime access is supplied and product test execution is forbidden here.
- Consequence: acceptance methods are planned, not executed; any environment-specific fixture gap, especially mutable team-domain configuration and pre-existing unused invitation rows, may change the evidence plan.
- Owner: future implementation owner. Next action: after implementation authorization, confirm harness access and fixture support for missing/different domains, older links, and concurrent configuration/acceptance; run API and web checks at the required gate. Stop when recorded results cover [S-01 criteria](slices/S-01.md#acceptance-and-planned-evidence).

## RISK-01 - Link disclosure

Possession of a link must not bypass signed-in target-email matching. Treat the opaque token as sensitive: do not put it in server logs, analytics, or outbound referrers; avoid showing team or board metadata to an unauthenticated or wrong-account visitor. A fragment-based share URL with client submission to an authenticated API is proposed to reduce routine server/referrer exposure, subject to U-01. Planned API and web checks cover the boundary. Revisit if actual routing or observability behavior differs.

## RISK-02 - Duplicate membership and partial consumption

The existing `(team_id, user_id)` uniqueness constraint is necessary but not sufficient to define a clean invitation outcome. One transaction must coordinate membership and consumed state. Concurrent requests, retries, and a pre-existing membership need deterministic terminal results. Planned integration checks use the disposable PostgreSQL fixture. Revisit if current persistence abstractions cannot supply row-level locking or equivalent atomicity.

## RISK-03 - Retention and operational scale

Expired and consumed invitation records have no supplied retention policy. S-01 checks expiry at request time and does not require cleanup for correctness. Retention, list-management UX, analytics, and volume objectives are deferred to an operational/product decision when measured usage or a release plan requires them. They cannot invalidate the first bounded outcome.

## RISK-04 - Domain normalization and configuration race

An email domain, a configured domain, and a concurrent domain change must not be compared under inconsistent rules or snapshots. Exact normalized comparison excludes subdomain and suffix matching. The acceptance decision and membership grant require a consistency boundary with current team configuration; an older unused invitation must not bypass the changed policy. U-01 owns inspection of the actual setting and normalization/transaction contracts. AC-11/AC-12 plan the corresponding negative and concurrency evidence. If the repository cannot provide a safe source or boundary, revise the contract and readiness review before implementation.
