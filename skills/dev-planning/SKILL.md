---
name: dev-planning
description: Plan full-stack work before implementation. Use for a product idea, a new feature in an existing system, a bug fix, or a migration that needs scope, design, acceptance criteria, and an implementation plan.
---

# Dev Planning

Turn a request into an evidence-backed plan for the next vertical slice. Define the product and system enough to guide delivery; specify the next slice enough to build and verify it.

## 0. Establish the starting point

1. Read the request, applicable project instructions, and available product or repository evidence. Inspect the current behavior for a change; reproduce a reported bug when access permits.
2. Identify the output destination and permitted actions: discussion, saved plan, tracker publication, or separately authorized implementation. Resolve the owning repository and execution environment through the project's own registry or instructions.
3. Record facts with sources, assumptions, inherited decisions, and unknowns. Ask about missing information only when it changes scope, correctness, risk, or authority. Continue independent planning while an answer is pending.
4. Choose planning depth from ambiguity, impact, reversibility, and coordination:
   - **Lite:** known behavior and bounded impact; reuse valid system decisions and produce a compact slice plan.
   - **Standard:** a feature or meaningful change; inspect affected boundaries and specify the slice, contracts, acceptance, and delivery.
   - **Deep:** uncertain viability, global decisions, significant coordination, or high-consequence transition; resolve alternatives and critical unknowns before committing to the slice.

Read [Full-stack coverage](references/full-stack-coverage.md) during triage. Evaluate every area once; expand the applicable areas at the level where they affect a decision. A short change can require Deep planning. A new product requires a product frame, system map, and delivery strategy even when its technology is familiar.

**Complete when:** the request type, evidence gaps, authority, initial depth, and coverage dispositions are explicit.

## Work through the levels

Use this sequence. Refine neighboring steps together when behavior, design, and acceptance expose a conflict.

```text
IDEA / REQUEST
  -> 0. Context / Triage
  -> 1. Product Frame
  -> 2. System Map
  -> 3. Delivery Strategy
  -> Next slice
       -> 4. Slice Definition
       -> 5. Acceptance / Done
       -> 6. Implementation Plan
       -> 7. Ready to Build?
            No: return to the level responsible for the gap
            Yes: hand off the plan for authorized implementation

Implementation evidence and feedback
  -> update affected decisions -> choose the next slice
```

For a **new product**, establish levels 1-3 and detail the first slice. For an **existing product**, inspect levels 1-3, inherit decisions with current evidence, and update the affected parts before detailing the change. An inherited level still receives an impact check.

Read [Planning levels](references/planning-levels.md) when creating or changing product framing, system design, or the delivery roadmap. For a bug, migration, or unclear request, also read its **Feature and change entry points** section, including when the global levels are inherited.

## 1. Product Frame

Define the problem, actors, desired outcome, success evidence, scope IN/OUT, and constraints that affect the choice. Separate observed needs from unvalidated hypotheses. For an existing product, express the feature's contribution and any change to the frame.

**Complete when:** the target outcome is observable, the actors and scope are explicit, and hypotheses that could invalidate the selected direction have a resolution action.

## 2. System Map

Map domain responsibilities, critical flows, external dependencies, data ownership, trust boundaries, and high-level architecture. Inspect affected client, server, persistence, and integration paths. Resolve expensive-to-reverse choices; record alternatives and consequences when a decision needs an ADR.

**Complete when:** every component or boundary affected by the proposed slice has an identified responsibility, and unresolved global choices that could invalidate it are identified.

## 3. Delivery Strategy

Order vertical outcomes by value, risk, and dependencies. For a new system, define a **walking skeleton**: the smallest executable path through essential components and the delivery environment. Distinguish this technical integration milestone from the first useful user outcome.

Choose one next slice with an observable result and a feasible validation path. Detail later slices only enough to expose sequencing constraints.

**Complete when:** the next slice, its prerequisites, its place in the roadmap, and the reason for its priority are explicit.

## 4. Slice Definition

Specify the slice's objective, scope, user or system flow, domain rules, interfaces, data changes, and contracts. Define relevant states, permissions, failures, edge cases, and recovery. Apply the coverage dispositions from triage to this slice and update them if its impact changes.

Use designs, wireframes, API schemas, or state models where they settle an implementation-relevant decision. For reversible internal details, state the constraint the implementation must satisfy.

**Complete when:** all in-scope scenarios have observable behavior, required interfaces and data changes are defined, and failure behavior is specified for material risks.

## 5. Acceptance / Done

Give each acceptance criterion an ID, a trigger or precondition, an observable result, and a verification method. Include significant failure cases and applicable quality targets.

Identify test boundaries, environments, fixtures, and access needed to prove the slice. Reuse the project's Definition of Done; add slice-specific evidence requirements. Distinguish implementation completion, release readiness, and deployment approval.

**Complete when:** every in-scope behavior or quality obligation has a verifiable criterion, and the validation prerequisites are available or explicitly tracked.

## 6. Implementation Plan

Read [Planning outputs](references/planning-outputs.md) when preparing the plan, task records, and handoff.

Translate the slice into ordered changes and granular issues grouped under its vertical outcome. Link each task to acceptance or a necessary prerequisite. Identify affected boundaries, dependencies, shared resources, review points, and sequencing conflicts.

Publish issues when tracker writes are authorized. Otherwise prepare tracker-ready records and label publication pending. If the project requires published issues before implementation, include publication in the readiness check. Use the project's supported tracker and delivery path.

For coordinated work, record `depends_on`, `touches`, `conflicts_with`, and `parallelizable`. Parallel work requires compatible contracts, independent ownership, and an integration point.

**Complete when:** every required change has a task or an explicitly grouped work item, dependencies are ordered, and each task has acceptance and evidence expectations.

## 7. Ready to Build

Review the complete slice against these checks:

- The outcome, actors, scope, and non-goals agree across artifacts.
- Current evidence supports inherited product and system decisions.
- In-scope scenarios, required contracts, data changes, and material failure behavior are defined.
- Applicable coverage areas have a disposition and supporting evidence or rationale.
- Acceptance criteria cover the slice and can be verified with identified environments, data, and access.
- Tasks cover the required changes; prerequisites, conflicts, and implementation order are explicit.
- Project-required planning reviews and tracker publication are complete.
- No unresolved unknown can invalidate this slice, its contracts, or its verification.

Return one planning status:

- **READY TO BUILD:** every applicable check passes with evidence.
- **NEEDS DECISION:** a product or technical choice needs an identified decision-maker. Name the options, consequence, and next action.
- **BLOCKED:** a required prerequisite or source is unavailable. State what is missing and which independent planning work is complete.

Report implementation authority separately. A ready plan is a technical handoff, not permission to implement, merge, or deploy. If the gate fails, return to the responsible level, update dependent artifacts, and rerun the affected checks.

**Complete when:** the status, evidence, open decisions, prerequisites, and next permitted action are explicit.

## Replanning

Revisit the affected level when new evidence changes scope, behavior, a contract, feasibility, or the validation strategy. Trace the consequences into the slice, criteria, and tasks. After implementation, use verified results and feedback to select the next slice.

Keep one authoritative home for each planning artifact. Link existing decisions and constraints rather than copying them into several documents. End planning when the next slice passes the gate, or when all independent planning is complete and an unresolved decision or prerequisite prevents progress. In the latter case, return NEEDS DECISION or BLOCKED with an owner and next action. Retain future uncertainty with its trigger for reconsideration.
