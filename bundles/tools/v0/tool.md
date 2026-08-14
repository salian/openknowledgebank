---
type: "Tool Guide"
title: "v0"
description: "Source-aware guidance for v0."
resource: "https://v0.dev/docs"
okb_bundle_id: v0
timestamp: "2026-08-14T00:00:00Z"
tool_category: "AI application and interface generation, code, preview, integration, collaboration, and deployment platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload proprietary code or data, expose secrets, install packages, connect services, generate or modify code, deploy applications, spend funds, or represent authorship, license, correctness, accessibility, security, deployment, or production readiness"
---
# v0 Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://v0.dev/docs
- https://v0.dev/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable v0 generated-application and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload proprietary code or data, expose secrets, install packages, connect services, generate or modify code, deploy applications, spend funds, or represent authorship, license, correctness, accessibility, security, deployment, or production readiness.

## Guardrails

- Do not invent feature or model availability, code provenance or ownership, dependency safety, secret handling, generated-code correctness, accessibility, security, deployment result, cost, availability, or production readiness.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
