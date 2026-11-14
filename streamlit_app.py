import streamlit as st
import pandas as pd
import altair as alt

st.title("Illinois Professional Licensing Data")
st.write("Exploring professional licenses in Illinois using Fall 2022 data.")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/licenses_fall2022.csv"
df = pd.read_csv(url)
st.write("Number of records:", len(df))
st.write("Dataset columns:", df.columns.tolist())
st.dataframe(df.head(10))
