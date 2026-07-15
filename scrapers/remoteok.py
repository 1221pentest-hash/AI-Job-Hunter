import requests


def get_jobs():

    jobs = []

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:
            return jobs

        data = response.json()

        # First element is metadata
        for job in data[1:]:

            jobs.append({

                "title": job.get("position", ""),

                "company": job.get("company", ""),

                "location": job.get("location", "Remote"),

                "url": job.get("url", ""),

                "source": "RemoteOK",

                "description": "",

                "date_posted": job.get("date", "")

            })

    except Exception as e:

        print(f"RemoteOK Error: {e}")

    return jobs


if __name__ == "__main__":

    jobs = get_jobs()

    print(f"Found {len(jobs)} jobs")