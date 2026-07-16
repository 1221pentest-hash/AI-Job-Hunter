import os
from datetime import datetime

import pandas as pd

OUTPUT_FOLDER = "output"


def _prepare_dataframe(jobs):
    """
    Convert jobs to a DataFrame and ensure common columns exist.
    """

    df = pd.DataFrame(jobs)

    columns = [
        "score",
        "category",
        "title",
        "company",
        "location",
        "source",
        "url",
        "description",
        "date_posted",
        "applied",
        "interview",
        "notes",
    ]

    for column in columns:
        if column not in df.columns:
            df[column] = ""

    return df


def export_all_jobs(jobs):
    """
    Export every collected job.
    """

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df = _prepare_dataframe(jobs)

    df.to_csv(
        os.path.join(OUTPUT_FOLDER, "all_jobs.csv"),
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )

    print(f"✓ Saved {len(df)} jobs -> all_jobs.csv")


def export_canadian_jobs(jobs):
    """
    Export location-filtered jobs.
    """

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df = _prepare_dataframe(jobs)

    df.to_csv(
        os.path.join(OUTPUT_FOLDER, "canadian_jobs.csv"),
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )

    print(f"✓ Saved {len(df)} jobs -> canadian_jobs.csv")


def export_apply_today(jobs):
    """
    Export today's highest-ranked jobs.
    """

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df = _prepare_dataframe(jobs)

    if "score" in df.columns:
        df = df.sort_values(
            by="score",
            ascending=False
        )

    # Keep only useful jobs
    df = df[df["score"] >= 40]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"apply_today_{timestamp}.csv"

    df.to_csv(
        os.path.join(OUTPUT_FOLDER, filename),
        sep=";",
        index=False,
        encoding="utf-8-sig",
    )

    print(f"✓ Saved {len(df)} jobs -> {filename}")