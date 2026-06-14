# Safety Checklist

Use this checklist before reading user materials, creating a session profile, or producing a draft.

## Must Confirm

- The user confirmed the materials are authorized for private-environment processing.
- The user selected 1 to 3 workflows.
- The user identified a primary workflow when multiple workflows are selected.
- Cold-start information is complete or conservative defaults were accepted.
- The session practice profile is generated before task analysis.

## Prohibited in Public Repository

Do not put these in the public repository:

- real client data
- real case materials
- real contracts
- real personal information
- real employee information
- real regulatory materials
- real transaction materials
- real internal investigation materials
- credentials, tokens, API keys, cookies
- private system configuration
- `practice-profile.md`

## Local Profile Rule

Default: do not write files.

If the user explicitly asks to save the session profile, save only to:

```text
.local-sessions/<timestamp>/practice-profile.local.md
```

Ensure `.local-sessions/` is ignored in `.gitignore`.

## MCP and Production Systems

Do not suggest real MCP or production system integration. If the user asks for real system integration, explain that this repository is controlled pilot-ready only and direct them to private deployment planning and security review.
