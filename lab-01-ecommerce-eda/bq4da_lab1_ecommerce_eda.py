{
  "metadata": {
    "kernelspec": {
      "name": "xsqlite",
      "display_name": "xsqlite",
      "language": "sqlite"
    },
    "language_info": {
      "codemirror_mode": "sql",
      "file_extension": "",
      "mimetype": "",
      "name": "sql",
      "version": "3.49.2"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "ce46346b-b128-46d6-b83a-41a6559927ae",
      "cell_type": "markdown",
      "source": "## Exploring an Ecommerce Dataset using SQL in Google BigQuery",
      "metadata": {}
    },
    {
      "id": "ad0a11ed-45fa-4865-8859-84a65cb1fb68",
      "cell_type": "markdown",
      "source": "In this introductory lab within the Big Query for Data Analyst course, I had the opportunity to set up a Big Query account and use the ecommerce dataset. In this notebook, I will be sharing how I handled EDA and data cleaning inside BQ.",
      "metadata": {}
    },
    {
      "id": "ce814bfb-1a38-4e23-ac8c-a2f9d8874e07",
      "cell_type": "markdown",
      "source": "In this lab, I used BigQuery to:\n\n* Access an ecommerce dataset\n* Look at the dataset metadata\n* Remove duplicate entries\n* Write and execute queries",
      "metadata": {}
    },
    {
      "id": "1e8c1709-bf7f-4b49-892a-4a99161bba9f",
      "cell_type": "markdown",
      "source": "### Identifying Duplicate Rows",
      "metadata": {}
    },
    {
      "id": "3317834e-12c0-4182-b53e-e310458a16db",
      "cell_type": "code",
      "source": "SELECT COUNT(*) as num_duplicate_rows, * FROM\n`data-to-insights.ecommerce.all_sessions_raw`\nGROUP BY\nfullVisitorId, channelGrouping, time, country, city, totalTransactionRevenue, transactions, timeOnSite, pageviews, sessionQualityDim, date, visitId, type, productRefundAmount, productQuantity, productPrice, productRevenue, productSKU, v2ProductName, v2ProductCategory, productVariant, currencyCode, itemQuantity, itemRevenue, transactionRevenue, transactionId, pageTitle, searchKeyword, pagePathLevel1, eCommerceAction_type, eCommerceAction_step, eCommerceAction_option\nHAVING num_duplicate_rows > 1;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "07f3a98e-9763-46ae-9867-006f57db8b11",
      "cell_type": "markdown",
      "source": "Scenario: Your data analyst team has provided you with this query, and your schema experts have identified the key fields that must be unique for each record per your schema. Confirm that no duplicates exist, this time in the all_sessions table.",
      "metadata": {}
    },
    {
      "id": "7ab3d6c8-134d-414e-a80c-876b023eef45",
      "cell_type": "code",
      "source": "# schema: https://support.google.com/analytics/answer/3437719?hl=en\nSELECT\nfullVisitorId, # the unique visitor ID\nvisitId, # a visitor can have multiple visits\ndate, # session date stored as string YYYYMMDD\ntime, # time of the individual site hit  (can be 0 to many per visitor session)\nv2ProductName, # not unique since a product can have variants like Color\nproductSKU, # unique for each product\ntype, # a visitor can visit Pages and/or can trigger Events (even at the same time)\neCommerceAction_type, # maps to ‘add to cart', ‘completed checkout'\neCommerceAction_step,\neCommerceAction_option,\n  transactionRevenue, # revenue of the order\n  transactionId, # unique identifier for revenue bearing transaction\nCOUNT(*) as row_count\nFROM\n`data-to-insights.ecommerce.all_sessions`\nGROUP BY 1,2,3 ,4, 5, 6, 7, 8, 9, 10,11,12\nHAVING row_count > 1 # find duplicates",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "e4da5ba3-58a5-4126-825d-5fededb7bfda",
      "cell_type": "markdown",
      "source": "The query returned zero rows, so there are no duplicates.",
      "metadata": {}
    },
    {
      "id": "bdca5e94-26be-49b8-9e88-5b569ddb34a1",
      "cell_type": "markdown",
      "source": "Now we want to find out the total unique visitors. The query needs to determine the total views by counting product_views and the number of unique visitors by counting fullVisitorID.",
      "metadata": {}
    },
    {
      "id": "512c23c9-ac6c-4307-bea2-b9587102e959",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(*) AS product_views,\n  COUNT(DISTINCT fullVisitorId) AS unique_visitors\nFROM `data-to-insights.ecommerce.all_sessions`;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "d5574051-1f7b-4289-9847-5d79aecdbba9",
      "cell_type": "markdown",
      "source": "Here is another query that looks at total unique visitors (fullVisitorID) by the referring site (channelGrouping):",
      "metadata": {}
    },
    {
      "id": "994431a8-f784-4e5e-83bf-33df4a79f9d1",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(DISTINCT fullVisitorId) AS unique_visitors,\n  channelGrouping\nFROM `data-to-insights.ecommerce.all_sessions`\nGROUP BY channelGrouping\nORDER BY channelGrouping DESC;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "23e92521-20ab-4938-b964-549f0fe5a3fa",
      "cell_type": "markdown",
      "source": "Another task for this lab was to write a query to list all the unique product names (v2ProductName) alphabetically.",
      "metadata": {}
    },
    {
      "id": "19274b62-1ac8-4ead-bbc0-2dcdc35f33c0",
      "cell_type": "code",
      "source": "SELECT\n  (v2ProductName) AS ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nGROUP BY ProductName\nORDER BY ProductName",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "1a537208-8d8b-40f6-90e6-625cea870020",
      "cell_type": "markdown",
      "source": "Next task: Write a query to list the five products with the most views (product_views) from all visitors (include people who have viewed the same product more than once). Your query counts number of times a product (v2ProductName) was viewed (product_views), puts the list in descending order, and lists the top 5 entries.",
      "metadata": {}
    },
    {
      "id": "f3b6b1cd-e302-4441-8fa8-c3217db1671a",
      "cell_type": "markdown",
      "source": "An interesting tip the lab gave us based on GA4: In Google Analytics, a visitor can \"view\" a product during the following interaction types: 'page', 'screenview', 'event', 'transaction', 'item', 'social', 'exception', 'timing'. For our purposes, simply filter for only type = 'PAGE'. \n\nSo nice, isn't it!",
      "metadata": {}
    },
    {
      "id": "8b2521d4-205f-4462-9877-3f3b467f6b29",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(*) AS product_views,\n  (v2ProductName) AS ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE type = 'PAGE'\nGROUP BY v2ProductName\nORDER BY product_views DESC\nLIMIT 5;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "153c7c48-ea5c-4464-9cfe-2d2bb42f7346",
      "cell_type": "markdown",
      "source": "Refine the query to no longer double-count product views for visitors who have viewed a product many times. Each distinct product view should only count once per visitor:",
      "metadata": {}
    },
    {
      "id": "cf4bb7c4-6c0e-4506-932b-e526144b81f4",
      "cell_type": "code",
      "source": "WITH unique_product_views_by_person AS (\n-- find each unique product viewed by each visitor\nSELECT\n fullVisitorId,\n (v2ProductName) AS ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE type = 'PAGE'\nGROUP BY fullVisitorId, v2ProductName )\n-- aggregate the top viewed products and sort them\nSELECT\n  COUNT(*) AS unique_view_count,\n  ProductName\nFROM unique_product_views_by_person\nGROUP BY ProductName\nORDER BY unique_view_count DESC\nLIMIT 5",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "c618ca85-3bcd-4f00-8b58-ad7803194f42",
      "cell_type": "markdown",
      "source": "The next step is to expand on the query in the previous line to include the total number of distinct products ordered and the total number of total units ordered (productQuantity).",
      "metadata": {}
    },
    {
      "id": "d2740337-9ed3-44bf-99f6-6512df1a6e50",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(*) AS product_views,\n  COUNT(productQuantity) AS orders,\n  SUM(productQuantity) AS quantity_product_ordered,\n  v2ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE type = 'PAGE'\nGROUP BY v2ProductName\nORDER BY product_views DESC\nLIMIT 5;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "7508b786-8e2a-461a-8460-ff97db3f8e4e",
      "cell_type": "markdown",
      "source": "And the one following step is: Expand the query to include the average amount of product per order (total number of units ordered/total number of orders, or SUM(productQuantity)/COUNT(productQuantity))",
      "metadata": {}
    },
    {
      "id": "218ef92b-f673-4619-ba2c-fa73b1e17b04",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(*) AS product_views,\n  COUNT(productQuantity) AS orders,\n  SUM(productQuantity) AS quantity_product_ordered,\n  SUM(productQuantity) / COUNT(productQuantity) AS avg_per_order,\n  (v2ProductName) AS ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE type = 'PAGE'\nGROUP BY v2ProductName\nORDER BY product_views DESC\nLIMIT 5;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "ece21be1-56f5-4c09-9951-e0633ef2d91d",
      "cell_type": "markdown",
      "source": "#### Challenge 1: Conversion Rates",
      "metadata": {}
    },
    {
      "id": "5f16d103-9d8a-470b-9d89-d6d7168ab072",
      "cell_type": "markdown",
      "source": "Here is the task for the first challenge: Write a conversion rate query for products with these qualities:\n\n* More than 1000 units were added to a cart or ordered\n* AND are not frisbees\n\nAnswer these questions:\n\n* How many distinct times was the product part of an order (either complete or incomplete order)?\n* How many total units of the product were part of orders (either complete or incomplete)?\n* Which product had the highest conversion rate?",
      "metadata": {}
    },
    {
      "id": "56bb96aa-f63a-4e99-9fd1-b38adb2256f9",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(*) AS product_views,\n  COUNT(productQuantity) AS potential_orders,\n  SUM(productQuantity) AS quantity_product_added,\n  (COUNT(productQuantity) / COUNT(*)) AS conversion_rate,\n  v2ProductName\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE LOWER(v2ProductName) NOT LIKE '%frisbee%'\nGROUP BY v2ProductName\nHAVING quantity_product_added > 1000\nORDER BY conversion_rate DESC\nLIMIT 10;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "2a79fa85-af79-45ec-8e3d-eba285f4ac36",
      "cell_type": "markdown",
      "source": "#### Challenge 2: Track visitor checkout progress",
      "metadata": {}
    },
    {
      "id": "ec5bda48-a60d-4f0e-90b9-aa5e664ac437",
      "cell_type": "markdown",
      "source": "Write a query that shows the eCommerceAction_type and the distinct count of fullVisitorId associated with each type.",
      "metadata": {}
    },
    {
      "id": "c62f9884-33f9-48b0-958b-411ee22cef69",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(DISTINCT fullVisitorId) AS number_of_unique_visitors,\n  eCommerceAction_type\nFROM `data-to-insights.ecommerce.all_sessions`\nGROUP BY eCommerceAction_type\nORDER BY eCommerceAction_type;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "c63eb7ac-4841-429d-946f-2febe0e6cf8c",
      "cell_type": "markdown",
      "source": "##### Bonus: \n\nYou are given this mapping for the action type: Unknown = 0 Click through of product lists = 1 Product detail views = 2 Add product(s) to cart = 3 Remove product(s) from cart = 4 Check out = 5 Completed purchase = 6 Refund of purchase = 7 Checkout options = 8\n\nUse a Case Statement to add a new column to your previous query to display the eCommerceAction_type label (such as “Completed purchase”).",
      "metadata": {}
    },
    {
      "id": "2b167a89-2e7f-49e0-9131-7f8eb2027f3e",
      "cell_type": "code",
      "source": "SELECT\n  COUNT(DISTINCT fullVisitorId) AS number_of_unique_visitors,\n  eCommerceAction_type,\n  CASE eCommerceAction_type\n  WHEN '0' THEN 'Unknown'\n  WHEN '1' THEN 'Click through of product lists'\n  WHEN '2' THEN 'Product detail views'\n  WHEN '3' THEN 'Add product(s) to cart'\n  WHEN '4' THEN 'Remove product(s) from cart'\n  WHEN '5' THEN 'Check out'\n  WHEN '6' THEN 'Completed purchase'\n  WHEN '7' THEN 'Refund of purchase'\n  WHEN '8' THEN 'Checkout options'\n  ELSE 'ERROR'\n  END AS eCommerceAction_type_label\nFROM `data-to-insights.ecommerce.all_sessions`\nGROUP BY eCommerceAction_type\nORDER BY eCommerceAction_type;",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "df6cfbee-0d98-46fd-a5fa-5a6c18739f63",
      "cell_type": "markdown",
      "source": "##### Challenge 3: Track abandoned carts from high quality sessions",
      "metadata": {}
    },
    {
      "id": "d53396e0-2701-427a-b6e9-80a1dcda8767",
      "cell_type": "markdown",
      "source": "Write a query using aggregation functions that returns the unique session IDs of those visitors who have added a product to their cart but never completed checkout (abandoned their shopping cart).",
      "metadata": {}
    },
    {
      "id": "06342de6-0ce1-4a80-aefe-d83c3b051d8e",
      "cell_type": "code",
      "source": "SELECT  \n  CONCAT(fullVisitorId,CAST(visitId AS STRING)) AS unique_session_id,\n  sessionQualityDim,\n  SUM(productRevenue) AS transaction_revenue,\n  MAX(eCommerceAction_type) AS checkout_progress\nFROM `data-to-insights.ecommerce.all_sessions`\nWHERE sessionQualityDim > 60 # high quality session\nGROUP BY unique_session_id, sessionQualityDim\nHAVING\n  checkout_progress = '3' # 3 = added to cart\n  AND (transaction_revenue = 0 OR transaction_revenue IS NULL)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}
