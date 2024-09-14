import pickle
import streamlit as st
# from streamlit_option_menu import option_menu
# import joblib

#save the model
# joblib.dump(model, 'HDModel.sav')
#loading models

dia_modal = pickle.load(open('HDModel.sav', 'rb'))

# dia_modal = joblib.load(open(r'C:\Users\hp\Desktop\Machine Learning\HeartDiseaseModel\HDModel.sav', 'rb'))

#slider for navigation

with st.sidebar:
    selected = st.radio('E-doctor Heart disease prediction system',
                           ['Heart disease prediction'],
                           icons= ['heart'],
                           default_index=0
                           )
    
#disease prediction page
if(selected== 'Heart disease prediction'):
    #page title
    st.title('Heart disease prediction using ML')

    #getting the input data from the user
    col1, col2= st.columns(2)

    with col1: 
         age= st.text_input('enter your Age')

    with col2:
        cp= st.text_input('Chest Pain Type(0, 1, or 2) (cp)')

    with col1:
        chol= st.text_input('serum cholesterol (chol)')

    with col2:
        thalach= st.text_input('maximum heart rate achieved (thalach)')

    with col1:
        exang= st.text_input('exercise induced angina(0 or 1) (exang)')

    with col2:
        oldpeak= st.text_input('ST depression induced by exercise relative to rest (0-6) (oldpeak)')

    with col1:
        ca= st.text_input('number of major vessels colored by floursopy (0-4) (ca)')

#code for prediction
hrt_disease= ''

#creating a button for prediction
if st.button('heart disease Test Result'):
    hrt_disease= dia_modal.predict([[age, cp, chol, thalach, exang, oldpeak, ca]])

    if(hrt_disease[0] == 1):
        hrt_disease = 'The person has heart disease'
    else:
        hrt_disease = 'The person does not have heart disease'

st.success(hrt_disease)