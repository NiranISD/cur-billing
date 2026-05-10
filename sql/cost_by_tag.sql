SELECT
  resource_tags_user_environment AS environment,
  line_item_product_code AS service,
  SUM(line_item_unblended_cost) AS amount_usd
FROM <CUR_DATABASE>.<CUR_TABLE>
WHERE bill_billing_period_start_date >= DATE '<START_DATE>'
  AND bill_billing_period_start_date < DATE '<END_DATE>'
GROUP BY 1, 2
ORDER BY 3 DESC;
