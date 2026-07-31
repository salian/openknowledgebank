---
type: Workflow
title: Ansible source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: Ansible core and collection versions; control node, inventory source, groups, hosts, variables, precedence, and target scope; playbooks, roles, modules, templates, handlers, tags, limits, and configuration; desired and observed state, check and diff output, idempotence tests, credentials, vault and secret handling, logs, rollback, and approval.
3. Label each item verified, provided, assumed, or needs verification.
4. Reconcile definitions, identifiers, dates, versions, scopes, permissions, filters, states, calculations, processing, and owners.
5. Produce the smallest reviewable Ansible change plan.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with `Prompt-provided request` under `Provided`
- **Verification plan** with source, local record, scope, date or version, and conflict checks
- **Confirmation boundary** with evidenced reviewer or `Needs verification`
- **Source note** with applicable authoritative URLs and limitations
