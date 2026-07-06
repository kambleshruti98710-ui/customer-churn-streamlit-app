import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl","rb"))

st.title("Customer Churn Prediction")
st.write("Enter Customer Details")

gender = st.selectbox("Gender",["Male","Female"])
SeniorCitizen = st.selectbox("Senior Citizen",[0,1])
Partner = st.selectbox("Partner",[0,1])
Dependents = st.selectbox("Dependents",[0,1])
tenure = st.number_input("Tenure",min_value=0,max_value=72)

PhoneService = st.selectbox("Phone Service",[0,1])
MultipleLines = st.selectbox("Multiple Lines",[0,1])
OnlineSecurity = st.selectbox("Online Security",[0,1])
OnlineBackup = st.selectbox("Online Backup",[0,1])
DeviceProtection = st.selectbox("Device Protection",[0,1])
TechSupport = st.selectbox("Tech Support",[0,1])
StreamingTV = st.selectbox("Streaming TV",[0,1])
StreamingMovies = st.selectbox("Streaming Movies",[0,1])
PaperlessBilling = st.selectbox("Paperless Billing",[0,1])

MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

InternetService = st.selectbox("Internet Service",["DSL","Fiber optic","No"])

Contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])

PaymentMethod = st.selectbox("Payment Method",
["Bank transfer (automatic)",
"Credit card (automatic)",
"Electronic check",
"Mailed check"])

if st.button("Predict"):

    if gender=="Male":
        gender=1
    else:
        gender=0

    InternetService_DSL=0
    InternetService_Fiber_optic=0
    InternetService_No=0

    if InternetService=="DSL":
        InternetService_DSL=1
    elif InternetService=="Fiber optic":
        InternetService_Fiber_optic=1
    else:
        InternetService_No=1

    Contract_Month_to_month=0
    Contract_One_year=0
    Contract_Two_year=0

    if Contract=="Month-to-month":
        Contract_Month_to_month=1
    elif Contract=="One year":
        Contract_One_year=1
    else:
        Contract_Two_year=1

    PaymentMethod_Bank_transfer=0
    PaymentMethod_Credit_card=0
    PaymentMethod_Electronic_check=0
    PaymentMethod_Mailed_check=0

    if PaymentMethod=="Bank transfer (automatic)":
        PaymentMethod_Bank_transfer=1
    elif PaymentMethod=="Credit card (automatic)":
        PaymentMethod_Credit_card=1
    elif PaymentMethod=="Electronic check":
        PaymentMethod_Electronic_check=1
    else:
        PaymentMethod_Mailed_check=1

    data=[[gender,
           SeniorCitizen,
           Partner,
           Dependents,
           tenure,
           PhoneService,
           MultipleLines,
           OnlineSecurity,
           OnlineBackup,
           DeviceProtection,
           TechSupport,
           StreamingTV,
           StreamingMovies,
           PaperlessBilling,
           MonthlyCharges,
           TotalCharges,
           InternetService_DSL,
           InternetService_Fiber_optic,
           InternetService_No,
           Contract_Month_to_month,
           Contract_One_year,
           Contract_Two_year,
           PaymentMethod_Bank_transfer,
           PaymentMethod_Credit_card,
           PaymentMethod_Electronic_check,
           PaymentMethod_Mailed_check]]

    df=pd.DataFrame(data,columns=[
        'gender',
        'SeniorCitizen',
        'Partner',
        'Dependents',
        'tenure',
        'PhoneService',
        'MultipleLines',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'PaperlessBilling',
        'MonthlyCharges',
        'TotalCharges',
        'InternetService_DSL',
        'InternetService_Fiber optic',
        'InternetService_No',
        'Contract_Month-to-month',
        'Contract_One year',
        'Contract_Two year',
        'PaymentMethod_Bank transfer (automatic)',
        'PaymentMethod_Credit card (automatic)',
        'PaymentMethod_Electronic check',
        'PaymentMethod_Mailed check'
    ])

    prediction=model.predict(df)

    if prediction[0]==1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Not Churn")