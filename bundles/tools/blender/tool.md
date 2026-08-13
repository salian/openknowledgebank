---
type: "Tool Guide"
title: "Blender"
description: "Source-aware guidance for Blender."
resource: "https://www.blender.org/"
okb_bundle_id: blender
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Open-source 3D creation suite"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "run untrusted scripts or add-ons, modify or overwrite production files, bake simulations, render at material cost, export assets, publish work, or represent rights or quality approval"
---
# Blender Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.blender.org/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Blender configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before run untrusted scripts or add-ons, modify or overwrite production files, bake simulations, render at material cost, export assets, publish work, or represent rights or quality approval.

## Guardrails

- Do not invent scene state, asset provenance or rights, script safety, compatibility, simulation or render result, color fidelity, output quality, publication, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
