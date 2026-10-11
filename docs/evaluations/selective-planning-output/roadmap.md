# Delivery strategy

Source: [project.md](../../evaluation-fixtures/team-invitations/project.md), revision 2026-10-11. Existing product, so no new-product walking skeleton is required. The first useful user outcome is the full invitation loop, not a standalone database or UI milestone.

| Order | Outcome | Dependency and reason |
| --- | --- | --- |
| [S-01](slices/S-01.md) | A team owner creates an initial durable link for an eligible email in the team's configured allowed domain, including an already-member target; a matching signed-in account without membership accepts once only while current domain policy permits and the token remains eligible. The saved member-role grant awaits D-02, policy-rejected token fate awaits D-05, already-member acceptance awaits D-06, and repeat-create reject/reuse/new-token behavior awaits D-07. | First useful result and highest immediate risk: authorization, domain policy, privacy, persistence, and concurrency. D-01/D-04 and the retained D-03 rules are settled; D-02/D-05/D-06/D-07 and U-01 affect the final grant, lifecycle, and contract. |
| Later, only if requested | Invitation management such as listing, cancellation, reissue, or reminders. | Depends on evidence of how S-01 is used and a separate scope decision. Not needed for S-01 acceptance. |
| Later, separate authority | Production release and support-process transition. | Requires actual product checks, deployment authorization, operational ownership, and release plan. |

For S-01, integration order is schema/domain transaction, authenticated API, web flow, then end-to-end evidence, with one writer for shared contracts. The [task records](tasks.md) give dependencies and review points. Planning stops at the [review gate](review.md); the project must establish its registered execution host and delivery owner through U-03, and a separately authorized future implementation team must inspect the repository and CI harness before executing.
