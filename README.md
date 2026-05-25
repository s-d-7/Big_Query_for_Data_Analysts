# BigQuery for Data Analysts

A collection of hands-on labs completed as part of Google's BigQuery for Data Analysts course on Google Cloud Skills Boost. Each lab covers a distinct area of applied SQL and data engineering in BigQuery, using a real Google Analytics ecommerce dataset from the Google Merchandise Store.

This repo documents not just the final queries, but the full problem-solving process: broken queries, iterative fixes, and the reasoning behind each decision. The goal is to show how I think through data problems, not just that I can write SQL that runs.

---

## Labs

### Lab 1 — Exploring an Ecommerce Dataset
**File:** `lab-01-ecommerce-eda/bq4da_lab1_ecommerce_eda.py`

Foundational EDA on the `all_sessions` table. Covers duplicate detection across raw vs. cleaned tables, unique visitor and channel attribution analysis, product view metrics, deduplication using CTEs, conversion rate calculations, checkout funnel tracking with CASE statements, and identifying abandoned high-intent sessions for remarketing.

### Lab 2 — Troubleshooting Common SQL Errors
**File:** `lab-02-sql-troubleshooting/bq4da_lab2_sql_troubleshooting.py`

A structured walkthrough of how to use BigQuery's Query Validator to diagnose and fix real SQL errors. Covers syntax issues (missing fields, wrong bracket style, missing commas), aggregation mistakes (unaggregated columns in GROUP BY, COUNT vs COUNT DISTINCT), and the WHERE vs HAVING distinction on aggregate expressions.

### Lab 3 — Troubleshooting and Solving Data Join Pitfalls
**File:** `lab-03-join-pitfalls/bq4da_lab3_join_pitfalls.py`

Deep dive into one of the most common and damaging mistakes in SQL analytics: joining on a non-unique key. Shows how a many-to-many relationship silently inflates aggregated values with no error or warning. Covers INNER, LEFT, RIGHT, FULL, and CROSS joins with real use cases for each, and demonstrates `ARRAY_AGG` and `STRING_AGG` as deduplication tools before joining.

### Lab 4 — Creating Permanent Tables and Access-Controlled Views
**File:** `lab-04-permanent-tables-views/bq4da_lab4_permanent_tables_views.py`

Moves from ad-hoc querying into production data layer design. Covers iterative schema debugging, NOT NULL constraints, revenue unit normalization from raw GA integers to USD, and view governance using `OPTIONS` metadata, `SESSION_USER()` for domain-based row-level access control, and `expiration_timestamp` for time-boxed data access.

---

## Dataset

All labs use Google's public ecommerce demo dataset, available at no cost to any Google Cloud account.

| Table | Description |
|-------|-------------|
| `data-to-insights.ecommerce.all_sessions_raw` | Raw Google Analytics hit-level data |
| `data-to-insights.ecommerce.all_sessions` | Cleaned and deduplicated session data |
| `data-to-insights.ecommerce.rev_transactions` | Revenue-bearing transactions |
| `data-to-insights.ecommerce.products` | Product inventory with stock levels |

---

## How Queries Are Organized

Each lab file is a Python script where queries are stored as named string variables. This format was chosen intentionally: it keeps the queries readable and portable, makes the progression from broken to fixed immediately visible through naming conventions (`QUERY_BROKEN_`, `QUERY_FIXED_`, `QUERY_FINAL_`), and makes it easy to integrate with the BigQuery Python SDK when needed.

---

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/bigquery)
[![SQL](https://img.shields.io/badge/Language-SQL-lightgrey?style=flat)](https://cloud.google.com/bigquery/docs/reference/standard-sql/introduction)
