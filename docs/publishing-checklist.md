# Public GitHub publishing checklist

Use this checklist before pushing the repository to a public GitHub repo.

## Remove or replace all sensitive values

- Replace real AWS account IDs with placeholders such as `000000000000`.
- Replace real S3 bucket names, Athena databases, CUR table names, and API URLs with placeholders.
- Remove customer names, internal project names, cost center labels, and business identifiers.
- Remove screenshots, exported CSV files, invoice PDFs, and raw CUR data.

## Secrets hygiene

- Never commit `.env`, credential files, or notebook outputs with secrets.
- If an AWS key was ever committed, rotate or revoke it before publishing.
- Check Git history as well, because deleting a file from the latest commit does not remove it from older commits.

## Final review commands

```bash
grep -R "AKIA" .
grep -R "aws_secret_access_key" .
grep -R "your-company-name" .
grep -R "123456789012" .
```

## Safe content to keep

- Python example scripts using environment variables.
- SQL examples with placeholder names.
- Mock sample data created specifically for demonstration.
- README and architecture documentation without customer-specific details.
