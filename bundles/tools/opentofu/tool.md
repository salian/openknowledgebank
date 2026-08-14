---
type: "Tool Guide"
title: "OpenTofu"
description: "Source-aware guidance for OpenTofu."
resource: "https://opentofu.org/docs/"
okb_bundle_id: opentofu
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source infrastructure-as-code, state, and automation tool"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "initialize providers, read or modify state, plan or apply infrastructure, import or destroy resources, rotate encryption metadata, expose credentials, change backends, run provisioners, or represent infrastructure, drift, security, or availability"
---
# OpenTofu Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://opentofu.org/docs/
- https://opentofu.org/docs/language/state/encryption/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable OpenTofu infrastructure, state, and change review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before initialize providers, read or modify state, plan or apply infrastructure, import or destroy resources, rotate encryption metadata, expose credentials, change backends, run provisioners, or represent infrastructure, drift, security, or availability.

## Guardrails

- Do not invent provider or module compatibility, resource identity, state completeness, encryption effectiveness, plan safety, apply result, drift, credential scope, cost, rollback, service availability, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
