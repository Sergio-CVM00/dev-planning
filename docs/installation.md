# Installation verification

Date: 2026-10-08. Skills CLI: 1.7.1. Source: public `Sergio-CVM00/dev-planning`, main revision `84a5029`. This is a packaging check, not an agent-behavior evaluation.

## Commands exercised

```sh
npx --yes skills@latest add Sergio-CVM00/dev-planning --list
npx --yes skills@latest add Sergio-CVM00/dev-planning --skill dev-planning --agent codex claude-code opencode --yes --copy
```

The commands ran in a disposable Linux project with an isolated npm cache and telemetry disabled. No global agent skill directories were installed or changed. Temporary project and cache files were removed after the check.

## Observed result

- Discovery found the `dev-planning` skill.
- Installation completed successfully for all three requested agent targets.
- Codex and OpenCode shared the project `.agents/skills/dev-planning` destination; Claude Code used `.claude/skills/dev-planning`.
- Installed `SKILL.md`, `LICENSE`, and all three reference files matched the source file hashes.

## Limits

The interactive selector, symlink mode, global installation, other agent targets, runtime skill activation, and planning behavior were not exercised. The README's generic interactive command follows the [official CLI options](https://github.com/vercel-labs/skills#options); the automated check exercised the explicit copy-mode variant.
