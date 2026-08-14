---
type: "Tool Guide"
title: "Wrike"
description: "Source-aware guidance for Wrike."
resource: "https://help.wrike.com/"
okb_bundle_id: wrike
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Collaborative work, project, resource, workflow, proofing, approval, automation, integration, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter projects, tasks, dependencies, workflows or approvals, assign people, run automations, share data, expose tokens, call APIs, or represent ownership, effort, resource capacity, status, approval, delivery date, or completion"
---
# Wrike Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.wrike.com/
- https://developers.wrike.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Wrike work-management, resource, and automation review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter projects, tasks, dependencies, workflows or approvals, assign people, run automations, share data, expose tokens, call APIs, or represent ownership, effort, resource capacity, status, approval, delivery date, or completion.

## Guardrails

- Do not invent plan or feature applicability, record state, assignment, estimate, resource capacity, dependency, automation or API result, approval, delivery date, completion, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
