---
type: "Tool Guide"
title: "Argo CD"
description: "Source-aware guidance for Argo CD."
resource: "https://argo-cd.readthedocs.io/"
okb_bundle_id: argo-cd
timestamp: "2026-08-13T00:00:00Z"
tool_category: "GitOps continuous delivery platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect repositories or clusters, change manifests or projects, sync or prune applications, rotate credentials, alter RBAC, or represent deployment health"
---
# Argo CD Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://argo-cd.readthedocs.io/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Argo CD configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect repositories or clusters, change manifests or projects, sync or prune applications, rotate credentials, alter RBAC, or represent deployment health.

## Guardrails

- Do not invent repository contents, desired or live state, cluster access, diff safety, hook behavior, sync result, health, rollback viability, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
