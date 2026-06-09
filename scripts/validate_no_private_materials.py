import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ["docs", "examples", "plugins", "shared", "connectors"]
FAIL_PATTERNS = [
    ("private key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----")),
    ("github token", re.compile(r"ghp_[A-Za-z0-9_]{30,}")),
    ("generic api key assignment", re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{12,}['\"]")),
    ("aws access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("jwt-like token", re.compile(r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}")),
]
WARN_PATTERNS = [
    ("Chinese ID keyword", "身份证号"),
    ("mobile keyword", "手机号"),
    ("bank account keyword", "银行账户"),
    ("commercial secret keyword", "商业秘密"),
]
ALLOW_TEXT = [
    "REPLACE_WITH_LOCAL_SECRET_DO_NOT_COMMIT",
    "API_TOKEN",
    "API_BASE_URL",
]


def should_scan(path: Path) -> bool:
    if any(part.startswith(".git") for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in {".md", ".csv", ".json", ".yml", ".yaml", ".py"}


def main() -> int:
    errors = []
    warnings = []
    for directory in SCAN_DIRS + ["scripts", ".github"]:
        base = ROOT / directory
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not should_scan(path):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            sanitized_text = text
            for allowed in ALLOW_TEXT:
                sanitized_text = sanitized_text.replace(allowed, "")
            for label, pattern in FAIL_PATTERNS:
                if pattern.search(sanitized_text):
                    errors.append(f"{path.relative_to(ROOT)}: possible {label}")
            for label, keyword in WARN_PATTERNS:
                if keyword in text:
                    warnings.append(f"WARNING: {path.relative_to(ROOT)} mentions {label}; verify it is a rule or placeholder, not real data")

    for warning in warnings:
        print(warning)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: no private material patterns found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
