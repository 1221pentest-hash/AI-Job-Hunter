import requests

COMPANIES = [
    # Enterprise
    "stripe",
    "airbnb",
    "cloudflare",
    "datadog",
    "openai",

    # IT / Security
    "1password",
    "crowdstrike",
    "elastic",
    "hashicorp",
    "gitlab",

    # Infrastructure
    "digitalocean",
    "canonical",

    # Canadian
    "shopify",

    # Customer Support
    "zapier",
    "sourcegraph"
]


def get_jobs():

    jobs = []

    session = requests.Session()

    headers = {
        "User-Agent": "AI-Job-Hunter/1.0"
    }

    for company in COMPANIES:

        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        try:

            response = session.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            data = response.json()

            for job in data.get("jobs", []):

                jobs.append({

                    "title": job.get("title", ""),

                    "company": company.replace("-", " ").title(),

                    "location": job.get("location", {}).get("name", ""),

                    "url": job.get("absolute_url", ""),

                    "source": "Greenhouse",

                    "description": "",

                    "date_posted": ""

                })

        except Exception as e:

            print(f"Greenhouse ({company}): {e}")

    return jobs


if __name__ == "__main__":

    jobs = get_jobs()

    print(f"Collected {len(jobs)} Greenhouse jobs")