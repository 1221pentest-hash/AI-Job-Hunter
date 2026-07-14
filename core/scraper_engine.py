from scrapers.government import get_jobs as government_jobs
from scrapers.greenhouse import get_jobs as greenhouse_jobs
from scrapers.lever import get_jobs as lever_jobs
from scrapers.remoteok import get_jobs as remoteok_jobs
from scrapers.adzuna import get_jobs as adzuna_jobs


def collect_jobs():
    all_jobs = []

    scrapers = [
        ("Government", government_jobs),
        ("Greenhouse", greenhouse_jobs),
        ("Lever", lever_jobs),
        ("RemoteOK", remoteok_jobs),
        ("Adzuna", adzuna_jobs),
    ]

    for name, scraper in scrapers:
        print(f"\nSearching {name}...")

        try:
            jobs = scraper()
            print(f"✓ Found {len(jobs)} jobs")
            all_jobs.extend(jobs)

        except Exception as error:
            print(f"✗ Error while searching {name}")
            print(error)

    return all_jobs