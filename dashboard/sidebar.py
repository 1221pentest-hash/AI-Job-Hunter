"""
dashboard/sidebar.py

Dashboard sidebar filters.
"""

import pandas as pd
import streamlit as st


def render_sidebar(df: pd.DataFrame):
    """
    Render dashboard sidebar filters.

    Returns
    -------
    dict
        Selected filter values.
    """

    st.sidebar.title("🔍 Filters")

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search = st.sidebar.text_input(
        "Search Job Title",
        "",
    )

    # --------------------------------------------------
    # Favorites
    # --------------------------------------------------

    show_favorites = st.sidebar.checkbox(
        "⭐ Show Favorites Only",
        value=False,
    )

    # --------------------------------------------------
    # Category
    # --------------------------------------------------

    if "category" in df.columns:

        categories = (
            ["All"]
            + sorted(
                df["category"]
                .fillna("")
                .unique()
                .tolist()
            )
        )

    else:

        categories = ["All"]

    selected_category = st.sidebar.selectbox(
        "Category",
        categories,
    )

    # --------------------------------------------------
    # Source
    # --------------------------------------------------

    if "source" in df.columns:

        sources = (
            ["All"]
            + sorted(
                df["source"]
                .fillna("")
                .unique()
                .tolist()
            )
        )

    else:

        sources = ["All"]

    selected_source = st.sidebar.selectbox(
        "Source",
        sources,
    )

    # --------------------------------------------------
    # Company
    # --------------------------------------------------

    if "company" in df.columns:

        companies = (
            ["All"]
            + sorted(
                df["company"]
                .fillna("")
                .unique()
                .tolist()
            )
        )

    else:

        companies = ["All"]

    selected_company = st.sidebar.selectbox(
        "Company",
        companies,
    )

    # --------------------------------------------------
    # Location
    # --------------------------------------------------

    if "location" in df.columns:

        locations = (
            ["All"]
            + sorted(
                df["location"]
                .fillna("")
                .unique()
                .tolist()
            )
        )

    else:

        locations = ["All"]

    selected_location = st.sidebar.selectbox(
        "Location",
        locations,
    )

    # --------------------------------------------------
    # Minimum Score
    # --------------------------------------------------

    max_score = 100

    if "score" in df.columns and not df.empty:
        max_score = int(df["score"].max())

    minimum_score = st.sidebar.slider(
        "Minimum AI Score",
        0,
        max_score,
        0,
    )

    # --------------------------------------------------
    # Resume Match
    # --------------------------------------------------

    max_match = 100

    if "resume_match" in df.columns and not df.empty:
        max_match = int(df["resume_match"].max())

    minimum_match = st.sidebar.slider(
        "Minimum Resume Match",
        0,
        max_match,
        0,
    )

    # --------------------------------------------------
    # High Priority
    # --------------------------------------------------

    high_priority = st.sidebar.checkbox(
        "🔥 High Priority (Score ≥ 90)",
        value=False,
    )

    # --------------------------------------------------
    # Return filters
    # --------------------------------------------------

    return {

        "search": search,

        "show_favorites": show_favorites,

        "category": selected_category,

        "source": selected_source,

        "company": selected_company,

        "location": selected_location,

        "minimum_score": minimum_score,

        "minimum_match": minimum_match,

        "high_priority": high_priority,

    }