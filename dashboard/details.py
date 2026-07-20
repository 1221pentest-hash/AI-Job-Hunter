"""
dashboard/details.py

Display detailed information about a selected job.
"""

import pandas as pd
import streamlit as st


def render_details(df: pd.DataFrame):

    """
    Display job details.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered dataframe.
    """

    st.subheader("📋 Job Details")

    if df.empty:
        st.info("No jobs found.")
        return

    titles = df["title"].fillna("").tolist()

    selected = st.selectbox(
        "Select a Job",
        titles,
    )

    job = df[df["title"] == selected].iloc[0]

    left, right = st.columns(2)

    with left:

        st.markdown("### Position")

        st.write(f"**Title:** {job.get('title', '')}")
        st.write(f"**Company:** {job.get('company', '')}")
        st.write(f"**Location:** {job.get('location', '')}")
        st.write(f"**Category:** {job.get('category', '')}")
        st.write(f"**Source:** {job.get('source', '')}")

    with right:

        st.markdown("### AI Analysis")

        st.metric(
            "Score",
            job.get("score", 0),
        )

        st.metric(
            "Resume Match",
            f"{job.get('resume_match',0)}%",
        )

    st.divider()

    st.markdown("### Description")

    description = job.get("description", "")

    if pd.isna(description) or description == "":
        st.info("No description available.")
    else:
        st.write(description)

    st.divider()

    matched = job.get("matched_skills", "")
    missing = job.get("missing_skills", "")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("### ✅ Matched Skills")

        if matched:
            for skill in str(matched).split(","):
                if skill.strip():
                    st.success(skill.strip())
        else:
            st.info("No matched skills.")

    with c2:

        st.markdown("### ❌ Missing Skills")

        if missing:
            for skill in str(missing).split(","):
                if skill.strip():
                    st.warning(skill.strip())
        else:
            st.info("No missing skills.")

    st.divider()

    url = job.get("url", "")

    if isinstance(url, str) and url.startswith("http"):

        st.link_button(
            "🚀 Apply Now",
            url,
            use_container_width=True,
        )