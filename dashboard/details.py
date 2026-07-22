"""
dashboard/details.py

Display detailed information about a selected job.
"""

import pandas as pd
import streamlit as st

from dashboard.data import toggle_favorite


def score_color(score):

    if score >= 90:
        return "🟢"

    if score >= 75:
        return "🟡"

    if score >= 50:
        return "🟠"

    return "🔴"


def recommendation(score):

    if score >= 90:
        return (
            "🔥 Excellent Match\n\n"
            "Apply immediately. This role closely matches your resume."
        )

    if score >= 75:
        return (
            "✅ Strong Match\n\n"
            "Recommended application. Consider tailoring your resume slightly."
        )

    if score >= 50:
        return (
            "⚠ Moderate Match\n\n"
            "Apply if interested, but improving missing skills could increase your chances."
        )

    return (
        "❌ Weak Match\n\n"
        "This position is probably not worth prioritizing."
    )


def render_details(df: pd.DataFrame):

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

    score = float(job.get("score", 0))
    resume_match = float(job.get("resume_match", 0))
    favorite = bool(job.get("favorite", 0))

    left, right = st.columns([2, 1])

    with left:

        st.markdown("## 💼 Position Information")

        st.write(f"**Title:** {job.get('title', '')}")
        st.write(f"**Company:** {job.get('company', '')}")
        st.write(f"**Location:** {job.get('location', '')}")
        st.write(f"**Category:** {job.get('category', '')}")
        st.write(f"**Source:** {job.get('source', '')}")

    with right:

        st.markdown("## 🤖 AI Analysis")

        st.metric(
            "AI Score",
            f"{score:.0f}",
        )

        st.metric(
            "Resume Match",
            f"{resume_match:.0f}%",
        )

        st.markdown(
            f"### {score_color(score)} Recommendation"
        )

        st.info(
            recommendation(score)
        )

    st.divider()

    # --------------------------------------------------
    # Favorites
    # --------------------------------------------------

    if "id" in job:

        if favorite:

            if st.button(
                "⭐ Remove Favorite",
                use_container_width=True,
            ):

                toggle_favorite(int(job["id"]))
                st.rerun()

        else:

            if st.button(
                "☆ Add to Favorites",
                use_container_width=True,
            ):

                toggle_favorite(int(job["id"]))
                st.rerun()

    st.divider()

    st.markdown("## 📝 Job Description")

    description = job.get("description", "")

    if pd.isna(description) or description == "":
        st.info("No description available.")
    else:
        st.write(description)

    st.divider()

    matched = job.get("matched_skills", "")
    missing = job.get("missing_skills", "")

    left, right = st.columns(2)

    with left:

        st.markdown("## ✅ Matching Skills")

        if matched:

            for skill in str(matched).split(","):

                skill = skill.strip()

                if skill:
                    st.success(skill)

        else:

            st.info("No matched skills.")

    with right:

        st.markdown("## ❌ Missing Skills")

        if missing:

            for skill in str(missing).split(","):

                skill = skill.strip()

                if skill:
                    st.warning(skill)

        else:

            st.info("No missing skills.")

    st.divider()

    if score >= 90:
        st.success("★★★★★ Excellent opportunity")

    elif score >= 75:
        st.success("★★★★☆ Strong opportunity")

    elif score >= 50:
        st.warning("★★★☆☆ Moderate opportunity")

    else:
        st.error("★☆☆☆☆ Low priority")

    url = job.get("url", "")

    if isinstance(url, str) and url.startswith("http"):

        st.link_button(
            "🚀 Apply Now",
            url,
            use_container_width=True,
        )