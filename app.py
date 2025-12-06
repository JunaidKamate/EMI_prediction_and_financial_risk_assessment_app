import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="EMIPredict Pro",
    page_icon="💳",
    layout="wide"
)

# ---------------------------
# Sidebar Branding (Advanced)
# ---------------------------
from datetime import datetime

st.sidebar.empty()
logo_path = Path("assets/logo.png")
if logo_path.exists():
    st.sidebar.image(str(logo_path), width=140)

st.sidebar.markdown("## EMIPredict Pro")
st.sidebar.markdown("**AI-based EMI Eligibility & Risk Assessment**")
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.radio(
    "Navigate",
    ["Dataset Preview", "EMI Prediction"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.write("Built by **Junaid S. Kamate**")
st.sidebar.caption(f"Updated: {datetime.now().strftime('%Y-%m-%d')}")

# ---------------------------
# Dataset Preview Page
# ---------------------------
if page == "Dataset Preview":
    st.title("📊 Dataset Preview")

    st.markdown(
        f"Project Directory: `{Path.cwd()}`"
    )
    st.write("Upload or place your `emi_prediction_dataset.csv` in the project root to preview it.")

    csv_path = Path("emi_prediction_dataset.csv")

    if csv_path.exists():
        df = pd.read_csv(csv_path)
        st.success("Dataset loaded successfully!")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Place your `emi_prediction_dataset.csv` in the project folder to see preview.")

# ---------------------------
# EMI Prediction Page
# ---------------------------
elif page == "EMI Prediction":
    st.title("💡 EMI Eligibility Prediction")
    st.write("Enter borrower details and click **Predict**.")

    # Input fields
    age = st.number_input("Age", min_value=18, max_value=75, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    monthly_salary = st.number_input("Monthly Salary", min_value=0.0, value=50000.0)
    current_emi_amount = st.number_input("Current EMI Amount", min_value=0.0, value=0.0)
    credit_score = st.number_input("Credit Score", min_value=0.0, max_value=900.0, value=700.0)
    emi_scenario = st.selectbox("EMI Scenario", ["Personal Loan EMI", "Home Loan EMI", "Vehicle Loan EMI"])
    requested_amount = st.number_input("Requested Amount", min_value=0.0, value=100000.0)
    requested_tenure = st.number_input("Requested Tenure (months)", min_value=1, value=12)
    existing_loans = st.selectbox("Existing Loans", ["Yes", "No"])

    if st.button("Predict"):
        # Convert inputs to dataframe
        df_input = pd.DataFrame({
            "age": [age],
            "gender": [gender],
            "monthly_salary": [monthly_salary],
            "current_emi_amount": [current_emi_amount],
            "credit_score": [credit_score],
            "emi_scenario": [emi_scenario],
            "requested_amount": [requested_amount],
            "requested_tenure": [requested_tenure],
            "existing_loans": [existing_loans]
        })

        try:
            from predict_wrapper import predict_df
            result = predict_df(df_input)
            st.success("Prediction successful!")
            st.dataframe(result, use_container_width=True)

        except Exception as e:
            st.error("Prediction failed. Please ensure `predict_wrapper.py` and models exist.")
            st.exception(e)
