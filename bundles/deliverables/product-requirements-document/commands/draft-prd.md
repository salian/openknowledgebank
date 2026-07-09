---
type: Command
title: /draft-prd
description: Declarative contract for Product Requirements Document (PRD) work with source discipline and local evidence separation.
okb_bundle_id: product-requirements-document
timestamp: "2026-07-09T00:00:00Z"
---

# /draft-prd

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce a source-aware Product Requirements Document (PRD) plan, review, or brief that separates official source categories from local evidence.

## Inputs

- User question and decision to support.
- Local evidence: ['problem statement, customer evidence, goals, non-goals, users, requirements, constraints, designs, dependencies, metrics, rollout plan, approvals, and open questions'].
- Any proposed change, publication, commitment, export, or live action.

## Output Contract

Return: `Source note`, `Direct answer`, `Evidence map`, `Findings`, `Risks`, `Recommended next step`, and `Confirmation needed`.

## Risk Boundary

Do not proceed with turning draft requirements into engineering, customer, legal, launch, or roadmap commitments without stakeholder review and evidence without explicit user confirmation.
