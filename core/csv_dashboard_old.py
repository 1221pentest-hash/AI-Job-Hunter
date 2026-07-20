"""
AI Job Hunter Dashboard

Main Streamlit application.
"""

import streamlit as st

from dashboard.data import load_jobs, get_statistics
from dashboard.metrics import render_metrics
from dashboard.sidebar import render_sidebar
from dashboard.tables import render_table
from dashboard.details import render_details
from dashboard.charts import render_charts


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Job Hunter",
    page_icon="💼",
    layout="wide",
)

st.title("💼 AI Job Hunter Dashboard")

st.caption("Find your next IT job with AI-powered scoring and resume matching.")

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

df = load_jobs()

if df.empty:
    st.warning("No jobs found in the database.")
    st.stop()

# ----------------------------------------------------
# Statistics
# ----------------------------------------------------

stats = get_statistics(df)

render_metrics(stats)

st.divider()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

filters = render_sidebar(df)

# ----------------------------------------------------
# Filtered Table
# ----------------------------------------------------

filtered_df = render_table(df, filters)

st.divider()

# ----------------------------------------------------
# Details
# ----------------------------------------------------

render_details(filtered_df)

st.divider()

# ----------------------------------------------------
# Charts
# ----------------------------------------------------

render_charts(filtered_df)