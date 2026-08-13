---
type: "Tool Guide"
title: "Superhuman Docs (formerly Coda)"
description: "Source-aware guidance for Superhuman Docs (formerly Coda)."
resource: "https://docs.superhuman.com/developers/apis/v1"
okb_bundle_id: coda
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Collaborative docs and structured workspace platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create, update, share, publish or delete docs, pages, tables or rows, run automations, install packs, connect API or MCP, expose data, or represent queued writes as complete"
---
# Superhuman Docs (formerly Coda) Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.superhuman.com/developers/apis/v1

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Superhuman Docs (formerly Coda) configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create, update, share, publish or delete docs, pages, tables or rows, run automations, install packs, connect API or MCP, expose data, or represent queued writes as complete.

## Guardrails

- Do not invent migration or product applicability, document contents, formula correctness, snapshot freshness, collaborator authority, queued mutation outcome, automation result, publication, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
