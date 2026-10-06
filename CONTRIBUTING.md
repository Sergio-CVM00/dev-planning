# Contributing

Help make the planning method useful for real full-stack work. Begin with a concrete starting point: a new product, a feature in an existing application, a bug, or a migration.

## Propose a change

1. Describe the request and available evidence. Use synthetic or shareable project material.
2. Show the decision or output the current workflow fails to produce. Explain the consequence for implementation.
3. Propose the smallest change that resolves it. Identify the affected planning level, coverage area, and depth.
4. Check whether existing instructions can cover the case before adding another procedure.
5. Explain how another contributor can evaluate the result. Record desk review and actual agent execution separately.

Open a scenario issue when the solution is unclear, or a module proposal when its boundary is already understood. Small corrections can go directly to a pull request.

## Define a planning module

A module is a reusable planning procedure. An application component is part of the product being planned. For a proposed procedure, specify:

| Field | Required information |
| --- | --- |
| Purpose | The decision the procedure helps resolve |
| Activation | Evidence or request conditions that require it |
| Inputs | Sources and earlier decisions it needs |
| Steps | The order needed to reach the decision |
| Output | The artifact or decision it produces, and its authoritative home |
| Completion | Observable conditions for finishing; behavior when evidence is unavailable |
| Dependencies | Which procedures must precede it and what can happen independently |
| Depth | What changes between Lite, Standard, and Deep |
| Reuse | When existing decisions can be inherited and what invalidates them |
| Evaluation | A realistic scenario and observable outcome |

Keep a procedure in a reference when it only supplies conditional detail to the coordinating skill. Propose a separate skill when it has a distinct activation boundary and can complete useful work independently. Preserve one authoritative definition and link to it.

Module count is a consequence of the applicable decisions, not a target. A contribution should improve coverage or clarity without making every request run every procedure.

## Prepare a pull request

1. Fork the repository and create a branch.
2. Make the focused change. Keep repository documentation and skill instructions in English.
3. Run `python3 scripts/validate.py` with Python 3.11 or newer.
4. Review affected entry points using the [evaluation guide](docs/evaluation.md). When executing an agent evaluation, retain the request, runtime/model, revision, output, and limits in a shareable record.
5. Submit a PR explaining the behavior changed, its reason, and the evidence. Link the relevant issue.

Keep private project context, credentials, personal paths, and transcripts out of contributions. Provide the minimum sanitized evidence needed to assess the result. Attribute third-party material and check license compatibility before copying it.

The automated validator checks file links and a narrow frontmatter convention. It does not replace review of semantics, runtime behavior, permissions, or planning quality.
