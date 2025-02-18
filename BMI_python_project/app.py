import streamlit as st
import pandas as pandas


st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100,250,175 )
weight = st.slider("Enter your weight (in kg)", 20, 200, 70)

bmi= weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("Underweight: BMI less than 18.5")
st.write("Normal weight: BMI 18.5 to 24.9")
st.write("Overweight: BMI 25 to 29.9")
st.write("Obese: BMI 30 or greater")


