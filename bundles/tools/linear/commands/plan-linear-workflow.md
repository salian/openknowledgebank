---
type: Command
title: /plan-linear-workflow
description: Declarative contract for Linear work with source discipline and local evidence separation.
okb_bundle_id: linear
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-linear-workflow

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce a source-aware Linear plan, review, or brief that separates official source categories from local evidence.

## Inputs

- User question and decision to support.
- Local evidence: ['workspace, team, issue, project, cycle, label, status, priority, assignee, estimate, dependency, automation, Git integration, and API permission evidence'].
- Any proposed change, publication, commitment, export, or live action.

## Output Contract

Return: `Source note`, `Direct answer`, `Evidence map`, `Findings`, `Risks`, `Recommended next step`, and `Confirmation needed`.

## Risk Boundary

Do not proceed with creating, editing, assigning, closing, deleting, importing, exporting, or automating Linear issues, projects, cycles, teams, comments, integrations, webhooks, or API actions without explicit user confirmation.
