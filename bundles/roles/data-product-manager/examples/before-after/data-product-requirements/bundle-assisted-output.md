---
type: Example Output
title: Bundle-Assisted Output
description: Illustrative bundle-assisted output.
okb_bundle_id: data-product-manager
timestamp: 2026-07-09T00:00:00Z
---

# Bundle-Assisted Output

Recommendation: draft a discovery-stage data product PRD, not an implementation-ready specification, because the source schemas, metric definitions, data owners, quality thresholds, privacy classification, and source-of-record policy are missing.

Source note: user provided the target consumer and broad use case only. Needed sources include CRM/account schema, product usage event definitions, support-ticket source, contract/revenue source, existing health-score definitions, access policy, privacy classification, data quality checks, and owner approvals.

## Requirements Draft

- Consumers: customer success managers.
- Decision supported: identify accounts needing intervention.
- Outcome: improve renewal and support prioritization, pending source-supported success metrics.
- Scope: define candidate inputs, trust requirements, and review workflow.
- Non-goals: final scoring formula, production schema, and automated actioning until source evidence is reviewed.
- Acceptance criteria: each input has an owner, source, definition, refresh expectation, quality check, privacy classification, and known limitation.
- Risks: false churn signals, sensitive customer data exposure, stale data, unclear account identity logic, and unsupported automation.
- Next decisions: confirm owner, source systems, metric definitions, quality thresholds, access rules, and launch criteria.
