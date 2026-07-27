# Q5 Documentation Audit

**Programme:** OmSaravanaBhava Learning Ecosystem (OSB)  
**Baseline date:** 2026-07-27

## Objective

Ensure that OSB documentation is accurate, navigable, non-duplicative, versioned, traceable to implementation, and suitable for engineering, editorial, security, operational and product audiences.

## Evidence reviewed

- `osb-platform-foundation/README.md`
- `osb-engineering-standards/README.md`
- Connected GitHub repository inventory
- Current ontology and platform-contract foundation outputs supplied for review

## Strengths

- The foundation repository clearly states its role as the source of truth for vision, architecture, roadmap, governance, ADRs, repository standards, security and contribution policy.
- The foundation README provides a useful document index.
- Architecture v1.0 is explicitly frozen behind ADR governance.
- The engineering-standards README states PR review, ADR and secret-handling expectations.
- The ontology and contract work uses established formats including OWL, RDF/Turtle, SHACL, JSON-LD, OpenAPI, GraphQL, Protobuf and AsyncAPI.

## Confirmed documentation defects

1. Repository-name drift exists between the foundation implementation sequence and actual GitHub repository names.
2. The engineering-standards README is too generic to act as a navigation entry point for the extensive contract, validator, pipeline and policy assets expected from that repository.
3. Generated ontology/API examples are presented as initial batches, not evidence of a complete 300–600-file implementation.
4. Some generated CI examples contain commented-out validation or refer to files/scripts whose existence has not yet been demonstrated; those examples must not be reported as completed controls.
5. Production-readiness percentages previously discussed are not supported by a complete repository-by-repository evidence audit and should be replaced by evidence states.

## Required documentation architecture

```text
docs/
  architecture/
  adrs/
  api/
  data/
  ontology/
  security/
  operations/
  testing/
  releases/
  runbooks/
  editorial/
  compliance/
  glossary/
```

Each repository README must include:

- Purpose and non-goals
- Ownership
- Architecture and dependencies
- Local development
- Validation and testing
- Security considerations
- Deployment and rollback
- Observability
- Versioning and compatibility
- Links to ADRs, runbooks and release evidence
- Current maturity status based on evidence

## Documentation quality rules

- Use stable IDs for requirements, ADRs, risks and controls.
- Label examples explicitly; do not present example snippets as deployed implementation.
- Separate traditional belief, historically documented material, scholarly interpretation and unverified claims.
- Include source provenance and confidence for devotional/historical content.
- Keep generated documents under review and assign accountable owners.
- Validate internal links, repository links, code references and diagrams in CI.
- Use Mermaid/PlantUML source files for maintainable diagrams.
- Maintain a shared glossary and canonical terminology registry.
- Record deprecations and superseded documents.

## Immediate actions

1. Expand the engineering-standards README into a real implementation index.
2. Correct repository names and links in the foundation roadmap.
3. Add document metadata: owner, status, version, approved date and review date.
4. Add automated Markdown linting, link checking and diagram validation.
5. Build a single master documentation portal from repository-owned source documents.
6. Replace unsupported completion claims with Specified/Mapped/Implemented/Verified/Deployed/Observed/Accepted states.

## Exit criteria

Q5 is complete when documentation is linked to real repository artifacts, all links and diagrams validate, terminology is consistent, duplicate/superseded material is controlled, and every production capability has an owner-approved runbook and release record.