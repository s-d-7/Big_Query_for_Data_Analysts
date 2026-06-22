# BigQuery Lab 8 — Create and Execute a SQL Workflow in Dataform (OCBL431)

This lab introduces Dataform, a SQL workflow tool built into Google Cloud that brings software engineering best practices to analytics: version control, modular code, dependency management, and automated execution. Instead of running standalone SQL scripts, you define your data objects declaratively in SQLX files and let Dataform handle the order of execution and the creation of objects in BigQuery.

---

## What This Lab Covers

| Task | What Was Done |
|------|---------------|
| 1 | Created a Dataform repository and saved the auto-generated service account ID for use in Task 5 |
| 2 | Created and initialized a development workspace within the repository |
| 3 | Created `definitions/quickstart-source.sqlx` to define a view containing a simple fruit inventory dataset |
| 4 | Created `definitions/quickstart-table.sqlx` to define a table that reads from the source view using `ref()` |
| 5 | Granted the Dataform service account three IAM roles in BigQuery: Job User, Data Editor, and Data Viewer |
| 6 | Executed the full workflow, authorized with student credentials, and reviewed the execution logs |

---

## SQLX Files Created

**quickstart-source.sqlx** — defines a BigQuery view

```sql
config {
  type: "view"
}

SELECT "apples"  AS fruit, 2 AS count
UNION ALL
SELECT "oranges" AS fruit, 5 AS count
UNION ALL
SELECT "pears"   AS fruit, 1 AS count
UNION ALL
SELECT "bananas" AS fruit, 0 AS count
```

**quickstart-table.sqlx** — defines a BigQuery table that depends on the view above

```sql
config {
  type: "table"
}

SELECT
  fruit,
  SUM(count) AS count
FROM ${ref("quickstart-source")}
GROUP BY 1
```

---

## Key Concepts

**SQLX**
Standard SQL with a `config {}` block at the top that tells Dataform what kind of object to create (view, table, assertion, incremental table) and how to configure it. The rest of the file is plain SQL.

**ref()**
The `${ref("object-name")}` function is how Dataform manages dependencies between files. Instead of hardcoding BigQuery paths, `ref()` resolves the correct dataset and table name at compile time and ensures the referenced object is created before the one that depends on it. This is the core of Dataform's dependency graph.

**Repositories and Workspaces**
A repository is the top-level container for a Dataform project, similar to a Git repo. A workspace is your personal working environment within it, similar to a feature branch. Changes in a workspace are isolated until committed.

**IAM Roles Required**
Dataform runs queries using its own service account, not your personal credentials. Three roles are needed: BigQuery Job User to submit query jobs, BigQuery Data Editor to create and write objects, and BigQuery Data Viewer to read from source tables.

---

## What Gets Created in BigQuery

After a successful execution, Dataform creates the following in your project:

| Object | Type | Dataset |
|--------|------|---------|
| `quickstart-source` | View | `dataform` |
| `quickstart-table` | Table | `dataform` |

---
