"""
AI Job Hunter
Job Validation & Normalization Engine
"""

REQUIRED_FIELDS = [
    "title",
    "company",
    "location",
    "url",
]


DEFAULT_VALUES = {
    "salary": "Not specified",
    "employment_type": "Unknown",
    "description": "",
    "posted_date": "Unknown",
    "source": "Unknown",
}


def validate_job(job: dict):

    """
    Validate a single job.

    Returns:
        (True, job) if valid
        (False, None) if invalid
    """

    if not isinstance(job, dict):
        return False, None

    # Required fields
    for field in REQUIRED_FIELDS:

        value = job.get(field)

        if value is None:
            return False, None

        if str(value).strip() == "":
            return False, None

    # Apply default values
    for field, default in DEFAULT_VALUES.items():

        if field not in job or job[field] is None:
            job[field] = default

    # Clean strings
    for key, value in job.items():

        if isinstance(value, str):
            job[key] = value.strip()

    return True, job