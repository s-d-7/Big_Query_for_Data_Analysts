# BigQuery for Data Analysts

A collection of hands-on labs completed as part of Google's BigQuery for Data Analysts course on Google Cloud Skills Boost. Each lab covers a distinct area of applied SQL and data engineering in BigQuery, using real Google Analytics ecommerce data from the Google Merchandise Store alongside other public Google Cloud datasets.

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

### Lab 5 — Ingesting New Datasets into BigQuery
**File:** `lab-05-ingesting-new-datasets/bq4da_lab5_ingesting_new_datasets.py`

Covers how to bring external data into BigQuery from multiple source types: local CSV upload, Google Cloud Storage, and Google Sheets via the Drive connector. Introduces the tradeoffs between native BigQuery tables and external tables, write preference options, and `SAFE_DIVIDE()` for null-safe inventory ratio calculations.

### Lab 6 — Connected Sheets: Qwik Start
**File:** `lab-06-connected-sheets/README.md`

Explores BigQuery Connected Sheets, which brings BigQuery's scale directly into Google Sheets for non-technical stakeholders. Covers pivot tables, charts, formulas, the Extract feature for pulling raw data subsets, and scheduled refresh for keeping analyses current. Dataset used: Chicago public taxi trips.

### Lab 7 — Explore and Create Reports with Looker Studio
**File:** `lab-07-looker-studio/README.md`

Connects BigQuery to Looker Studio to build interactive reports from a live data source. Covers the dimensions vs. metrics distinction, connecting to BigQuery via the native connector, and field type formatting at the report level without modifying the underlying table.

### Lab 8 — Create and Execute a SQL Workflow in Dataform
**File:** `lab-08-dataform-sql-workflow/bq4da_lab8_dataform_sql_workflow.py`

Introduces Dataform as a SQL workflow tool built into Google Cloud. Covers SQLX file structure, the `ref()` function for automatic dependency management between objects, IAM role configuration for the Dataform service account, and executing a full workflow with logs.

### Lab 9 — Analyze Data with Gemini Assistance
**File:** `lab-09-gemini-data-analysis/README.md`

Explores Gemini as an AI assistant within BigQuery for generating, completing, and explaining SQL queries using natural language prompts. Covers enabling the Cloud AI Companion API, prompting Gemini for query explanation and generation, and building an ARIMA_PLUS sales forecasting model using BigQuery ML with `ML.FORECAST`.

---

## Datasets

| Table | Description |
|-------|-------------|
| `data-to-insights.ecommerce.all_sessions_raw` | Raw Google Analytics hit-level data |
| `data-to-insights.ecommerce.all_sessions` | Cleaned and deduplicated session data |
| `data-to-insights.ecommerce.rev_transactions` | Revenue-bearing transactions |
| `data-to-insights.ecommerce.products` | Product inventory with stock levels |
| `bigquery-public-data.chicago_taxi_trips.taxi_trips` | Chicago public taxi trip records |
| `bigquery-public-data.thelook_ecommerce.*` | Synthetic ecommerce and digital marketing data |

---

## How Files Are Organized

Labs with significant SQL work include a Python script where queries are stored as named string variables. This format keeps queries readable and portable, makes the progression from broken to fixed immediately visible through naming conventions (`QUERY_BROKEN_`, `QUERY_FIXED_`, `QUERY_FINAL_`), and makes it straightforward to integrate with the BigQuery Python SDK when needed.

Labs completed primarily through UI tools (Connected Sheets, Looker Studio, Gemini) include a README only, with all key queries and concepts documented there for reference.

---

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-BigQuery-4285F4?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/bigquery)
[![SQL](https://img.shields.io/badge/Language-SQL-lightgrey?style=flat)](https://cloud.google.com/bigquery/docs/reference/standard-sql/introduction)
[![Looker Studio](https://img.shields.io/badge/Looker_Studio-Reports-4285F4?style=flat&logo=google&logoColor=white)](https://lookerstudio.google.com)
[![Dataform](https://img.shields.io/badge/Dataform-Workflows-34A853?style=flat&logo=google-cloud&logoColor=white)](https://cloud.google.com/dataform)
