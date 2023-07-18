import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv("diabetes_data_jos_urban_2012_no_missing_values_Updated_2.csv")
    del df[df.columns[0]]
    return df

def show_explore_page():
    st.title("This Page Displays Information About the Dataset")
    st.write("""## COMING SOON!!""")
    st.write("""### On this page we'll explore the dataset used to train our machine learning models""")

    
    #data = load_data()

    #st.write("""#### Top five rows of the diabetes Dataset""")
    #st.dataframe(data.head())

    #st.write("""#### Bottom five rows of the diabetes Dataset""")
    #st.dataframe(data.tail())


    #st.write("""#### Description of the diabetes Dataset""")
    #st.dataframe(data.describe())


    

    #st.dataframe(data["Diagnosis"].value_counts())

    #df = data["Diagnosis"].value_counts()

    #fig1, ax1 = plt.subplots()
    #ax1.pie(df, labels = ['No Diabetes', 'Diabetes'], autopct="%1.1f%%", shadow=True, startangle=90)
    #ax1.axis("equal")

    #st.write("""#### Percentage of Target Variable""")
    #st.pyplot(fig1)

    #df2 = data["Gender_M"].value_counts()

    #fig2, ax2 = plt.subplots()
    #ax2.pie(df2, labels = ['Female','Male'], autopct="%1.1f%%", shadow=True, startangle=90)
    #ax2.axis("equal")
    

    #st.write("""#### Percentage of Gender""")
    #st.pyplot(fig2)



