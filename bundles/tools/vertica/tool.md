---
type: "Tool Guide"
title: "OpenText Vertica"
description: "Source-aware guidance for OpenText Vertica."
resource: "https://docs.vertica.com/latest/"
okb_bundle_id: vertica
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Columnar analytic database, SQL, workload, security, Eon, deployment, backup, and recovery platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect or expose data, execute queries or DDL, load or delete records, alter projections, privileges or resource pools, upgrade clusters, back up or restore data, or represent schema, query, performance, durability, security, availability, or recovery"
---
# OpenText Vertica Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://docs.vertica.com/latest/
- https://www.opentext.com/products/vertica-data-platform

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable OpenText Vertica architecture, performance, and recovery review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect or expose data, execute queries or DDL, load or delete records, alter projections, privileges or resource pools, upgrade clusters, back up or restore data, or represent schema, query, performance, durability, security, availability, or recovery.

## Guardrails

- Do not invent version or deployment applicability, schema, data completeness or freshness, query correctness, projection state, privilege, performance, backup or restore, durability, security, availability, recovery, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
