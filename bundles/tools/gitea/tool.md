---
type: "Tool Guide"
title: "Gitea"
description: "Source-aware guidance for Gitea."
resource: "https://docs.gitea.com/"
okb_bundle_id: gitea
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Self-hosted Git collaboration and software delivery platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or delete repositories, merge code, change access, run workflows, expose secrets, publish packages, upgrade or migrate a server, restore backups, or represent security or deployment state"
---
# Gitea Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.gitea.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Gitea documentation for the deployed version.
- Deployment, repository, organization, authentication, permission, runner, secret, package, webhook, and log state.
- Backup, migration, security review, test, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Gitea deployment and repository operations review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or delete repositories, merge code, change access, run workflows, expose secrets, publish packages, upgrade or migrate a server, restore backups, or represent security or deployment state.

## Guardrails

- Do not invent repository contents, branch protection, review or merge state, access, secret safety, workflow result, package provenance, backup validity, deployment health, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
