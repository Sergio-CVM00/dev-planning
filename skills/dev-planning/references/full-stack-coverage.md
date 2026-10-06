# Full-stack coverage

At triage, evaluate each area below. Then apply the result to the next slice. A compact plan can group inherited areas that share a valid source; retain separate dispositions for exceptions and risks.

Use these dispositions:

- **Detail now:** a decision or specification is needed for the next slice.
- **Inherited:** an existing decision remains valid after an impact check. Link its source and evidence of applicability.
- **Deferred:** relevant later; record why it cannot invalidate this slice, the owner, and the trigger for reconsideration.
- **Not applicable:** record the contextual reason.

For each area retain the disposition, evidence or reason, and any open action. A disposition describes planning work; it does not waive a required behavior or quality constraint.

## Product, UX, and content

Evaluate actors, journeys, information architecture, navigation, and business rules. For affected UI, define normal, loading, empty, error, disabled, and recovery states as relevant. Assess responsive behavior, input methods, keyboard use, and accessibility. Consider design-system reuse, content, localization, SEO, and product analytics where the product needs them.

Detail new interactions or uncertain journeys with a flow, wireframe, prototype, or explicit scenarios. Define acceptance for observable interaction behavior.

## Domain, backend, and contracts

Evaluate domain invariants, service responsibilities, APIs, events, jobs, and integrations. Define input/output schemas, validation, errors, version compatibility, and authorization where affected. For asynchronous or retryable work, settle timeouts, ordering, idempotency, deduplication, cancellation, and recovery when they affect correctness.

Detail new rules, changed responsibilities, new interfaces, or altered behavior across a boundary. Identify which layer enforces each invariant.

## Data, persistence, and migration

Evaluate schema, relationships, ownership, lifecycle, sensitivity, and sources of truth. Consider transaction boundaries, consistency, concurrent updates, access patterns, indexes, and retention where material. Define deletion, export, backup, and restoration requirements where applicable.

For a transition, plan compatibility, migration, backfill, validation of data integrity, intermediate states, and rollback or forward recovery. Distinguish reverting code from restoring data.

## Security and privacy

Evaluate identity, sessions, server-side permissions, trust boundaries, and tenant isolation. Assess sensitive data, secrets, abuse, auditing, and external exposure. Determine applicable consent, minimization, retention, and legal obligations without inventing certifications or requirements.

Detail threat scenarios for new trust boundaries, authorization changes, sensitive data, payments, or external entry points. Give each material control observable acceptance evidence.

## Performance, reliability, and integrations

Evaluate expected volume, latency, availability, capacity, and operating cost. Consider pagination, caching, limits, resource budgets, degraded modes, and recovery. For external systems, inspect required capability, authentication model, sandbox availability, quotas, timeout behavior, and failure modes.

Detail objectives and failure handling when they influence design or verification. Research current provider facts when the decision depends on them. Avoid treating a provider's marketing claim as tested runtime evidence.

## Infrastructure, delivery, and operation

Evaluate environments, hosting, network, runtime configuration, build and CI constraints, and delivery artifacts. Plan deployment compatibility, feature flags, release activation, rollback, backup, and recovery when affected. Define logs, metrics, traces, health checks, alerts, support paths, and operational ownership according to the risk.

Separate planning a production operation from executing it. Record required authorization and the verification that would precede the operation.

## Research and feasibility

Identify unknowns that could change the product direction, architecture, contract, implementation order, or evidence strategy. For each investigation, state the question, evidence source, decision criterion, and stopping condition.

Use a spike or prototype when existing evidence cannot settle the decision. Keep its scope and authority explicit. Record what was actually proven and what remains untested.

## Coordination, risks, and traceability

Evaluate decision-makers, reviewers, execution owners, repository boundaries, shared resources, and dependent work. Keep assumptions, risks, and unresolved questions with their consequence, owner, and next action.

Connect outcomes to slices, acceptance criteria, tasks, and evidence. Select an authoritative home for each artifact. Respect project-required independent review and issue creation before implementation.

## Specialized domains

Extend coverage when the product includes domain-specific obligations, such as financial transactions, clinical or health decisions, regulated records, AI evaluation, offline synchronization, real-time collaboration, hardware, or native mobile behavior. Identify the domain's controlling sources and validation requirements rather than assuming the generic list proves completeness.
