import streamlit as st

from dashboard.data import load_jobs, get_statistics
from dashboard.metrics import render_metrics
from dashboard.sidebar import render_sidebar
from dashboard.tables import render_table
from dashboard.details import render_details
from dashboard.charts import render_charts

st.set_page_config(
    page_title="AI Job Hunter",
    page_icon="💼",
    layout="wide",
)

st.title("💼 AI Job Hunter Dashboard")

df = load_jobs()

if df.empty:
    st.warning("No jobs found.")
    st.stop()

stats = get_statistics(df)
render_metrics(stats)

st.divider()

filters = render_sidebar(df)

filtered = render_table(df, filters)

st.divider()

render_details(filtered)

st.divider()

render_charts(filtered)