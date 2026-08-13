---
type: "Tool Guide"
title: "Conga CLM"
description: "Source-aware guidance for Conga CLM."
resource: "https://conga.com/products/conga-clm"
okb_bundle_id: conga-clm
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Contract lifecycle management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "generate, modify, approve, send or execute contracts, accept AI redlines, change clause or playbook controls, expose privileged information, trigger signatures, or represent enforceability or compliance"
---
# Conga CLM Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://conga.com/products/conga-clm

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Conga CLM configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before generate, modify, approve, send or execute contracts, accept AI redlines, change clause or playbook controls, expose privileged information, trigger signatures, or represent enforceability or compliance.

## Guardrails

- Do not invent party identity or authority, contract version, extracted term, clause risk, legal interpretation, obligation or renewal status, approval, signature validity, enforceability, or compliance.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
