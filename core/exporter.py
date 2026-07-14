import pandas as pd


def export_jobs(jobs):

    dataframe = pd.DataFrame(jobs)

    dataframe.to_csv(
        "output/jobs.csv",
        index=False
    )

    print("\nJobs exported successfully!")