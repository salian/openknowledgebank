---
type: "Tool Guide"
title: "Spacelift"
description: "Source-aware guidance for Spacelift."
resource: "https://docs.spacelift.io/"
okb_bundle_id: spacelift
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Infrastructure-as-code delivery, state, policy, drift, worker, integration, and governance platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect cloud or source-control accounts, expose credentials, plan or apply infrastructure, alter state, approve runs, reconcile drift, change policies, execute tasks, or represent plan accuracy, policy result, infrastructure state, security, availability, cost, or deployment success"
---
# Spacelift Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.spacelift.io/
- https://docs.spacelift.io/concepts/policy

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Spacelift infrastructure delivery and policy review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect cloud or source-control accounts, expose credentials, plan or apply infrastructure, alter state, approve runs, reconcile drift, change policies, execute tasks, or represent plan accuracy, policy result, infrastructure state, security, availability, cost, or deployment success.

## Guardrails

- Do not invent stack or state identity, plan completeness, policy result, approval, drift, credential safety, apply result, infrastructure state, security, availability, cost, compliance, or deployment success.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
