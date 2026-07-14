from config import APP_NAME, VERSION, AUTHOR

from core.scraper_engine import collect_jobs
from core.database import initialize_database, save_jobs
from core.exporter import export_jobs


def main():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print(f"Author: {AUTHOR}")
    print("=" * 50)

    print("\nStarting AI Job Hunter...\n")

    # Initialize database
    initialize_database()

    # Collect jobs from all scrapers
    jobs = collect_jobs()

    # Save new jobs to the database
    new_jobs = save_jobs(jobs)

    print(f"\nNew jobs saved: {new_jobs}")
    print(f"Total Jobs Found: {len(jobs)}")

    # Export jobs to CSV
    if jobs:
        print("\nExporting jobs...")
        export_jobs(jobs)
    else:
        print("\nNo jobs found.")

    print("\nAI Job Hunter completed successfully.")


if __name__ == "__main__":
    main()