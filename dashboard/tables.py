"""
dashboard/tables.py

Job table and filtering.
"""

import pandas as pd
import streamlit as st


def render_table(df: pd.DataFrame, filters: dict):
    """
    Apply filters and display jobs.

    Returns
    -------
    pandas.DataFrame
        Filtered dataframe.
    """

    filtered = df.copy()

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

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
                na=False,
            )
        ]

    # --------------------------------------------------
    # Favorites
    # --------------------------------------------------

    if (
        filters.get("show_favorites", False)
        and "favorite" in filtered.columns
    ):

        filtered = filtered[
            filtered["favorite"] == 1
        ]

    # --------------------------------------------------
    # Category
    # --------------------------------------------------

    if (
        filters["category"] != "All"
        and "category" in filtered.columns
    ):

        filtered = filtered[
            filtered["category"]
            == filters["category"]
        ]

    # --------------------------------------------------
    # Source
    # --------------------------------------------------

    if (
        filters["source"] != "All"
        and "source" in filtered.columns
    ):

        filtered = filtered[
            filtered["source"]
            == filters["source"]
        ]

    # --------------------------------------------------
    # Company
    # --------------------------------------------------

    if (
        filters["company"] != "All"
        and "company" in filtered.columns
    ):

        filtered = filtered[
            filtered["company"]
            == filters["company"]
        ]

    # --------------------------------------------------
    # Location
    # --------------------------------------------------

    if (
        filters["location"] != "All"
        and "location" in filtered.columns
    ):

        filtered = filtered[
            filtered["location"]
            == filters["location"]
        ]

    # --------------------------------------------------
    # Minimum AI Score
    # --------------------------------------------------

    if "score" in filtered.columns:

        filtered = filtered[
            filtered["score"]
            >= filters["minimum_score"]
        ]

    # --------------------------------------------------
    # Resume Match
    # --------------------------------------------------

    if "resume_match" in filtered.columns:

        filtered = filtered[
            filtered["resume_match"]
            >= filters["minimum_match"]
        ]

    # --------------------------------------------------
    # High Priority
    # --------------------------------------------------

    if (
        filters.get("high_priority", False)
        and "score" in filtered.columns
    ):

        filtered = filtered[
            filtered["score"] >= 90
        ]

    # --------------------------------------------------
    # Sort
    # --------------------------------------------------

    sort_columns = []

    ascending = []

    if "favorite" in filtered.columns:
        sort_columns.append("favorite")
        ascending.append(False)

    if "score" in filtered.columns:
        sort_columns.append("score")
        ascending.append(False)

    if "resume_match" in filtered.columns:
        sort_columns.append("resume_match")
        ascending.append(False)

    if sort_columns:

        filtered = filtered.sort_values(
            by=sort_columns,
            ascending=ascending,
        )

    # --------------------------------------------------
    # Display
    # --------------------------------------------------

    st.subheader("💼 Available Jobs")

    display = filtered.copy()

    if "favorite" in display.columns:

        display["★"] = display["favorite"].apply(
            lambda x: "⭐" if x else ""
        )

    preferred = [

        "★",

        "title",

        "company",

        "location",

        "category",

        "score",

        "resume_match",

        "source",

    ]

    display_columns = [
        c
        for c in preferred
        if c in display.columns
    ]

    st.dataframe(

        display[display_columns],

        use_container_width=True,

        hide_index=True,

    )

    st.caption(
        f"Showing {len(filtered)} job(s)"
    )

    return filtered