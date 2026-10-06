#!/usr/bin/env python3
"""Check the repository's simple skill metadata and local Markdown file links.

This intentionally supports only single-line, unquoted name and description
fields, as used by this repository. It is not a general YAML or Markdown parser.
External URLs and in-page fragments are not validated.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills/*/SKILL.md files found")
    for skill in skills:
        content = skill.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
        if not frontmatter:
            errors.append(f"{skill.relative_to(root)}: missing frontmatter")
            continue
        for field in ("name", "description"):
            values = re.findall(rf"^{field}: ([^\n]+)$", frontmatter.group(1), re.MULTILINE)
            if len(values) != 1 or not values[0].strip():
                errors.append(f"{skill.relative_to(root)}: expected one nonempty {field}")
                continue
            value = values[0].strip()
            if field == "name" and (value != skill.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value) or len(value) > 64):
                errors.append(f"{skill.relative_to(root)}: name must match its lowercase folder name")
            if value.startswith(("'", '"')) or value in ("|", ">"):
                errors.append(f"{skill.relative_to(root)}: {field} must use the supported single-line unquoted format")

    for document in sorted(root.rglob("*.md")):
        if ".git" in document.relative_to(root).parts:
            continue
        content = document.read_text(encoding="utf-8")
        # Fenced examples are not live links. Inline code is kept: link labels
        # may legitimately contain backticks.
        content = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", content, flags=re.MULTILINE | re.DOTALL)
        for match in re.finditer(r"\[[^\]\n]*\]\(([^)\n]+)\)", content):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = (document.parent / unquote(parts.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"{document.relative_to(root)}: link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{document.relative_to(root)}: missing local link: {target}")
    return errors


if __name__ == "__main__":
    problems = validate(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("Validated skill metadata and local Markdown file links")
