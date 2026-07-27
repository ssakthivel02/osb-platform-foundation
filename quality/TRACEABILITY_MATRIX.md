# Q3 Architecture Traceability Matrix

**Programme:** OmSaravanaBhava Learning Ecosystem (OSB)  
**Baseline date:** 2026-07-27

## Purpose

Trace approved architecture and standards into repositories, executable controls, test evidence, and production outcomes.

## Initial matrix

| Capability / standard | Primary repository | Expected implementation evidence | Current baseline |
|---|---|---|---|
| Vision, roadmap, governance | `osb-platform-foundation` | Approved documents, ADR process, ownership model | Documented baseline present |
| Engineering standards | `osb-engineering-standards` | Validators, templates, policy-as-code, CI workflows | Requires deeper evidence review |
| Infrastructure | `osb-infra-terraform` | Terraform modules, plans, policy checks, state strategy | Not yet assessed |
| Shared UI | `osb-shared-ui` | Tokens, components, accessibility tests, Storybook | Not yet assessed |
| Identity and access | `osb-services-auth` | OIDC/OAuth flows, RBAC/ABAC, key rotation, tests | Not yet assessed |
| API gateway | `osb-services-api-gateway` | Routing, auth enforcement, rate limits, CORS, telemetry | Not yet assessed |
| Canonical data platform | `osb-platform-data` | PostgreSQL, graph, vector/search mappings, migrations | Not yet assessed |
| CMS/editorial governance | `osb-services-cms` | Workflow, evidence, approval, publication, audit | Not yet assessed |
| AI tutor / RAG | `osb-services-ai-tutor` | Retrieval, citations, safety, evaluation, observability | Not yet assessed |
| Search | `osb-services-search` | Lexical, semantic, graph and Tamil search validation | Not yet assessed |
| Web product | `osb-web` | Build, tests, deployment, accessibility, performance | Not yet assessed |
| Mobile product | `osb-mobile` | Expo/native build, test, privacy and store evidence | Not yet assessed |
| Administration | `osb-admin-portal` | Protected workflows, audit, role enforcement | Not yet assessed |
| Monitoring | `osb-monitoring` | SLO dashboards, alerts, synthetic checks | Not yet assessed |
| Observability | `osb-observability` | Logs, metrics, traces, request correlation | Not yet assessed |

## Required evidence states

Each matrix row must progress through the following states:

1. **Specified** — approved requirement exists.
2. **Mapped** — owning repository and component identified.
3. **Implemented** — executable artifact exists.
4. **Verified** — automated test or review evidence exists.
5. **Deployed** — artifact is present in an environment.
6. **Observed** — operational telemetry confirms behaviour.
7. **Accepted** — accountable owner signs off the release gate.

A document alone satisfies only the Specified state.

## Traceability record format

Every requirement should carry:

- Requirement ID
- Standard and section
- Owning repository
- Implementing file/component
- Verification test
- CI run or release evidence
- Environment
- Owner
- Status
- Exception/ADR reference

## Immediate actions

- Allocate stable requirement IDs to the existing standards.
- Add `implements:` metadata to ADRs and implementation documents.
- Add `verifies:` metadata to automated tests.
- Generate this matrix from machine-readable YAML rather than maintaining it manually.
- Block production acceptance for capabilities without Implemented and Verified evidence.

## Exit criteria

Q3 is complete when every P0/P1 requirement is connected to an implementation artifact and objective verification evidence, with no orphaned standards or undocumented implementations.