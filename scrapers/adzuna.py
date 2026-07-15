import requests

# Add your own Adzuna credentials here
APP_ID = ""
APP_KEY = ""

COUNTRY = "ca"


def get_jobs():

    jobs = []

    # No credentials yet
    if not APP_ID or not APP_KEY:
        return jobs

    url = (
        f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"
        f"?app_id={APP_ID}"
        f"&app_key={APP_KEY}"
        f"&results_per_page=50"
        f"&what=IT+Support+OR+Help+Desk+OR+Desktop+Support"
    )

    try:

        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            return jobs

        data = response.json()

        for job in data.get("results", []):

            jobs.append({

                "title": job.get("title", ""),

                "company": job.get("company", {}).get("display_name", ""),

                "location": job.get("location", {}).get("display_name", ""),

                "url": job.get("redirect_url", ""),

                "source": "Adzuna",

                "description": job.get("description", ""),

                "date_posted": job.get("created", "")

            })

    except Exception as e:

        print(f"Adzuna Error: {e}")

    return jobs


if __name__ == "__main__":

    jobs = get_jobs()

    print(f"Found {len(jobs)} jobs")