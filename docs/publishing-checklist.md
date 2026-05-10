# Public GitHub publishing checklist

Use this checklist before pushing the repository to a public GitHub repo.

## Remove or replace all sensitive values

- Replace real AWS account IDs with placeholders such as `000000000000`.[cite:7]
- Replace real S3 bucket names, Athena databases, CUR table names, and API URLs with placeholders.[cite:7][cite:23]
- Remove customer names, internal project names, cost center labels, and business identifiers.[cite:58]
- Remove screenshots, exported CSV files, invoice PDFs, and raw CUR data.[cite:23][cite:24]

## Secrets hygiene

- Never commit `.env`, credential files, or notebook outputs with secrets.[cite:49][cite:52][cite:56]
- If an AWS key was ever committed, rotate or revoke it before publishing.[cite:52][cite:56]
- Check Git history as well, because deleting a file from the latest commit does not remove it from older commits.[cite:52][cite:56]

## Final review commands

```bash
grep -R "AKIA" .
grep -R "aws_secret_access_key" .
grep -R "your-company-name" .
grep -R "123456789012" .
```

## Safe content to keep

- Python example scripts using environment variables.[cite:7][cite:49]
- SQL examples with placeholder names.[cite:23][cite:24]
- Mock sample data created specifically for demonstration.[cite:23][cite:24]
- README and architecture documentation without customer-specific details.[cite:7]
