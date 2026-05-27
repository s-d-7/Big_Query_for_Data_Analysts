# BigQuery Lab 7 — Explore and Create Reports with Looker Studio

This lab covers how to connect BigQuery to Looker Studio (formerly Data Studio) and build interactive reports from a live data source. The focus is on translating data into visual stories that business stakeholders can read and interact with without needing SQL access.

The dataset used is the `ecommerce.sales_report` table from the `data-to-insights` public BigQuery project.

---

## What This Lab Covers

| Task | What Was Done |
|------|---------------|
| 1 | Launched Looker Studio, created a blank report, and connected it to the `sales_report` BigQuery table via the BigQuery connector |
| 2 | Built a customized table chart with the `ratio` field formatted as a percentage, exploring the relationship between dimensions and metrics |

---

## Key Concepts

**Dimensions vs Metrics**

In Looker Studio, dimensions are categorical fields used to slice and group data (for example, product category or date), while metrics are numeric values that get aggregated (for example, total revenue or conversion rate). Understanding this distinction is fundamental to building reports that answer the right questions.

**Connecting BigQuery to Looker Studio**

The connection is made through the BigQuery connector, which requires authorization to access your Google Cloud project. Once connected, any table or view in your dataset becomes available as a data source for charts and reports. This means views built in earlier labs (like `vw_large_transactions` from Lab 4) could feed directly into a Looker Studio dashboard without any additional data movement.

**Field Type Formatting**

Numeric fields pulled from BigQuery come in as raw numbers by default. Looker Studio lets you override the data type at the report level, for example changing a decimal ratio to display as a percentage, without modifying the underlying table.

---

## Dataset

**Source:** Google public BigQuery project
**Table:** `data-to-insights.ecommerce.sales_report`
**Access:** Available to any Google Cloud account at no cost

---

## Note on Lab Format

This lab was completed entirely in the Looker Studio UI. There are no SQL or Python files associated with it since the work involved connecting to an existing table and configuring visual report elements rather than writing queries. The concepts here complement the SQL labs in this course by showing how the data layer built in BigQuery surfaces to end users through a BI tool.
