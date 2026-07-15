import requests

COMPANIES = [
    "stripe",
    "airbnb",
    "cloudflare",
    "datadog",
    "openai"
]


def get_jobs():

    jobs = []

    for company in COMPANIES:

        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        try:

            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                continue

            data = response.json()

            for job in data.get("jobs", []):

                jobs.append({
                    "title": job.get("title"),
                    "company": company.title(),
                    "location": job.get("location", {}).get("name", "Unknown"),
                    "url": job.get("absolute_url"),
                    "source": "Greenhouse"
                })

        except Exception as e:

            print(f"Error collecting {company}: {e}")

    return jobs