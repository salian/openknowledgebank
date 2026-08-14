---
type: "Tool Guide"
title: "Penpot"
description: "Source-aware guidance for Penpot."
resource: "https://help.penpot.app/"
okb_bundle_id: penpot
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Open-source collaborative design, prototyping, code-handoff, and self-hosted platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload protected assets, edit shared designs or libraries, publish prototypes, run plugins, expose tokens, change team access, export production assets, deploy or upgrade servers, or represent design fidelity, accessibility, code quality, rights, or availability"
---
# Penpot Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.penpot.app/
- https://penpot.app/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Penpot design-system and deployment review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload protected assets, edit shared designs or libraries, publish prototypes, run plugins, expose tokens, change team access, export production assets, deploy or upgrade servers, or represent design fidelity, accessibility, code quality, rights, or availability.

## Guardrails

- Do not invent asset ownership, design version, component or token state, prototype behavior, accessibility, generated code correctness, plugin safety, permission, export fidelity, backup validity, uptime, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
