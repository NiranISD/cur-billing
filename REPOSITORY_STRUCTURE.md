# Repository structure

This document explains the folder layout for the public-safe AWS CUR + Python billing example repository. The structure follows common GitHub and Python project practices by keeping documentation at the root, code under `src/`, SQL examples in a dedicated folder, and private or generated files excluded via `.gitignore`.[cite:49][cite:64][cite:65][cite:67]

```text
aws-cur-python-public-repo/
├─ README.md
├─ REPOSITORY_STRUCTURE.md
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

## Root files

- `README.md` — overview, setup steps, usage, and safety notes for publishing the repository publicly.[cite:65][cite:67]
- `REPOSITORY_STRUCTURE.md` — explains what each file and folder is for so the repo is easy to understand for reviewers and collaborators.[cite:65]
- `.gitignore` — prevents private files, temporary files, local environments, and billing exports from being committed.[cite:49][cite:65][cite:67]
- `.env.example` — documents required environment variables without exposing real values.[cite:64][cite:65]
- `requirements.txt` — lists the Python dependencies needed to run the examples.[cite:64][cite:68]

## Source code

The `src/` folder contains the runnable Python examples and keeps application code separate from documentation and data files, which is a common Python project pattern.[cite:63][cite:64][cite:68]

- `config.py` — loads environment variables and centralizes placeholder configuration values.
- `query_cur_athena.py` — example script that submits an Athena query against CUR data and reads the result.
- `get_cost_explorer.py` — example script that calls AWS Cost Explorer API for summarized billing data.

## SQL examples

The `sql/` folder contains reusable Athena query templates. Keeping SQL separate from Python makes the examples easier to review, copy, and adapt to a real CUR table.[cite:24][cite:65]

- `total_cost_by_service.sql` — summarized cost grouped by AWS service.
- `cost_by_tag.sql` — summarized cost grouped by tag and service.

## Documentation

The `docs/` folder is reserved for operational notes such as publishing guidance, architecture notes, or setup walkthroughs. A separate docs folder helps keep the root of the repository clean while preserving useful project documentation.[cite:65]

- `publishing-checklist.md` — checklist for removing secrets and replacing account-specific identifiers before pushing to a public repo.[cite:52][cite:56]

## Sample data

The `data/` folder contains only mock demonstration data. In a public repository, this folder should never contain real CUR exports, Athena result sets, invoices, or customer billing records.[cite:23][cite:24][cite:65]

- `sample_cur_extract.csv` — fabricated sample rows for explaining schema and expected output shape.
