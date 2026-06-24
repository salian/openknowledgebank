---
type: Slash Command
command: /reconcile-stackoverflow-sources
title: Reconcile Stack Overflow Sources
description: Explain discrepancies between Stack Overflow source counts.
okb_bundle_id: stackoverflow-data-analyst
inputs: [sources, counts, queries, filters, run times]
outputs: [source reconciliation note]
requires_confirmation: false
timestamp: 2026-06-24T00:00:00Z
---

# /reconcile-stackoverflow-sources

Use [reconcile sources](../workflows/reconcile-sources.md) and output a [source reconciliation note](../deliverables/source-reconciliation-note.md).

## Required Behavior

- Do not pick a winner prematurely.
- Align source definitions first.
- Request exact query/filter evidence.
- Recommend a source of record only for the user's decision context.
