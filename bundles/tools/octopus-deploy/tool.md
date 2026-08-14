---
type: "Tool Guide"
title: "Octopus Deploy"
description: "Source-aware guidance for Octopus Deploy."
resource: "https://octopus.com/docs/"
okb_bundle_id: octopus-deploy
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Continuous deployment, release orchestration, runbook, and operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or deploy releases, run runbooks, change variables, secrets, targets, lifecycles or permissions, call production APIs, execute scripts, promote packages, upgrade servers, or represent deployment, rollback, security, or service health"
---
# Octopus Deploy Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://octopus.com/docs/
- https://octopus.com/docs/octopus-rest-api

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Octopus Deploy release and runbook review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or deploy releases, run runbooks, change variables, secrets, targets, lifecycles or permissions, call production APIs, execute scripts, promote packages, upgrade servers, or represent deployment, rollback, security, or service health.

## Guardrails

- Do not invent space or project state, package provenance, variable or secret value, target health, approval, deployment execution, runbook result, environment state, rollback validity, API result, service availability, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
