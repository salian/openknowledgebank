---
type: Reference
title: QuickBooks Online Source Checks
description: "Official source categories and local evidence checks for QuickBooks Online work."
okb_bundle_id: quickbooks-online
resource:
  - https://developer.intuit.com/app/developer/qbo/docs/develop
  - https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api
  - https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
  - https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/manage-your-sandboxes
  - https://developer.intuit.com/app/developer/qbo/docs/develop/webhooks
  - https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/data-queries
timestamp: "2026-07-09T00:00:00Z"
---

# QuickBooks Online Source Checks

Use current official Intuit sources for source-sensitive QuickBooks Online work:

- QuickBooks Online product documentation for UI/product behavior.
- Intuit Developer QuickBooks Online Accounting API documentation for app-development behavior.
- QuickBooks Online API Explorer for current entities, fields, operations, and parameters.
- OAuth 2.0 documentation for authorization flow and app access.
- Sandbox documentation for test companies and environment boundaries.
- Webhook documentation for callback planning and verification.
- Query documentation for SQL-like query limitations.

## Local Evidence Checks

Ask the user for the relevant company evidence before concluding:

- company, region, plan/SKU, permissions, enabled features, accounting basis, fiscal year, closing date, and currency;
- chart of accounts, classes, locations, products/services, customers, vendors, employees, tax agencies/codes, custom fields, and list state;
- report name, date range, accounting basis, filters, grouping, export method, timestamp, and owner;
- transaction samples, invoices, bills, payments, deposits, refunds, credit memos, journal entries, voids, deletes, attachments, and audit/change evidence;
- bank-feed, reconciliation, payment, payroll, sales-tax, app, automation, webhook, and integration configuration;
- API app/environment/scope evidence, sandbox tests, entity/operation references, payload examples from current docs, and rate-limit/minor-version checks.

## Do Not Treat As Verified

- A generic QuickBooks concept without user company evidence.
- A sandbox test as production proof.
- An API example as permission to run production calls.
- An ecommerce, bank, payroll, payment, CRM, or BI total as automatically matching QuickBooks definitions.
- A tax, payroll, sales-tax, or accounting treatment as final without qualified review.
