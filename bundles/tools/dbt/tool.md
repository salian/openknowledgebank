---
type: Tool Guide
title: "dbt (Data Build Tool)"
description: "Defines source-aware analytics engineering and data transformation, evidence handling, and action boundaries."
tool_category: "Data transformation framework"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review analytics engineering and data transformation from supplied evidence."
  - "Draft a dbt transformation and review brief with explicit evidence states."
confirmation_required:
  - "running production jobs, changing models or contracts, modifying targets, deploying packages, or altering warehouse objects"
okb_bundle_id: dbt
timestamp: "2026-07-31T00:00:00Z"
---

# dbt (Data Build Tool)

Source-aware tool bundle for dbt projects, models, sources, tests, lineage, runs, artifacts, environments, and controlled transformation briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- dbt product and version
- project, packages, adapter, profile, and target
- models, sources, seeds, snapshots, macros, and exposures
- properties, contracts, tests, and documentation
- selection syntax and invocation parameters
- manifest, run results, catalog, logs, and lineage
- warehouse permissions, deployment, and approval evidence

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before running production jobs, changing models or contracts, modifying targets, deploying packages, or altering warehouse objects.
