import time
import boto3
from config import AWS_REGION, ATHENA_OUTPUT, CUR_DATABASE, CUR_TABLE, START_DATE, END_DATE, ACCOUNT_ID

QUERY = f"""
SELECT
  line_item_product_code AS service,
  SUM(line_item_unblended_cost) AS amount_usd
FROM {CUR_DATABASE}.{CUR_TABLE}
WHERE bill_billing_period_start_date >= DATE '{START_DATE}'
  AND bill_billing_period_start_date < DATE '{END_DATE}'
  AND line_item_usage_account_id = '{ACCOUNT_ID}'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 20
"""


def main():
    client = boto3.client("athena", region_name=AWS_REGION)
    response = client.start_query_execution(
        QueryString=QUERY,
        QueryExecutionContext={"Database": CUR_DATABASE},
        ResultConfiguration={"OutputLocation": ATHENA_OUTPUT},
    )

    execution_id = response["QueryExecutionId"]

    while True:
        status = client.get_query_execution(QueryExecutionId=execution_id)
        state = status["QueryExecution"]["Status"]["State"]
        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(2)

    if state != "SUCCEEDED":
        reason = status["QueryExecution"]["Status"].get("StateChangeReason", "Unknown error")
        raise RuntimeError(f"Athena query failed: {reason}")

    results = client.get_query_results(QueryExecutionId=execution_id)
    for row in results["ResultSet"]["Rows"]:
        print([col.get("VarCharValue", "") for col in row["Data"]])


if __name__ == "__main__":
    main()
