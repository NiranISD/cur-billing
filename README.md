# AWS CUR + Python Billing Examples (Public-Safe Starter)

This repository is a **public-safe starter** for sharing how to query AWS billing data from CUR (Cost and Usage Report), Athena, and Cost Explorer API with Python. It is designed to avoid uploading real billing data, AWS credentials, customer names, or internal resource identifiers to a public GitHub repository.[cite:7][cite:23][cite:24]

## What this repo includes

- Example Python scripts for querying CUR via Athena.[cite:23][cite:24]
- Example Python script for calling AWS Cost Explorer API.[cite:11]
- Example Athena SQL queries for cost analysis by service and by tag.[cite:23][cite:24][cite:58]
- `.env.example` and `.gitignore` files for safer public publishing.[cite:49][cite:51]
- Mock sample data only; no real billing exports or CUR files.[cite:23][cite:24]

## What this repo must NOT contain

Do **not** upload any of the following to a public repository:

- AWS access keys, secret keys, session tokens, `.env`, or local credential files.[cite:52][cite:56]
- Real AWS account IDs, real S3 bucket names, Athena database names, table names, or API endpoints.[cite:7]
- CUR raw files, Athena query exports, invoices, screenshots, or customer billing JSON/CSV outputs.[cite:23][cite:24]
- Customer names, internal cost-center tags, or organization-specific identifiers.[cite:58]

If any AWS credential was previously committed, revoke it immediately and rotate the credential before publishing the repository.[cite:52][cite:56]

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

1. Enable AWS Cost and Usage Report (CUR) and deliver it to Amazon S3.[cite:23][cite:24]
2. Configure Athena to query CUR data, either manually or with AWS-provided integration steps.[cite:23][cite:24]
3. Copy `.env.example` to `.env` locally and fill in placeholder values with your own environment-specific values. Keep `.env` private and never commit it.[cite:49][cite:51]
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

- CUR is best when detailed billing line items, allocation logic, and custom SQL are required.[cite:23][cite:24]
- Cost Explorer API is better for summarized cost views such as daily or monthly dashboard widgets.[cite:11]
- This repository intentionally uses placeholders and mock values so it can be uploaded safely to a public repo.[cite:7][cite:49][cite:56]
