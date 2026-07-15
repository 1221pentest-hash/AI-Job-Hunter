from config import PRIORITY_LOCATIONS, SECONDARY_LOCATIONS, ALLOW_REMOTE


def filter_locations(jobs):
    """
    Keep only jobs located in our target areas.
    """

    filtered = []

    for job in jobs:

        location = job.get("location", "").lower()

        # Remote jobs
        if ALLOW_REMOTE and "remote" in location:
            filtered.append(job)
            continue

        # Priority locations
        if any(city.lower() in location for city in PRIORITY_LOCATIONS):
            filtered.append(job)
            continue

        # Secondary locations
        if any(city.lower() in location for city in SECONDARY_LOCATIONS):
            filtered.append(job)
            continue

    return filtered