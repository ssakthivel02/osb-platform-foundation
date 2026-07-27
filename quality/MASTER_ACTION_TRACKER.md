# OSB Master Production Action Tracker

## Wave Q6 — Execution Quality

| ID | Priority | Repository / scope | Action | Required evidence | Status |
|---|---:|---|---|---|---|
| Q6-001 | P0 | osb-platform-foundation | Merge Q1–Q5 baseline and establish production gate | Merged PR and gate document | Completed |
| Q6-002 | P0 | osb-platform-foundation | Correct repository naming drift in architecture and roadmap references | Updated documents and link validation | Ready |
| Q6-003 | P0 | Portfolio | Build machine-readable repository inventory with owner, runtime, deployment and maturity | Validated catalogue | In progress |
| Q6-004 | P0 | osb-engineering-standards | Verify schemas, vocabularies, examples and validation workflows exist and execute | Passing CI evidence | Not started |
| Q6-005 | P0 | osb-platform-data | Establish executable PostgreSQL baseline, migrations, tests and backup/restore instructions | Migration and restore test output | Not started |
| Q6-006 | P0 | osb-infra-terraform | Validate Terraform without provisioning paid infrastructure | fmt, validate and security scan | Not started |
| Q6-007 | P1 | osb-shared-ui | Validate package build, TypeScript checks, accessibility and component tests | Passing package CI | Not started |
| Q6-008 | P1 | osb-services-auth | Validate real authentication boundaries before any protected production route | Threat model and end-to-end auth tests | Not started |
| Q6-009 | P1 | osb-services-api-gateway | Validate CORS, rate limits, request IDs, error handling and upstream failure behaviour | Integration/load-test evidence | Not started |
| Q6-010 | P1 | osb-web / osb-admin-portal | Validate critical journeys, loading/error states and deployment rollback | Playwright and release evidence | Not started |
| Q6-011 | P1 | Portfolio | Add reusable secret, dependency, schema and documentation checks | Passing reusable workflows | Not started |
| Q6-012 | P1 | Portfolio | Establish release evidence record and NO-GO/GO decision template | Completed release record | Not started |

## Immediate controlled-production sequence

1. Foundation governance baseline.
2. Engineering contract validation.
3. Data schema and migration validation.
4. Infrastructure validation without paid deployment.
5. Shared UI build and accessibility validation.
6. Authentication and gateway integration.
7. Web/admin critical-path tests.
8. Staging deployment.
9. Observability and rollback verification.
10. Repository-specific production approval.

## Stop conditions

Production promotion must stop when any of the following is true:

- A secret or credential is exposed.
- A critical/high exploitable vulnerability remains unresolved without accepted risk.
- Rights, privacy classification or data-processing purpose is unknown.
- A database migration has no tested rollback or recovery path.
- Critical user journeys fail.
- Health, logs or alerts cannot identify a failed release.
- The deployment cannot be traced to an approved commit and artifact.
