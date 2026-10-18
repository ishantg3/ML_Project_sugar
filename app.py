import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

st.set_page_config(layout="wide")
st.title("Diabetes Prediction App")
st.write("This app predicts whether a person has diabetes or not " \
"based on their health parameters.")

# load the saved model
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.number_input('Number of Pregnancies')

with col2:
    Glucose = st.number_input('Glucose Level')

with col3:
    BloodPressure = st.number_input('Blood Pressure value')

with col1:
    SkinThickness = st.number_input('Skin Thickness value')

with col2:
    Insulin = st.number_input('Insulin Level')

with col3:
    BMI = st.number_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')

with col2:
    Age = st.number_input('Age of the Person')




# save the user input into a dataframe
input_data = pd.DataFrame([[Pregnancies,
                             Glucose,
                             BloodPressure,
                             SkinThickness,
                               Insulin,
                                 BMI,
                                 DiabetesPedigreeFunction,
                                   Age]])


# predict whether the person has diabetes or not
diabetes_prediction = diabetes_model.predict(input_data)

if st.button('Predict'):
    if diabetes_prediction[0] == 1:
        st.error('The person is likely to have diabetes.')
    else:
        st.success('The person is not likely to have diabetes.')