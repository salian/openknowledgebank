---
type: "Tool Guide"
title: "JFrog Artifactory"
description: "Source-aware guidance for JFrog Artifactory."
resource: "https://jfrog.com/artifactory/"
okb_bundle_id: jfrog-artifactory
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Universal artifact repository and software supply-chain platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload, promote, copy, move or delete artifacts, change repositories or permissions, expose tokens, replicate or federate content, alter retention, restore backups, or represent provenance or security"
---
# JFrog Artifactory Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://jfrog.com/artifactory/
- https://docs.jfrog.com/artifactory/docs/repository-management

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable JFrog Artifactory repository and supply-chain review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload, promote, copy, move or delete artifacts, change repositories or permissions, expose tokens, replicate or federate content, alter retention, restore backups, or represent provenance or security.

## Guardrails

- Do not invent artifact identity, checksum, provenance, package type, build status, permission, token safety, replication completeness, vulnerability status, backup validity, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
