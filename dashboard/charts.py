"""
dashboard/charts.py

Dashboard charts.
"""

import pandas as pd
import streamlit as st


def render_charts(df: pd.DataFrame):
    """
    Render dashboard analytics.
    """

    if df.empty:
        st.info("No data available.")
        return

    st.subheader("📊 Dashboard Analytics")

    # ----------------------------------------
    # Row 1
    # ----------------------------------------

    left, right = st.columns(2)

    with left:

        if "category" in df.columns:

            st.markdown("### Jobs by Category")

            category_counts = (
                df["category"]
                .fillna("Unknown")
                .value_counts()
            )

            st.bar_chart(category_counts)

    with right:

        if "source" in df.columns:

            st.markdown("### Jobs by Source")

            source_counts = (
                df["source"]
                .fillna("Unknown")
                .value_counts()
            )

            st.bar_chart(source_counts)

    st.divider()

    # ----------------------------------------
    # Row 2
    # ----------------------------------------

    left, right = st.columns(2)

    with left:

        if "score" in df.columns:

            st.markdown("### Score Distribution")

            score_data = (
                df["score"]
                .fillna(0)
                .sort_values()
                .reset_index(drop=True)
            )

            st.line_chart(score_data)

    with right:

        if "resume_match" in df.columns:

            st.markdown("### Resume Match Distribution")

            match_data = (
                df["resume_match"]
                .fillna(0)
                .sort_values()
                .reset_index(drop=True)
            )

            st.line_chart(match_data)

    st.divider()

    # ----------------------------------------
    # Top Companies
    # ----------------------------------------

    if "company" in df.columns:

        st.markdown("### 🏢 Top Hiring Companies")

        companies = (
            df["company"]
            .fillna("Unknown")
            .value_counts()
            .head(10)
        )

        st.bar_chart(companies)

    st.divider()

    # ----------------------------------------
    # Jobs by Location
    # ----------------------------------------

    if "location" in df.columns:

        st.markdown("### 🌍 Top Locations")

        locations = (
            df["location"]
            .fillna("Unknown")
            .value_counts()
            .head(10)
        )

        st.bar_chart(locations)