![A thoughtful cartographer and a luminous agent drawing branching routes on a parchment map.](docs/assets/cartographer-cover.webp)

# Dev Planning

**Plan the route before you build.**

Agent skills for planning full-stack products before implementation.

The goal is to help a person or agent decide **which planning areas to cover, which planning modules are needed within each area, in what order, and at what depth**. Start from a product idea or an existing application, and leave the next vertical slice sufficiently defined for an implementation agent to build and verify it.

**Status: 0.2.0 draft.** The repository currently contains one coordinating skill and five supporting references. Structure and links are validated. The skill adds selective decision ownership, persistent session maps, and requirement-to-verification traceability. Behavioral evidence and its limits are recorded in the [evaluation guide](docs/evaluation.md). This is an evolving method, and contributions should bring concrete scenarios and evidence.

## A map of decisions

Planning connects questions, alternatives, evidence, and decisions. Keep the chosen route, its reason, and the next uncertainty visible.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/decision-map.svg">
  <img src="docs/assets/decision-map.gif" width="900" alt="A conceptual decision map: define the flow before sketching a screen, retain the reason, and leave the access-rules question open.">
</picture>

[View the static map](docs/assets/decision-map.svg).

This schematic illustrates the visual direction. The skill now defines a persistent map and derived visual review contract. A live HTML map generator with node-linked editing is not implemented in the published skill.

## Install

With Node.js, npm/npx, and Git available, run this from your project directory:

```sh
npx skills@latest add Sergio-CVM00/dev-planning --skill dev-planning
```

