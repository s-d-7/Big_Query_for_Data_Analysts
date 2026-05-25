# BigQuery Lab 5 — Ingesting New Datasets into BigQuery (GSP411)

This lab covers how to bring external data into BigQuery from multiple source types, and when to use each one. The business scenario runs throughout: an operations team needs inventory and restocking data analyzed alongside the existing ecommerce dataset.

---

## Tasks

| Task | Topic | Method |
|------|-------|--------|
| 1 | Create a dataset | BigQuery Console UI |
| 2 | Ingest from CSV | Local file upload with auto-detected schema |
| 3 | Ingest from Cloud Storage | GCS bucket path, write preference fix |
| 4 | Ingest from Google Sheets | Drive connector, external table |
| 5 | Save results to Google Sheets | Query results export, bi-directional workflow |
| 6 | External table tradeoffs | Performance and consistency considerations |

---

## Key Concepts

**Write Preference** controls what happens when a table already exists at load time. The default ("Write if empty") fails if the table is present, which is intentional as a safety guard. For a full refresh, switch to "Overwrite table" so the load is idempotent and safe to re-run.

**SAFE_DIVIDE()** is the null-safe alternative to the `/` operator in BigQuery. Regular division raises an error on division by zero. SAFE_DIVIDE() returns NULL instead, which is the correct behavior for inventory ratio calculations where stockLevel could be zero.

**External tables** link BigQuery to a live source (Google Sheets, GCS) without copying the data. Any edits to the source are reflected immediately on the next query. This makes them well-suited for operational annotation workflows but poorly suited for high-frequency analytics queries where consistency and performance matter.

---

## When to Use External Tables vs Native Tables

| | External Table | Native BQ Table |
|-|---------------|-----------------|
| Data freshness | Always current | Requires re-ingestion |
| Query performance | Slower | Optimized columnar storage |
| Consistency | Not guaranteed mid-query | Guaranteed |
| Best for | Operational lookups, annotations | Analytics, reporting, scale |

---

## Dataset

| Table | Source | Description |
|-------|--------|-------------|
| `ecommerce.products` | CSV / GCS | Product inventory with stock levels and sentiment scores |
| `ecommerce.products_comments` | Google Sheets (external) | Supply chain team annotations on restock priority items |

---

## How to Run

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery)
2. Tasks 1 through 5 involve UI steps documented in the `.py` file comments
3. The SQL queries can be copied directly into the BigQuery editor
4. For the external table query to work, the Google Sheet must be shared with the lab student account
