import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("Simple data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
st.write("File Uploaded")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
   
    st.subheader("Data Summary")
    st.write(df.describe())
   
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by:" ,columns)
    unique_values = df[selected_column].unique()
    selected_value =  st.selectbox("Select Value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_coloumn = st.selectbox("Select column for x-axis", columns)
    y_coloumn = st.selectbox("Select column for y-axis", columns)
   
    if st.button("Generate Plot"):
       st.line_chart(filtered_df.set_index(x_coloumn)[y_coloumn])

st.write("Waiting for File Upload")       
   