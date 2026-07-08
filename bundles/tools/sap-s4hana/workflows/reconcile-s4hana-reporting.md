---
type: Workflow
title: Reconcile SAP S/4HANA Reporting Differences
description: "Source-aware workflow for explaining differences between SAP S/4HANA reports, extracts, dashboards, and downstream systems."
okb_bundle_id: sap-s4hana
timestamp: "2026-07-09T00:00:00Z"
---

# Reconcile SAP S/4HANA Reporting Differences

## When To Use

Use this workflow when two SAP S/4HANA reports, analytical apps, extracts, interfaces, or downstream dashboards show different values.

## Reconciliation Pattern

Neither number is automatically right until the source, definition, filter, time, entity, currency, and processing rules are aligned.

## Required Checks

- Source object: app, report, CDS view, API, table/extract, BW object, data lake table, or downstream dashboard.
- Scope: company code, controlling area, plant, sales organization, purchasing organization, ledger, valuation area, profit center, segment, material, customer, vendor, or other entity filter used.
- Time logic: posting date, document date, fiscal period, open/closed period, extraction timestamp, refresh cadence, and currency conversion timing.
- Measure definition: posted value, committed value, planned value, quantity, open item, cleared item, accrual, tax, freight, discount, reversal, or adjustment logic.
- Processing effects: authorization filters, custom fields, extensions, replication lag, interface failures, document status, cancellations, reversals, and manual adjustments.

## Output Requirements

Return:

1. Direct answer: which value is fit for the user's decision, or why the answer is not yet knowable.
2. Definition comparison: what each value measures.
3. Evidence table: source, scope, filters, period, refresh, owner, and missing evidence.
4. Expected differences: legitimate reasons the values may differ.
5. Unresolved discrepancies: what still needs inspection in SAP S/4HANA or downstream systems.
6. Source note: official SAP source categories, user-provided evidence, and missing verification.
