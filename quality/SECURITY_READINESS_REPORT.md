# Q4 Security Readiness Report

**Programme:** OmSaravanaBhava Learning Ecosystem (OSB)  
**Baseline date:** 2026-07-27

## Scope

Repository security, software supply chain, identity, data protection, runtime controls, auditability, incident response, and release assurance.

## Current evidence

The inspected foundation and engineering-standards README files both state security expectations, including security policy ownership, pull-request review, ADR governance, and prohibition of committed secrets. Those statements are necessary governance controls, but they do not by themselves prove implementation or runtime enforcement.

## Mandatory security gates

### Repository and supply chain

- Branch protection and required reviews
- CODEOWNERS for security-sensitive paths
- Secret scanning and push protection
- Dependency review and automated updates
- SAST, IaC scanning, container scanning and licence scanning
- SBOM generation in CycloneDX or SPDX
- Build provenance and signed release artifacts
- Pinned third-party GitHub Actions
- Least-privilege workflow permissions

### Identity and access

- OIDC/OAuth2 implementation
- MFA/passkey support for privileged users
- RBAC plus ABAC where contextual policy is required
- Segregation of duties for editorial approval and publication
- Service identities and short-lived credentials
- Key and token rotation

### Data protection

- Data classification
- Encryption in transit and at rest
- Secrets in an approved secrets manager
- Tenant and environment isolation
- Backup encryption and restore testing
- Retention, deletion and legal-hold controls
- Audit trails for canonical content and administrative actions

### Runtime

- API authentication and authorisation
- Rate limiting, abuse protection and request validation
- Secure headers and restrictive CORS
- Network policies and workload isolation
- Health endpoints that do not disclose sensitive internals
- Central logs, metrics, traces and request IDs
- Alerting for authentication, privilege, publication and data-integrity events

### AI and RAG

- Retrieval-source allow-listing
- Citation and provenance enforcement
- Prompt-injection controls
- Sensitive-data filtering
- Model and prompt versioning
- Hallucination and faithfulness evaluation
- Human approval for high-impact canonical publication

## Preliminary risk register

| Risk | Severity | Reason | Required control |
|---|---|---|---|
| Documentation mistaken for enforcement | High | Security statements may not be backed by CI/runtime controls | Evidence-based release gates |
| Scaffold repositories deployed prematurely | High | Several repositories appear very small and may not contain complete security controls | Mandatory readiness audit |
| Cross-repository contract drift | High | Names and interfaces may diverge | Contract registry and compatibility checks |
| Secrets or overly broad workflow tokens | Critical if present | Could compromise the estate | Secret scanning and least-privilege permissions |
| Unverified devotional content published as canonical | High | Creates integrity and trust risk | Evidence, editorial approval and provenance controls |
| AI output without grounding | High | Can introduce fabricated religious or historical claims | Citation, confidence and human-review gates |

## Immediate actions

1. Enable and verify GitHub secret scanning, dependency review and code scanning where available.
2. Add a reusable security workflow in `osb-engineering-standards`.
3. Add SBOM and provenance generation to release pipelines.
4. Inspect workflow permissions and pin third-party Actions by immutable commit SHA.
5. Create threat models for auth, API gateway, CMS/editorial, platform-data and AI tutor.
6. Define production-security acceptance criteria before any public launch.

## Exit criteria

Q4 is complete only when controls are both documented and demonstrably enforced through repository settings, CI evidence, deployment configuration and runtime telemetry.