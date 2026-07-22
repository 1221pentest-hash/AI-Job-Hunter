# API Documentation

## Overview

AI Job Hunter does not currently expose a public REST API. Instead, the project is organized as a collection of Python modules that work together to collect, process, score, and export job postings.

This document describes the internal modules and their responsibilities.

---

# Application Entry Point

## app.py

Coordinates the complete workflow.

Responsibilities:

- Initialize the database
- Execute all job scrapers
- Validate collected jobs
- Remove duplicate jobs
- Filter Canadian opportunities
- Classify jobs
- Match jobs against the resume
- Score each job
- Save jobs to SQLite
- Export CSV reports
- Display execution summary

---

# Core Modules

## scraper_engine.py

Collects jobs from all supported sources.

Functions:

- Execute individual scrapers
- Merge job results
- Return a unified job list

---

## database.py

Manages SQLite database operations.

Responsibilities:

- Create database
- Create tables
- Insert jobs
- Update existing jobs
- Retrieve stored jobs

---

## exporter.py

Exports processed data into CSV reports.

Generated reports include:

- all_jobs.csv
- canadian_jobs.csv
- apply_today.csv

---

## deduplicator.py

Removes duplicate job postings.

Duplicate detection considers:

- Job title
- Company
- Location

---

## job_validator.py

Validates job records before processing.

Checks include:

- Required fields
- Empty values
- Data consistency

---

## location_filter.py

Filters jobs based on preferred locations.

Supported examples include:

- Canada
- Ottawa
- Remote

---

## classifier.py

Assigns job categories based on titles and descriptions.

Example categories:

- IT Support
- Help Desk
- Systems Administration
- Networking
- Cloud
- Cybersecurity

---

## resume_matcher.py

Compares the resume against each job description.

Outputs:

- Resume match percentage
- Matched skills
- Missing skills

---

## scorer.py

Calculates the final score for every job.

Scoring factors include:

- Job category
- Job title
- Technical skills
- Company
- Location
- Resume compatibility

---

## rules.py

Defines the weighted scoring rules used by the scoring engine.

Includes:

- Title rules
- Skill rules
- Company rules
- Penalty rules

---

## logger.py

Provides centralized logging for the application.

Responsibilities:

- Record execution events
- Log warnings
- Log errors
- Support troubleshooting

---

# Scraper Modules

Located in:

```text
scrapers/
```

Current scrapers:

- government.py
- greenhouse.py
- lever.py
- remoteok.py
- ashby.py
- adzuna.py

Each scraper is responsible for:

- Connecting to its source
- Collecting jobs
- Returning standardized job dictionaries

---

# Dashboard

## dashboard.py

Built with Streamlit.

Displays:

- Total jobs collected
- Canadian jobs
- Resume matches
- Highest-scoring jobs
- Daily application recommendations

---

# Configuration

## config.py

Stores application-wide configuration values such as:

- Application name
- Version
- Author
- Default settings

---

# Future API Plans

Future releases may include:

- REST API
- JSON endpoints
- Authentication
- Job search endpoints
- Resume upload endpoint
- AI recommendation endpoint