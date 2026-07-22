"""
dashboard/data.py

Database access layer for the AI Job Hunter dashboard.
"""

from pathlib import Path
import sqlite3

import pandas as pd

# --------------------------------------------------
# Database Path
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_FILE = PROJECT_ROOT / "data" / "jobs.db"


# --------------------------------------------------
# Database Connection
# --------------------------------------------------

def get_connection():
    """Return a SQLite connection."""
    return sqlite3.connect(DB_FILE)


# --------------------------------------------------
# Load Jobs
# --------------------------------------------------

def load_jobs() -> pd.DataFrame:
    """
    Load all jobs from the database.
    """

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM jobs
            ORDER BY
                favorite DESC,
                score DESC,
                resume_match DESC,
                date_found DESC
            """,
            conn,
        )

    finally:
        conn.close()

    return df


# --------------------------------------------------
# Favorites
# --------------------------------------------------

def set_favorite(job_id: int, value: bool):
    """
    Mark or unmark a job as favorite.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE jobs
        SET favorite = ?
        WHERE id = ?
        """,
        (1 if value else 0, job_id),
    )

    conn.commit()
    conn.close()


def toggle_favorite(job_id: int):
    """
    Toggle favorite status.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT favorite
        FROM jobs
        WHERE id = ?
        """,
        (job_id,),
    )

    row = cursor.fetchone()

    if row is None:
        conn.close()
        return

    new_value = 0 if row[0] else 1

    cursor.execute(
        """
        UPDATE jobs
        SET favorite = ?
        WHERE id = ?
        """,
        (new_value, job_id),
    )

    conn.commit()
    conn.close()


def get_favorites() -> pd.DataFrame:
    """
    Return favorite jobs only.
    """

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM jobs
            WHERE favorite = 1
            ORDER BY
                score DESC,
                resume_match DESC
            """,
            conn,
        )

    finally:
        conn.close()

    return df


# --------------------------------------------------
# Dashboard Statistics
# --------------------------------------------------

def get_statistics(df: pd.DataFrame):

    if df.empty:

        return {
            "total_jobs": 0,
            "favorite_jobs": 0,
            "average_score": 0,
            "average_resume_match": 0,
            "top_matches": 0,
        }

    average_score = round(df["score"].mean(), 1)

    average_resume = round(
        df["resume_match"].mean(),
        1,
    )

    top_matches = len(
        df[df["score"] >= 100]
    )

    favorite_jobs = len(
        df[df["favorite"] == 1]
    )

    return {

        "total_jobs": len(df),

        "favorite_jobs": favorite_jobs,

        "average_score": average_score,

        "average_resume_match": average_resume,

        "top_matches": top_matches,

    }