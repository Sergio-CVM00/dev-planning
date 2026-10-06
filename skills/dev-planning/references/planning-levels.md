# Planning levels

Read the sections for levels being created or changed. These checks deepen the core workflow; they do not require a separate document for each topic.

## Product Frame

### Inputs

Use the request, existing product brief, user evidence, current workflows, and known business or operational constraints. Mark evidence unavailable when access is missing.

### Decisions

- **Problem:** affected actors, current workaround, frequency, and consequence when known.
- **Outcome:** the observable improvement and evidence of success. Define numerical targets only when needed for a decision and supported by the owner or a stated hypothesis.
- **Boundary:** initial scope, non-goals, and conditions that would expand scope.
- **Constraints:** time, budget, platforms, data sensitivity, legal obligations, and operating model when they affect viability.
- **Viability:** resolve product, technical, economic, or operational uncertainty that could invalidate the intended outcome.

Choose discovery work by the hypothesis it will resolve: interviews, existing evidence, a flow prototype, or a bounded technical investigation. Record the question and exit criterion before starting.

### Output

Use a compact product brief for one owner and a bounded outcome. Use a PRD when several stakeholders, epics, or acceptance obligations need a shared specification. For a feature, record the change to the existing frame and link its authoritative source.

### Closure

Each material hypothesis has evidence, a bounded resolution action, or a documented reason it can wait without invalidating the next slice. Material missing inputs remain visible in readiness.

## System Map

### Inputs

Use architecture and domain documents, actual repository boundaries, representative runtime flows, integration contracts, and current data or operational constraints. Prefer owning sources over summaries when they disagree.

### Decisions

- **Topology:** actors, clients, services, persistence, background processes, external systems, and environments that participate in critical flows.
- **Domain:** responsibilities, invariants, ownership, and boundaries between modules.
- **Data:** sources of truth, lifecycle, sensitivity, consistency, and transaction boundaries.
- **Trust:** authentication, authorization, tenant boundaries, and external inputs.
- **Quality:** objectives that influence architecture, capacity, availability, accessibility, or operating costs.
- **Architecture:** the simplest structure satisfying these constraints; dependencies on stack, hosting, and provider capabilities.
- **Transition:** coexistence, compatibility, migration, and recovery requirements for an existing system.

For a significant choice, compare viable alternatives against explicit criteria. Record the selected option, reason, consequences, and when to revisit it. Create an ADR for a consequential or expensive-to-reverse choice, rather than for every library or implementation detail.

When research cannot settle feasibility, define a spike with a question, allowed environment, time bound, expected evidence, and disposition of experimental code. A prototype may validate interaction; a technical spike may validate a contract or operational assumption. Label their evidence limits.

### Output

Create or update a system diagram and responsibility map, with the constraints and decisions needed by the next slice. For a feature, capture the impact and affected paths in the existing map.

### Closure

Each affected boundary has an owner or responsibility, necessary global contracts are understood, and choices that can invalidate the slice are resolved or explicitly gate readiness.

## Delivery Strategy

### Inputs

Use the product frame, system map, risk register, available resources, and dependencies. Planning depth is an input to how much detail to produce, not a requirement to fill a fixed template.

### Decisions

- Prioritize a result for user value, learning value, risk reduction, or a necessary prerequisite.
- Define vertical slices that cross the technical layers needed for their outcome. Some tasks may be infrastructure or horizontal prerequisites; name the slice they enable and how they will be verified.
- In a new product, use a walking skeleton to expose integration and delivery risks early. State which user capabilities it intentionally lacks.
- Map ordering constraints, shared resources, and points of integration.
- For transitions, define coexistence, release sequencing, rollback or forward-recovery conditions, and verification at each stage.
- Assign ownership and identify external commitments, access, quotas, or data availability that can delay a slice.

### Output

A roadmap of outcomes and dependencies, detailed for the next slice and coarse for later ones. Add release or migration plans when the outcome requires them. Estimates should expose their assumptions and confidence when schedules or coordination need them.

### Closure

The next slice has a clear result, feasible prerequisites and verification, and a reason to precede the alternatives. Future detail is deferred with a trigger, not silently treated as resolved.

## Feature and change entry points

- **Ordinary feature:** check whether actors, objectives, boundaries, dependencies, or quality constraints change. Inherit supported decisions and update affected areas.
- **Bug:** use a reproduction or the strongest available observation as evidence of current behavior. State the expected behavior and a regression check. Record any reproduction limitation.
- **Migration:** evaluate old and new behavior, intermediate states, compatibility, data integrity, operational continuity, and recovery. A reversible code change can still cause an irreversible data transition.
- **Unclear request:** resolve the outcome and boundary before committing to a technical approach. Offer concrete alternatives when inspection cannot answer the decision.
