import requests

LEVER_COMPANIES = [
    "lever",
    "hackerrank",
    "asana",
    "plaid",
    "rippling",
    "benchling",
    "scale-ai",
]

def get_jobs():

    jobs = []

    session = requests.Session()

    headers = {
        "User-Agent": "AI-Job-Hunter/1.0"
    }

    for company in LEVER_COMPANIES:

        url = f"https://api.lever.co/v0/postings/{company}?mode=json"

        try:

            response = session.get(
                url,
                headers=headers,
                timeout=10
            )

            if response.status_code != 200:
                continue

            data = response.json()

            for job in data:

                jobs.append({

                    "title": job.get("text", ""),

                    "company": company.replace("-", " ").title(),

                    "location": job.get("categories", {}).get("location", ""),

                    "url": job.get("hostedUrl", ""),

                    "source": "Lever",

                    "description": "",

                    "date_posted": job.get("createdAt", "")

                })

        except Exception as e:

            print(f"Lever ({company}): {e}")

    return jobs


if __name__ == "__main__":

    jobs = get_jobs()

    print(f"Collected {len(jobs)} Lever jobs")