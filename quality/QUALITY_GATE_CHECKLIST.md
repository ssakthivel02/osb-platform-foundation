# OSB Quality Gate Checklist

Use this checklist for every repository before staging or production promotion.

## Gate A — Repository
- [ ] README, SECURITY, CONTRIBUTING and ownership are present.
- [ ] Repository purpose and deployment type are documented.
- [ ] Branch protection and required checks are configured.
- [ ] No secrets, private keys or production credentials are committed.

## Gate B — Build and test
- [ ] Build is reproducible from a clean checkout.
- [ ] Unit and integration tests pass.
- [ ] Critical user journeys have end-to-end coverage.
- [ ] Accessibility validation has no release-blocking defects.
- [ ] Performance thresholds are declared and measured.

## Gate C — Security, privacy and rights
- [ ] Secret and dependency scans pass.
- [ ] SAST results contain no unresolved critical findings.
- [ ] SBOM or dependency inventory is retained as evidence.
- [ ] Personal-data processing is documented where applicable.
- [ ] Content and media rights are verified where applicable.

## Gate D — Deployment and operations
- [ ] Staging deployment succeeds.
- [ ] Health and readiness checks pass.
- [ ] Logs, metrics, alerts and request identifiers are available.
- [ ] Rollback has been executed successfully.
- [ ] Backup and restore evidence exists for authoritative data.
- [ ] Runbook, support owner and escalation route are documented.

## Decision
- **GO:** all mandatory controls pass.
- **CONDITIONAL GO:** no critical gaps; written conditions, owner and deadline recorded.
- **NO-GO:** any security, privacy, rights, data-integrity, recovery or rollback blocker remains.
