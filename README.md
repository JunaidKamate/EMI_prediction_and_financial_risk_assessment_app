---

# EMIPredict Pro — EMI & Financial Risk Assessment

---

EMIPredict Pro is a streamlined FinTech application that predicts:
• EMI Eligibility (Classification)
• Maximum Monthly EMI (Regression)

The app is powered by MLflow-tracked machine learning models and deployed through a clean, modern Streamlit interface.

---

### Live App

https://emipredictionandfinancialriskassessmentapp-5dsfbxrvga9rtyay8rt.streamlit.app/EMI_Prediction

---
### Features

User-friendly Streamlit UI

EMI eligibility prediction

Maximum EMI estimation

MLflow experiment tracking

Clear input summary + clean visualization

Deployment-ready structure

---

### Project Structure

EMIPredict_Pro/
• app.py — landing page
• predict_wrapper.py — model loading and prediction logic
• requirements.txt — dependencies
• assets/logo.png — app logo
• pages/1_EMI_Prediction.py — prediction interface

---

### Run Locally

1. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Start the application
streamlit run app.py

--- 

### Author

**Junaid S. Kamate**

---
