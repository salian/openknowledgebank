---
type: Command
title: /review-kano-features
description: Declarative contract for Kano Model work with source discipline and local evidence separation.
okb_bundle_id: kano-model
timestamp: "2026-07-09T00:00:00Z"
---

# /review-kano-features

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce a source-aware Kano Model plan, review, or brief that separates official source categories from local evidence.

## Inputs

- User question and decision to support.
- Local evidence: ['feature list, customer segment, functional/dysfunctional survey wording, response data, sample size, product context, current expectations, and decision criteria'].
- Any proposed change, publication, commitment, export, or live action.

## Output Contract

Return: `Source note`, `Direct answer`, `Evidence map`, `Findings`, `Risks`, `Recommended next step`, and `Confirmation needed`.

## Risk Boundary

Do not proceed with labeling features as must-be, performance, attractive, indifferent, reverse, or questionable without validated customer research without explicit user confirmation.
