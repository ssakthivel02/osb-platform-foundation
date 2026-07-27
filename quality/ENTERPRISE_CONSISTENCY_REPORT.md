# Q2 Enterprise Consistency Report

**Programme:** OmSaravanaBhava Learning Ecosystem (OSB)  
**Baseline date:** 2026-07-27

## Objective

Verify that repository names, service identifiers, API versions, canonical identifiers, namespaces, event names, data contracts, and operational terminology are consistent across the OSB estate.

## Confirmed inconsistency

The foundation README's implementation sequence uses repository names that do not match the connected GitHub repositories:

| Foundation reference | Actual repository | Required disposition |
|---|---|---|
| `osb-auth-service` | `osb-services-auth` | Update foundation reference |
| `osb-api-gateway` | `osb-services-api-gateway` | Update foundation reference |
| `osb-data-platform` | `osb-platform-data` | Update foundation reference |
| `osb-cms-service` | `osb-services-cms` | Update foundation reference |

This drift affects traceability, automation, documentation links, release orchestration, and ownership mapping.

## Canonical conventions proposed for enforcement

### Repositories

- Platform repositories: `osb-platform-*`
- Shared services: `osb-services-*`
- Shared libraries/UI: `osb-shared-*`
- Infrastructure: `osb-infra-*`
- Product surfaces: `osb-web`, `osb-mobile`, `osb-admin-portal`
- Operations: `osb-monitoring`, `osb-observability`

### APIs

- Public REST base path: `/api/v1`
- OpenAPI version: `3.1.x`
- Error envelope fields: `code`, `message`, `requestId`, `timestamp`, optional `details`
- Correlation identifier: `X-Request-ID`
- Idempotency header for eligible writes: `Idempotency-Key`

### Canonical identity

- Persistent entity IDs: UUID or approved canonical URN
- Canonical URN pattern: `urn:osb:<domain>:<entity-type>:<identifier>`
- Ontology namespace and API identifiers must map explicitly rather than relying on display names.

### Events

- Event names: past tense, for example `EditorialApproved`, `CanonicalPublished`
- Topic names: lower-case dot notation, for example `osb.editorial.approved.v1`
- Every event requires `eventId`, `eventType`, `eventVersion`, `occurredAt`, `producer`, `correlationId`, and payload.

## Consistency checks to automate

1. Repository references resolve to real GitHub repositories.
2. OpenAPI operation IDs are globally unique.
3. JSON Schema, GraphQL, Protobuf, AsyncAPI, and database enum values agree.
4. Ontology class names map to canonical API entity names.
5. Database tables use stable IDs and do not use display names as keys.
6. All timestamps are UTC ISO 8601.
7. Language tags use BCP 47 values such as `ta`, `en`, and `sa` where applicable.
8. Status enums are centrally governed and versioned.
9. Package names and deployment service names match repository ownership records.
10. Documentation does not refer to superseded repository names.

## Priority remediations

- Correct the four confirmed repository-name mismatches.
- Create `standards/naming/repository-naming.md` in `osb-engineering-standards`.
- Create a canonical enum registry.
- Create a contract-diff CI job across OpenAPI, GraphQL, Protobuf, AsyncAPI, and JSON Schema.
- Publish a machine-readable service catalogue.

## Exit criteria

Q2 is complete when all canonical names are registered, repository references validate automatically, and cross-contract drift is blocked in CI.