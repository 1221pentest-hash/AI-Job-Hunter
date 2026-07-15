from config import APP_NAME, VERSION, AUTHOR

from core.scraper_engine import collect_jobs
from core.filters import filter_jobs
from core.scorer import score_jobs
from core.database import init_db, save_jobs
from core.exporter import export_jobs


def main():

    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print(f"Author: {AUTHOR}")
    print("=" * 50)

    print("\nStarting AI Job Hunter...\n")

    # Initialize database
    init_db()

    # Collect jobs
    jobs = collect_jobs()

    print(f"\nCollected Jobs: {len(jobs)}")

    # Filter jobs
    jobs = filter_jobs(jobs)

    print(f"Jobs After Filtering: {len(jobs)}")

    # Score jobs
    jobs = score_jobs(jobs)

    print("\n==============================")
    print("TOP MATCHES")
    print("==============================")

    for job in jobs[:10]:

        print(f"\nScore    : {job.get('score', 0)}")
        print(f"Title    : {job.get('title', 'N/A')}")
        print(f"Company  : {job.get('company', 'N/A')}")
        print(f"Location : {job.get('location', 'N/A')}")
        print(f"Source   : {job.get('source', 'N/A')}")

    # Save jobs
    new_jobs = save_jobs(jobs)

    print("\n==============================")
    print("DATABASE")
    print("==============================")
    print(f"New Jobs Saved : {new_jobs}")

    # Export CSV
    if jobs:

        print("\nExporting jobs...")

        export_jobs(jobs)

        print("Jobs exported successfully!")

    else:

        print("\nNo matching jobs found.")

    print("\n==============================")
    print("AI Job Hunter completed successfully.")
    print("==============================")


if __name__ == "__main__":
    main()