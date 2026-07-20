"""
AI Job Hunter Dashboard v1.1
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
# Locate Project Folder
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_FOLDER = PROJECT_ROOT / "output"
CSV_FILE = OUTPUT_FOLDER / "canadian_jobs.csv"

if not CSV_FILE.exists():
    st.error(f"CSV not found:\n\n{CSV_FILE}")
    st.stop()

# --------------------------------------------------
# Load CSV
# --------------------------------------------------

try:
    # Auto-detect separator (, or ;)
    df = pd.read_csv(
        CSV_FILE,
        sep=None,
        engine="python",
    )

except Exception as e:
    st.exception(e)
    st.stop()

# --------------------------------------------------
# Clean Data
# --------------------------------------------------

df.columns = [c.strip().lower() for c in df.columns]

if "score" in df.columns:
    df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0)

if "resume_match" in df.columns:
    df["resume_match"] = (
        pd.to_numeric(df["resume_match"], errors="coerce")
        .fillna(0)
    )

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("Filters")

search = st.sidebar.text_input("Search")

if "category" in df.columns:

    categories = ["All"] + sorted(
        df["category"].fillna("").unique().tolist()
    )

else:

    categories = ["All"]

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

if search and "title" in filtered.columns:

    filtered = filtered[
        filtered["title"]
        .fillna("")
        .str.contains(search, case=False)
    ]

if (
    selected_category != "All"
    and "category" in filtered.columns
):

    filtered = filtered[
        filtered["category"] == selected_category
    ]

if "score" in filtered.columns:

    filtered = filtered[
        filtered["score"] >= minimum_score
    ]

# --------------------------------------------------
# Metrics
# --------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric(
    "Canadian Jobs",
    len(df),
)

c2.metric(
    "Filtered",
    len(filtered),
)

highest = 0

if "score" in filtered.columns and len(filtered):

    highest = int(filtered["score"].max())

c3.metric(
    "Highest Score",
    highest,
)

st.divider()

# --------------------------------------------------
# Table
# --------------------------------------------------

columns = []

for col in [
    "title",
    "company",
    "location",
    "category",
    "score",
    "resume_match",
    "source",
]:

    if col in filtered.columns:
        columns.append(col)

st.dataframe(
    filtered[columns],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# --------------------------------------------------
# Job Details
# --------------------------------------------------

if len(filtered):

    st.header("Job Details")

    titles = filtered["title"].fillna("").tolist()

    selected = st.selectbox(
        "Select Job",
        titles,
    )

    job = filtered[
        filtered["title"] == selected
    ].iloc[0]

    st.subheader(job["title"])

    st.write(f"**Company:** {job.get('company','')}")
    st.write(f"**Location:** {job.get('location','')}")
    st.write(f"**Category:** {job.get('category','')}")
    st.write(f"**Score:** {job.get('score',0)}")
    st.write(f"**Resume Match:** {job.get('resume_match',0)}%")

    if (
        "url" in job
        and pd.notna(job["url"])
        and str(job["url"]).startswith("http")
    ):
        st.link_button(
            "Apply Here",
            job["url"],
        )

else:

    st.warning("No jobs match the selected filters.")