"""
dashboard/sidebar.py

Dashboard sidebar filters.
"""

import streamlit as st
import pandas as pd


def render_sidebar(df: pd.DataFrame):
    """
    Render the dashboard sidebar.

    Returns a dictionary containing
    the selected filters.
    """

    st.sidebar.title("🔍 Filters")

    # -----------------------------
    # Search
    # -----------------------------

    search = st.sidebar.text_input(
        "Search Job Title",
        "",
    )

    # -----------------------------
    # Category
    # -----------------------------

    if "category" in df.columns:

        categories = ["All"] + sorted(
            df["category"]
            .fillna("")
            .unique()
            .tolist()
        )

    else:

        categories = ["All"]

    selected_category = st.sidebar.selectbox(
        "Category",
        categories,
    )

    # -----------------------------
    # Source
    # -----------------------------

    if "source" in df.columns:

        sources = ["All"] + sorted(
            df["source"]
            .fillna("")
            .unique()
            .tolist()
        )

    else:

        sources = ["All"]

    selected_source = st.sidebar.selectbox(
        "Source",
        sources,
    )

    # -----------------------------
    # Minimum Score
    # -----------------------------

    max_score = 100

    if "score" in df.columns and len(df):

        max_score = int(df["score"].max())

    minimum_score = st.sidebar.slider(
        "Minimum Score",
        0,
        max_score,
        0,
    )

    # -----------------------------
    # Resume Match
    # -----------------------------

    max_match = 100

    if "resume_match" in df.columns and len(df):

        max_match = int(df["resume_match"].max())

    minimum_match = st.sidebar.slider(
        "Minimum Resume Match",
        0,
        max_match,
        0,
    )

    return {

        "search": search,

        "category": selected_category,

        "source": selected_source,

        "minimum_score": minimum_score,

        "minimum_match": minimum_match,

    }