---
type: "Tool Guide"
title: "Sketch"
description: "Source-aware guidance for Sketch."
resource: "https://www.sketch.com/docs/"
okb_bundle_id: sketch
timestamp: "2026-08-14T00:00:00Z"
tool_category: "macOS product design, prototyping, collaboration, developer handoff, and plugin platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "upload confidential designs, change shared libraries, publish documents, install plugins, execute scripts, grant access, export protected assets, or represent authorship, rights, accessibility, implementation fidelity, review, or approval"
---
# Sketch Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.sketch.com/docs/
- https://developer.sketch.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Sketch design-system and handoff review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before upload confidential designs, change shared libraries, publish documents, install plugins, execute scripts, grant access, export protected assets, or represent authorship, rights, accessibility, implementation fidelity, review, or approval.

## Guardrails

- Do not invent document or library state, asset ownership, permission, plugin safety, export fidelity, prototype behavior, accessibility, implementation result, rights, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
