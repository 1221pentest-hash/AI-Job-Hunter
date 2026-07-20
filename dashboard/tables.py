"""
dashboard/tables.py

Job table and filtering.
"""

import pandas as pd
import streamlit as st


def render_table(df: pd.DataFrame, filters: dict):

    """
    Apply filters and display jobs.

    Returns:
        filtered dataframe
    """

    filtered = df.copy()

    # ----------------------------------------
    # Search
    # ----------------------------------------

    if (
        filters["search"]
        and "title" in filtered.columns
    ):

        filtered = filtered[
            filtered["title"]
            .fillna("")
            .str.contains(
                filters["search"],
                case=False,
            )
        ]

    # ----------------------------------------
    # Category
    # ----------------------------------------

    if (
        filters["category"] != "All"
        and "category" in filtered.columns
    ):

        filtered = filtered[
            filtered["category"]
            == filters["category"]
        ]

    # ----------------------------------------
    # Source
    # ----------------------------------------

    if (
        filters["source"] != "All"
        and "source" in filtered.columns
    ):

        filtered = filtered[
            filtered["source"]
            == filters["source"]
        ]

    # ----------------------------------------
    # Minimum Score
    # ----------------------------------------

    if "score" in filtered.columns:

        filtered = filtered[
            filtered["score"]
            >= filters["minimum_score"]
        ]

    # ----------------------------------------
    # Resume Match
    # ----------------------------------------

    if "resume_match" in filtered.columns:

        filtered = filtered[
            filtered["resume_match"]
            >= filters["minimum_match"]
        ]

    # ----------------------------------------
    # Sort
    # ----------------------------------------

    sort_columns = []

    if "score" in filtered.columns:
        sort_columns.append("score")

    if "resume_match" in filtered.columns:
        sort_columns.append("resume_match")

    if sort_columns:

        filtered = filtered.sort_values(
            by=sort_columns,
            ascending=False,
        )

    # ----------------------------------------
    # Display
    # ----------------------------------------

    st.subheader("Available Jobs")

    display_columns = []

    preferred = [

        "title",
        "company",
        "location",
        "category",
        "score",
        "resume_match",
        "source",

    ]

    for column in preferred:

        if column in filtered.columns:
            display_columns.append(column)

    st.dataframe(

        filtered[display_columns],

        use_container_width=True,

        hide_index=True,

    )

    return filtered