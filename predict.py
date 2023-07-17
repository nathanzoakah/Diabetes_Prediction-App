import streamlit as st
import pickle
import numpy as np
import time
import sklearn
#from sklearn.preprocessing import StandardScaler



def load_first_model():
    with open('cv_model_sem.pkl', 'rb') as file:
        model = pickle.load(file)

    return model


trained_first_model = load_first_model()



def load_second_model():
    with open('cv_model_svm.pkl', 'rb') as file:
        model = pickle.load(file)

    return model


trained_second_model = load_second_model()


def show_predict_page():
    st.title("Web Application for Diabetes Prediction")

    st.write("""###  The following variables are needed for Diabetes Prediction""")


    with st.form(key="form", clear_on_submit=True):

        Age = st.number_input("Age", max_value=85, min_value=10)
        
        gender = st.text_input("Gender", placeholder="M or F", max_chars=1)
        gender = gender.lower()

        Gender_M = 5
        Gender_F = 5
        if gender == "m":
            Gender_M = 1
            Gender_F = 0
        else:
            Gender_M= 0
            Gender_F= 1

        
        # Variables

        Fgp = st.number_input("Fasting Plasma Glucose (mg/dl)")
        Dbp = st.number_input("Diastolic Blood Pressure (mm Hg)")
        Sbp = st.number_input("Systolic Blood Pressure (mm Hg)")
        Weight = st.number_input("Weight (Kilogram)")
        Height = st.number_input("height (Meters)")


        # Derived Variables
        
        if Height != 0:
            H_sqrd = np.square(Height)
            H_sqrd = st.number_input("Height Squared (Meter Square)", H_sqrd) 

        
        if Weight!=0 and Height!=0:
            Bmi = Weight / H_sqrd
            Bmi = st.number_input("Body Mass Index (Weight / Height_Squared)", Bmi)


        
        # Other Variables
        Wc = st.number_input("Waist Circumference (Centimeters)")
        Hc = st.number_input("Hip Circumference (Centimeters)")


        # Derived Variables
        if Wc!=0 and Hc!=0:
            Whr = Wc/Hc
            Whr = st.number_input("Waist Hip Ratio", Whr)


        # Prediction
        submit = st.form_submit_button("Prediction")

    try:


        if submit:
            X = np.array([[Age, Gender_F, Gender_M, Fgp, Sbp, Dbp, Weight, Height, H_sqrd, Bmi, Wc, Hc, Whr]])

            # Scale Feature Data
            #scaler = StandardScaler()
            #X_scaled = scaler.fit_transform(X)
            first_prediction = trained_first_model.predict(X)
            second_prediction =trained_second_model.predict(X)

            # Progress Bar as model is making prediction
            progress_text = "Prediction in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1, text=progress_text)

            
            st.success("Prediction Completed")

            # Display Results
            st.write(X)
            st.write("First Prediction", first_prediction)
            st.write("Second Prediction", second_prediction)

            if first_prediction == 0 and second_prediction == 0:
                st.success("No Diabetes- Results can further be varified by a Medical Practitioner")
            elif first_prediction == 1 and second_prediction == 1:
                st.error("Diabetic - Results can further be varified by a Medical Practitioner")
            else:
                st.warning("Cannot verify results with these variables above. Please check your inputs properly ")

    except:
        st.warning("Fill the Appropriate Variables Before Making Prediction!!!")
    





