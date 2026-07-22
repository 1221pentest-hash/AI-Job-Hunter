# Database Documentation

## Overview

AI Job Hunter uses SQLite as its local database to store collected, processed, and scored job postings.

SQLite was selected because it is lightweight, portable, requires no server installation, and is ideal for desktop automation projects.

---

# Database Engine

- SQLite 3

Database location:

```text
data/jobs.db
```

---

# Data Flow

```text
Job Scrapers
      │
      ▼
Job Validator
      │
      ▼
Duplicate Removal
      │
      ▼
Location Filter
      │
      ▼
Resume Matcher
      │
      ▼
Scoring Engine
      │
      ▼
SQLite Database
      │
      ├───────────────┐
      ▼               ▼
CSV Reports     Dashboard
```

---

# Main Table

The application stores processed jobs in a single table.

## jobs

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Primary Key |
| title | TEXT | Job title |
| company | TEXT | Company name |
| location | TEXT | Job location |
| description | TEXT | Job description |
| url | TEXT | Original job posting URL |
| source | TEXT | Job source |
| salary | TEXT | Salary information |
| employment_type | TEXT | Employment type |
| posted_date | TEXT | Posting date |
| category | TEXT | Job classification |
| resume_match | REAL | Resume compatibility percentage |
| score | REAL | Final job score |

---

# Processing Pipeline

Every job passes through the following stages before being saved:

1. Collection
2. Validation
3. Duplicate removal
4. Location filtering
5. Classification
6. Resume matching
7. Scoring
8. Database storage

---

# Exported Reports

The database is used to generate:

- All Jobs
- Canadian Jobs
- Apply Today report

These reports are exported as CSV files in the `output/` directory.

---

# Benefits of SQLite

- Lightweight
- Fast
- Serverless
- Cross-platform
- Easy backup
- Ideal for local automation projects

---

# Future Database Enhancements

Planned improvements include:

- Multiple tables for normalization
- Job history tracking
- Saved application status
- Employer database
- Interview tracking
- User profiles
- PostgreSQL support