# Reproducibility and Data Governance

## Overview
Reproducibility and auditability are foundational standards of credible data analysis:
- **Reproducibility**: The same analysis can be rerun from sufficiently specified inputs, transformations, code, definitions, and environment. Exact numerical equality may depend on whether source systems are immutable, whether retroactive data corrections occur, and whether environment dependencies and random seeds are strictly pinned.
- **Auditability**: Another analyst or auditor can clearly understand where data originated, what transformations occurred, what assumptions were made, and why specific conclusions were reached.
- **Data Governance**: Ensures data assets are managed ethically, securely, compliantly, and transparently throughout their lifecycle.

## The Reproducibility and Auditability Standard

Every analytical deliverable (memo, report, model, dashboard) must preserve an audit trail satisfying four core pillars:

### 1. Source Data Provenance and Versioning
- Record the exact system of record, database name, and table versions queried.
- Document extraction timestamps and temporal query filter boundaries:
  ```text
  Source: warehouse.analytics.fct_orders
  Extraction Timestamp: 2025-06-15T09:30:00Z
  Filter Bounds: order_date >= '2025-01-01' AND order_date < '2025-06-01'
  Record Count: 142,518 rows
  ```
- If analyzing static extracts (CSV/Parquet), archive the immutable snapshot with a cryptographic hash (SHA-256) or store in versioned object storage (S3/GCS). Note that live production tables often undergo retroactive updates or late-arriving data; exact reproducibility requires point-in-time snapshots or immutable table partitions.

### 2. Query and Code Preservation
- **Preserve Verbatim SQL**: Check raw SQL extraction scripts into Git version control. Never rely on temporary scratchpads or unversioned client query tabs.
- **Deterministic Operations**: Set explicit random seeds (`random_state=42`) when executing stochastic algorithms (e.g., bootstrap resampling, train/test splitting).
- **Environment and Dependency Tracking**: Document software library versions (e.g., `requirements.txt`, `environment.yml`) to prevent subtle numerical drift caused by library updates.

### 3. Transformation Transparency
- Document every step of data cleansing, typecasting, filtering, and imputation.
- Record the count and percentage of rows affected by each data quality filter (e.g., *"Excluded 312 test accounts (0.22% of rows) with internal email domains"*).
- Never perform manual in-place edits in spreadsheets without formula preservation and an accompanying change log.

### 4. Assumptions and Limitations Documentation
- State all domain assumptions explicitly (e.g., currency exchange rates used, fiscal calendar definitions).
- Proactively document analytical limitations, unmeasured confounding variables, and boundary conditions that constrain the generalizability of findings.

## Data Governance and Compliance

### 1. Data Ownership and Stewardship
- **Data Owner**: Executive or business lead accountable for the definition, access approval, and business integrity of a data domain (e.g., VP of Finance for billing tables).
- **Data Steward**: Technical or analytical custodian responsible for data quality rules, metadata definitions, schema consistency, and lineage mapping.

### 2. Privacy and Personally Identifiable Information (PII)
- **PII Definition**: Any information that can identify an individual directly (name, email, phone, SSN) or indirectly (IP address, device UUID, precise geolocation).
- **The Data Minimization Principle (Hard Rule)**: Only query, extract, and analyze the minimum PII strictly necessary to answer the analytical question.
- **Privacy Preservation Techniques**:
  - **Pseudonymization / Hashing**: Replace raw user identifiers with salted one-way hashes (`SHA256(user_id + salt)`).
  - **Masking / Truncation**: Display only partial strings (e.g., `user@*****.com`, credit card `****-1234`).
  - **Aggregation / K-Anonymity (Policy-Dependent Heuristic)**: Ensure analytical cohorts and public report cells group at least $k$ individuals (e.g., suppressing reporting on cells with small counts based on organizational privacy policy). Note that $k$-anonymity alone does not guarantee full privacy; awareness of homogeneity attacks (when all $k$ individuals share the same sensitive attribute) and background-knowledge attacks is required when releasing aggregated data.

### 3. Access Control and Security Awareness
- **Principle of Least Privilege (PoLP)**: Analysts should only have read access to the specific database schemas and tables required for their active analytical projects.
- **Role-Based Access Control (RBAC)**: Access granted based on defined organizational roles rather than ad-hoc individual grants.
- **Data Storage Security (Hard Rule)**: Never export unencrypted PII or sensitive commercial data to local desktop folders, unapproved cloud drives, or unencrypted portable drives.

### 4. Data Retention and Lifecycle Management
- Understand legal and regulatory retention horizons (e.g., GDPR right-to-be-forgotten, CCPA compliance, financial audit requirements).
- Ensure analytical sandbox tables, intermediate temporary files, and ad-hoc extracts have documented expiration policies (TTL) to prevent data sprawl.

## Analytical Audit Checklist
Before publishing or handing off an analytical deliverable to decision-makers:
- [ ] Can another analyst trace the analysis from documented inputs, transformations, and code, and rerun it with expected consistency?
- [ ] Are raw data extraction queries, database names, and extraction dates recorded?
- [ ] Are random seeds fixed for stochastic operations?
- [ ] Are all row exclusion criteria documented with counts and rationales?
- [ ] Does the dataset contain unmasked or unhashed PII that should be sanitized?
- [ ] Are metric definitions and business assumptions documented?

## Cross-References
- For data quality dimensions, profiling checks, and validation: [Data Quality](./data-quality.md)
- For data pipeline architectures, schema contracts, and observability: [Data Engineering for Analysts](./data-engineering.md)
- For clean query formulation, grain definition, and deduplication: [SQL for Analysis](./sql-for-analysis.md)
- For framing assumptions, scope limits, and project criteria: [Problem Definition and Framing](./problem-definition.md)
