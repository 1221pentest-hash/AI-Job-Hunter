"""
Career Classification Engine
"""

KEEP_CATEGORIES = {

    "IT Support": [

        "it support",
        "help desk",
        "desktop support",
        "technical support",
        "service desk",

        "support analyst",
        "support specialist",
        "support technician",

        "it technician",
        "it analyst",
        "technical analyst",

        "desktop analyst",
        "desktop engineer",

        "end user support",
        "end user computing",

        "endpoint support",
        "endpoint specialist",
        "endpoint administrator",

        "workplace support",
        "workplace technology",

        "client support",
        "customer support",

        "technology support",

        "service operations",
        "service operations analyst",

    ],

    "Systems": [

        "system administrator",
        "systems administrator",
        "sysadmin",

        "windows administrator",
        "linux administrator",

        "server administrator",

        "systems support",

        "infrastructure support",
        "infrastructure analyst",

        "junior administrator",

    ],

    "Networking": [

        "network administrator",
        "network support",
        "network technician",
        "network analyst",

        "noc",
        "noc analyst",

    ],

    "Security": [

        "soc analyst",
        "security analyst",
        "cybersecurity analyst",

    ],

}


REJECT = [

    "software engineer",
    "software developer",
    "developer",

    "backend",
    "frontend",
    "full stack",

    "machine learning",
    "ai engineer",
    "data scientist",

    "product manager",
    "product owner",

    "finance",
    "financial",

    "marketing",
    "sales",

    "account executive",
    "account manager",

    "director",
    "manager",
    "principal",
    "architect",

]


def classify_job(job):

    title = job.get("title", "").lower()

    # Reject FIRST
    for word in REJECT:
        if word in title:
            return "Reject"

    # Keep categories
    for category, keywords in KEEP_CATEGORIES.items():

        for keyword in keywords:

            if keyword in title:
                return category

    return "Other"


def filter_categories(jobs):

    filtered = []

    for job in jobs:

        category = classify_job(job)

        job["category"] = category

        if category in [
            "IT Support",
            "Systems",
            "Networking",
            "Security",
        ]:

            filtered.append(job)

    return filtered