import streamlit as st
import numpy as np
import pickle

st.header("Obesity Predictor")
st.image("https://d12jofbmgge65s.cloudfront.net/wp-content/uploads/2023/01/Obesity_and_Children_Blog_WIP_2_header-1-1024x536.png")
st.divider()
st.write("Fill out the form below:")
form = st.form ("form")
#https://www.kaggle.com/competitions/playground-series-s4e2/discussion/472516
gender = form.radio ( "Are you male or female?", ["Male", "Female"], index=None)
if gender == "Male":
    genderM = True
    genderF = False
else:
    genderM = False
    genderF = True
age = form.number_input("Age")
height = form.number_input("Height (meters)")
weight = form.number_input("Weight (kilograms)")
famHistVar = form.radio( "Does your family have a history with being overweight?", ["Yes", "No"], index=None)
if famHistVar == "Yes":
    famHistY = True
    famHistN = False
else:
    famHistY = False
    famHistN = True
favcVar = form.radio("Do you have a frequency of consuming high caloric food?",["Yes", "No"], index=None)
if favcVar == "Yes":
    favcY = True
    favcN = False
else:
    favcY = False
    favcN = True
fcvc = form.slider("What is your frequency of consuming vegetables?", 0.0, 3.0)
ncp = form.slider("How many main meals do you eat per day?", 0.0, 4.0 )
caecVar = form.selectbox('How often do you eat food between meals?', ['no','sometimes','frequently','always'], index=None,)
if caecVar == "no":
    caecN = True
    caecS = False
    caecF = False
    caecA = False
elif caecVar == "sometimes":
    caecN = False
    caecS = True
    caecF = False
    caecA = False
elif caecVar == "frequently":
    caecN = False
    caecS = False
    caecF = True
    caecA = False
else:
    caecN = False
    caecS = False
    caecF = False
    caecA = True
smokeVar = form.radio ("Do you smoke?",["Yes", "No"], index=None)
if smokeVar == "Yes":
    smokeY = True
    smokeN = False
else:
    smokeY = False
    smokeN = True
ch20 = form.slider ("How much water do you drink?", 0.0, 3.0)
sccVar = form.radio ("Do you monitor your calorie consumption?",["Yes", "No"], index=None)
if sccVar == "Yes":
    sccY = True
    sccN = False
else:
    sccY = False
    sccN = True
faf = form.slider ("How frequently do you partake in physical activity?", 0.0, 3.0)
tue = form.slider ("How much time do you spend on technology devices?", 0.0, 2.0)
calcVar = form.selectbox ('How frequently do you consume alcohol?', ['no','sometimes','frequently','always'], index=None,)
if calcVar == "no":
    calcN = True
    calcS = False
    calcF = False
    calcA = False
elif calcVar == "sometimes":
    calcN = False
    calcS = True
    calcF = False
    calcA = False
elif calcVar == "frequently":
    calcN = False
    calcS = False
    calcF = True
    calcA = False
else:
    calcN = False
    calcS = False
    calcF = False
    calcA = True
mtransVar = form.selectbox ('What type of transportation do you use?', ['walking','bike','public transportation','motorbike','automobile'], index=None,)
if mtransVar == "walking":
    mtransW = True
    mtransB = False
    mtransPT = False
    mtransM = False
    mtransA = False
elif mtransVar == "bike":
    mtransW = False
    mtransB = True
    mtransPT = False
    mtransM = False
    mtransA = False
elif mtransVar == "public transportation":
    mtransW = False
    mtransB = False
    mtransPT = True
    mtransM = False
    mtransA = False
elif mtransVar == "motorbike":
    mtransW = False
    mtransB = False
    mtransPT = False
    mtransM = True
    mtransA = False
else:
    mtransW = False
    mtransB = False
    mtransPT = False
    mtransM = False
    mtransA = True

form.form_submit_button("Submit")

st.divider()
st.write("Results:")

new_entry = np.array([[2112, age, height, weight, fcvc, ncp, ch20, faf, tue, genderF, genderM, famHistN, famHistY, favcN, favcY, caecA, caecF, caecS, caecN, smokeN, smokeY, sccN, sccY, calcA, calcF, calcS, calcN, mtransA, mtransB, mtransM, mtransPT, mtransW ]])

with open("obesity_classifier.pkl", "rb") as f:
    model = pickle.load(f)

prediction = model.predict(new_entry)
st.write(prediction)