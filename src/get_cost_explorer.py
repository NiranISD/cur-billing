import boto3
from config import START_DATE, END_DATE


def main():
    client = boto3.client("ce", region_name="us-east-1")
    response = client.get_cost_and_usage(
        TimePeriod={"Start": START_DATE, "End": END_DATE},
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}],
    )

    for period in response.get("ResultsByTime", []):
        print(period["TimePeriod"]["Start"])
        for group in period.get("Groups", []):
            service = group["Keys"][0]
            amount = group["Metrics"]["UnblendedCost"]["Amount"]
            unit = group["Metrics"]["UnblendedCost"]["Unit"]
            print(f"  {service}: {amount} {unit}")


if __name__ == "__main__":
    main()
