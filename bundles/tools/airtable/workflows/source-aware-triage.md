---
type: Workflow
title: Airtable source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: workspace, base, table, field, view, interface, form, and record IDs; schema, field types, formulas, linked records, filters, sorting, permissions, collaborators, personal or OAuth token scopes, API pagination and limits, automations, integrations, webhooks, source-of-record rules, snapshots, tests, and approvals.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Airtable base change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
