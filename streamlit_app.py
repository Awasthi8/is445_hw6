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
st.write("""This graph displays the 10 most frequently appearing professional licenses in the data set. I chose to use horizontal bars because they help in comparing different categories more easily. Another thing that I did was to arrange the bars in descending order so that one can see which licenses appear most frequently. The dropdown for the counties helps the user to explore the findings for different parts of Illinois. With more time, I would like to include comparison of two counties at the same time.""")


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
st.write("""The heatmap represents variations in license statuses for the top 10 license types. The heatmap is preferred since different shades of colors enable the detection of combinations with many records easily. The license type is represented on the y-axis while the license status is on the x-axis. The county dropdown can also be used to view differences based on location. With extra time, I could have added percentages for easy comparison of license types with different record numbers.""")

st.write("""
I did not complete hw5, so no overlap in plots, data, or writting.
""")
