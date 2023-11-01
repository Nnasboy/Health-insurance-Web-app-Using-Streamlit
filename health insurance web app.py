# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:38:05 2023

@author: user
"""

import numpy as np
import pickle
import streamlit as st


#LOADING THE SAVED MODEL
loaded_model=pickle.load(open(r"C:\Users\user\Downloads\Health_Insurance_Pred.sav",'rb'))



#CREATING A FUNCTION FOR PREDICTION

def health_insurance(input_data):
    
    
    
    #CHANGING THE INPUT DATA TO NUMPY ARRAY
    input_data_as_numpy=np.asarray(input_data)
    #RESHAPE THE ARRAY AS WE ARE PREDICTING FPR ONE INSTANCE
    input_data_reshape=input_data_as_numpy.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    return 'The health insurance cost is',prediction




def main():
    
    #GIVING A TITLE FOR THE WEB PAGE
    st.title('HEALTH INSURANCE COST')
    
    
    #GETTING INPUT DATA FROM USER

    Age = st.text_input('How old are you?')
    Sex = st.text_input('Gender')
    BMI = st.text_input('Your body mass')
    Children = st.text_input('Do you have children?')
    Smoker = st.text_input('Are you a smoker?')
    Region = st.text_input('What region are you from?')
    
    
    #CODE FOR PREDICTION
    biodata = ''
    
    #CREATIN A PATTERN FOR PREDICTION
    
    if st.button('Charges'):
        biodata = health_insurance([Age, Sex, BMI, Children, Smoker, Region])
        
    st.success(biodata)
    
    
    
if __name__ == '__main__':
    main()
    
    
    