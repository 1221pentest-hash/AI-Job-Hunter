"""
AI Job Hunter
Deduplicator
"""

from typing import List, Dict, Tuple


def remove_duplicates(jobs: List[Dict]) -> Tuple[List[Dict], int]:
    """
    Remove duplicate jobs.

    Returns:
        unique_jobs, duplicates_removed
    """

    seen = set()
    unique_jobs = []

    for job in jobs:
        key = (
            job.get("title", "").strip().lower(),
            job.get("company", "").strip().lower(),
            job.get("location", "").strip().lower(),
        )

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    duplicates_removed = len(jobs) - len(unique_jobs)

    return unique_jobs, duplicates_removed