# Boardroom team invitations - planning index

Revision: 2026-10-11. Source: [project evidence](../../evaluation-fixtures/team-invitations/project.md). This index is the global map; linked records own the detail. Planning is the only authorized action. No product code, product tests, network services, tracker publication, or deployment are authorized. Execution ownership remains Lenovo.

## Destination and outcome

Boardroom owners currently request membership changes through support. The outcome is that a signed-in team owner creates a durable, 24-hour invitation link only for a valid email whose normalized domain exactly matches the team's configured allowed domain. A team without that setting rejects creation. Only a signed-in account matching the target email may accept, and acceptance must still satisfy the team's current allowed-domain policy, including for unused older links. The flow survives reload and restart; team boards remain invisible to nonmembers. The granted member role is the saved plan's pending D-02 proposal.

IN: invitation creation, link sharing by people, signed-in acceptance, allowed-domain enforcement at creation and acceptance, persisted state, expiration, single-use consumption, concurrent acceptance safety, client states, server authorization, and tenant isolation. OUT: allowed-domain configuration, email delivery, reminders, billing, production deployment, and an orchestration framework. Do not infer invitation revocation, owner-role grants, or broader membership administration from this slice.

Planning depth: **Standard, with deep treatment of authorization and token use**. This is an existing product feature crossing client, API, persistence, and a new bearer-link trust boundary. [Product and system impact](product-system.md) and the [delivery roadmap](roadmap.md) retain the global destination.

## Evidence and authority

- [project.md](../../evaluation-fixtures/team-invitations/project.md) is the sole supplied product, system, and CI evidence. No repository, running app, API schema, or executable harness is supplied. Current behavior and system facts below are fixture statements, not independently observed runtime behavior.
- [Decision and unknown records](decisions.md) record D-01 owner-only, D-03 account/membership eligibility and matching identity, D-04 allowed-domain enforcement, the provisional D-02 grant role, and implementation prerequisites. D-04 supersedes D-03's any-valid-domain permission. A future implementation session must inspect actual contracts and CI harness before choosing concrete routes or field names.
- Saved Markdown in `planning/` is authoritative. No tracker exists in this exercise; all [task records](tasks.md) are planning-only and unpublished.

## Frontier and dependencies

| ID | Question / record | Owner | Status | Depends on | Next action |
| --- | --- | --- | --- | --- | --- |
| [D-01](decisions.md#d-01---invitation-sender-role) | Which roles may create invitations? | Product owner / user | Confirmed: owner-only for S-01 | None | Apply to server permission and UI plan. |
| [D-03](decisions.md#d-03---target-account-eligibility-and-acceptance-identity) | Which target accounts and accepting identities are allowed? | Product owner / user | Confirmed for account/membership eligibility and matching identity; domain portion superseded | None | Apply together with D-04. |
| [D-04](decisions.md#d-04---team-allowed-domain-policy) | Which domain permits creation and acceptance? | Product owner / user | Confirmed: exact normalized match to current configured team domain | None | Apply to new and unused existing invitations. |
| [D-02](decisions.md#d-02---member-role-target-for-s-01) | Which role does acceptance grant? | Product owner / user | Proposed: member-only; confirmation pending | None | Confirm member-only or choose another grant policy; reconcile affected records. |
| [U-01](decisions.md#u-01---actual-contract-and-repository) | What are the actual API, auth, email identity, and migration conventions? | Future implementation owner | Prerequisite | Access to product repository | Inspect owning code/docs before final route and schema selection. |
| [U-02](decisions.md#u-02---validation-access) | Is the documented CI fixture and journey runner available? | Future implementation owner | Prerequisite | Runtime and CI access | Confirm fixtures and run checks only after implementation authorization. |

The active decision frontier is D-02. U-01 and U-02 require the actual product repository and runtime, which are unavailable in this exercise. Not yet specified: later invitation management, cancellation, and support migration. Revisit when the first slice is accepted or the product owner expands scope.

## Next deliverable

[S-01: Create and accept a member invitation](slices/S-01.md) is the next useful vertical slice. It joins the web journey, authenticated API, PostgreSQL persistence, current team-domain policy, and integration evidence. Owner-only creation and exact allowed-domain matching are confirmed; the member-role grant remains provisional pending D-02. [Task records](tasks.md) and [planning review](review.md) complete the handoff.

## Coverage dispositions

| Area | Disposition | Evidence / reason and action |
| --- | --- | --- |
| Product, UX, content | Detail now | Owner create/share and target accept, missing-domain, mismatched-domain, expired, wrong-account, and recovery journeys in [S-01](slices/S-01.md); reuse design system per project.md. Domain configuration UI is out of scope; grant role awaits D-02. |
| Domain, backend, contracts | Detail now | Server-enforced permission, exact normalized domain comparison at creation and acceptance, target match, one-use state, and failure outcomes in [S-01](slices/S-01.md). Exact routes and normalization contract wait for U-01. |
| Data, persistence, migration | Detail now | Existing team's current allowed-domain setting is authoritative; new invitation record, unique membership, atomic acceptance, expiration, and forward recovery are in [S-01](slices/S-01.md). Setting location and migration convention wait for U-01. |
| Security, privacy | Detail now | Bearer token handling, current domain-policy recheck for unused older links, account email match, nonmember board isolation, and enumeration controls in [S-01](slices/S-01.md). |
| Performance, reliability, integrations | Detail now for restart, retries, and concurrent acceptance; deferred for scale targets | PostgreSQL is source of truth; no external provider. Capacity/latency targets have no evidence and do not choose this slice's architecture. Revisit on measured volume. |
| Infrastructure, delivery, operation | Detail now for migration/CI boundary; deferred for production release | Documented CI methods are planned in [S-01](slices/S-01.md). Deployment is out of authority and scope. Revisit with a release request. |
| Research and feasibility | Detail now | U-01 and U-02 bound missing repository/runtime evidence. No prototype or product execution is authorized. |
| Coordination, risks, traceability | Detail now | D-01/D-03/D-04, open D-02, U-01/U-02, criteria, tasks, and [review](review.md) give ownership and dependency order. One implementation writer per affected area. |
| Specialized domains | Not applicable | Supplied feature contains none of the listed specialized domains. |

## Status and next permitted action

**NEEDS DECISION** at [review revision 2026-10-11, domain-policy update](review.md): D-02 can change the membership grant and acceptance criteria. D-01, the surviving parts of D-03, and D-04 are reconciled. U-01 and U-02 are unavailable implementation prerequisites that also prevent a READY TO BUILD gate. The next permitted planning action is to confirm D-02 and, when the product repository is provided under separate implementation authority, verify U-01/U-02 before finalizing executable contracts. Product implementation, product test execution, and issue publication are not authorized here.
