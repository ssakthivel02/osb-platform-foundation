# Production Stop Conditions

Production promotion is blocked when any of the following applies:

- The build cannot be reproduced from the approved commit.
- A critical or high-risk secret exposure remains unresolved.
- Authentication or authorisation is bypassed for protected functionality.
- Personal data, children's data or restricted content lacks an approved handling basis.
- Copyright, licence or temple/media permission is unknown for published material.
- Database migrations lack rollback or recovery evidence.
- Health checks, monitoring or alert ownership are absent.
- Backup restoration has not been demonstrated for authoritative data.
- Critical accessibility defects block essential user journeys.
- Performance testing shows instability, cascading failure or unacceptable error rates.
- The release artifact cannot be traced to its commit and workflow.
- A production rollback has not been defined and tested.
- Required manual approval is missing.

A stop condition may be cleared only with recorded evidence and an accountable approver. Documentation alone is not evidence that a runtime control works.
