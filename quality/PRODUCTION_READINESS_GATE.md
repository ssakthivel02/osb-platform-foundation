# OSB Production Readiness Gate

**Status:** Mandatory release control  
**Applies to:** All OSB repositories, services, websites, mobile applications and data pipelines.

## Release rule

A workload may be promoted to production only when every mandatory gate is supported by current evidence. Documentation alone does not satisfy implementation, verification, deployment or observability requirements.

## Evidence states

1. **Specified** — requirement is documented.
2. **Mapped** — owner, repository and control are identified.
3. **Implemented** — executable code or configuration exists.
4. **Verified** — automated or recorded testing has passed.
5. **Deployed** — the approved artifact is running in the target environment.
6. **Observed** — health, logs, metrics and alerts are operating.
7. **Accepted** — release owner has reviewed evidence and accepted residual risk.

## Mandatory gates

| Gate | Minimum production evidence | Blocking condition |
|---|---|---|
| Ownership | Repository owner, service owner and escalation route | Ownership absent or ambiguous |
| Build reproducibility | Lockfile, deterministic build command and successful CI run | Build cannot be reproduced |
| Automated tests | Unit/integration tests appropriate to risk; critical journeys covered | Critical path untested or failing |
| Security | Secret scan, dependency scan, least-privilege configuration and no unresolved critical findings | Secret exposure or critical vulnerability |
| Privacy and rights | Data classification, rights status and processing purpose recorded | Unknown rights or unlawful/undefined processing |
| API and schema compatibility | Contract validation and migration compatibility checks | Breaking change without approved migration |
| Deployment | Versioned artifact, rollback method and environment-specific configuration | Manual-only or irreversible deployment |
| Reliability | Health/readiness checks, timeout/retry policy and dependency failure behaviour | No health signal or unsafe failure mode |
| Observability | Structured logs, correlation IDs, metrics and actionable alerts | Release cannot be diagnosed |
| Backup and recovery | Backup scope and restore procedure tested where stateful data exists | Stateful release without recovery evidence |
| Accessibility | Automated checks plus manual review for critical user flows | Critical accessibility blocker |
| Documentation | README, deployment guide, runbook, security notes and changelog current | Operators cannot safely support release |

## Deployment decision

- **GO:** All mandatory gates pass; residual risks are documented and accepted.
- **CONDITIONAL GO:** No critical blocker; time-bound remediation owner and rollback trigger are documented.
- **NO-GO:** Any blocking condition exists, evidence is stale, or the deployed artifact cannot be traced to reviewed source.

## Minimum release evidence bundle

Each production release must retain:

- Git commit SHA and release version
- CI workflow/run identifier
- Test and security reports
- Schema or migration results
- Deployment target and timestamp
- Health-check result
- Rollback procedure
- Change summary and approver
- Known risks and remediation dates

## Current programme decision

The OSB portfolio is **not approved for blanket production promotion**. Individual applications may proceed only after repository-specific evidence is collected and this gate records a GO decision. The immediate priority is to validate the foundation, engineering standards, platform data, infrastructure and shared UI repositories before dependent services are promoted.