---
type: Example Output
title: Bundle-Assisted Output
okb_bundle_id: quickbooks-online
timestamp: "2026-07-09T00:00:00Z"
---

# Bundle-Assisted Output

Neither number is automatically right yet. The answer depends on what each report measures and whether the source scope, timing, accounting basis, filters, and entity logic match.

Source note: QuickBooks Online guidance should be checked against current Intuit QuickBooks Online product documentation and, if API data is used, Intuit Developer QBO Accounting API/API Explorer sources. Local evidence used: none provided. Missing before conclusion: QuickBooks report name/settings/export, ecommerce report definition, date range, timezone, accounting basis, refund/discount/tax/shipping handling, payment/deposit timing, entity matching rules, and any integration sync evidence.

Plan:

1. Get the QuickBooks report/export and record its report name, accounting basis, date range, filters, grouping, currency, and timestamp.
2. Get the ecommerce report definition and record whether it measures gross orders, net sales, paid orders, shipped orders, refunds, discounts, taxes, shipping, fees, or deposits.
3. Align entity identities: order ID, invoice/sales receipt, customer, product/service, payment, deposit, refund, and credit memo.
4. Compare expected differences first: refunds, voids, discounts, taxes, shipping, payment processor fees, pending orders, deposits crossing month-end, sync lag, manual adjustments, and multi-currency effects.
5. Sample exceptions from the $3,500 gap and trace each from ecommerce source record to QuickBooks transaction and deposit.
6. Do not change QuickBooks records, resend invoices, alter sync settings, or export customer/payment data without explicit approval and a rollback plan.

Current answer: there is not enough evidence to choose one number. Treat the gap as unresolved until the report definitions and source records are aligned.
