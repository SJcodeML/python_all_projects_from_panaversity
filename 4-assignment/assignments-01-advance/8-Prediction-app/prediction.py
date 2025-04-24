import streamlit as st
import joblib

model =joblib.load("linear_regression_model.pkl")

st.title("Linear Regression Streamlit App")
st.write("Enter the feature value to get a prediction.")

feature_value = st.number_input("Enter a value for the feature:" , min_value=0 , max_value=100 , value=2)

if st.button("Predict"):
    prediction = model.predict([[feature_value]])
    st.write(f"The predicted target value is : {prediction}")

