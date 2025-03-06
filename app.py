import streamlit as st
import pickle

# Change the title and icon of the page
st.set_page_config(page_title="Disease Prediction", page_icon="🚑")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
                #MainMenu {visibility:hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                * {color: white;}
                @media (prefers-color-scheme: dark){
                    * {color: white;}
                }
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)

# Adding background image
background_image_url = "https://static.scientificamerican.com/sciam/cache/file/01C9741F-6F6D-4882-8217D92370325AA7_source.jpg"

page_bg_img = f"""
<style>
    [data-testid = "stAppViewContainer"]{{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stAppViewContainer"]::before{{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.7);
    }}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# Load the saved models
models = {
    "diabetes": pickle.load(open("Models/diabetes_prediction.sav","rb")),
    "heart_disease": pickle.load(open("Models/heart_disease_prediction_model.sav","rb")),
    "parkinsons": pickle.load(open("Models/parkinsons_model.sav","rb")),
    "lung_cancer": pickle.load(open("Models/lungs_disease_model.sav","rb")),
    "thyroid": pickle.load(open("Models/hypothyroid_prediction_model.sav","rb"))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox("Select a Disease to Predict",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction","Lung Cancer Prediction","Hypo-thyroid Prediction"])

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes")
    st.write("Enter the following details to predict diabetes")
    
    Pregnancies = st.number_input(label="Number of pregnancies",min_value=0,key="Pregnancies",help="Enter number of times pregnant")
    Glucose = st.number_input(label="Glucose Level",min_value=0,key="Glucose",help="Enter glucose level")
    BloodPressure = st.number_input(label="Blood Pressure value",min_value=0,key="BloodPressure",help="Enter blood pressure value")
    SkinThickness = st.number_input(label="Skin Thickness value",min_value=0,key="SkinThickness",help="Enter skin thickness value")
    Insulin = st.number_input(label="Insulin Level",min_value=0,key="Insulin",help="Enter insulin level")
    BMI = st.number_input(label="BMI value",min_value=0.0,key="BMI",help="Enter Body Mass Index value")
    DiabetesPedigreeFunction = st.number_input(label="Diabetes Pedigree Function value",min_value=0.0,key="DiabetesPedigreeFunction",help="Enter diabetes pedigree function")
    Age = st.number_input(label="Age of the Person",min_value=0,key="Age",help="Enter age of the person")

    diab_diagnosis = ""
    if st.button("Diabetes Test Result"):
        diab_diagnosis = models['diabetes'].predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        diab_diagnosis = "The person is diabetic" if diab_diagnosis[0] == 1 else "The person is not diabetic"
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease")
    st.write("Enter the following details to predict heart disease")

    age = st.number_input(label="Age",min_value=0,key="age",help="Enter age of the person")
    sex = st.number_input(label="Sex (1 = male, 0 = female)",min_value=0,max_value=1,key="sex",help="Enter sex of the person")
    cp = st.number_input(label="chest Pain types (0,1,2,3) (cp)",min_value=0,max_value=3,key="cp",help="Enter chest pain type")
    trestbps = st.number_input(label="Resting Blood Pressure (trestbps)",min_value=0,key="trestbps",help="Enter resting blood pressure")
    chol = st.number_input(label="Serum Cholesterol in mg/dl (chol)",min_value=0,key="chol",help="Enter serum cholestrol")
    fbs = st.number_input(label="Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false) (fbs)",min_value=0,max_value=1,key="fbs",help="Enter fasting blood sugar")
    restecg = st.number_input(label="Resting Electrocardiographic results (0,1,2) (restecg)",min_value=0,max_value=2,key="restecg",help="Enter resting ECG results")
    thalach = st.number_input(label="Maximum Heart Rate Achieved (thalach)",min_value=0,key="thalach",help="Enter maximum heart rate")
    exang = st.number_input(label="Exercise Induced Angina (1 = yes, 0 = no) (exang)",min_value=0,max_value=1,key="exang",help="Enter exercise induced angina")
    oldpeak = st.number_input(label="ST depression induced by exercise (oldpeak)",min_value=0.0,key="oldpeak",help="Enter ST depression value")
    slope = st.number_input(label="Slope of the peak exercise ST segment (0,1,2) (slope)",min_value=0,max_value=2,key="slope",help="Enter slope value")
    ca = st.number_input(label="Major vessels colored by fluoroscopy (0-3) (ca)",min_value=0,max_value=3,key="ca",help="Enter number of major vessels")
    thal = st.number_input(label="Thal (0 = normal, 1 = fixed defect, 2 = reversible defect, 3 = unknown) (thal)",min_value=0,max_value=3,key="thal",help="Enter thal value")

    heart_diagnosis = ""
    if st.button("Heart Disease Test Result"):
        heart_prediction = models['heart_disease'].predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        heart_diagnosis = "The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
        st.success(heart_diagnosis)

# Parkinsons Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease")

    fo = st.number_input(label="MDVP:Fo(Hz)",min_value=0.0,key="fo",help="Enter MDVP:Fo(Hz) value")
    fhi = st.number_input(label="MDVP:Fhi(Hz)",min_value=0.0,key="fhi",help="Enter MDVP:Fhi(Hz) value")
    flo = st.number_input(label="MDVP:Flo(Hz)",min_value=0.0,key="flo",help="Enter MDVP:Flo(Hz) value")
    Jitter_percent = st.number_input(label="MDVP:Jitter(%)",min_value=0.0,key="Jitter_percent",help="Enter MDVP:Jitter(%) value")
    Jitter_Abs = st.number_input(label="MDVP:Jitter(Abs)",min_value=0.0,key="Jitter_Abs",help="Enter MDVP:Jitter(Abs) value")
    RAP = st.number_input(label="MDVP:RAP",min_value=0.0,key="RAP",help="Enter MDVP:RAP value")
    PPQ = st.number_input(label="MDVP:PPQ",min_value=0.0,key="PPQ",help="Enter MDVP:PPQ value")
    DDP = st.number_input(label="Jitter:DDP",min_value=0.0,key="DDP",help="Enter Jitter:DDP value")
    Shimmer = st.number_input(label="MDVP:Shimmer",min_value=0.0,key="Shimmer",help="Enter MDVP:Shimmer value")
    Shimmer_dB = st.number_input(label="MDVP:Shimmer(dB)",min_value=0.0,key="Shimmer_dB",help="Enter MDVP:Shimmer(dB) value")
    APQ3 = st.number_input(label="Shimmer:APQ3",min_value=0.0,key="APQ3",help="Enter Shimmer:APQ3 value")
    APQ5 = st.number_input(label="Shimmer:APQ5",min_value=0.0,key="APQ5",help="Enter Shimmer:APQ5 value")
    APQ = st.number_input(label="MDVP:APQ",min_value=0.0,key="APQ",help="Enter MDVP:APQ value")
    DDA = st.number_input(label="Shimmer:DDA",min_value=0.0,key="DDA",help="Enter Shimmer:DDA value")
    NHR = st.number_input(label="NHR",min_value=0.0,key="NHR",help="Enter NHR value")
    HNR = st.number_input(label="HNR",min_value=0.0,key="HNR",help="Enter HNR value")
    RPDE = st.number_input(label="RPDE",min_value=0.0,key="RPDE",help="Enter RPDE value")
    DFA = st.number_input(label="DFA",min_value=0.0,key="DFA",help="Enter DFA value")
    Spread1 = st.number_input(label="Spread1",min_value=-10.0,value=0.0,key="Spread1",help="Enter Spread1 value")
    Spread2 = st.number_input(label="Spread2",min_value=0.0,key="Spread2",help="Enter Spread2 value")
    D2 = st.number_input(label="D2",min_value=0.0,key="D2",help="Enter D2 value")
    PPE = st.number_input(label="PPE",min_value=0.0,key="PPE",help="Enter PPE value")

    parkinsons_diagonsis = ""
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models["parkinsons"].predict([[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,Spread1,Spread2,D2,PPE]])
        parkinsons_diagonsis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagonsis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer")

    GENDER = st.number_input(label="Gender (1 = male, 0 = female)",min_value=0,max_value=1,key="GENDER",help="Enter gender of the person")
    AGE = st.number_input(label="Age",min_value=0,key="AGE",help="Enter age of the person")
    SMOKING = st.number_input(label="Smoking (1 = yes, 0 = no)",min_value=0,max_value=1,key="SMOKING",help="Enter if the person smokes")
    YELLOW_FINGERS = st.number_input(label="Yellow Fingers (1 = yes, 0 = no)",min_value=0,max_value=1,key="YELLOW_FINGERS",help="Enter if the person has yellow fingers")
    ANXIETY = st.number_input(label="Anxiety (1 = yes, 0 = no)",min_value=0,max_value=1,key="ANXIETY",help="Enter if the person has anxiety")
    PEER_PRESSURE = st.number_input(label="Peer Pressure (1 = yes, 0 = no)",min_value=0,max_value=1,key="PEER_PRESSURE",help="Enter if the person is under peer pressure")
    CHRONIC_DISEASE = st.number_input(label="Chronic Disease (1 = yes, 0 = no)",min_value=0,max_value=1,key="CHRONIC_DISEASE",help="Enter if the person has a chronic disease")
    FATIGUE = st.number_input(label="Fatigue (1 = yes, 0 = no)",min_value=0,max_value=1,key="FATIGUE",help="Enter if the person experiences fatigue")
    ALLERGY = st.number_input(label="Allergy (1 = yes, 0 = no)",min_value=0,max_value=1,key="ALLERGY",help="Enter if the person has allergies")
    WHEEZING = st.number_input(label="Wheezing (1 = yes, 0 = no)",min_value=0,max_value=1,key="WHEEZING",help="Enter if the person experiences wheezing")
    ALCOHOL_CONSUMING = st.number_input(label="Alcohol Consuming (1 = yes, 0 = no)",min_value=0,max_value=1,key="ALCOHOL_CONSUMING",help="Enter if the person consumes alcohol")
    COUGHING = st.number_input(label="Coughing (1 = yes, 0 = no)",min_value=0,max_value=1,key="COUGHING",help="Enter if the person experiences coughing")
    SHORTNESS_OF_BREATH = st.number_input(label="Shortness of Breath (1 = yes, 0 = no)",min_value=0,max_value=1,key="SHORTNESS_OF_BREATH",help="Enter if the person experiences shortness of breath")
    SWALLOWING_DIFFICULTY = st.number_input(label="Swallowing Difficulty (1 = yes, 0 = no)",min_value=0,max_value=1,key="SWALLOWING_DIFFICULTY",help="Enter if the person has difficulty swallowing")
    CHEST_PAIN = st.number_input(label="Chest Pain (1 = yes, 0 = no)",min_value=0,max_value=1,key="CHEST_PAIN",help="Enter if the person experiences chest pain")

    lungs_diagnosis = ""
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models["lung_cancer"].predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer" if lungs_prediction[0] == 1 else "The person does not have lung cancer"
        st.success(lungs_diagnosis)

# Hypo-thyroid Prediction Page
if selected == "Hypo-thyroid Prediction":
    st.title("Hypo-thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease")

    age = st.number_input(label="Age",min_value=0,key="AGE",help="Enter age of the person")
    sex = st.number_input(label="Sex (1 = male, 0 = female)",min_value=0,max_value=1,key="sex",help="Enter sex of the person")
    on_thyroxine = st.number_input(label="On Thyroxine (1 = yes, 0 = no)",min_value=0,max_value=1,key="on_thyroxine",help="Enter if the person is on thyroxine")
    tsh = st.number_input(label="TSH Level",min_value=0,key="tsh",help="Enter TSH level")
    t3_measured = st.number_input(label="T3 Measured (1 = yes,0 = no)",min_value=0,max_value=1,key="t3_measured",help="Enter if T3 was measured")
    t3 = st.number_input(label="T3 Level",min_value=0,key="t3",help="Enter T3 level")
    tt4 = st.number_input(label="TT4 Level",min_value=0,key="tt4",help="Enter TT4 level")

    thyroid_diagnosis = ""
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models["thyroid"].predict([[age,sex,on_thyroxine,tsh,t3_measured,t3,tt4]])
        thyroid_diagnosis = "The person has Hypo-thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-thyroid disease"
        st.success(thyroid_diagnosis)