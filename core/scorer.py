from config import (
    JOB_KEYWORDS,
    JOB_LOCATIONS,
    TITLE_MATCH_SCORE,
    LOCATION_MATCH_SCORE,
    REMOTE_BONUS,
    CANADA_BONUS,
    GOOD_WORD_BONUS,
    BAD_WORD_PENALTY,
    GOOD_WORDS,
    BAD_WORDS,
)


def score_jobs(jobs):

    scored_jobs = []

    for job in jobs:

        score = 0

        title = job.get("title", "").lower()
        location = job.get("location", "").lower()

        # Title scoring
        for keyword in JOB_KEYWORDS:
            if keyword.lower() in title:
                score += TITLE_MATCH_SCORE

        # Location scoring
        for city in JOB_LOCATIONS:
            if city.lower() in location:
                score += LOCATION_MATCH_SCORE

        # Bonuses
        if "remote" in location:
            score += REMOTE_BONUS

        if "canada" in location:
            score += CANADA_BONUS

        # Entry-level bonus
        for word in GOOD_WORDS:
            if word in title:
                score += GOOD_WORD_BONUS

        # Seniority penalty
        for word in BAD_WORDS:
            if word in title:
                score -= BAD_WORD_PENALTY

        # Never allow negative scores
        score = max(score, 0)

        job["score"] = score

        scored_jobs.append(job)

    scored_jobs.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_jobs