# pages/1_EMI_Prediction.py
import streamlit as st
import pandas as pd

st.title("💳 EMI Eligibility Prediction")
st.write("Fill borrower details. Inputs are grouped for clarity.")

# Two-column layout: left = personal, right = financial
with st.form("emi_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Personal")
        age = st.number_input("Age", min_value=18, max_value=75, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        existing_loans = st.selectbox("Existing Loans", ["No", "Yes"])

    with col2:
        st.subheader("Financial")
        monthly_salary = st.number_input("Monthly Salary (INR)", min_value=0.0, value=50000.0, step=1000.0)
        current_emi_amount = st.number_input("Current EMI Amount (INR)", min_value=0.0, value=0.0, step=500.0)
        credit_score = st.number_input("Credit Score", min_value=300.0, max_value=1200.0, value=700.0)

    st.subheader("Loan Request")
    emi_scenario = st.selectbox("EMI Scenario", [
        "Personal Loan EMI", "E-commerce Shopping EMI", "Home Appliances EMI",
        "Vehicle EMI", "Education EMI"
    ])
    requested_amount = st.number_input("Requested Amount (INR)", min_value=1000.0, value=100000.0, step=500.0)
    requested_tenure = st.number_input("Requested Tenure (months)", min_value=1, value=12)

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "monthly_salary": monthly_salary,
        "current_emi_amount": current_emi_amount,
        "credit_score": credit_score,
        "emi_scenario": emi_scenario,
        "requested_amount": requested_amount,
        "requested_tenure": requested_tenure,
        "existing_loans": existing_loans
    }])

    st.markdown("### Input summary")
    st.table(input_df.T.rename(columns={0: "value"}))

    # Try both function names (predict_df or predict) to be robust
    try:
        from predict_wrapper import predict_df as predict_func
    except Exception:
        try:
            from predict_wrapper import predict as predict_func
        except Exception as e:
            st.error("Prediction helper not found. Ensure predict_wrapper.py exists and defines `predict` or `predict_df`.")
            st.exception(e)
            predict_func = None

    if predict_func is not None:
        try:
            res = predict_func(input_df)
            # present predictions as metrics if single row
            if len(res) == 1:
                row = res.iloc[0]
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("EMI Eligibility", str(row.get("emi_eligibility_pred", row.get("emi_eligibility", "N/A"))))
                with col_b:
                    val = row.get("max_monthly_emi_pred", row.get("max_monthly_emi", None))
                    try:
                        val_display = f"₹{float(val):,.2f}" if val is not None else "N/A"
                    except Exception:
                        val_display = str(val)
                    st.metric("Max Monthly EMI", val_display)
                # also show the raw dataframe under
                st.markdown("#### Raw model output")
                st.dataframe(res, use_container_width=True)
            else:
                st.dataframe(res, use_container_width=True)
        except Exception as e:
            st.error("Prediction failed. See error below.")
            st.exception(e)
