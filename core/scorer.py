from config import (
    JOB_KEYWORDS,
    PRIORITY_LOCATIONS,
    TITLE_MATCH_SCORE,
    LOCATION_MATCH_SCORE,
    REMOTE_BONUS,
    CANADA_BONUS,
    GOOD_WORD_BONUS,
    BAD_WORD_PENALTY,
    GOOD_WORDS,
    BAD_WORDS,
)

TECH_SKILLS = [
    "windows",
    "windows server",
    "active directory",
    "azure",
    "entra",
    "microsoft 365",
    "office 365",
    "powershell",
    "dns",
    "dhcp",
    "vpn",
    "vmware",
    "virtualization",
    "network",
    "networking",
    "tcp/ip",
    "cisco",
    "linux",
    "docker",
    "intune",
    "sccm",
]


def score_jobs(jobs):

    scored_jobs = []

    for job in jobs:

        score = 0

        title = job.get("title", "").lower()
        location = job.get("location", "").lower()
        description = job.get("description", "").lower()

        text = f"{title} {description}"

        # Title keywords
        for keyword in JOB_KEYWORDS:
            if keyword.lower() in title:
                score += TITLE_MATCH_SCORE

        # Good words
        for word in GOOD_WORDS:
            if word in title:
                score += GOOD_WORD_BONUS

        # Seniority penalty
        for word in BAD_WORDS:
            if word in title:
                score -= BAD_WORD_PENALTY

        # Technical skills
        for skill in TECH_SKILLS:
            if skill in text:
                score += 10

        # Location bonus
        for city in PRIORITY_LOCATIONS:
            if city.lower() in location:
                score += LOCATION_MATCH_SCORE

        # Remote bonus
        if "remote" in location:
            score += REMOTE_BONUS

        if "canada" in location:
            score += CANADA_BONUS

        job["score"] = max(score, 0)

        scored_jobs.append(job)

    scored_jobs.sort(
        key=lambda job: job["score"],
        reverse=True
    )

    return scored_jobs