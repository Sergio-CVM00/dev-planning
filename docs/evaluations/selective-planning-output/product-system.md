# Product frame and system impact

Source and revision: [project.md](../../evaluation-fixtures/team-invitations/project.md), supplied 2026-10-11. All claims of current behavior below come from that fixture; no running product or code is available for corroboration.

## Product frame

- Actors: a signed-in team owner who may create for the team's configured allowed domain, a member or nonmember who may not create, a signed-in account matching an eligible target email that may accept, and an unauthenticated or different account that may not accept.
- Current need: owners request membership changes through support. The feature lets an authorized sender share a link themselves and lets the target account join without support. Frequency, support cost, and adoption targets are unknown and are not needed to choose the first bounded slice.
- Observable outcome: a current owner can create a link for a valid email whose normalized domain exactly matches the team's configured allowed domain, including one without an account or already in the team. Missing configuration or another domain prevents creation. A matching signed-in account can accept after a reload or restart only if the invitation target still matches the team's current allowed domain; at most one membership results, while nonmembers never see board data. Success evidence is planned API integration and web journey results, not a numerical adoption target.
- Scope and constraints: see [index](index.md). Allowed-domain configuration itself is outside this feature. A new invitation grants the existing member role only in the proposed slice; owner transfer and role selection are outside its boundary. This is a scoped proposal, not a confirmed product policy.

## Existing system and affected path

```text
Signed-in web client -> authenticated HTTP interface -> server authorization/domain handling
                                                       -> PostgreSQL users, teams, memberships
                                                       -> proposed invitations table
```

The signed-in client has a selected team. The server receives identity and selected team but must derive authorization from persisted membership and enforce it server-side. Membership uniqueness is `(team_id, user_id)`. Invitation links are externally shareable, so token possession enters through a new trust boundary. The server must still require signed-in identity and target-email match. PostgreSQL owns invitation lifecycle and membership state so both survive process restart. There is no email provider or background job in this slice.

The creation boundary checks the sender's current owner role, validates target email syntax without requiring a target account or checking target membership, then compares the target's normalized domain exactly with the team's authoritative configured allowed domain. A missing domain or mismatch prevents insertion. The acceptance boundary touches authentication, token lookup, authoritative account-email comparison, a fresh current team-domain comparison, atomic consumption, and membership insert. The fresh comparison rejects unused invitations issued under another domain, including links created before the policy change. Existing board reads must keep their server-side membership check; accepting a link cannot reveal boards before membership commit. The client must treat link and error responses as sensitive and avoid putting board data in invitation preview states.

## System proposal and consequences

Use an opaque high-entropy random token in the shared link, store only its cryptographic digest, and persist team ID, canonical target email, creator ID, creation/expiry timestamps, consumption timestamp, and consuming user ID. The invitation table is the source of truth for the link; current team configuration is the source of truth for allowed-domain eligibility. Do not rely on a domain copied into an invitation to authorize acceptance. The token must not appear in logs, analytics, or outbound referrer data. Exact field names, URL shape, response status codes, allowed-domain storage and normalization, and migration tooling follow the existing repository after [U-01](decisions.md#u-01---actual-contract-and-repository) is resolved. No background expiry job is needed: compare against server time at read and acceptance; retain expired rows until a later retention policy is chosen.

Acceptance should run in one database transaction that locks the invitation row, confirms unconsumed and unexpired state, compares the current signed-in account email with the target under existing account semantics, and checks the target's normalized domain against current team configuration before inserting one membership and marking the invitation consumed. A missing or different current allowed domain rejects acceptance without consumption or membership; recheck under a consistency boundary that cannot race a domain change into an unauthorized grant. The exact locking/version method depends on U-01. Member-role insertion is provisional until [D-02](decisions.md#d-02---member-role-target-for-s-01) is confirmed. A matching account that already belongs to the team gets an already-member terminal outcome without a duplicate or role change only after domain eligibility passes; creation was still allowed for eligible addresses. Competing accepts must yield exactly one successful consumption; the loser receives a stable used/ineligible result. A failed transaction leaves the invitation usable if still within 24 hours. The code path must be safe to retry after a lost HTTP response.

This uses the existing HTTP/PostgreSQL architecture and avoids a new queue, provider, or orchestration framework. A relational transaction is necessary because consumption and membership are one domain event. If the actual repository has different identity or transaction semantics, U-01 may require a revised plan before building.
