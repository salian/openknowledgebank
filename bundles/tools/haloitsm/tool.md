---
type: "Tool Guide"
title: "HaloITSM"
description: "Source-aware guidance for HaloITSM."
resource: "https://usehalo.com/haloitsm/"
okb_bundle_id: haloitsm
timestamp: "2026-08-13T00:00:00Z"
tool_category: "IT service, enterprise service, asset, and change management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "change or close tickets, approve changes, modify assets or configuration, run automation, publish knowledge, alter SLAs or access, bill customers, or represent service restoration or compliance"
---
# HaloITSM Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://usehalo.com/haloitsm/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current HaloITSM documentation for the deployed version, modules, and integrations.
- Tenant, service, ticket, asset, configuration item, workflow, SLA, approval, automation, integration, role, and log state.
- Change authority, security and privacy review, testing, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable HaloITSM service configuration and change review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before change or close tickets, approve changes, modify assets or configuration, run automation, publish knowledge, alter SLAs or access, bill customers, or represent service restoration or compliance.

## Guardrails

- Do not invent ticket classification or state, ownership, SLA, root cause, asset or configuration state, change approval, automation result, billing, service restoration, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
