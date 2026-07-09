---
type: Workflow
title: Reconcile QuickBooks Online Report or API Data
description: "Compare QuickBooks Online reports, exports, API data, and external-system totals without assuming either number is automatically right."
okb_bundle_id: quickbooks-online
timestamp: "2026-07-09T00:00:00Z"
---

# Reconcile QuickBooks Online Report or API Data

Use this workflow when a QuickBooks Online report/export/API value differs from another QuickBooks value or an external system.

## Required Evidence

- QuickBooks Online report name/export/API query, date range, accounting basis, filters, grouping, currency, timezone, and refresh timing.
- Source system report/query definition and timestamp.
- Entity identity rules: customer, vendor, item/product, account, invoice, bill, payment, deposit, tax, class, location, order, or transaction identifiers.
- Treatment of voids, deletes, credits, refunds, deposits, unapplied payments, discounts, fees, taxes, multi-currency, sync failures, and manual journal entries when relevant.
- User confirmation of whether sandbox/test evidence or production evidence is being used.

## Reconciliation Pattern

- State that neither value is automatically right until definitions, inputs, settings, and methods are aligned.
- Define what each value measures.
- Compare source scope, date range, accounting basis, filters, entity matching, aggregation, currency, timing, and refresh logic.
- Separate expected differences from unresolved discrepancies.
- Require current Intuit documentation or API Explorer inspection before relying on exact API fields, operations, query syntax, minor-version behavior, or limits.

## Output Shape

Return a concise reconciliation brief with:

- direct answer on whether the discrepancy is explainable from the evidence;
- source note;
- definition table for each compared value;
- aligned comparison plan;
- expected-difference list;
- unresolved discrepancy list;
- validation sample and next evidence request;
- confirmation boundary before changing records, settings, integrations, or reports.
