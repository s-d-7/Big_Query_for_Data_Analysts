# BigQuery Lab 3 — Troubleshooting and Solving Data Join Pitfalls (GSP412)

Hands-on lab using Google's public ecommerce dataset to diagnose and fix the most common SQL join mistakes. The core theme: a query can succeed and return results while being completely wrong — and knowing how to catch that is what separates junior from senior analysts.

---

## What's Covered

| Task | Topic | Key Concept |
|------|-------|-------------|
| 3 | Examine the fields | Schema exploration; candidate key identification |
| 4 | Identify the join key | `DISTINCT` vs unique; `STRING_AGG` to audit many-to-many |
| 5 | Non-unique key pitfall | How a many-to-many join silently inflates aggregates |
| 6a | Fix: deduplicate before joining | `ARRAY_AGG(DISTINCT ... LIMIT 1)` as a pre-join normaliser |
| 6b | INNER JOIN coverage check | Quantifying SKU overlap between two tables |
| 6c | LEFT JOIN + NULL filter | Finding website SKUs absent from inventory |
| 6d | RIGHT JOIN + NULL filter | Finding inventory items not listed on the website |
| 6e | FULL JOIN reconciliation | Gaps in both directions in a single query |
| — | CROSS JOIN: promotional pricing | Intentional Cartesian product for multi-tier discount logic |

---

## The Core Pitfall, Explained

The join key — `productSKU` — has a many-to-many relationship in the website table: one SKU can map to multiple product name variants (size, colour, locale differences). The inventory table has one clean row per SKU.

When you join them without pre-deduplication:

```
website rows for SKU X  ×  1 inventory row  =  N result rows
```

If you then `SUM(stockLevel)`, you get `N × stockLevel` — not the actual stock. The query doesn't error. It just lies.

**The fix:** collapse the website table to one row per SKU before joining, using `ARRAY_AGG(DISTINCT name LIMIT 1)` or a CTE with `GROUP BY productSKU`.

---

## Dataset

**Source:** Google's public BigQuery demo dataset  
**Tables:**
- `data-to-insights.ecommerce.all_sessions_raw` — raw GA hit-level data (website behaviour)
- `data-to-insights.ecommerce.products` — product inventory with stock levels

**Access:** Available to any Google Cloud / BigQuery account at no cost.

---

## Join Type Reference

| Join Type | Rows Returned |
|-----------|--------------|
| `INNER JOIN` | Only rows with matching keys in **both** tables |
| `LEFT JOIN` | All rows from the left table; `NULL` where no right-side match |
| `RIGHT JOIN` | All rows from the right table; `NULL` where no left-side match |
| `FULL JOIN` | All rows from both tables; `NULL` wherever a side has no match |
| `CROSS JOIN` | Every row from table A paired with every row from table B |

---

## How to Run

1. Open [BigQuery Console](https://console.cloud.google.com/bigquery)
2. Create a dataset named `ecommerce` in your project (required for the CROSS JOIN section)
3. Copy any query string from `bq4da_lab3_join_pitfalls.py` and paste it into the editor
4. The DDL statement (`CREATE OR REPLACE TABLE`) must be run first before the CROSS JOIN queries

---

## Key Takeaways

- Always audit join key uniqueness before writing any join — `COUNT(DISTINCT key)` vs `COUNT(*)` is your first check
- A many-to-many join key corrupts `SUM()` and `AVG()` silently; `DISTINCT` at the row level does not fix aggregation inflation
- `LEFT JOIN WHERE right.key IS NULL` and `RIGHT JOIN WHERE left.key IS NULL` are standard patterns for data reconciliation and gap analysis
- `CROSS JOIN` is a deliberate tool for pricing matrices, scenario modelling, and test data generation — not a mistake to always avoid
- `STRING_AGG()` and `ARRAY_AGG()` are BigQuery-native tools for auditing and resolving one-to-many string relationships before joining
