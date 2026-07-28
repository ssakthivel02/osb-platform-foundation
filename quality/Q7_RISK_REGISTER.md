# Q7 Risk Register

| ID | Risk | Impact | Current control | Required next evidence |
|---|---|---|---|---|
| Q7-R01 | Architecture mistaken for implementation | False readiness claims | Evidence-state model | Verified CI and runtime evidence |
| Q7-R02 | Repository naming drift | Broken automation and references | Authoritative catalogue | Link and workflow validation |
| Q7-R03 | Empty or documentation-only service repositories | Missing executable platform capability | MVP classification | Buildable implementation or explicit deferral |
| Q7-R04 | Secrets committed during rapid delivery | Credential compromise | Security policy | Secret scan result and rotation process |
| Q7-R05 | Unlicensed content enters search or AI corpus | Copyright and contractual exposure | Rights gate | Asset-level rights record |
| Q7-R06 | Personal or children’s data used without review | Privacy and safeguarding harm | Privacy gate | Processing record and DPIA decision |
| Q7-R07 | Tamil text corruption or poor rendering | Loss of content integrity and usability | Tamil-first criteria | Unicode, font and device tests |
| Q7-R08 | API/schema drift | Client failures | Contract-first rule | Compatibility diff and contract tests |
| Q7-R09 | Backups exist but cannot restore | Irrecoverable data loss | Restore gate | Timestamped restore test |
| Q7-R10 | Production change cannot roll back | Extended outage | Release gate | Tested rollback record |
| Q7-R11 | Missing observability | Silent failures | OTel/monitoring requirement | Alert and dashboard test |
| Q7-R12 | Premature infrastructure complexity | Cost and operational burden | PostgreSQL-first MVP | ADR for every added platform dependency |

## Escalation rule

Any unresolved critical risk results in NO-GO. High risks require a named owner, deadline and compensating control before CONDITIONAL GO.