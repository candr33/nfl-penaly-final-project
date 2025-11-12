import streamlit as st
import pandas as pd

# --- Sidebar Filters ---
st.sidebar.title("Filter Options")
selected_team = st.sidebar.selectbox("Select Team", [])
selected_penalty_type = st.sidebar.multiselect("Penalty Type", [])

# --- Main Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Questions Overview",
    "Team Comparison",
    "Penalties vs Success",
    "Weekly Trends",
    "Season Insights"
])

# --- Tab 1: Questions Overview ---
with tab1:
    st.header("Research Goals")
    st.markdown("""
    This dashboard explores how penalties affect team success across NFL seasons.
    Use the filters to explore trends by team, penalty type, and year.
    

    # Key Research Questions
    - Do teams with fewer penalties tend to win more games?
    - Which teams were the most and least disciplined in 2023?
    - Are offensive or defensive penalties more common — and do they impact success differently?
    - How do penalty trends shift over the course of the season?
     """)


# --- Tab 2: Team Comparison ---
with tab2:
    st.header("Team Comparison")
    st.markdown("Bar charts showing penalties and yards lost by team.")
    # Placeholder for future visualizations

# --- Tab 3: Penalties vs Success ---
with tab3:
    st.header("Penalties vs Success")
    st.markdown("Scatter plot showing correlation between discipline and win rate.")
    # Placeholder for future visualizations

# --- Tab 4: Weekly Trends ---
with tab4:
    st.header("Weekly Trends")
    st.markdown("Line chart showing penalty trends across selected years.")
    # Placeholder for future visualizations

# --- Tab 5: Season Insights ---
with tab5:
    st.header("Season Insights")
    st.markdown("Summary table and heatmap comparing offensive vs defensive penalties.")
    # Placeholder for future visualizations