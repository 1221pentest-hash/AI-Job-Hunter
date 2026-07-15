import requests

ASHBY_COMPANIES = [
    "openai",
    "anthropic",
    "notion",
    "figma",
    "vercel",
    "perplexity",
    "scaleai",
    "cursor",
    "windsurf",
]


def get_jobs():

    jobs = []

    session = requests.Session()

    headers = {
        "User-Agent": "AI-Job-Hunter/1.0"
    }

    for company in ASHBY_COMPANIES:

        url = f"https://jobs.ashbyhq.com/api/non-user-graphql?organization={company}"

        try:

            response = session.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            # Placeholder until we verify each company's API
            # Different Ashby organizations expose slightly different endpoints.

        except Exception:
            pass

    return jobs


if __name__ == "__main__":

    jobs = get_jobs()

    print(f"Collected {len(jobs)} Ashby jobs")