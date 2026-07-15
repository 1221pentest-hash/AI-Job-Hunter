from config import JOB_KEYWORDS


def filter_jobs(jobs):

    filtered_jobs = []

    for job in jobs:

        title = job.get("title", "").lower()

        if any(keyword.lower() in title for keyword in JOB_KEYWORDS):
            filtered_jobs.append(job)

    return filtered_jobs