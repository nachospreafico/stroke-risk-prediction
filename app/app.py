import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -------------------------
# Load Model
# -------------------------

model = joblib.load("model.joblib")

st.set_page_config(page_title="Risk Scoring Engine", layout="centered")

st.title("Risk Scoring Engine v1")
st.caption("Operational Risk Stratification Prototype")

# -------------------------
# User Inputs
# -------------------------

st.header("Patient Profile")

age = st.slider("Age", 0, 100, 50)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", value=100.0)
bmi = st.number_input("BMI", value=25.0)
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# -------------------------
# Decision Settings
# -------------------------

st.header("Decision Settings")

threshold = st.slider("Classification Threshold", 0.0, 1.0, 0.5)
cost_ratio = st.selectbox("FN:FP Cost Ratio", [2, 5, 10])

# -------------------------
# Prepare Input Data
# -------------------------

input_data = pd.DataFrame([{
    "age": age,
    "hypertension": hypertension,
    "heart_disease": heart_disease,
    "avg_glucose_level": avg_glucose_level,
    "bmi": bmi,
    "bmi_missing": 0,
    "gender": "Male",  # placeholder (can extend later)
    "ever_married": ever_married,
    "work_type": work_type,
    "Residence_type": Residence_type,
    "smoking_status": smoking_status
}])

# -------------------------
# Prediction
# -------------------------

probability = model.predict_proba(input_data)[0][1]
prediction = int(probability >= threshold)

# -------------------------
# Risk Tier
# -------------------------

if probability < 0.05:
    tier = "Low"
elif probability < 0.15:
    tier = "Moderate"
else:
    tier = "High"

# -------------------------
# Output
# -------------------------

st.header("Risk Output")

st.metric("Predicted Stroke Risk", f"{probability:.2%}")
st.write(f"Risk Tier: **{tier}**")

if prediction == 1:
    st.error("⚠ Patient would be flagged under current threshold.")
else:
    st.success("✓ Patient would not be flagged under current threshold.")

st.caption("This prototype is for demonstration purposes and is not a clinical decision tool.")
