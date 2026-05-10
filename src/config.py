import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
ATHENA_OUTPUT = os.getenv("ATHENA_OUTPUT", "s3://your-query-results-bucket/prefix/")
CUR_DATABASE = os.getenv("CUR_DATABASE", "your_cur_database")
CUR_TABLE = os.getenv("CUR_TABLE", "your_cur_table")
START_DATE = os.getenv("START_DATE", "2026-05-01")
END_DATE = os.getenv("END_DATE", "2026-05-31")
ACCOUNT_ID = os.getenv("ACCOUNT_ID", "000000000000")
