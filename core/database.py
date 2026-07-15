import sqlite3
from typing import Dict, List

DB_NAME = "data/jobs.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_NAME)


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

            score INTEGER DEFAULT 0,

            date_found TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_job(job: Dict):
    """Save a single job. Duplicate URLs are ignored."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jobs (
            title,
            company,
            location,
            url,
            source,
            description,
            date_posted,
            score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        job.get("title", ""),
        job.get("company", ""),
        job.get("location", ""),
        job.get("url", ""),
        job.get("source", ""),
        job.get("description", ""),
        job.get("date_posted", ""),
        job.get("score", 0)

    ))

    conn.commit()
    conn.close()


def save_jobs(jobs: List[Dict]):
    """Save multiple jobs and return the number of new jobs inserted."""

    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0

    for job in jobs:

        cursor.execute("""
            INSERT OR IGNORE INTO jobs (
                title,
                company,
                location,
                url,
                source,
                description,
                date_posted,
                score
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            job.get("title", ""),
            job.get("company", ""),
            job.get("location", ""),
            job.get("url", ""),
            job.get("source", ""),
            job.get("description", ""),
            job.get("date_posted", ""),
            job.get("score", 0)

        ))

        if cursor.rowcount == 1:
            inserted += 1

    conn.commit()
    conn.close()

    return inserted


def get_all_jobs():
    """Return all jobs ordered by score."""

    conn = get_connection()
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM jobs
        ORDER BY score DESC, date_found DESC
    """)

    jobs = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jobs


def get_job_count():
    """Return the total number of jobs."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM jobs")

    count = cursor.fetchone()[0]

    conn.close()

    return count


def clear_jobs():
    """Delete all jobs."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM jobs")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")