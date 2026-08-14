---
type: "Tool Guide"
title: "Gorgias"
description: "Source-aware guidance for Gorgias."
resource: "https://www.gorgias.com/products/helpdesk"
okb_bundle_id: gorgias
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Ecommerce customer support, automation, and AI agent platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "reply to customers, change or cancel orders, issue refunds or discounts, deploy automation or AI Agent, change routing or access, export data, or represent resolution or performance"
---
# Gorgias Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.gorgias.com/products/helpdesk
- https://docs.gorgias.com/en-US

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current Gorgias product and help documentation for the subscribed products and plan.
- Store, channel, ticket, customer, order, rule, macro, knowledge, AI skill, action, integration, role, and report state.
- Customer privacy, action authorization, test, monitoring, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Gorgias support automation and action review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before reply to customers, change or cancel orders, issue refunds or discounts, deploy automation or AI Agent, change routing or access, export data, or represent resolution or performance.

## Guardrails

- Do not invent customer identity, ticket or order state, policy entitlement, refund or discount authority, response accuracy, AI action, resolution, CSAT, SLA, performance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
