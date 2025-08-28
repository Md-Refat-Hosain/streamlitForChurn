import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

continuous_cols = ["tenure", "monthlycharges"]
binary_cols = [
    "seniorcitizen",
    "gender_male",
    "partner_yes",
    "dependents_yes",
    "phoneservice_yes",
    "multiplelines_yes",
    "internetservice_fiber_optic",
    "internetservice_no",
    "onlinesecurity_yes",
    "onlinebackup_yes",
    "deviceprotection_yes",
    "techsupport_yes",
    "streamingtv_yes",
    "streamingmovies_yes",
    "contract_one_year",
    "contract_two_year",
    "paperlessbilling_yes",
    "paymentmethod_credit_card",
    "paymentmethod_electronic_check",
    "paymentmethod_mailed_check",
]

st.title("Customer Churn Prediction - (created by MD REFAT HOSAIN)")

input_data = {}

# Continuous inputs stacked vertically
st.header("Continuous Inputs")
for col_name in continuous_cols:
    if col_name == "tenure":
        input_data[col_name] = st.number_input(
            "Tenure (months)", min_value=0.0, max_value=100.0, value=12.0, step=1.0
        )
    elif col_name == "monthlycharges":
        input_data[col_name] = st.number_input(
            "Monthly Charges ($)", min_value=0.0, max_value=1000.0, value=70.0, step=0.1
        )

# Binary inputs arranged in 3 columns
st.header("Binary Inputs (Checked means Yes / 1  ------ Blank means No / 0 )")
cols = st.columns(3)

for idx, col_name in enumerate(binary_cols):
    with cols[idx % 3]:
        input_data[col_name] = st.checkbox(col_name.replace("_", " ").capitalize())

# Convert booleans to int for binary inputs
for col_name in binary_cols:
    input_data[col_name] = int(input_data[col_name])

if st.button("Predict Churn"):
    response = requests.post(API_URL, json=input_data)
    if response.status_code == 200:
        result = response.json()
        st.success(result["prediction"])
        st.balloons()
    else:
        st.error("Prediction failed. Please try again.")
