# Decision policy

Use this policy when deciding whether to inspect evidence, choose a detail, or ask the human. Project instructions, standing preferences, and explicit delegation take precedence. Planning authority never supplies missing authority for external actions.

## Separate facts from choices

- **Fact:** a claim supported by a named source, with revision/date when change matters. Investigate accessible code, docs, tests, and configuration before asking the user. Missing or contradictory sources remain unknown; plausible recall is not evidence.
- **Proposal:** a recommended choice with alternatives, reasons, and consequences. It has not been accepted by its decision-maker.
- **Confirmed decision:** an explicit user choice or applicable standing decision. Cite its source and preserve its scope.
- **Delegated decision:** a choice the agent may make within the user's or project's delegated constraints. Record the choice, rationale, and revisit trigger; do not attribute it to the user.
- **Assumption/unknown:** an unverified premise or unanswered question with consequence, owner, and resolution action. An assumption cannot silently become a requirement.

## What the agent may settle

Within the authorized planning work, choose low-impact, reversible internal details that preserve the requested behavior and existing contracts. Examples include grouping a plan's sections, reusing an established testing interface, or ordering independent investigations. Record details only when another session or implementer needs them.

A choice is not delegated merely because code can be reverted. User-visible behavior, data loss, contracts, recurring cost, and privacy can have lasting consequences. Honor explicit preferences even when an alternative looks cheaper or simpler.

## When to consult

Ask the identified decision-maker when the choice changes scope, priority, user-visible behavior or UX, access policy, privacy, material cost, external commitments, or a costly-to-reverse architecture/transition. Also ask when sources conflict in a way that changes correctness or authority. Reuse a current standing decision instead of reopening it.

Present the decision, the minimum relevant evidence, viable options, a recommended answer, and the consequence of waiting. Group independent questions in a small round; do not ask a dependent question before its prerequisite is settled. A recommendation is not consent. Silence, elapsed time, or a planned label is not an answer.

Continue investigations and specifications that do not depend on the answer. Keep dependent outcomes provisional and return NEEDS DECISION when the missing choice can invalidate the next slice. An unavailable prerequisite returns BLOCKED, not an invented decision. Stop investigating when adequate evidence resolves the bounded question or no independent work remains.

## Plan review and authority

Review whether every applicable obligation has observable acceptance and a feasible verification path. Consider normal behavior, permissions, persistence, errors, recovery, accessibility, operations, and domain-specific constraints where affected; the coverage checklist decides applicability.

Planning review proves only that the plan is sufficiently specified for its next permitted action. Tests, screenshots, CI checks, and product verification that have not run remain **planned**. Describe the intended environment, fixtures, and evidence; do not claim those results passed.

Save, publish, implement, merge, and deploy are distinct actions. Resolve each from the user's request and project instructions. A READY TO BUILD status expresses technical readiness. It neither starts implementation nor adds an execution-ready tracker label. Where the tracker has no planning status, use its draft/backlog convention or an explicit planning-only body; do not invent a scheduler integration.
