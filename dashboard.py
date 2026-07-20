"""
AI Job Hunter Dashboard
Version 1.0
"""

from pathlib import Path

import pandas as pd
import streamlit as st


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Job Hunter",
    page_icon="💼",
    layout="wide",
)

st.title("💼 AI Job Hunter Dashboard")
st.caption("Your Personal AI Job Search Assistant")


# --------------------------------------------------
# Load Data
# --------------------------------------------------

OUTPUT_FOLDER = Path("output")
CSV_FILE = OUTPUT_FOLDER / "canadian_jobs.csv"

if not CSV_FILE.exists():
    st.error("canadian_jobs.csv was not found.")
    st.info("Run app.py first.")
    st.stop()

df = pd.read_csv(CSV_FILE)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Filters")

search = st.sidebar.text_input(
    "Search Job Title",
    "",
)

categories = ["All"] + sorted(
    df["category"].dropna().unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Category",
    categories,
)

minimum_score = st.sidebar.slider(
    "Minimum Score",
    0,
    250,
    0,
)


# --------------------------------------------------
# Filtering
# --------------------------------------------------

filtered = df.copy()

if search:

    filtered = filtered[
        filtered["title"]
        .fillna("")
        .str.contains(search, case=False)
    ]

if selected_category != "All":

    filtered = filtered[
        filtered["category"] == selected_category
    ]

if "score" in filtered.columns:

    filtered = filtered[
        filtered["score"] >= minimum_score
    ]


# --------------------------------------------------
# Statistics
# --------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Canadian Jobs",
    len(df),
)

c2.metric(
    "Filtered Jobs",
    len(filtered),
)

if "score" in df.columns:

    c3.metric(
        "Highest Score",
        int(df["score"].max()),
    )

else:

    c3.metric(
        "Highest Score",
        "-",
    )


st.divider()


# --------------------------------------------------
# Job Table
# --------------------------------------------------

columns = [
    col
    for col in [
        "title",
        "company",
        "location",
        "category",
        "score",
        "resume_match",
        "source",
        "url",
    ]
    if col in filtered.columns
]

st.dataframe(
    filtered[columns],
    use_container_width=True,
    hide_index=True,
)

st.divider()


# --------------------------------------------------
# Job Details
# --------------------------------------------------

st.header("Job Details")

if len(filtered) == 0:

    st.warning("No jobs match the current filters.")

else:

    titles = filtered["title"].fillna("").tolist()

    selected = st.selectbox(
        "Select a Job",
        titles,
    )

    job = filtered[
        filtered["title"] == selected
    ].iloc[0]

    st.subheader(job["title"])

    st.write(f"**Company:** {job.get('company', '')}")
    st.write(f"**Location:** {job.get('location', '')}")
    st.write(f"**Category:** {job.get('category', '')}")

    if "score" in job:
        st.write(f"**Score:** {job['score']}")

    if "resume_match" in job:
        st.write(f"**Resume Match:** {job['resume_match']}%")

    if "url" in job:
        st.link_button(
            "Apply Here",
            job["url"],
        )