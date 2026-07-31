---
type: Tool Guide
title: Ansible
description: Defines source-aware Ansible inventory, playbook, role, configuration, validation, and controlled execution, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Ansible change plan with explicit evidence states.
confirmation_required:
- decrypt secrets, connect to hosts, run a playbook or ad hoc command, change infrastructure, install collections, or alter inventory
okb_bundle_id: ansible
timestamp: '2026-07-31T00:00:00Z'
---
# Ansible

Source-aware tool bundle for Ansible inventory, playbook, role, configuration, validation, and controlled execution, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://www.redhat.com/en/technologies/management/ansible
- https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html
- https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_vault.html

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- Ansible core and collection versions
- control node, inventory source, groups, hosts, variables, precedence, and target scope
- playbooks, roles, modules, templates, handlers, tags, limits, and configuration
- desired and observed state, check and diff output, idempotence tests, credentials, vault and secret handling, logs, rollback, and approval

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer inventory contents, target state, reachability, module support, check-mode fidelity, idempotence, execution result, or rollback success.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that decrypt secrets, connect to hosts, run a playbook or ad hoc command, change infrastructure, install collections, or alter inventory.
