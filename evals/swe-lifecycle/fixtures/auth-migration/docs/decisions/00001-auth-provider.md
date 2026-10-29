---
id: "ADR-00001"
title: "Use the current provider package"
status: accepted
owner: "Security team"
created_at: "2026-09-01"
updated_at: "2026-09-01"
supersedes: []
superseded_by: []
---

# Use the current provider package

## Context

The service needs a maintained authentication provider behind the Python adapter.

## Decision

Use the provider package called by `src/auth.py`.

## Consequences

The adapter delegates credential verification to the package. The security team owns provider changes.
