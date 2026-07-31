---
type: Workflow
title: monday.com source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: account, product, workspace, board, item, subitem, column, view, dashboard, document, and user IDs; schema, permissions, teams, guests, token type and scopes, API version, GraphQL query or mutation, complexity, pagination, automations, integrations, webhooks, source-of-record rules, audit logs, tests, and approvals.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable monday.com workflow change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
