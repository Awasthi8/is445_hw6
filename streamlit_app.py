import streamlit as st
import pandas as pd
import altair as alt

st.title("Illinois Professional Licensing Data")
st.write("Exploring professional licenses in Illinois using Fall 2022 data.")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/licenses_fall2022.csv"
df = pd.read_csv(url)
county = st.selectbox("Select a County", ["All"] + sorted(df["County"].dropna().unique()))
if county != "All":
    df = df[df["County"] == county]


st.header("Top 10 Professional License Types")
counts = df.groupby("License Type").size().reset_index(name="Count")
top10 = counts.sort_values("Count", ascending=False).head(10)
chart1 = alt.Chart(top10).mark_bar().encode(
    x=alt.X("Count:Q", title="Number of Licenses"),
    y=alt.Y("License Type:N", sort="-x"),
    tooltip=["License Type:N", "Count:Q"]
).properties(height=350)
st.altair_chart(chart1, use_container_width=True)


st.header("License Status by License Type")
data2 = df[df["License Type"].isin(top10["License Type"])]
status = data2.groupby(["License Type", "License Status"]).size().reset_index(name="Count")
chart2 = alt.Chart(status).mark_rect().encode(
    x=alt.X("License Status:N", title="License Status"),
    y=alt.Y("License Type:N", title="License Type"),
    color=alt.Color("Count:Q", title="Number of Licenses"),
    tooltip=["License Type:N", "License Status:N", "Count:Q"]
).properties(height=350)
st.altair_chart(chart2, use_container_width=True)
