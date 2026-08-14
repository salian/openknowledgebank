---
type: "Tool Guide"
title: "Sourcetree"
description: "Source-aware guidance for Sourcetree."
resource: "https://www.atlassian.com/software/sourcetree"
okb_bundle_id: sourcetree
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Desktop Git client, visual history, branching, remote-hosting, and repository workflow tool"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "clone private repositories, stage or commit files, rewrite history, merge or rebase branches, push, force push, change remotes, store credentials, run custom actions, or represent conflict resolution, synchronization, deployment, or approval"
---
# Sourcetree Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.atlassian.com/software/sourcetree
- https://support.atlassian.com/sourcetree/docs/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Sourcetree repository change and recovery review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before clone private repositories, stage or commit files, rewrite history, merge or rebase branches, push, force push, change remotes, store credentials, run custom actions, or represent conflict resolution, synchronization, deployment, or approval.

## Guardrails

- Do not invent repository identity or state, file ownership, diff correctness, credential safety, merge result, history rewrite, remote synchronization, deployment, release status, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
