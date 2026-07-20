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

    Returns
    -------
    pandas.DataFrame
    """

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM jobs
            ORDER BY score DESC,
                     resume_match DESC,
                     date_found DESC
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

    return {

        "total_jobs": len(df),

        "average_score": average_score,

        "average_resume_match": average_resume,

        "top_matches": top_matches,

    }