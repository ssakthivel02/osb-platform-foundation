# Contributing

## Contribution principles

- Preserve Architecture v1.0 unless an ADR is approved.
- Keep documentation concise and implementation-ready.
- Do not introduce unapproved technology choices.
- Include tests, diagrams, and operational notes where relevant.

## Pull request rules

Every PR must include:

- Clear summary
- Related issue or ADR
- Testing evidence
- Security impact
- Documentation impact
- Rollback notes if applicable

## Branch naming

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
adr/<short-description>
security/<short-description>
```

## Review requirements

- Minimum one technical reviewer.
- Security reviewer required for auth, data, API, infra, AI, and marketplace changes.
- Architecture reviewer required when ADR is involved.

