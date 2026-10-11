# Planning sessions

Use for saved plans, multi-session work, or a request whose unresolved decisions cannot fit a useful single session. Lite work can use one compact record; do not require a tracker map for every question.

## Authoritative records and a readable map

Use the project's configured repository or tracker. Preserve existing canonical formats: when JSON is canonical, update JSON and derive Markdown/visual views; when the tracker owns a record, link to it. Do not introduce two editable copies of the same decision or requirement. This skill defines information and reconciliation, not a new persistence engine.

The **map** is an index. It records:

- Destination, outcome, scope IN/OUT, constraints, and permitted actions.
- Links to authoritative product/system decisions and the selected next slice.
- Decision/question IDs and titles, owners, dependencies, status, and links to full records.
- The **frontier**: precise unresolved questions whose prerequisites are settled; unresolved prerequisites keep downstream questions blocked.
- **Not yet specified**: in-scope areas that cannot yet be phrased as precise questions. Turn them into records when prerequisites clarify them.
- Coverage dispositions and links to the spec, acceptance, issue records, and plan-review result.
- Latest reviewed revision, open blockers, publication status, and next permitted action.

Show names with links in human views rather than bare IDs. Prefer the existing tracker UI or an allowed visual review artifact when it makes the map easier to assess. A visual view is derived from the records and states its source revision; it cannot become a second editable truth. This workflow does not require a particular GUI, graph runtime, or another skill package.

Each precise question has a bounded resolution action: **research** for discoverable facts, **decision** for a choice, or **prerequisite** for unavailable evidence/access. Apply [Decision policy](decision-policy.md) to decide whether its owner is the agent or human. A research result supplies sources, uncertainty, alternatives when relevant, and the question it unblocks. A prototype or operational prerequisite needs its own scope and authority; planning does not implicitly authorize product code or external effects.

## Save and resume

1. Read the destination, authority, current map, and the relevant linked records. Do not reconstruct settled choices from a chat summary when the owning record exists.
2. Reconcile source revisions, decision status, dependencies, and existing tracker IDs. Locate the previously published record before retrying an uncertain write; do not create a duplicate because a response was lost.
3. Select the next unblocked question or slice. Research accessible facts and continue independent work; consult only the decisions that need their decision-maker. Do not reopen confirmed choices without new evidence or an explicit request.
4. Save the resolution in its authoritative record with source, owner, rationale, consequences, and revision. Update the map's pointer and newly exposed questions. Promote not-yet-specifiable areas only when their questions are precise.
5. Before ending, save the next permitted action, open decisions, and review status so a fresh context can continue from artifacts alone.

Respect another session's ownership. Use the tracker's claim/version facilities or the project's single-writer convention. Read the latest records before updating a shared map and reconcile concurrent changes. Plain Markdown or a prompt does not provide atomic writes, exactly-once publication, or safe automatic parallel execution. A suspected write conflict blocks that mutation until reconciled; independent planning can continue.

## Change and invalidate

Keep stable IDs across revisions. A changed requirement, source, decision, or constraint requires an impact check through:

`decision/requirement -> scenario -> slice -> criterion -> issue -> planned verification`

Record what changed and supersede the old decision; do not erase its rationale. Mark dependent outputs and the prior readiness review **stale** until updated. Recheck relevant coverage and inherited evidence. Unaffected work may be reused with an impact check. For published issues, inspect the current records and authorized tracker workflow before updating them.

A **needs-review** plan can hold provisional material. A **current** review states its source revision, checks, findings, and residual uncertainty. A **stale** review cannot support READY TO BUILD. These are planning-review states, not product-test results. Question and deliverable dependencies must be acyclic; a dependency cycle requires revising the boundary or sequencing before readiness.

## End the planning session

Stop when the next slice passes the readiness gate, or when all independent work is done and a named decision/prerequisite prevents progress. The global map may still contain future uncertainty with owners and revisit triggers. Do not force every future branch to resolve before a bounded slice is ready.

Return the planning status, the authoritative artifact links, review revision/findings, pending publication or prerequisites, and the next permitted action. Keep execution authority explicit and separate.

## Pattern sources

The index/frontier and planning-only boundary draw on Matt Pocock's [Wayfinder](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/wayfinder/SKILL.md). Specification and ticket boundaries draw on [To Spec](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md) and [To Tickets](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md). This adaptation uses selective decision ownership and preserves project-specific storage and authority; those upstream skills are not runtime dependencies.
