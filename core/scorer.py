"""
AI Job Hunter
Job Scoring Engine
Version 2.0
"""

import re

from config import (
    PRIORITY_LOCATIONS,
    LOCATION_MATCH_SCORE,
    REMOTE_BONUS,
    CANADA_BONUS,
)

from core.rules import (
    TITLE_RULES,
    SKILL_RULES,
    COMPANY_RULES,
    PENALTY_RULES,
)

# ==========================================================
# CATEGORY BONUS
# ==========================================================

CATEGORY_SCORES = {
    "IT Support": 30,
    "System Administration": 25,
    "Networking": 20,
    "Cybersecurity": 15,
    "Cloud / DevOps": 10,
    "Software Development": -40,
    "Sales": -100,
    "Other": -20,
}


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def apply_rules(text, rules, score, reasons, label):
    """
    Apply keyword-based scoring rules using whole-word matching.
    """

    for keyword, value in rules.items():

        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, text):

            score += value
            reasons.append(f"{value:+} {label}: {keyword}")

    return score

def apply_location_bonus(location, score, reasons):
    """
    Apply bonuses based on job location.
    """

    for city in PRIORITY_LOCATIONS:

        if city.lower() in location:
            score += LOCATION_MATCH_SCORE
            reasons.append(
                f"{LOCATION_MATCH_SCORE:+} Location: {city}"
            )

    if "remote" in location:
        score += REMOTE_BONUS
        reasons.append(f"{REMOTE_BONUS:+} Remote")

    if "canada" in location:
        score += CANADA_BONUS
        reasons.append(f"{CANADA_BONUS:+} Canada")

    return score


def apply_resume_match(job, score, reasons):
    """
    Add Resume Matcher score.
    """

    resume_match = job.get("resume_match", 0)

    score += resume_match

    reasons.append(
        f"+{resume_match} Resume Match ({resume_match}%)"
    )

    return score


# ==========================================================
# MAIN SCORING ENGINE
# ==========================================================

def score_jobs(jobs):
    """
    Score every job and return the ranked list.
    """

    scored_jobs = []

    for job in jobs:

        score = 0
        reasons = []

        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        company = job.get("company", "").lower()
        location = job.get("location", "").lower()
        category = job.get("category", "Other")

        text = f"{title} {description}"

        # ==================================================
        # CATEGORY
        # ==================================================

        category_score = CATEGORY_SCORES.get(category, 0)

        score += category_score

        reasons.append(
            f"{category_score:+} Category: {category}"
        )

        # ==================================================
        # TITLE
        # ==================================================

        score = apply_rules(
            title,
            TITLE_RULES,
            score,
            reasons,
            "Title",
        )

        # ==================================================
        # SKILLS
        # ==================================================

        score = apply_rules(
            text,
            SKILL_RULES,
            score,
            reasons,
            "Skill",
        )

        # ==================================================
        # COMPANY
        # ==================================================

        score = apply_rules(
            company,
            COMPANY_RULES,
            score,
            reasons,
            "Company",
        )

        # ==================================================
        # PENALTIES
        # ==================================================

        score = apply_rules(
            text,
            PENALTY_RULES,
            score,
            reasons,
            "Penalty",
        )

        # ==================================================
        # LOCATION
        # ==================================================

        score = apply_location_bonus(
            location,
            score,
            reasons,
        )

                # ==================================================
        # RESUME MATCH
        # ==================================================

        score = apply_resume_match(
            job,
            score,
            reasons,
        )

        # Temporary Debug
        if job["title"] == "IT Support Technician":
            print("\n===== SCORE BREAKDOWN =====")
            for reason in reasons:
                print(reason)
            print(f"FINAL SCORE: {score}")
            print("===========================\n")

        # ==================================================
        # SAVE RESULTS
        # ==================================================

        job["score"] = score
        job["reasons"] = reasons

        scored_jobs.append(job)

    scored_jobs.sort(
        key=lambda job: job["score"],
        reverse=True,
    )

    return scored_jobs