The installer lets you choose your agent and installation method. It supports Codex, Claude Code, OpenCode, Cursor, and other [supported agents](https://github.com/vercel-labs/skills#supported-agents).

Add `--global` to make the skill available across projects:

```sh
npx skills@latest add Sergio-CVM00/dev-planning --skill dev-planning --global
```

For an explicit agent, add `--agent codex`, `--agent claude-code`, or another supported identifier. See the [installer options](https://github.com/vercel-labs/skills#options).

Alternatively, copy the entire [`skills/dev-planning`](skills/dev-planning) directory into your agent's configured skills directory. Keep `SKILL.md`, `references/`, and the included `LICENSE` together.

CLI discovery and project-scoped file installation were verified for Codex, Claude Code, and OpenCode. That installation check does not prove activation in every harness; see the [installation verification](docs/installation.md) and the separate [behavioral evaluation](docs/evaluation.md).

## Try it

Start with a request such as:

> Use dev-planning to plan a new web application for booking appointments. Identify unresolved product decisions, map the system, choose the first slice, and prepare its acceptance criteria and implementation tasks.

Or:

> Use dev-planning to add team invitations to this existing application. Inspect the current roles, data model, and delivery process. Inherit valid decisions and plan the affected slice.

Provide the request and available project evidence. The skill distinguishes a discussion, a saved plan, tracker publication, and authorized implementation. A ready plan does not grant permission to build, merge, or deploy.

## Planning with selective autonomy

The agent investigates accessible facts and settles delegated, reversible internal details within agreed constraints. The decision-maker retains choices affecting scope, user-visible behavior, UX, access policy, privacy, material cost, or difficult-to-reverse commitments. Proposals and unverified assumptions never silently become confirmed requirements.

For saved or multi-session work, maintain a readable index of authoritative decisions, dependencies, unresolved questions, and the next slice. Resume from those records; a changed decision makes dependent outputs and the previous readiness review stale until reconciled. Preserve the project's canonical format, including JSON where required, and derive visual views instead of duplicating editable truth.

The output connects requirements and decisions to scenarios, slices, acceptance criteria, issues, and planned verification. Planning tickets retain a draft/planned/backlog status. READY TO BUILD describes technical readiness and never starts implementation or adds an execution-ready label by itself.

See [decision policy](skills/dev-planning/references/decision-policy.md) and [planning sessions](skills/dev-planning/references/planning-sessions.md). These adapt Matt Pocock's planning patterns without requiring his full skill package, a particular tracker, or a graph runtime.

## Four separate decisions

| Concept | Question | Example |
| --- | --- | --- |
| Planning level | Which decision depends on which earlier decision? | Product frame before selecting a delivery slice |
| Planning area | Which aspects of the product or system could affect this work? | UX, data, security, operations |
| Planning module | Which reusable procedure resolves an applicable decision? | Define permissions, design an API contract, plan a migration |
| Planning depth | How much evidence and detail does this decision need? | Lite, Standard, Deep |

A **planning module** is a procedure with an activation rule, inputs, output, and completion condition. An **application module** is a domain or technical component of the product. Keep those meanings distinct when contributing.

There is no fixed module count per area. Select the smallest set of procedures that covers the applicable decisions and risks. Reuse current evidence; detail uncertain or expensive-to-reverse decisions; defer future decisions with a reason and a trigger for revisiting them.

The current skill routes by levels and coverage areas. A named module catalog with explicit dependencies is a proposed next step, tracked in [issue #2](https://github.com/Sergio-CVM00/dev-planning/issues/2).

## Planning sequence

```mermaid
flowchart TD
    A["Idea / request"] --> T["0. Context / triage: evidence, authority, depth"]
    T --> P["1. Product frame: what and why"]
    P --> S["2. System map: how the pieces fit"]
    S --> D["3. Delivery strategy: order and dependencies"]
    D --> N["Choose next vertical slice"]
    N --> F["4. Slice definition: behavior, interfaces, data"]
    F --> C["5. Acceptance / done: observable proof"]
    C --> I["6. Implementation plan: ordered tasks"]
    I --> G{"7. Ready to build?"}
    G -- "Gap" --> R["Resolve at the responsible level"]
    R --> G
    G -- "Ready and authorized" --> B["Implementation handoff"]
    B --> E["Verified results and feedback"]
    E --> N
```

The sequence expresses dependencies, not a requirement to write a full PRD for every change. Refine adjacent levels together when they expose a conflict.

| Starting point | Approach |
| --- | --- |
| New product | Establish product frame, system map, and delivery strategy; detail the first slice |
| Existing feature | Check the impact on global decisions, inherit valid evidence, and detail the affected slice |
| Bug | Establish observed and expected behavior, reproduce when possible, and plan a bounded correction |
| Migration | Define current and target states, compatibility, transition, validation, and recovery |

Read the [skill entrypoint](skills/dev-planning/SKILL.md) for the workflow, [planning levels](skills/dev-planning/references/planning-levels.md) for level details and change entry points, and [planning outputs](skills/dev-planning/references/planning-outputs.md) when preparing a handoff.

## Coverage and depth

Review [full-stack coverage](skills/dev-planning/references/full-stack-coverage.md) during triage. It covers product/UX/content, domain/backend/contracts, data/migrations, security/privacy, performance/reliability/integrations, infrastructure/delivery/operations, research/feasibility, and coordination/traceability. Add domain-specific requirements when they affect the decision.

Give each area a disposition: **Detail now**, **Inherited**, **Deferred**, or **Not applicable**, with evidence or rationale. Areas may require work at several planning levels.

Choose depth from ambiguity, impact, reversibility, and coordination:

- **Lite:** bounded work with known behavior and reusable decisions.
- **Standard:** a meaningful feature or change that needs affected boundaries, contracts, acceptance, and delivery specified.
- **Deep:** uncertain feasibility, global choices, significant coordination, or consequential transitions.

A small change can require Deep planning. A new product can reuse known technology while still needing its own product frame.

The output is a plan for the next slice with evidence, acceptance criteria, ordered tasks, open decisions, and one status: **READY TO BUILD**, **NEEDS DECISION**, or **BLOCKED**. Keep implementation authority separate.

## Contribute

Start with a scenario that the current workflow handles poorly. Propose a focused correction or a module whose trigger, dependencies, output, and completion condition are clear.

See [CONTRIBUTING.md](CONTRIBUTING.md), the [evaluation guide](docs/evaluation.md), and the [open issues](https://github.com/Sergio-CVM00/dev-planning/issues). Contributions can improve the method, clarify routing, document a case, or add a module. A separate skill is useful when it can be invoked independently; conditional detail can remain a reference.

Run the repository checks with Python 3.11 or newer:

```sh
python3 scripts/validate.py
```

These checks validate the repository's limited metadata format and local Markdown file links. They do not evaluate planning quality or prove that an agent follows the method.

## License and authoring influence

[MIT](LICENSE).

The instructions were written with the principles in Matt Pocock's [writing-for-agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents): progressive disclosure, precise context pointers, and checkable completion conditions.
