---
type: "Tool Guide"
title: "Adobe XD"
description: "Source-aware guidance for Adobe XD."
resource: "https://developer.adobe.com/xd/uxp/"
okb_bundle_id: adobe-xd
timestamp: "2026-08-12T00:00:00Z"
tool_category: "Legacy design and prototyping software"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "recommend new adoption without lifecycle verification, run plugins, modify or export files, migrate assets, publish prototypes, or represent migration completeness"
---
# Adobe XD Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.adobe.com/xd/uxp/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Adobe XD configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before recommend new adoption without lifecycle verification, run plugins, modify or export files, migrate assets, publish prototypes, or represent migration completeness.

## Guardrails

- Do not invent current support status, document fidelity, plugin compatibility, asset rights, prototype state, migration result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
