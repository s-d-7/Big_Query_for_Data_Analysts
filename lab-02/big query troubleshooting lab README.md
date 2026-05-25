# BigQuery Troubleshooting Lab

Hands-on SQL lab using Google's public `data-to-insights.ecommerce.rev_transactions` dataset in BigQuery. The focus is debugging and iterating on queries — starting from broken or naive versions and building up to correct, production-style SQL.

---

## What's Covered

| Task | Topic | Key Concept |
|------|-------|-------------|
| 1 | City-level transaction analysis | `SUM` vs raw column in `GROUP BY`, `HAVING` on aggregates |
| 2 | Product category breakdown | `COUNT` vs `COUNT(DISTINCT ...)` |
| 3 | Checkout funnel — confirmation page | Filtering on page title for funnel metrics |

---

## Dataset

**Source:** Google's public BigQuery demo dataset
**Table:** `data-to-insights.ecommerce.rev_transactions`
**Access:** Available to anyone with a Google Cloud / BigQuery account. No setup required beyond enabling the BigQuery API.

---

## How to Run

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery)
2. Paste any query from `bigquery_troubleshooting_lab.sql` into the editor
3. Run — no additional configuration needed since the dataset is public

---

## File Structure

Commented-out queries in the SQL file show the step-by-step troubleshooting progression for each task. The final uncommented query at the end of each section is the corrected, complete version.

---

## Key Takeaways

- Always aggregate columns that aren't in `GROUP BY` — bare references cause inflated row counts
- Use `HAVING` (not `WHERE`) to filter on aggregated expressions
- `COUNT(DISTINCT col)` vs `COUNT(col)` produces very different results on non-unique data
- Iterating on queries in small steps makes bugs easier to isolate
