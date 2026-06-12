from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGINS = [
    "cn-commercial-legal",
    "cn-corporate-legal",
    "cn-litigation-legal",
    "cn-privacy-legal",
    "cn-ai-governance-legal",
    "cn-employment-legal",
    "cn-regulatory-legal",
    "cn-ip-legal",
]
REQUIRED = [
    ".codex-plugin/plugin.json",
    "skills",
    "profiles",
    "templates",
    "references",
    "evals",
]


def main() -> int:
    errors = []
    for plugin in PLUGINS:
        plugin_dir = ROOT / "plugins" / plugin
        if not plugin_dir.exists():
            errors.append(f"missing plugin directory: {plugin_dir}")
            continue
        for item in REQUIRED:
            path = plugin_dir / item
            if not path.exists():
                errors.append(f"missing required path: {path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: plugin structure is complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
