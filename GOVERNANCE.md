# Governance

## Architecture baseline

Architecture v1.0 is frozen. Material changes require an ADR.

## ADR process

1. Create ADR from `/templates/ADR_TEMPLATE.md`.
2. Add it to `/adrs` using format `ADR-0001-title.md`.
3. Submit pull request.
4. Obtain required approvals.
5. Update affected documentation.

## Approval matrix

| Change type | Required approval |
|---|---|
| Architecture | Chief Architect |
| Security | Security Lead |
| Data model | Data Architect |
| API contract | API Owner + affected service owners |
| Infrastructure | Platform / DevOps Lead |
| UX system | Design System Owner |
| AI behaviour | AI Governance Lead |

## Repository maturity levels

| Level | Meaning |
|---|---|
| L0 | Idea |
| L1 | Architecture approved |
| L2 | Repository scaffolded |
| L3 | Development active |
| L4 | Testable MVP |
| L5 | Production ready |
| L6 | Live |
| L7 | Enterprise certified |

## Required repository health files

Every repository must include:

- README.md
- CONTRIBUTING.md
- SECURITY.md
- CHANGELOG.md
- CODEOWNERS
- ADR folder
- GitHub issue templates
- Pull request template
- CI/CD workflow

