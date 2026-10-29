---
id: "KNW-authentication"
title: "Authentication implementation"
status: verified
owner: "Platform team"
created_at: "2026-09-01"
updated_at: "2026-09-01"
requirements: ["REQ-00001"]
decisions: ["ADR-00001"]
components: ["src/auth.py"]
---

# Authentication implementation

## Overview

Authentication uses the provider package through a Python adapter.

## Current implementation

`AuthProvider.authenticate` passes the Authorization header to the configured provider's `verify` method.

## Known limitations

The fixture does not include a real provider package or deployment configuration.
