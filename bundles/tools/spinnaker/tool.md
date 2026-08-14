---
type: "Tool Guide"
title: "Spinnaker"
description: "Source-aware guidance for Spinnaker."
resource: "https://spinnaker.io/docs/"
okb_bundle_id: spinnaker
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source multi-cloud continuous delivery, pipeline, deployment-strategy, and operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect cloud accounts, expose credentials, trigger pipelines, approve judgments, deploy or roll back services, change traffic or infrastructure, install plugins, or represent artifact provenance, stage success, availability, security, or release readiness"
---
# Spinnaker Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://spinnaker.io/docs/
- https://spinnaker.io/docs/guides/user/pipeline/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Spinnaker pipeline and deployment governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect cloud accounts, expose credentials, trigger pipelines, approve judgments, deploy or roll back services, change traffic or infrastructure, install plugins, or represent artifact provenance, stage success, availability, security, or release readiness.

## Guardrails

- Do not invent version or deployment-method applicability, account state, artifact provenance, trigger event, stage result, approval, deployment or rollback result, traffic state, availability, security, or release readiness.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
