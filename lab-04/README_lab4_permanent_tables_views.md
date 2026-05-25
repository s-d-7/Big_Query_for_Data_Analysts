# BigQuery Lab 4 — Creating Permanent Tables and Access-Controlled Views (GSP410)

This lab transitions from ad-hoc querying against a shared public dataset to building a structured, governed data layer — the kind of work that separates analysts who just write queries from those who architect reliable reporting systems.

---

## What's Covered

| Task | Topic | Key Concept |
|------|-------|-------------|
| 1 | Create a dataset | Organising a project-level reporting namespace in BQ |
| 2a | Schema-less table | Why inferred schemas are fragile in production |
| 2b | Schema field mismatch | Explicit schema column count must match SELECT output exactly |
| 2c | Column name mismatch | Schema field names must match SELECT aliases |
| 2d | Typed schema + NOT NULL | Column-level `OPTIONS(description)` and nullability constraints |
| 2e (Final) | Revenue transactions table | `CAST()`, revenue unit normalisation (`/ 1000000`), `FLOAT64`, `DISTINCT` |
| 3a | Preview query | Always validate the SELECT before wrapping in a VIEW |
| 3b | Basic view | `CREATE OR REPLACE VIEW` — functional but undocumented |
| 3c | View with OPTIONS | `description`, `labels` — production cataloguing standards |
| 3d | CREATE VIEW pitfall | `CREATE VIEW` (no `OR REPLACE`) errors if view exists |
| 3e | Loss-prevention view | High-value USD transactions > $1,000 with `STRING_AGG` for products |
| 3f | SESSION_USER() filter | Domain-based row-level access control without separate IAM policies |
| 3g (Final) | Access-controlled + expiry | `expiration_timestamp` auto-expires the view after 90 days |

---

## Dataset

**Source:** Google's public BigQuery demo dataset  
**Table:** `data-to-insights.ecommerce.all_sessions_raw`  
**Access:** Available to any Google Cloud / BigQuery account at no cost.

---

## Key Technical Concepts

### Revenue Unit Normalisation
Google Analytics stores transaction revenue as an integer scaled by 10⁶ (e.g., $150.00 is stored as `150000000`). Always divide by `1000000` before surfacing revenue figures in any table or view.

### CAST(visitId AS STRING)
`visitId` is an INT64 in the source schema but is semantically an identifier, not a number. Casting prevents accidental arithmetic and ensures correct JOIN behaviour in downstream queries.

### CREATE OR REPLACE vs CREATE
Always use `CREATE OR REPLACE VIEW` unless you explicitly want the operation to fail on collision. `CREATE VIEW` raises an `Already Exists` error if the view already exists — acceptable as a deployment safety check, but not as a default.

### SESSION_USER() Row-Level Access Control
```sql
AND REGEXP_EXTRACT(SESSION_USER(), r'@(.+)') IN ('your-domain.com')
```
This pattern restricts rows returned by a view to users whose email domain matches the allowlist. Users outside the allowed domain receive 0 rows — no error, no data leakage. The filter is evaluated at query execution time, not view creation time.

### View Expiration
```sql
expiration_timestamp = TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
```
Setting an expiration on a view automatically removes it after the specified window — useful for time-boxed investigations, compliance review periods, or temporary access grants that should not persist indefinitely.

### NOT NULL in BigQuery
BigQuery documents `NOT NULL` as a schema constraint but does **not** enforce it at write time (unlike traditional RDBMS). Its value is as authoritative documentation that is respected by BI connectors and surfaced in `INFORMATION_SCHEMA`.

---

## How to Run

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery)
2. Create a dataset named `ecommerce` in your project (Task 1 — UI step)
3. Replace `'your-domain.com'` in the SESSION_USER() queries with your organisation's domain
4. Run queries in order — later steps depend on the dataset created in earlier ones

---

## Folder Structure

```
lab-04-permanent-tables-views/
├── bq4da_lab4_permanent_tables_views.py
└── README.md
```

---

## Key Takeaways

- Explicit schemas with column-level `OPTIONS(description)` are a documentation investment that pays dividends at scale — inferred schemas are fine for exploration, not production
- Revenue columns from Google Analytics always need the `/ 1000000` normalisation step — skip it and every downstream number will be wrong by six orders of magnitude
- `SESSION_USER()` enables lightweight row-level security inside a view definition, without requiring separate IAM bindings per user
- View expiration is an underused but powerful governance tool for time-sensitive data access
- Always validate the underlying SELECT before creating a view — a broken view creates confusion for anyone who queries it later
