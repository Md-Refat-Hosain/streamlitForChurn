import streamlit as st
import requests
from PIL import Image


API_URL = "https://fastapi-1sb8.onrender.com/predict"


image_path = "Image/A11789B1-928B-4E79-A7FA-40D6FE317615.jpg"
image = Image.open(image_path)  # Replace with your image path

resized_image = image.resize((120, 120))


# Center the card using columns
col1, col2, col3 = st.columns([0.01, 1, 1])

with col2:  # middle column
    st.image(resized_image, caption="Md Refat Hosain")  # profile image

    # Buttons below image & name
    st.markdown(
        """
        <div style="text-align: left;">
            <a href="https://github.com/Md-Refat-Hosain" target="_blank">
                <button style="padding:10px 20px; margin:5px; border-radius:10px; 
                               background:#24292e; color:white; border:none; cursor:pointer;">
                    GitHub
                </button>
            </a>
            <a href="https://www.linkedin.com/in/your-profile/" target="_blank">
                <button style="padding:10px 20px; margin:5px; border-radius:10px; 
                               background:#0077B5; color:white; border:none; cursor:pointer;">
                    LinkedIn
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


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


st.title("Customer Churn Prediction App")

st.markdown(
    "<h3  <span style='color:blue'>(created by MD REFAT HOSAIN).</span>  </h3>",
    unsafe_allow_html=True,
)

st.markdown("<br><br>", unsafe_allow_html=True)  # add 3 line breaks


st.markdown(
    "<h5 <span >  🟥 NOTE: It will take while to run; be patient.</span>  </h5>",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)  # add 3 line breaks


input_data = {}

# Continuous inputs stacked vertically
st.header("Continuous Inputs")
for col_name in continuous_cols:
    if col_name == "tenure":
        input_data[col_name] = st.number_input(
            "Tenure (months)", min_value=0.0, max_value=100.0, value=20.0, step=1.0
        )
    elif col_name == "monthlycharges":
        input_data[col_name] = st.number_input(
            "Monthly Charges ($)", min_value=0.0, max_value=1000.0, value=20.0, step=0.1
        )

st.markdown("<br><br>", unsafe_allow_html=True)  # add 3 line breaks

# Binary inputs arranged in 3 columns
st.header("Binary Inputs (Checked means Yes / 1  ------ Unchecked means No / 0 )")
cols = st.columns(3)

for idx, col_name in enumerate(binary_cols):
    with cols[idx % 3]:
        input_data[col_name] = st.checkbox(col_name.replace("_", " ").capitalize())

# Convert booleans to int for binary inputs
for col_name in binary_cols:
    input_data[col_name] = int(input_data[col_name])

# if st.button("Predict Churn", type="primary"):
#     response = requests.post(API_URL, json=input_data)
#     if response.status_code == 200:
#         result = response.json()
#         st.success(result["prediction"])
#         st.balloons()
#     else:
#         st.error("Prediction failed. Please try again.")
st.markdown("<br>", unsafe_allow_html=True)  # add 3 line breaks

col1, col2 = st.columns([1, 3])  # Adjust ratios if needed
with col1:
    if st.button("Predict Churn", type="primary"):
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(result["prediction"])
            st.balloons()
        else:
            st.error("Prediction failed. Please try again.")

with col2:
    st.markdown(
        "<h5 <span >  🟥 NOTE: It will take while to run; be patient.</span>  </h5>",
        unsafe_allow_html=True,
    )
