---
type: "Tool Guide"
title: "Gitee"
description: "Source-aware guidance for Gitee."
resource: "https://gitee.com/help"
okb_bundle_id: gitee
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Git repository hosting and code collaboration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or delete repositories, push or merge code, change access, run delivery workflows, publish artifacts, migrate data, or represent review, security, or deployment state"
---
# Gitee Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://gitee.com/help

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official Gitee help and product documentation applicable to the account.
- Repository, branch, organization, user, role, permission, integration, workflow, and log state.
- Code ownership, license, security review, test, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Gitee repository and delivery review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or delete repositories, push or merge code, change access, run delivery workflows, publish artifacts, migrate data, or represent review, security, or deployment state.

## Guardrails

- Do not invent code ownership, repository contents, branch or review state, access, workflow result, artifact provenance, security, deployment, license compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
