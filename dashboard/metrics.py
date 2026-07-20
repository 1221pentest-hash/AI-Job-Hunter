"""
dashboard/metrics.py

Dashboard KPI cards.
"""

import streamlit as st


def render_metrics(stats: dict):
    """
    Render the dashboard KPI cards.
    """

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Total Jobs",
        stats["total_jobs"],
    )

    c2.metric(
        "⭐ Avg Score",
        stats["average_score"],
    )

    c3.metric(
        "🎯 Avg Resume Match",
        f"{stats['average_resume_match']}%",
    )

    c4.metric(
        "🏆 Top Matches",
        stats["top_matches"],
    )