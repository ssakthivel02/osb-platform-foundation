# Repository Structure

## Recommended repository list

```text
osb-platform-foundation
osb-engineering-standards
osb-infra-terraform
osb-shared-ui
osb-auth-service
osb-api-gateway
osb-data-platform
osb-cms-service
osb-learning-service
osb-ai-tutor
osb-assessment-engine
osb-certification-engine
osb-search-service
osb-recommendation-engine
osb-notification-service
osb-analytics-service
osb-marketplace
osb-community
osb-admin-portal
osb-mobile
osb-web
osb-monitoring
osb-observability
```

## Naming rules

- Prefix all repositories with `osb-`.
- Use lowercase kebab-case.
- Repository names must describe a bounded context.
- Avoid generic names such as `backend`, `frontend`, or `app` unless they are official top-level products.

## Standard repository layout

```text
repo-name/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── CODEOWNERS
├── docs/
├── adrs/
├── templates/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
└── src/               # only for code repositories
```

