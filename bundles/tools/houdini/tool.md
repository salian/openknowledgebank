---
type: "Tool Guide"
title: "SideFX Houdini"
description: "Source-aware guidance for SideFX Houdini."
resource: "https://www.sidefx.com/products/houdini/"
okb_bundle_id: houdini
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Procedural 3D modeling, animation, simulation, rendering, and pipeline platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "modify production scenes or assets, run simulations or renders, distribute jobs, install plug-ins, consume licenses or compute, publish media, overwrite outputs, or represent quality or delivery"
---
# SideFX Houdini Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.sidefx.com/products/houdini/
- https://www.sidefx.com/docs/houdini/basics/intro.html

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current SideFX documentation for the Houdini version, edition, renderer, engine, and plug-in.
- Project, scene, node graph, asset, geometry, cache, simulation, material, render, dependency, color, license, output, and log state.
- Asset rights, technical review, render tests, resource budget, rollback, and delivery approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Houdini procedural production and render review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before modify production scenes or assets, run simulations or renders, distribute jobs, install plug-ins, consume licenses or compute, publish media, overwrite outputs, or represent quality or delivery.

## Guardrails

- Do not invent asset ownership, scene or node state, cache validity, simulation accuracy, render settings, color result, plug-in safety, license entitlement, resource use, output quality, delivery, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
