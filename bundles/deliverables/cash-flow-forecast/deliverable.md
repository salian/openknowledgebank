---
type: Deliverable
title: Cash Flow Forecast Package
description: Defines the evidence, timing, reconciliation, assumption, scenario, variance, liquidity, and decision-status contract for a reviewable cash forecast.
okb_bundle_id: cash-flow-forecast
required_inputs:
- entity, perimeter, currency, cash definition, opening balance, and forecast period
- expected receipts and payments with sources and timing drivers
- facilities, restrictions, minimum cash, covenants, and scenarios when applicable
- actual cash records, owners, review criteria, and approvals when available
outputs:
- period-by-period cash flow forecast
- assumption and evidence register
- liquidity, headroom, scenario, and variance report
- risks, gaps, proposed actions, owners, and review status
quality_criteria:
- each material cash flow traces to a source or explicit assumption
- opening cash, movements, and ending cash reconcile for every period
- forecast, actual, cash, available liquidity, approval, and execution states remain distinct
resource: https://www.gov.uk/government/publications/college-management-accounts-good-practice-guide/management-accounts-good-practice-guide-for-colleges
timestamp: '2026-08-07T00:00:00Z'
---

# Cash Flow Forecast Package

## Output Contract

1. **Document control:** identify entity and consolidation perimeter, reporting and functional currencies, cash definition, included accounts, forecast start, horizon, cadence, cut-off, version, preparation date, owner, reviewer, and status only when evidenced.
2. **Source note:** distinguish external references from local evidence: bank and ledger balances, receivables, payables, payroll, tax, capital, financing, investment, intercompany, FX, contract, budget, and approval records.
3. **Evidence status:** list `Verified`, `Provided`, `Assumed`, and `Needs verification`. With no local evidence, set the first three to `None` except facts explicitly supplied in the request.
4. **Opening position:** reconcile the opening balance to named source records at a stated timestamp. Show restricted cash, cash equivalents, overdrafts, and excluded accounts separately when applicable; do not assume they are available.
5. **Forecast schedule:** for each period show opening cash, receipt categories, payment categories, internal transfers or eliminations, relevant FX effects, net change, and ending cash. The core arithmetic is `opening cash + inflows - outflows +/- separately identified reconciling effects = ending cash`.
6. **Flow detail:** for each material line record category, counterparty or driver at an appropriate confidentiality level, amount, currency, expected date or period, source, timing rule, confidence or uncertainty, owner, and last update. Avoid unsupported flat spreading.
7. **Assumption register:** record each assumption, source, rationale, applicable periods, dependencies, uncertainty, sensitivity, owner, review date, and whether it is proposed, reviewed, approved, superseded, or unresolved.
8. **Liquidity and headroom:** keep cash balance, unrestricted cash, cash equivalents, available facility, available liquidity, minimum cash, covenant headroom, and excess or shortfall distinct. Facility limits are not available liquidity unless draw conditions, restrictions, usage, and approval are evidenced.
9. **Scenarios and risks:** present a named base case and only evidence-supported alternatives. State the changed drivers, timing, dependencies, thresholds, and resulting cash path. Mark mitigations as proposed, approved, or executed from evidence rather than embedding them as assumed cash flows.
10. **Forecast-versus-actual:** compare a frozen forecast version with actual cash using consistent entity, account, currency, cut-off, category, and timing rules. Explain material timing, amount, classification, scope, and one-off variances without overwriting the original forecast.
11. **Reconciliation and controls:** prove period roll-forward, internal-transfer elimination, currency treatment, subtotal and sign consistency, scenario completeness, and any tie-out to projected balance sheet or historical cash reporting. Keep unresolved differences visible.
12. **Review and decisions:** summarize the lowest cash point, timing and concentration risks, headroom, breaches or near-breaches, data gaps, forecast limitations, proposed decisions, accountable owners, and review status. Separate draft, reviewed, approved, communicated, funded, and executed states.

## Reconciliation Rule

When balances, dates, forecasts, actuals, or systems disagree, neither value is automatically right. Align entity and account perimeter, source timestamp, value date versus posting date, currency and FX rule, gross versus net presentation, sign, category, tax treatment, internal transfers, duplicates, cut-off, version, and scenario. Classify the difference as explained or unresolved; do not create a plug or change an actual to force agreement.

## Source Note

IAS 7 provides context for historical cash and cash-equivalent definitions and operating, investing, and financing classifications; it does not by itself prescribe or validate this forecast. Government guidance supports rolling updates, timing profiles, assumption commentary, reconciliation, sensitivity, headroom, and variance review. Local evidence remains authoritative for every balance, flow, timing rule, facility, threshold, scenario, owner, approval, and action.

## Safety Boundary

This package contains no transaction commands, executable model, credentials, account-access instructions, or financing actions. Transfers, facility draws, investments, collection changes, supplier-payment changes, covenant responses, and external disclosures require explicit accountable authorization and approved systems.
