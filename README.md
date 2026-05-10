# AWS CUR + Python Billing Examples

This repository is for sharing how to query AWS billing data from CUR (Cost and Usage Report), Athena, and Cost Explorer API with Python. It is designed to avoid uploading real billing data, AWS credentials, customer names, or internal resource identifiers to a public GitHub repository.

## What this repo includes

- Example Python scripts for querying CUR via Athena.
- Example Python script for calling AWS Cost Explorer API.
- Example Athena SQL queries for cost analysis by service and by tag.
- `.env.example` and `.gitignore` files for safer public publishing.
- Mock sample data only; no real billing exports or CUR files.

## What this repo must NOT contain

Do **not** upload any of the following to a public repository:

- AWS access keys, secret keys, session tokens, `.env`, or local credential files.
- Real AWS account IDs, real S3 bucket names, Athena database names, table names, or API endpoints.
- CUR raw files, Athena query exports, invoices, screenshots, or customer billing JSON/CSV outputs.
- Customer names, internal cost-center tags, or organization-specific identifiers.

If any AWS credential was previously committed, revoke it immediately and rotate the credential before publishing the repository.

## Repository structure

```text
aws-cur-python-public-repo/
├─ README.md
├─ .gitignore
├─ .env.example
├─ requirements.txt
├─ src/
│  ├─ config.py
│  ├─ query_cur_athena.py
│  └─ get_cost_explorer.py
├─ sql/
│  ├─ total_cost_by_service.sql
│  └─ cost_by_tag.sql
├─ docs/
│  └─ publishing-checklist.md
└─ data/
   └─ sample_cur_extract.csv
```

## Setup

1. Enable AWS Cost and Usage Report (CUR) and deliver it to Amazon S3.
2. Configure Athena to query CUR data, either manually or with AWS-provided integration steps.
3. Copy `.env.example` to `.env` locally and fill in placeholder values with your own environment-specific values. Keep `.env` private and never commit it.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Query CUR with Athena

```bash
python src/query_cur_athena.py
```

### Query summarized cost using Cost Explorer API

```bash
python src/get_cost_explorer.py
```

## Notes

- CUR is a good choice when detailed billing line items, allocation logic, and custom SQL are required.
- Cost Explorer API is better for summarized cost views such as daily or monthly dashboard widgets.
- This repository intentionally uses placeholders and mock values so it can be uploaded safely to a public repo.
