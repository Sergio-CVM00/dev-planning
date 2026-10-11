# Boardroom team invitations - planning index

Revision: 2026-10-11, repaired after separate plan-review feedback. Source: [project evidence](../../evaluation-fixtures/team-invitations/project.md). This index is the global map; linked records own the detail. Planning is the only authorized action. No product code, product tests, network services, tracker publication, or deployment are authorized. Global planning/coordination ownership remains Lenovo under host instructions; Boardroom has no registered product execution host in the supplied evidence, and this evaluation host supplies no future implementation authority ([U-03](decisions.md#u-03---registered-product-execution-host-and-authority)).

## Destination and outcome

Boardroom owners currently request membership changes through support. The outcome is that a signed-in team owner creates a durable, 24-hour invitation link only for an email whose normalized domain exactly matches the team's configured allowed domain; a team without that configuration rejects creation. A signed-in account matching the target email accepts it once only if the current team domain policy permits it, including after a reload or server restart when no prior policy rejection has changed its eligibility. Team boards remain invisible to nonmembers. The granted member role is the saved plan's pending D-02 proposal; policy-rejected token fate is pending D-05.

IN: invitation creation, link sharing by people, signed-in acceptance, current allowed-domain checks, persisted state, expiration, single-use consumption, concurrent acceptance safety, client states, server authorization, and tenant isolation. OUT: allowed-domain configuration, email delivery, reminders, billing, production deployment, and an orchestration framework. Do not infer invitation revocation, owner-role grants, or broader membership administration from this slice.

Planning depth: **Standard, with deep treatment of authorization and token use**. This is an existing product feature crossing client, API, persistence, and a new bearer-link trust boundary. [Product and system impact](product-system.md) and the [delivery roadmap](roadmap.md) retain the global destination.

## Evidence and authority

- [project.md](../../evaluation-fixtures/team-invitations/project.md) is the sole supplied product, system, and CI evidence. No repository, running app, API schema, or executable harness is supplied. Current behavior and system facts below are fixture statements, not independently observed runtime behavior.
- [Decision and unknown records](decisions.md) record D-01 owner-only creation, D-03 matching-account and account/membership independence, and D-04 current allowed-domain eligibility, which supersedes D-03's any-email rule. D-02 grant role and D-05 policy-rejected token lifecycle remain open. U-03 records the absent product execution host. A future authorized implementation session must inspect actual contracts and CI harness before choosing concrete routes or field names.
- Saved Markdown in `planning/` is authoritative. No tracker exists in this exercise; all [task records](tasks.md) are planning-only and unpublished.

## Frontier and dependencies

| ID | Question / record | Owner | Status | Depends on | Next action |
| --- | --- | --- | --- | --- | --- |
| [D-01](decisions.md#d-01---invitation-sender-role) | Which roles may create invitations? | Product owner / user | Confirmed: owner-only for S-01 | None | Apply to server permission and UI plan. |
| [D-03](decisions.md#d-03---target-email-eligibility-and-acceptance-identity) | Which accepting account is allowed, regardless of account or membership at creation? | Product owner / user | Matching signed-in account confirmed; any-email eligibility superseded by D-04 | None | Preserve matching identity and account/membership independence. |
| [D-04](decisions.md#d-04---team-allowed-domain-policy) | Which target domains are eligible at creation and acceptance? | Product owner / user | Confirmed: exact normalized match to current configured team domain; rejected-token fate not settled | None | Apply current-domain checks at both boundaries; reject unconfigured creation and legacy mismatches. |
| [D-02](decisions.md#d-02---member-role-target-for-s-01) | Which role does acceptance grant? | Product owner / user | Proposed: member-only; confirmation pending | None | Confirm member-only or choose another grant policy; reconcile affected records. |
| [D-05](decisions.md#d-05---rejected-invitation-token-lifecycle) | What happens to an unused token rejected by current domain policy, including after a later policy change? | Product owner / user | Open: terminal invalidation or retained pending eligibility; neither confirmed | D-04 | Decide token lifecycle and recovery guidance; reconcile AC-12 and tasks. |
| [U-01](decisions.md#u-01---actual-contract-and-repository) | What are the actual API, auth, email identity, and migration conventions? | Future implementation owner | Prerequisite | Access to product repository | Inspect owning code/docs before final route and schema selection. |
| [U-02](decisions.md#u-02---validation-access) | Is the documented CI fixture and journey runner available? | Future implementation owner | Prerequisite | Runtime and CI access | Confirm fixtures and run checks only after implementation authorization. |
| [U-03](decisions.md#u-03---registered-product-execution-host-and-authority) | Which registered host and delivery owner may execute Boardroom work? | Product/project owner through registry | Prerequisite | Project registry/instructions | Establish product route and separate implementation authority before assigning tasks. |

The active decision frontier is D-02 and D-05; D-05 follows the confirmed D-04 boundary and needs a product-owner choice. U-01/U-02 require the actual product repository and runtime; U-03 requires the project registry and execution owner. All are unavailable in this exercise. Not yet specified: later invitation management, cancellation, allowed-domain configuration, and support migration. Revisit when the first slice is accepted or the product owner expands scope.

## Next deliverable

[S-01: Create and accept a member invitation](slices/S-01.md) is the next useful vertical slice. It joins the web journey, authenticated API, current team-domain policy, PostgreSQL persistence, and integration evidence. Owner-only creation and exact allowed-domain eligibility are confirmed; the member-role grant and rejected-token lifecycle remain provisional pending D-02/D-05. [Task records](tasks.md) and [planning review](review.md) complete the handoff.

## Coverage dispositions

| Area | Disposition | Evidence / reason and action |
| --- | --- | --- |
| Product, UX, content | Detail now | Owner create/share and target accept, including missing/mismatched-domain, expired, wrong-account, and recovery journeys in [S-01](slices/S-01.md); reuse design system per project.md. Grant role awaits D-02; policy-rejection recovery awaits D-05. |
| Domain, backend, contracts | Detail now | Server-enforced permission, exact normalized domain and target-account matches, one-use state, and failure outcomes in [S-01](slices/S-01.md). Exact route and normalization conventions wait for U-01. |
| Data, persistence, migration | Detail now | New invitation record, authoritative current team-domain read, unique membership, atomic successful acceptance, expiration, and forward recovery in [S-01](slices/S-01.md). Rejection state awaits D-05; existing team configuration and migration conventions wait for U-01. |
| Security, privacy | Detail now | Bearer token handling, current team-domain and account-email checks, nonmember board isolation, and enumeration controls in [S-01](slices/S-01.md); D-01 fixes sender access, D-03 fixes account identity, and D-04 fixes domain eligibility. |
| Performance, reliability, integrations | Detail now for restart, retries, and concurrent acceptance; deferred for scale targets | PostgreSQL is source of truth; no external provider. Capacity/latency targets have no evidence and do not choose this slice's architecture. Revisit on measured volume. |
| Infrastructure, delivery, operation | Detail now for migration/CI boundary; deferred for production release | Documented CI methods are planned in [S-01](slices/S-01.md). U-03 must establish the product execution host and owner; the evaluation host cannot supply them. Deployment is out of authority and scope. Revisit with a release request. |
| Research and feasibility | Detail now | U-01 includes current allowed-domain storage, normalization, and concurrent update semantics; U-02 bounds missing runtime evidence. No prototype or product execution is authorized. |
| Coordination, risks, traceability | Detail now | D-01/D-03/D-04, open D-02/D-05, U-01/U-02/U-03, criteria, tasks, and [review](review.md) give ownership and dependency order. One implementation writer per affected area after product ownership is established. |
| Specialized domains | Not applicable | Supplied feature contains none of the listed specialized domains. |

## Status and next permitted action

**NEEDS DECISION** at [review revision 2026-10-11](review.md): D-02 can change the membership grant; D-05 can change rejected-token state, later retry, and recovery. D-01, the retained part of D-03, and D-04 are confirmed and reconciled within their authority. U-01/U-02/U-03 are unavailable prerequisites that also prevent READY TO BUILD. The repaired plan needs a fresh independent planning review after these decisions and evidence are reconciled. The next permitted planning action is to obtain D-02/D-05 owner decisions and the project registry/repository/validation evidence for U-03/U-01/U-02 through separately authorized access. Product implementation, product test execution, and issue publication are not authorized here.
