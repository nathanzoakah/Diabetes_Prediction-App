import streamlit as st
from predict import show_predict_page

st.sidebar.selectbox("MENU", ("Diabetes Prediction", "Exploratory Data Analysis", "Blood Glucose Level Prediction"))

show_predict_page()