# Q1 Repository Completeness Report

**Programme:** OmSaravanaBhava Learning Ecosystem (OSB)  
**Baseline date:** 2026-07-27  
**Scope:** OSB platform repositories visible in the connected GitHub account.

## Executive result

The programme has a broad repository topology, but the repositories are at materially different maturity levels. The foundation repository is documentation-led and already identifies itself as the source of truth for vision, architecture, roadmap, governance, ADR process, repository standards, security, and contribution policy. The engineering-standards repository currently exposes only a minimal implementation-package README and therefore requires a deeper file-level completeness pass before it can be treated as the enforceable engineering baseline.

## Repository tiers

### Tier A — governance and standards

- `osb-platform-foundation`
- `osb-engineering-standards`

### Tier B — shared platform capabilities

- `osb-infra-terraform`
- `osb-shared-ui`
- `osb-platform-data`
- `osb-services-auth`
- `osb-services-api-gateway`
- `osb-services-search`
- `osb-services-cms`
- `osb-services-ai-tutor`

### Tier C — product and operations surfaces

- `osb-web`
- `osb-mobile`
- `osb-admin-portal`
- `osb-monitoring`
- `osb-observability`
- remaining OSB services and community/marketplace repositories

## Mandatory repository controls

Every active repository must contain or deliberately inherit the following controls:

- `README.md`
- `LICENSE`
- `SECURITY.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `.gitignore`
- `.editorconfig`
- `.github/CODEOWNERS`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/dependabot.yml` or an approved Renovate configuration
- `CHANGELOG.md`
- `VERSION` or a clearly defined package/version source
- `docs/architecture/`
- `docs/adrs/`
- at least one validation workflow under `.github/workflows/`

## Initial findings

1. `osb-platform-foundation` has a coherent documentation index and explicitly freezes Architecture v1.0 behind ADR governance.
2. Its documented implementation sequence contains naming drift against the actual repository names, including `osb-auth-service` versus `osb-services-auth`, `osb-api-gateway` versus `osb-services-api-gateway`, `osb-data-platform` versus `osb-platform-data`, and `osb-cms-service` versus `osb-services-cms`.
3. `osb-engineering-standards` currently presents a generic README but does not, from the inspected file alone, prove the presence of the executable contract libraries, policy-as-code, validators, templates, or CI controls expected from the repository purpose.
4. Multiple OSB repositories are very small, which is a strong indicator that they are scaffolds or documentation-only baselines rather than implemented services. Size alone is not a release decision; each repository still requires file and workflow inspection.

## Quality-gate classification

- **Green:** required controls present and validated by CI.
- **Amber:** controls partially present, inherited, or not yet executable.
- **Red:** missing mandatory governance, security, build, test, or release controls.
- **Not assessed:** insufficient repository evidence inspected.

## Required next actions

1. Add a machine-readable repository inventory at `quality/repository-inventory.yaml`.
2. Inspect every Tier A and Tier B repository for the mandatory controls.
3. Correct repository-name drift in the foundation documentation.
4. Establish a reusable `.github` governance template or synchronisation workflow.
5. Add a repository compliance validator that fails CI when mandatory files or metadata are absent.
6. Do not mark any repository production-ready based only on architecture documents or README claims.

## Exit criteria

Q1 is complete only when every in-scope repository has an evidence-backed Green/Amber/Red status, all Red controls have tracked remediation issues, and the compliance validator runs on pull requests.