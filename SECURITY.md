# Security Policy

## Security posture

The platform follows a Zero Trust model. Identity, authorization, observability, encryption, and auditability are mandatory across all services.

## Reporting vulnerabilities

Do not open public GitHub issues for security vulnerabilities.

Report privately to the security owner defined by the repository CODEOWNERS file.

## Minimum security requirements

- No hardcoded secrets.
- Secrets must be stored in approved secret management systems.
- All APIs must enforce authentication and authorization.
- Logs must not expose PII, credentials, tokens, or private keys.
- Dependencies must be scanned.
- Containers must be scanned.
- Infrastructure must be reviewed before deployment.

## Required checks

- SAST
- Dependency scanning
- Secret scanning
- Container scanning
- IaC scanning
- Security review for P0/P1 services

