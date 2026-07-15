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

    all_jobs = []

    total_sources = 0
    total_jobs = 0

    for name, scraper in SCRAPERS:

        print(f"\nSearching {name}...")

        try:

            jobs = scraper()

            print(f"✓ Found {len(jobs)} jobs")

            total_sources += 1
            total_jobs += len(jobs)

            all_jobs.extend(jobs)

        except Exception as error:

            print(f"✗ {name} failed")
            print(error)

    print("\n==============================")
    print("COLLECTION SUMMARY")
    print("==============================")
    print(f"Sources Checked : {total_sources}")
    print(f"Jobs Collected  : {total_jobs}")
    print("==============================")

    return all_jobs