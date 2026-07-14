from config import APP_NAME, VERSION, AUTHOR
from core.scraper_engine import collect_jobs
from core.exporter import export_jobs

def main():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print(f"Author: {AUTHOR}")
    print("=" * 50)

    print("\nStarting AI Job Hunter...\n")

    jobs = collect_jobs()

    print(f"\nTotal Jobs Found: {len(jobs)}")

    if jobs:
        print("\nExporting jobs...")
        export_jobs(jobs)
        print("Jobs exported successfully!")
    else:
        print("\nNo jobs found.")

    print("\nAI Job Hunter completed successfully.")


if __name__ == "__main__":
    main()