import pickle
load_model=pickle.load(open('insurance.sav','rb'))

import streamlit as st
st.title('Health Insurance Premium Cost Prediction')
st.header('Enter Your Details')
age=st.text_input('Enter Your Age')


gender=st.selectbox('Select Your Gender',("",'Male','Female'))
if gender=='Male':
    g=1
elif gender=='Female':
    g=0
bmi=st.text_input('Enter Your BMI')
if bmi==0:
    st.error('Please enter Your BMI')
child=st.text_input("Enter Number Of Childrens ")
if child==0:
    st.error('Please Enter Number Of Childrens')
smoke=st.selectbox('You Smoke',('','Yes','No'))
if smoke=='Yes':
    s=1
elif smoke=='No':
    s=0

if st.button('Calculate'):
    if age and gender and bmi and child and smoke:
        output=load_model.predict([[age,g,bmi,child,s]])

        st.write ('Your Health Insurance Premium Cost = ',int(output[0]))
    else:
        if age:
            pass
        else:
            st.error('Enter your age')
        if gender:
            pass
        else:
            st.error('Select Your Gender')
        if bmi:
            pass
        else:
            st.error('Enter Your BMI')
        if child:
            pass
        else:
            st.error('Enter Number of Child')
        if smoke:
            pass
        else:
            st.error('Please Select You Smoke Or Not')
        