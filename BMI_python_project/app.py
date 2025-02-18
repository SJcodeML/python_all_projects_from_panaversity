import streamlit as st
import pandas as pandas
st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100,250,175 )
weight = st.slider("Enter your weight (in kg)", 40, 200, 70)

bmi weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

