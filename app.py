from config import APP_NAME, VERSION, AUTHOR

from core.scraper_engine import collect_jobs
from core.location_filter import filter_locations
from core.scorer import score_jobs
from core.database import init_db, save_jobs

from core.exporter import (
    export_all_jobs,
    export_canadian_jobs,
    export_apply_today,
)


def main():

    print("=" * 50)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print(f"Author: {AUTHOR}")
    print("=" * 50)

    print("\nStarting AI Job Hunter...\n")

    # ----------------------------------------
    # Initialize Database
    # ----------------------------------------

    init_db()

    # ----------------------------------------
    # Collect Jobs
    # ----------------------------------------

    all_jobs = collect_jobs()

    print(f"\nCollected Jobs: {len(all_jobs)}")

    # ----------------------------------------
    # Export All Jobs
    # ----------------------------------------

    print("\nExporting all collected jobs...")

    export_all_jobs(all_jobs)

    # ----------------------------------------
    # Location Filter
    # ----------------------------------------

    canadian_jobs = filter_locations(all_jobs)

    print(f"Jobs After Location Filter: {len(canadian_jobs)}")

    # ----------------------------------------
    # Export Canadian Jobs
    # ----------------------------------------

    export_canadian_jobs(canadian_jobs)

    # ----------------------------------------
    # Score Jobs
    # ----------------------------------------

    scored_jobs = score_jobs(canadian_jobs)

    print(f"Jobs Scored: {len(scored_jobs)}")

    # ----------------------------------------
    # Keep only relevant jobs
    # ----------------------------------------

    top_jobs = [
        job
        for job in scored_jobs
        if job.get("score", 0) >= 40
    ]

    print(f"Top Matches: {len(top_jobs)}")

    # ----------------------------------------
    # Save Database
    # ----------------------------------------

    new_jobs = save_jobs(top_jobs)

    print("\n==============================")
    print("DATABASE")
    print("==============================")
    print(f"New Jobs Saved : {new_jobs}")

    # ----------------------------------------
    # Export Today's Apply List
    # ----------------------------------------

    export_apply_today(top_jobs)

    # ----------------------------------------
    # Display Results
    # ----------------------------------------

    print("\n==============================")
    print("TODAY'S APPLY LIST")
    print("==============================")

    if not top_jobs:

        print("\nNo matching jobs found.")

    else:

        for job in top_jobs[:10]:

            print(f"\nScore    : {job.get('score', 0)}")
            print(f"Title    : {job.get('title', '')}")
            print(f"Company  : {job.get('company', '')}")
            print(f"Location : {job.get('location', '')}")
            print(f"Source   : {job.get('source', '')}")
            print(f"URL      : {job.get('url', '')}")

    # ----------------------------------------
    # Mission Summary
    # ----------------------------------------

    print("\n==============================")
    print("MISSION COMPLETE")
    print("==============================")

    print(f"Jobs Collected      : {len(all_jobs)}")
    print(f"Canadian Jobs       : {len(canadian_jobs)}")
    print(f"Jobs Scored         : {len(scored_jobs)}")
    print(f"Today's Top Jobs    : {len(top_jobs)}")

    print("\nReports Generated")

    print("------------------------------")

    print("✓ output/all_jobs.csv")
    print("✓ output/canadian_jobs.csv")
    print("✓ output/apply_today_YYYYMMDD_HHMMSS.csv")

    print("\nObjective:")
    print("Apply to today's highest-ranked jobs.")


if __name__ == "__main__":
    main()