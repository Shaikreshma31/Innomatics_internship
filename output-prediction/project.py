import streamlit as st
import os
import numpy as np
import pandas as pd
from pickle import dump,load

st.markdown('<style>body{background-color:lightgreen;}</style>',unsafe_allow_html=True)

st.title("OUTPUT PREDICTION")

col1 = st.number_input("Column 1")
col2 = st.number_input("Column 2")
classifier=load(open('pickle/clf.pkl','rb'))
prediction = classifier.predict([[col1,col2]])
click = st.button('SUBMIT')
if click:
    if prediction==1:
        st.write('**OUTPUT : 1**:sunglasses:')
    else:
        st.write('**OUTPUT : 0** :cry::angry:')
