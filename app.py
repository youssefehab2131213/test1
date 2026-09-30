import streamlit as st
import pandas as pd 

st.title("CSV REader")

uploaded_file =st.file_uploader(
   
    "uploaadd file",
   type=["csv"]

)

if uploaded_file is not None:
      df= pd.read_csv(uploaded_file)
      st.success("sucess upload")
      st.subheader("first 3 row")
      st.dataframe(df.head(3))