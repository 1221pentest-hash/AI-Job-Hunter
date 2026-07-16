from config import (
    PRIORITY_LOCATIONS,
    TITLE_MATCH_SCORE,
    LOCATION_MATCH_SCORE,
    REMOTE_BONUS,
    CANADA_BONUS,
)

# ----------------------------------------
# Positive keywords
# ----------------------------------------

POSITIVE = {

    "help desk": 40,
    "service desk": 40,

    "it support": 45,
    "technical support": 40,
    "desktop support": 40,

    "support": 20,

    "it technician": 35,
    "field technician": 35,

    "systems administrator": 45,
    "system administrator": 45,
    "administrator": 20,

    "technical analyst": 35,
    "it analyst": 35,
    "desktop analyst": 35,
    "analyst": 10,

    "infrastructure": 25,

    "endpoint": 20,

    "workplace": 15,

    "windows": 15,
    "active directory": 20,
    "powershell": 15,
    "dns": 10,
    "dhcp": 10,
    "microsoft 365": 15,
    "azure": 15,
    "entra": 15,
    "intune": 15,
    "sccm": 15,
    "vmware": 15,
    "linux": 10,
    "docker": 10,
    "network": 15,
    "vpn": 10,
}

# ----------------------------------------
# Negative keywords
# ----------------------------------------

NEGATIVE = {

    "software engineer": -80,
    "software developer": -80,

    "machine learning": -80,
    "ai engineer": -80,

    "backend": -60,
    "frontend": -60,
    "full stack": -60,

    "data scientist": -70,

    "marketing": -50,
    "sales": -50,
    "finance": -40,

    "account executive": -60,

    "director": -40,
    "principal": -40,
    "staff": -30,
    "senior": -20,
}


def score_jobs(jobs):

    scored = []

    for job in jobs:

        score = 0

        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        location = job.get("location", "").lower()

        text = f"{title} {description}"

        # Positive scoring
        for word, value in POSITIVE.items():

            if word in text:
                score += value

        # Negative scoring
        for word, value in NEGATIVE.items():

            if word in text:
                score += value

        # Preferred locations
        for city in PRIORITY_LOCATIONS:

            if city.lower() in location:
                score += LOCATION_MATCH_SCORE

        if "remote" in location:
            score += REMOTE_BONUS

        if "canada" in location:
            score += CANADA_BONUS

        job["score"] = score

        scored.append(job)

    scored.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored