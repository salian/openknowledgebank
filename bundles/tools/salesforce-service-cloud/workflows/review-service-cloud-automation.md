---
type: Workflow
title: Review Service Cloud Automation
description: "Review Salesforce Service Cloud automation plans before changing production behavior."
okb_bundle_id: salesforce-service-cloud
timestamp: "2026-07-09T00:00:00Z"
---

# Review Service Cloud Automation

## Purpose

Evaluate a proposed Flow, assignment rule, escalation rule, entitlement/milestone rule, macro, quick action, integration, or AI/customer-facing automation change before it affects customers or support agents.

## Evidence to Inspect First

- Current official Salesforce source category for the feature being changed.
- Existing active and draft automation definitions from the user's org.
- Entry criteria, object/field dependencies, record types, channels, user context, permission requirements, and downstream side effects.
- Test records, sandbox evidence, owner approvals, deployment plan, and rollback plan.
- Privacy, security, compliance, retention, and customer communication policy where customer data or AI behavior is involved.

## Output Shape

1. Source note.
2. Readiness answer: ready, ready with gaps, or not ready.
3. Dependency map: objects, fields, users, permissions, records, reports, integrations, and automations touched.
4. Risk review: duplicate automation, recursion, bulk behavior, limits, customer impact, reporting impact, and data exposure.
5. Test plan: sandbox setup, sample records, expected outcomes, negative cases, regression checks, and monitoring.
6. Deployment plan: approver, change window, backup/export evidence, activation steps, communication plan, and rollback steps.
7. Confirmation boundary: actions that require explicit approval before execution.

## Safety Boundary

Production automation changes are risky. Treat recommendations as review material until an authorized Salesforce owner confirms the change, verifies the source evidence, and approves execution.
