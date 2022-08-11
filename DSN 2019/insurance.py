# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:01:47 2022

@author: User
"""

import pandas as pd
import streamlit as st
import pickle

filename = 'insurance_prediction.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Insurance Policy Prediction App')
st.subheader("""This app takes in certain variable to enable prediction whether or not a building is insured""")
#image = ima.open('ima.jpg')
#st.image(image, '')


def user_input():
    YearObservation = st.slider('What year was your building insured?', 2010, 2022)
    Insured_Period = st.slider('What is the duration of insurance policy?', 0.0, 1.0)
    Residential = st.selectbox('Is your building residential or not?  0 is FALSE, 1 is TRUE', options = [0,1], index = 0)
    Building_Painted = st.selectbox('Is your building painted?  0 is NOT PAINTED, 1 is PAINTED', options = [0,1], index = 0)
    Building_Fenced = st.selectbox('Is your building fenced or not?  0 is NOT FENCED, 1 is FENCED', options = [0,1], index = 0)
    Settlement = st.selectbox('Where is your building located?  0 is URBAN, 1 is RURAL', options = [0,1], index = 0)
    Building_Dimension = st.slider('What is the dimension of your building?  Values are in m²', 1.00, 30000.00)
    Building_Type = st.selectbox('What building type do you fall under?', options = [1,2,3,4], index = 0)
    Date_of_Occupancy = st.slider('Which date did you move in?', 1900, 2021)
    NumberOfWindows = st.slider('How many windows do you have in your house?', 0, 10)
    Geo_Code = st.slider('What is the geographical code of the building', 0, 1306)
    
    
    data = {'Year of Observation': YearObservation,
            'Insurance Period': Insured_Period,
            'Residential' : Residential,
            'Building Painted' : Building_Painted,
            'Building Fenced' : Building_Fenced,
            'Settlement' : Settlement,
            'Building Dimension' : Building_Dimension,
            'Building Type' : Building_Type,
            'Date of Occupancy' : Date_of_Occupancy,
            'Number Of Windows' : NumberOfWindows,
            'Geo Code' : Geo_Code}
    
    features = pd.DataFrame(data, index = [0])
    return features

df = user_input()

def prediction():
    predict_ = model.predict(df)
    result = ''
    if predict_ == 0:
        result = 'Not Qualified'
    else:
        result = 'Qualified'
    return result


if st.button('Predict'):
    result = prediction()
    st.success('Thank you for filling this form. You are {}'.format(result))