---
type: Bundle Index
title: Cash Flow Forecast
description: Source-aware deliverable bundle for building and reviewing evidence-backed cash projections, liquidity headroom, scenarios, and forecast variance.
schema_version: 0.1.0
bundle_format: okf-compatible
category: deliverables
tags:
- cash flow forecast
- liquidity planning
- treasury
- working capital
- financial forecasting
aliases:
- Cash Flow Projection
- Liquidity Forecast
- Rolling Cash Forecast
problems_solved:
- Project cash receipts, payments, and ending balances from supported timing assumptions.
- Reconcile forecast cash and distinguish cash balance from available liquidity and headroom.
- Expose unsupported assumptions, downside scenarios, forecast variance, and decision status.
industries:
- financial services
- corporate finance
- software
- professional services
tools: []
frameworks:
- direct cash forecasting
- assumption and evidence register
- forecast-versus-actual variance analysis
deliverables:
- rolling cash flow forecast
- liquidity and headroom view
- scenario and variance report
commands: []
skills: []
evaluations:
- Cash Flow Forecast quality check
okb_bundle_id: cash-flow-forecast
okb_bundle_version: 0.1.0
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- treasury-analyst-corporate-treasurer
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc: []
  soc: []
  isco_08: []
  esco: []
limitations:
- This bundle is a forecasting and review aid, not accounting, investment, legal, or financing advice; audit assurance; a solvency opinion; or a guarantee of future cash.
- Horizon, cadence, method, categories, cash definition, currencies, facilities, covenants, thresholds, and scenarios must be tailored from current local evidence.
- Balances, transactions, timing, assumptions, actuals, facility availability, headroom, approvals, mitigations, and forecast accuracy require supplied evidence.
safety_notes:
- Protect bank, counterparty, payroll, tax, facility, covenant, and commercially sensitive information.
- Require accountable authorization before transfers, borrowing, investments, collection changes, supplier-payment changes, or external communication.
- Route material liquidity, covenant, going-concern, insolvency, or regulated-reporting questions to qualified finance, treasury, accounting, and legal reviewers.
timestamp: '2026-08-07T00:00:00Z'
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No reviewed public-safe benchmark task set, runnable evaluator configuration, or reviewer-scored aggregate results were available for this run.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Create and approve three public-safe tasks covering empty evidence, conflicting opening balances, and an unapproved facility draw; configure matched baseline and bundle-assisted runs; obtain reviewer-scored aggregate results; and build a listing scorecard.
---

# Cash Flow Forecast

Use this bundle to build and review a cash projection from identified balances, expected receipts and payments, timing assumptions, liquidity constraints, and actual evidence.

Start with the [deliverable contract](deliverable.md), follow the [forecast workflow](workflow.md), and apply the [quality check](evaluations/quality-check.md).

This bundle does not move money, arrange financing, change collection or payment behavior, certify liquidity, or establish that a forecast will occur.
