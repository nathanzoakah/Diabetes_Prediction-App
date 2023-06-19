import streamlit as st
from predict import show_predict_page
from explore import show_explore_page
from glucose import show_glucose_page

page = st.sidebar.selectbox("MENU", ("Diabetes Prediction", "Exploratory Data Analysis", "Blood Glucose Level Prediction"))

if page == "Diabetes Prediction":
    show_predict_page()
elif page == "Exploratory Data Analysis": 
    show_explore_page()
elif page =="Blood Glucose Level Prediction":
    show_glucose_page()