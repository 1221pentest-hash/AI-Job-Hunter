import sqlite3

DATABASE = "data/jobs.db"


def initialize_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT UNIQUE,
            source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_jobs(jobs):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    inserted = 0

    for job in jobs:

        cursor.execute("""
            INSERT OR IGNORE INTO jobs
            (title, company, location, url, source)
            VALUES (?, ?, ?, ?, ?)
        """, (
            job["title"],
            job["company"],
            job["location"],
            job["url"],
            job["source"]
        ))

        # rowcount == 1 means a new row was inserted
        if cursor.rowcount == 1:
            inserted += 1

    connection.commit()
    connection.close()

    return inserted


def get_all_jobs():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            title,
            company,
            location,
            url,
            source,
            created_at
        FROM jobs
        ORDER BY created_at DESC
    """)

    jobs = cursor.fetchall()

    connection.close()

    return jobs