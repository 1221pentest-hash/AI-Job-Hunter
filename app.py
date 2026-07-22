from config import APP_NAME, VERSION, AUTHOR

from core.scraper_engine import collect_jobs
from core.location_filter import filter_locations
from core.classifier import classify_jobs
from core.resume_matcher import match_job
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
    # Filter by Location
    # ----------------------------------------

    canadian_jobs = filter_locations(all_jobs)

    print(f"Jobs After Location Filter: {len(canadian_jobs)}")

    # ----------------------------------------
    # Export Canadian Jobs
    # ----------------------------------------

    export_canadian_jobs(canadian_jobs)

    # ----------------------------------------
    # Classify Jobs
    # ----------------------------------------

    classified_jobs = classify_jobs(canadian_jobs)

    print(f"Jobs Classified: {len(classified_jobs)}")

    # ----------------------------------------
    # Resume Matcher
    # ----------------------------------------

    matched_jobs = []

    for job in classified_jobs:
        matched_jobs.append(match_job(job))

    print("\n===== SAMPLE JOB =====")
    print(classified_jobs[0])
    print("======================\n")

    # ----------------------------------------
    # Score Jobs
    # ----------------------------------------

    scored_jobs = score_jobs(matched_jobs)

    print(f"Jobs Scored: {len(scored_jobs)}")

    # ----------------------------------------
    # Keep Only Good Matches
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

            print("-" * 60)
            print(f"Category      : {job.get('category', 'Other')}")
            print(f"Resume Match  : {job.get('resume_match', 0)}%")
            print(f"Score         : {job.get('score', 0)}")
            print(f"Title         : {job.get('title', '')}")
            print(f"Company       : {job.get('company', '')}")
            print(f"Location      : {job.get('location', '')}")
            print(f"Source        : {job.get('source', '')}")
            print(f"URL           : {job.get('url', '')}")

            matched = job.get("matched_skills", [])
            missing = job.get("missing_skills", [])

            if matched:
                print(f"Matched Skills: {', '.join(matched)}")

            if missing:
                print(f"Missing Skills: {', '.join(missing[:5])}")

    # ----------------------------------------
    # Mission Summary
    # ----------------------------------------

    print("\n==============================")
    print("MISSION COMPLETE")
    print("==============================")

    print(f"Jobs Collected       : {len(all_jobs)}")
    print(f"Canadian Jobs        : {len(canadian_jobs)}")
    print(f"Jobs Classified      : {len(classified_jobs)}")
    print(f"Resume Matched Jobs  : {len(matched_jobs)}")
    print(f"Jobs Scored          : {len(scored_jobs)}")
    print(f"Top Matches          : {len(top_jobs)}")

    print("\nReports Generated")
    print("------------------------------")
    print("✓ output/all_jobs.csv")
    print("✓ output/canadian_jobs.csv")
    print("✓ output/apply_today_YYYYMMDD_HHMMSS.csv")

    print("\nObjective:")
    print("Apply to today's highest-ranked jobs.")


if __name__ == "__main__":
    main()