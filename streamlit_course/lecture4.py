import streamlit as st
import pandas as pd

st.title("chai sales dashboard")

file=st.file_uploader("upload your sales data csv file",type=["csv"])
if file:
    df=pd.read_csv(file)
    st.subheader("data preview")
    st.dataframe(df.head())

if file:
    st.subheader("file summary")
    st.write(df.describe())

if file:
    countries=df['Geography'].unique()
    select_cities=st.selectbox("filter countries",countries)
    filtared_data=df[df["Geography"]==select_cities]
    st.dataframe(filtared_data)
