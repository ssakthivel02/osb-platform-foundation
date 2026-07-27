# Manual actions required

The following actions require repository-owner or environment-owner access and cannot be proven through documentation alone.

1. Configure branch protection on `main` with one qualified reviewer and mandatory automated checks.
2. Add repository or environment secrets only through GitHub Environments; never commit them to source.
3. Confirm production domains, Cloudflare routes and DNS ownership before deployment.
4. Approve any paid cloud resource creation before Terraform apply.
5. Complete legal, privacy and rights review for user accounts, children's features, restricted devotional content and media.
6. Perform a real staging deployment and capture workflow URLs, commit SHA and artifact digest.
7. Execute rollback and data-restore tests in the target environment.
8. Confirm monitoring destinations, alert recipients and escalation contacts.
9. Record the final GO, CONDITIONAL GO or NO-GO decision in a release-evidence file.

No production release should proceed solely from a written checklist.
