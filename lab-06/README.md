# BigQuery Lab 6 — Connected Sheets: Qwik Start (GSP870)

This lab explores BigQuery Connected Sheets, a feature that brings the scale of a BigQuery data warehouse directly into Google Sheets. The key value here is accessibility: non-technical stakeholders can run pivot tables, charts, and formulas against billions of rows of data without writing a single line of SQL.

The dataset used throughout is the public Chicago taxi trips dataset available in BigQuery.

---

## What This Lab Covers

| Task | Topic | What Was Done |
|------|-------|---------------|
| 1 | Open Google Sheets | Created a blank spreadsheet using the lab student account |
| 2 | Connect to a BigQuery dataset | Linked the `chicago_taxi_trips.taxi_trips` public dataset to the sheet via Data > Data Connectors |
| 3 | Formulas | Used `COUNTUNIQUE` and `COUNTIF` to find the number of taxi companies and the percentage of trips that included a tip |
| 4 | Charts | Built a pie chart of payment types by fare value and count, and a line chart of mobile payment trends over time with a payment_type filter |
| 5 | Pivot tables | Analyzed ride volume and average fare by hour of day and day of week, with conditional color formatting to surface peak periods |
| 6 | Using Extract | Pulled 25,000 rows of raw data into the sheet, scoped to trip_start_timestamp, fare, tips, and tolls, ordered by most recent trip |
| 7 | Calculated columns | Created a new column derived from existing fields using sheet-side transformations |
| 8 | Scheduled refresh | Configured automatic data refresh so analyses stay current without manual intervention |

---

## Key Findings from the Analysis

- Around 38.6% of Chicago taxi trips included a tip
- Cash transactions significantly outnumber credit card transactions, but credit card trips have a higher average fare value
- Overall taxi revenue peaked in 2015, while mobile payments have trended upward over time
- Peak ride volume on weekdays clusters around typical commute hours; weekend peaks shift to early morning
- Monday early morning fares are the most expensive on average

---

## Key Concepts

**Connected Sheets vs Querying in BigQuery directly**

Connected Sheets is not a replacement for SQL analytics. It is a bridge for business users who need to explore or monitor data without querying. For a data analyst, the main value is being able to hand off a live, governed data connection to a stakeholder team and let them build their own views without giving them direct BigQuery access or waiting on you for every question.

**Extract**

By default, Connected Sheets only previews 500 rows of raw data. The Extract feature lets you pull a defined subset (up to the row limit you set) into the sheet for closer inspection or for sharing with someone who needs raw data without BigQuery access.

**Scheduled Refresh**

Charts, pivot tables, and formulas built on Connected Sheets do not update in real time. Scheduled refresh lets you configure an automatic update window so the analyses stay current without anyone needing to manually trigger a refresh.

---

## Dataset

**Source:** Google public BigQuery dataset
**Table:** `bigquery-public-data.chicago_taxi_trips.taxi_trips`
**Access:** Available to any Google Cloud account at no cost

---

## Note on Lab Format

This lab was completed entirely in Google Sheets using the Connected Sheets interface. There are no SQL files associated with this lab since all analysis was performed through the Sheets UI rather than the BigQuery query editor. The concepts covered here complement the SQL-based labs in this course by demonstrating how the same underlying data can be surfaced to non-technical audiences.
