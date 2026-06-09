from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors = []
    skill_files = sorted((ROOT / "plugins").glob("*/skills/**/SKILL.md"))
    if not skill_files:
        errors.append("no SKILL.md files found")

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"missing YAML frontmatter: {path}")
            continue
        for key in ("name", "description"):
            if not frontmatter.get(key):
                errors.append(f"missing {key} in frontmatter: {path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {len(skill_files)} skill files have required metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
