import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/waynetsa/codex-for-legal-cn"
EXPECTED = {
    "cn-commercial-legal",
    "cn-corporate-legal",
    "cn-litigation-legal",
    "cn-privacy-legal",
    "cn-ai-governance-legal",
    "cn-employment-legal",
    "cn-regulatory-legal",
    "cn-ip-legal",
}
FORBIDDEN = ["cla" + "ude"]


def main() -> int:
    errors = []
    for name in sorted(EXPECTED):
        path = ROOT / "plugins" / name / ".codex-plugin" / "plugin.json"
        if not path.exists():
            errors.append(f"missing plugin manifest: {path}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        checks = {
            "name": name,
            "repository": REPOSITORY,
            "author": "waynetsa",
            "license": "Apache-2.0",
            "skills": "./skills/",
        }
        for key, expected in checks.items():
            if data.get(key) != expected:
                errors.append(f"{path}: expected {key}={expected!r}, got {data.get(key)!r}")
        manifest_text = json.dumps(data, ensure_ascii=False).lower()
        for word in FORBIDDEN:
            if word in manifest_text:
                errors.append(f"{path}: forbidden external naming found: {word}")

    extra = {
        p.parent.parent.name
        for p in (ROOT / "plugins").glob("*/.codex-plugin/plugin.json")
    } - EXPECTED
    for name in sorted(extra):
        errors.append(f"unexpected plugin manifest: {name}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: plugin manifests are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
