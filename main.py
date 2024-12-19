import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import pickle
with open('Student_model.pkl','rb') as obj2:
  dict1=pickle.load(obj2)
model=dict1['model']
st.title('STUDENT PERFORMANCE')
st.image(r"C:\Users\hp\Downloads\std_img.jpeg", width=800)
text = """
<div style="text-align:justify;">
    This interface offers a user-friendly platform to analyze and predict student performance based on key metrics such as 
    study hours, previous scores, extracurricular involvement, sleep patterns, and practice sessions. By offering actionable 
    insights, it empowers students and educators to identify strengths, address weaknesses, and make data-driven decisions 
    for better academic outcomes.
</div>
"""
st.markdown(text, unsafe_allow_html=True)

Hours_Studied=st.selectbox('Hours Studied:',range(1,10))
Previous_Scores=st.selectbox('Previous Scores:',range(10,101))
Extracurricular_Activities=st.selectbox('Extracurricular Activities:',['Yes','No'])
if Extracurricular_Activities=='Yes':
    Extracurricular_Activities=1
else:
    Extracurricular_Activities=0
Sleep_Hours=st.selectbox('Sleep Hours:',range(1,11))
Sample_Question_Papers_Practiced=st.number_input('Sample Question Papers Practiced:',0,10)
x1=np.array([[Hours_Studied, Previous_Scores, Extracurricular_Activities, Sleep_Hours, Sample_Question_Papers_Practiced]])
new=np.hstack([x1])
var1=st.button('Predict')
if var1:
    prediction=round(dict1['model'].predict(new)[0])
    st.write(f'The student performance is {prediction}.')
    st.balloons()