---
type: Tool Guide
title: "Terraform"
description: "Defines source-aware infrastructure as code planning and review, evidence handling, and action boundaries."
tool_category: "Infrastructure as code"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review infrastructure as code planning and review from supplied evidence."
  - "Draft a terraform plan and change brief with explicit evidence states."
confirmation_required:
  - "initializing untrusted code, changing state or backends, applying plans, replacing or destroying resources, or exposing credentials"
okb_bundle_id: terraform
timestamp: "2026-07-31T00:00:00Z"
---

# Terraform

Source-aware tool bundle for Terraform configuration, providers, state, plans, workspaces, modules, policy, and controlled infrastructure change briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- Terraform and provider versions
- configuration, modules, variables, and outputs
- backend, workspace, state, and lock evidence
- provider schemas and credentials boundaries
- plan file, refresh behavior, and proposed actions
- policy, cost, dependency, and drift evidence
- apply, rollback, and approval controls

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before initializing untrusted code, changing state or backends, applying plans, replacing or destroying resources, or exposing credentials.
