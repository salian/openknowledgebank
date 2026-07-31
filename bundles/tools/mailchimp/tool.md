---
type: Tool Guide
title: "Mailchimp"
description: "Defines source-aware email marketing and audience operations, evidence handling, and action boundaries."
tool_category: "email marketing and audience operations"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review email marketing and audience operations from supplied evidence."
  - "Draft a mailchimp campaign and audience brief with explicit evidence states."
confirmation_required:
  - "sending or publishing campaigns, modifying contacts or consent, changing audiences or automations, changing domains, or committing spend"
okb_bundle_id: mailchimp
timestamp: "2026-07-31T00:00:00Z"
---

# Mailchimp

Source-aware tool bundle for Mailchimp audiences, consent, segments, campaigns, templates, journeys, senders, reports, integrations, and controlled sends.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- account and plan
- audience, contact, consent, and subscription status
- segments and tags
- campaign, template, and content versions
- journeys and automations
- domains, senders, reports, attribution, and integrations

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer consent, contact status, segment membership, delivery outcome, attribution, and domain authentication.
- Require accountable confirmation before sending or publishing campaigns, modifying contacts or consent, changing audiences or automations, changing domains, or committing spend.
