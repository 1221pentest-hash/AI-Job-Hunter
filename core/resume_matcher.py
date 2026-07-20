"""
resume_matcher.py

AI Job Hunter
Resume Matcher 2.0

Compares a job against the user's professional profile
using weighted skills and skill aliases.
"""

from core.resume_data import PROFILE
from core.skill_aliases import SKILL_ALIASES


# ==========================================================
# SKILL WEIGHTS
# ==========================================================

LEVEL_WEIGHTS = {
    "Advanced": 10,
    "Intermediate": 7,
    "Beginner": 4,
}


# ==========================================================
# PROFILE
# ==========================================================

def get_resume_skills():
    """
    Return every skill in the profile with its weight.
    """

    resume_skills = []

    for category in PROFILE["skills"].values():

        for skill in category:

            resume_skills.append(
                {
                    "name": skill["name"],
                    "level": skill["level"],
                    "weight": LEVEL_WEIGHTS.get(
                        skill["level"],
                        5,
                    ),
                }
            )

    return resume_skills


# ==========================================================
# JOB
# ==========================================================

def extract_job_text(job):
    """
    Build one searchable string from the job.
    """

    title = job.get("title", "")
    description = job.get("description", "")

    return f"{title} {description}".lower()


# ==========================================================
# ALIASES
# ==========================================================

def get_skill_aliases(skill_name):
    """
    Return every known alias for a skill.
    """

    return SKILL_ALIASES.get(
        skill_name.lower(),
        [skill_name.lower()],
    )


# ==========================================================
# MATCHING
# ==========================================================

def compare_skills(resume_skills, job_text):
    """
    Compare resume skills against a job description.
    """

    matched_skills = []
    missing_skills = []

    matched_weight = 0
    total_weight = 0

    for skill in resume_skills:

        skill_name = skill["name"]
        skill_weight = skill["weight"]

        total_weight += skill_weight

        aliases = get_skill_aliases(skill_name)

        found = False

        for alias in aliases:

            if alias.lower() in job_text:

                found = True
                break

        if found:

            matched_skills.append(skill_name)
            matched_weight += skill_weight

        else:

            missing_skills.append(skill_name)

    return (
        matched_skills,
        missing_skills,
        matched_weight,
        total_weight,
    )


# ==========================================================
# MATCH %
# ==========================================================

def calculate_match_percentage(
    matched_weight,
    total_weight,
):
    """
    Calculate weighted resume match.
    """

    if total_weight == 0:
        return 0

    return round(
        (matched_weight / total_weight) * 100,
        1,
    )


# ==========================================================
# SUMMARY
# ==========================================================

def build_summary(job):
    """
    Create a readable summary of the match.
    """

    return (
        f"{job['resume_match']}% match | "
        f"{len(job['matched_skills'])} matched | "
        f"{len(job['missing_skills'])} missing"
    )


# ==========================================================
# MAIN
# ==========================================================

def match_job(job):
    """
    Analyze one job against the user's resume.
    """

    resume_skills = get_resume_skills()

    job_text = extract_job_text(job)

    (
        matched_skills,
        missing_skills,
        matched_weight,
        total_weight,
    ) = compare_skills(
        resume_skills,
        job_text,
    )

    match_percentage = calculate_match_percentage(
        matched_weight,
        total_weight,
    )

    job["resume_match"] = match_percentage
    job["matched_skills"] = matched_skills
    job["missing_skills"] = missing_skills
    job["matched_weight"] = matched_weight
    job["total_weight"] = total_weight
    job["match_summary"] = build_summary(job)

    return job