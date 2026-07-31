---
type: Workflow
title: Azure Data Factory source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: tenant, subscription, resource group, factory, region, environment, and API version; pipeline, activity, dataset, linked service, integration runtime, trigger, parameter, expression, dependency, source and sink contracts; identity, RBAC, networking, credentials, Key Vault, data classification, Git and deployment state, tests, run history, monitoring, alerts, costs, rollback, and approvals.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Azure Data Factory change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
