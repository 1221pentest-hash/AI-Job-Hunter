import sqlite3
from typing import Dict, List

DB_NAME = "data/jobs.db"


# --------------------------------------------------
# Connection
# --------------------------------------------------

def get_connection():
    """Create and return a SQLite connection."""
    return sqlite3.connect(DB_NAME)


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

def init_db():
    """Create the jobs table if it doesn't exist."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            company TEXT,

            location TEXT,

            url TEXT UNIQUE,

            source TEXT,

            description TEXT,

            date_posted TEXT,

            category TEXT,

            score REAL DEFAULT 0,

            resume_match REAL DEFAULT 0,

            matched_skills TEXT,

            missing_skills TEXT,

            date_found TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# Save One Job
# --------------------------------------------------

def save_job(job: Dict):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO jobs (

            title,
            company,
            location,
            url,
            source,
            description,
            date_posted,
            category,
            score,
            resume_match,
            matched_skills,
            missing_skills

        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        job.get("title", ""),
        job.get("company", ""),
        job.get("location", ""),
        job.get("url", ""),
        job.get("source", ""),
        job.get("description", ""),
        job.get("date_posted", ""),
        job.get("category", ""),
        job.get("score", 0),
        job.get("resume_match", 0),
        ", ".join(job.get("matched_skills", [])),
        ", ".join(job.get("missing_skills", []))

    ))

    conn.commit()
    conn.close()


# --------------------------------------------------
# Save Multiple Jobs
# --------------------------------------------------

def save_jobs(jobs: List[Dict]):

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0

    for job in jobs:

        cursor.execute("""
            INSERT OR REPLACE INTO jobs (

                title,
                company,
                location,
                url,
                source,
                description,
                date_posted,
                category,
                score,
                resume_match,
                matched_skills,
                missing_skills

            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            job.get("title", ""),
            job.get("company", ""),
            job.get("location", ""),
            job.get("url", ""),
            job.get("source", ""),
            job.get("description", ""),
            job.get("date_posted", ""),
            job.get("category", ""),
            job.get("score", 0),
            job.get("resume_match", 0),
            ", ".join(job.get("matched_skills", [])),
            ", ".join(job.get("missing_skills", []))

        ))

        if cursor.rowcount == 1:
            inserted += 1

    conn.commit()
    conn.close()

    return inserted


# --------------------------------------------------
# Queries
# --------------------------------------------------

def get_all_jobs():

    conn = get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM jobs
        ORDER BY score DESC,
                 resume_match DESC,
                 date_found DESC
    """)

    jobs = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jobs


def get_top_jobs(limit=20):

    conn = get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM jobs
        ORDER BY score DESC,
                 resume_match DESC
        LIMIT ?
    """, (limit,))

    jobs = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jobs


def get_job_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM jobs
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


def clear_jobs():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM jobs
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    init_db()

    print("Database initialized successfully.")