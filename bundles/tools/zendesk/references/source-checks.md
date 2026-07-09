---
type: Reference
title: Zendesk Source Checks
description: "Official source categories and local evidence checks for Zendesk work."
okb_bundle_id: zendesk
resource:
  - https://developer.zendesk.com/api-reference/
  - https://support.zendesk.com/
timestamp: "2026-07-09T00:00:00Z"
---

# Zendesk Source Checks

## Official Source Categories

- Zendesk Help for product behavior, Admin Center tasks, ticketing, business rules, Help Center, AI agents, reporting, and support operations concepts.
- Zendesk Developer documentation for APIs, authentication, endpoints, payloads, pagination, side-loading, apps, webhooks, and integrations.
- Zendesk release, product, commercial, and packaging pages when current availability, pricing, plan, add-on, or limit claims matter.
- User-provided Zendesk account evidence for local configuration and actual behavior.

## Inspect Before Claiming

- Account subdomain, products, plan, add-ons, brands, channels, enabled features, and release context.
- Ticket fields, forms, statuses, tags, users, groups, organizations, roles, permissions, views, macros, triggers, automations, SLAs, routing, apps, webhooks, and integrations.
- Help Center brands, articles, locales, user segments, permissions, publishing state, knowledge sources, and AI agent connections.
- AI agent configuration, tone, languages, channels, actions, handoff, escalation, test evidence, monitoring, and approval.
- Explore/report/dashboard datasets, metrics, filters, ownership, sharing, schedules, time zones, and export logic.
- API endpoint, version, auth scope, integration user, payload, pagination, rate limit, and data-handling constraints.

## Source Note Pattern

```text
Source note: Zendesk source category checked: [Help / Developer docs / release or commercial page / user-provided account evidence]. Local evidence used: [specific evidence]. Still needed before action or conclusion: [missing doc check, account evidence, approval, test, security/privacy/compliance/AI review].
```

## Red Flags

- The plan names ticket fields, groups, organizations, trigger order, automations, report filters, AI settings, API payloads, or permissions without account evidence.
- The output treats a Zendesk Help page as proof that the user's account has the feature enabled.
- The output recommends live changes, customer messages, exports, API calls, or AI activation without explicit confirmation.
- The output reconciles metrics without checking dataset, filters, time zone, status logic, requester/assignee/group logic, deduplication, snapshots, and freshness.
