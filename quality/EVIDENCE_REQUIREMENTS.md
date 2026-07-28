# Implementation Evidence Requirements

A repository is not complete because files exist. Each control requires inspectable evidence.

| Control | Minimum evidence | Blocking |
|---|---|---|
| Build | Reproducible command and successful CI run | Yes |
| Unit/integration tests | Test report and exit status | Yes |
| Contract compatibility | OpenAPI/schema diff or consumer contract report | Yes for APIs |
| Security | Dependency, secret and code scan reports | Yes |
| Privacy | Data classification and processing review | Yes when personal data exists |
| Rights | Source, licence and permitted-use evidence | Yes for content/media/AI ingestion |
| Accessibility | Automated scan plus manual critical-path review | Yes for UI releases |
| Performance | Defined workload, p95/p99 and resource results | Yes for production APIs |
| Resilience | Dependency-failure and recovery results | Yes for critical services |
| Observability | Logs, metrics, traces, dashboards and alert test | Yes |
| Backup/restore | Successful restore evidence, not backup creation alone | Yes for authoritative data |
| Deployment | Staging deployment record and configuration reference | Yes |
| Rollback | Tested rollback or forward-fix procedure | Yes |
| Operations | Owner, runbook and escalation route | Yes |

## Evidence states

- **Specified:** requirement documented.
- **Mapped:** repository/component identified.
- **Implemented:** working code or configuration exists.
- **Verified:** automated or manual test passed.
- **Deployed:** released to the intended environment.
- **Observed:** telemetry confirms expected behaviour.
- **Accepted:** accountable approver records the release decision.

Only **Accepted** evidence supports a production-ready statement.