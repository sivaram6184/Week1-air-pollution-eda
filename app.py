# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("clean_dataset.csv")

# Set page config
st.set_page_config(page_title="Air Pollution Deaths Dashboard", layout="wide")

# Title
st.title("Air Pollution Deaths Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", df["Entity"].unique())
selected_year = st.sidebar.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), (int(df["Year"].min()), int(df["Year"].max())))

# Filtered data
filtered_df = df[(df["Entity"] == selected_country) & 
                 (df["Year"] >= selected_year[0]) & 
                 (df["Year"] <= selected_year[1])]

# Show dataset summary
st.subheader("Dataset Summary")
st.dataframe(df.describe())

# Show deaths by year and country
st.subheader(f"Deaths Data for {selected_country}")
st.dataframe(filtered_df[["Year", "air_total", "household", "pm25", "ozone"]].rename(columns={
    "air_total": "Deaths - Air Pollution",
    "household": "Deaths - Household Air Pollution",
    "pm25": "Deaths - Ambient Particulate Matter",
    "ozone": "Deaths - Ambient Ozone"
}))

# Visualizations
st.subheader(f"Deaths Trend for {selected_country}")
fig = px.line(
    filtered_df,
    x="Year",
    y=["air_total", "household", "pm25", "ozone"],
    labels={
        "value": "Deaths",
        "Year": "year",
        "variable": "Pollution Type"
    },
    title=f"Deaths by Pollution Type in {selected_country}"
)
st.plotly_chart(fig, use_container_width=True)
