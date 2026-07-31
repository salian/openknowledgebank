---
type: Workflow
title: "Terraform source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: Terraform and provider versions, configuration, modules, variables, and outputs, backend, workspace, state, and lock evidence, provider schemas and credentials boundaries, plan file, refresh behavior, and proposed actions, policy, cost, dependency, and drift evidence, and apply, rollback, and approval controls.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, and owners.
5. Produce the smallest reviewable terraform plan and change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations
