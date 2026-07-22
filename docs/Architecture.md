# AI Job Hunter Architecture

## Overview

AI Job Hunter is a Python-based job search automation platform that collects job postings from multiple sources, processes and scores them, and generates reports to help users prioritize job applications.

The application follows a modular architecture, making each component independent and easy to maintain.

---

# System Workflow

```text
Job Sources
│
├── Government of Canada
├── Greenhouse
├── Lever
├── RemoteOK
├── Ashby
└── Adzuna
        │
        ▼
Scraper Engine
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
Job Classification
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
        ├──────────────┐
        ▼              ▼
CSV Reports     Streamlit Dashboard
```

---

# Core Modules

## Scraper Engine

Responsible for collecting jobs from every supported source.

Functions:

- Execute all scrapers
- Merge results
- Return a single job list

---

## Job Validator

Ensures every job contains the required fields before processing.

Examples:

- Title
- Company
- Location
- Description

---

## Duplicate Removal

Removes duplicate jobs collected from different sources.

Duplicates are detected using combinations of:

- Title
- Company
- Location

---

## Location Filter

Filters jobs based on preferred locations.

Examples:

- Canada
- Ottawa
- Remote

---

## Job Classification

Categorizes jobs into technical fields.

Examples:

- IT Support
- Help Desk
- System Administration
- Networking
- Cloud

---

## Resume Matcher

Compares the user's resume against each job description.

Produces:

- Matching skills
- Missing skills
- Resume match percentage

---

## Scoring Engine

Ranks jobs using weighted rules.

Scoring factors include:

- Job category
- Job title
- Technical skills
- Company preference
- Location
- Resume compatibility

---

## Database

Stores processed jobs in SQLite for reporting and dashboard visualization.

---

## Dashboard

Built using Streamlit.

Displays:

- Total jobs
- Canadian jobs
- Highest-scoring jobs
- Daily application list

---

# Design Goals

- Modular architecture
- Easy maintenance
- Simple to extend
- Reusable components
- Fast processing
- Clear separation of responsibilities

---

# Future Improvements

- Docker deployment
- REST API
- Machine learning ranking
- AI-generated cover letters
- Email notifications
- Telegram integration
- Cloud deployment