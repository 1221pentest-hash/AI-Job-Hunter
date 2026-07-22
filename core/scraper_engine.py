"""
AI Job Hunter
Collection Engine
"""

import time

from core.logger import logger
from core.job_validator import validate_job
from core.deduplicator import remove_duplicates

from scrapers.government import get_jobs as government_jobs
from scrapers.greenhouse import get_jobs as greenhouse_jobs
from scrapers.lever import get_jobs as lever_jobs
from scrapers.remoteok import get_jobs as remoteok_jobs
from scrapers.adzuna import get_jobs as adzuna_jobs
from scrapers.ashby import get_jobs as ashby_jobs


SCRAPERS = [
    ("Government", government_jobs),
    ("Greenhouse", greenhouse_jobs),
    ("Lever", lever_jobs),
    ("RemoteOK", remoteok_jobs),
    ("Adzuna", adzuna_jobs),
    ("Ashby", ashby_jobs),
]


def collect_jobs():
    """
    Collect jobs from all configured job sources.
    Returns a list of validated, cleaned, and unique jobs.
    """

    start_time = time.perf_counter()

    attempted_sources = len(SCRAPERS)
    successful_sources = 0
    failed_sources = 0

    all_jobs = []

    print("\n" + "=" * 60)
    print("AI JOB HUNTER - COLLECTION ENGINE")
    print("=" * 60)

    logger.info("=" * 60)
    logger.info("Starting collection")

    for index, (name, scraper) in enumerate(SCRAPERS, start=1):

        print(f"\n[{index}/{attempted_sources}] {name}")
        print("-" * 40)

        scraper_start = time.perf_counter()

        logger.info(f"{name} scraper started")

        try:

            jobs = scraper()

            valid_jobs = 0
            invalid_jobs = 0

            for job in jobs:

                is_valid, cleaned_job = validate_job(job)

                if is_valid:
                    all_jobs.append(cleaned_job)
                    valid_jobs += 1
                else:
                    invalid_jobs += 1

            elapsed = time.perf_counter() - scraper_start

            successful_sources += 1

            logger.info(
                f"{name} SUCCESS | "
                f"Found={len(jobs)} | "
                f"Valid={valid_jobs} | "
                f"Invalid={invalid_jobs} | "
                f"Time={elapsed:.2f}s"
            )

            print("Status      : SUCCESS")
            print(f"Jobs Found  : {len(jobs)}")
            print(f"Valid Jobs  : {valid_jobs}")
            print(f"Invalid     : {invalid_jobs}")
            print(f"Time        : {elapsed:.2f} sec")

        except Exception as error:

            failed_sources += 1

            elapsed = time.perf_counter() - scraper_start

            logger.error(
                f"{name} FAILED | {error} | Time={elapsed:.2f}s"
            )

            print("Status      : FAILED")
            print(f"Reason      : {error}")
            print(f"Time        : {elapsed:.2f} sec")

    # Remove duplicate jobs
    unique_jobs, duplicates_removed = remove_duplicates(all_jobs)

    total_jobs = len(unique_jobs)

    total_time = time.perf_counter() - start_time

    logger.info("=" * 60)
    logger.info("COLLECTION SUMMARY")
    logger.info(f"Sources Attempted : {attempted_sources}")
    logger.info(f"Sources Successful: {successful_sources}")
    logger.info(f"Sources Failed    : {failed_sources}")
    logger.info(f"Unique Jobs       : {total_jobs}")
    logger.info(f"Duplicates Removed: {duplicates_removed}")
    logger.info(f"Elapsed Time      : {total_time:.2f}s")
    logger.info("=" * 60)

    print("\n" + "=" * 60)
    print("COLLECTION SUMMARY")
    print("=" * 60)
    print(f"Sources Attempted : {attempted_sources}")
    print(f"Sources Successful: {successful_sources}")
    print(f"Sources Failed    : {failed_sources}")
    print(f"Unique Jobs       : {total_jobs}")
    print(f"Duplicates Removed: {duplicates_removed}")
    print(f"Elapsed Time      : {total_time:.2f} sec")
    print("=" * 60)

    return unique_jobs