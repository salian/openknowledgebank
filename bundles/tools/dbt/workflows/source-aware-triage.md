---
type: Workflow
title: "dbt (Data Build Tool) source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: dbt product and version, project, packages, adapter, profile, and target, models, sources, seeds, snapshots, macros, and exposures, properties, contracts, tests, and documentation, selection syntax and invocation parameters, manifest, run results, catalog, logs, and lineage, and warehouse permissions, deployment, and approval evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, and owners.
5. Produce the smallest reviewable dbt transformation and review brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations
