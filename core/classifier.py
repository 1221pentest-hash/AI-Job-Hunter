"""
AI Job Hunter
Job Classifier
"""

CATEGORY_RULES = {
    "IT Support": [
        "it support",
        "help desk",
        "service desk",
        "technical support",
        "desktop support",
        "support technician",
        "field technician",
        "deployment technician",
    ],

    "System Administration": [
        "system administrator",
        "systems administrator",
        "windows administrator",
        "server administrator",
        "infrastructure administrator",
    ],

    "Networking": [
        "network technician",
        "network administrator",
        "network engineer",
        "noc",
    ],

    "Cybersecurity": [
        "security analyst",
        "soc analyst",
        "cybersecurity",
        "information security",
    ],

    "Cloud / DevOps": [
        "devops",
        "cloud engineer",
        "cloud administrator",
        "platform engineer",
        "site reliability",
        "sre",
    ],

    "Software Development": [
        "software engineer",
        "software developer",
        "backend",
        "frontend",
        "full stack",
        "full-stack",
        "web developer",
        "mobile developer",
    ],

    "Sales": [
        "sales",
        "account executive",
        "business development",
    ],

    "Other": []
}


def classify_job(job):
    """
    Classify a single job.
    """

    title = job.get("title", "").lower()
    description = job.get("description", "").lower()

    text = f"{title} {description}"

    for category, keywords in CATEGORY_RULES.items():

        for keyword in keywords:

            if keyword in text:
                job["category"] = category
                return job

    job["category"] = "Other"
    return job


def classify_jobs(jobs):
    """
    Classify every collected job.
    """

    classified = []

    for job in jobs:
        classified.append(classify_job(job))

    return classified