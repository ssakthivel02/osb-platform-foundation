# Staging Entry Criteria

A workload may enter staging only when:

- The target repository and deployment path are identified.
- The build succeeds from a clean checkout.
- Required configuration is documented and secrets are externalised.
- Automated tests and schema validation pass.
- Critical security findings are resolved or formally accepted.
- Privacy and rights checks are complete where applicable.
- Health and readiness endpoints are defined.
- Monitoring and rollback procedures are documented.
- The staging environment uses synthetic, public or appropriately anonymised data.

## Staging exit evidence

Before production consideration, retain:

- Commit SHA and release version
- Workflow run URL
- Artifact digest
- Test and scan summaries
- Endpoint and health-check results
- Performance results
- Accessibility results
- Rollback result
- Backup/restore result for authoritative data
- Remaining risks and decision owner
