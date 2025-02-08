import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide')

diabetes_model = pickle.load(open("C:\\Users\\SAI NIVEDA T\\Downloads\\Desease Pridiction\\training models\\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open("C:\\Users\\SAI NIVEDA T\\Downloads\\Desease Pridiction\\training models\\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:\\Users\\SAI NIVEDA T\\Downloads\\Desease Pridiction\\training models\\parkinsons_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital.fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Value')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Value')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    if st.button('Diabetes Test Result'):
        if '' in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
            st.error("Please ensure all input fields are filled.")
        else:
            try:
                user_input = [
                    float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                    float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)
                ]
                diab_prediction = diabetes_model.predict([user_input])

                if diab_prediction[0] == 1:
                    st.success('The person is diabetic.')
                else:
                    st.success('The person is not diabetic.')
            except ValueError:
                st.error("Please ensure all input fields are filled with correct values.")

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Age = st.text_input('Age of the Person')
    with col2:
        Sex = st.selectbox('Sex of the Person 0=F & 1=M', options=[0, 1])
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia')

    if st.button('Heart Test Result'):
        if '' in [Age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            st.error("Please ensure all input fields are filled.")
        else:
            try:
                user_input = [
                    float(Age), float(Sex), float(cp), float(trestbps),
                    float(chol), float(fbs), float(restecg), float(thalach), 
                    float(exang), float(oldpeak), float(slope), float(ca), 
                    float(thal)
                ]
                heart_prediction = heart_model.predict([user_input])

                if heart_prediction[0] == 1:
                    st.success('The person has heart disease.')
                else:
                    st.success('The person does not have heart disease.')
            except ValueError:
                st.error("Please ensure all input fields are filled with numeric values.")
else:
    selected == 'Parkinsons Disease Prediction'
    st.title('Parkinsons Disease Prediction Using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:FO(HZ)')
    with col2:
        fhi = st.text_input('MDVP:FHI(HZ)')
    with col3:
        flo = st.text_input('MDVP:FLO(HZ)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('Shimmer:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    if st.button('Parkinsons Test Result'):
        if '' in [fo,fhi,flo,Jitter_percent,Jitter_Abs,
                    RAP,PPQ,DDP,Shimmer,Shimmer_dB,
                    APQ3,APQ5,APQ,DDA,NHR,HNR,
                    RPDE,DFA,spread1,spread2,
                    D2,PPE]:
            st.error("Please ensure all input fields are filled.")
        else:
            try:
                user_input = [
                    float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                    float(RAP), float(PPQ), float(DDP), float(Shimmer), 
                    float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), 
                    float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA),
                    float(spread1), float(spread2), float(D2), float(PPE)
                ]
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    st.success('The person has Parkinsons disease.')
                else:
                    st.success('The person does not have Parkinsons disease.')
            except ValueError:
                    st.error("Please ensure all input fields are filled with numeric values.")

