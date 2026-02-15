
# Stroke Risk Scoring Engine v1
## Decision-Aware Predictive Modeling Prototype

This project implements an end-to-end machine learning pipeline for stroke risk prediction, designed and framed as a deployable **risk scoring engine** rather than a standalone modeling exercise.

The goal is not only to build a predictive model, but to demonstrate how probabilistic outputs can be translated into operational decisions through threshold tuning and cost-sensitive evaluation.

---

## Project Overview

This project includes:

- Structured exploratory data analysis (EDA)
- A fully reproducible preprocessing + modeling pipeline
- Class imbalance handling
- ROC and Precision-Recall evaluation
- Threshold tuning under varying false-negative to false-positive cost assumptions
- Exported pipeline for deployment
- Streamlit-based interactive scoring prototype

The model serves as a prototype for operational risk stratification systems in healthcare or similar high-stakes domains.

---

## Modeling Approach

### Preprocessing Pipeline

- Median imputation for missing numeric values
- Standard scaling for continuous variables
- One-hot encoding for categorical variables
- Binary passthrough for boolean indicators
- Strict train/test separation to prevent data leakage

All preprocessing steps are embedded inside a `scikit-learn` Pipeline to ensure reproducibility and deployment consistency.

---

### Baseline Model

- Logistic Regression
- `class_weight="balanced"` to address 19:1 class imbalance
- Probabilistic output (risk scoring, not just classification)

---

## Model Performance

On held-out test data:

- ROC-AUC ≈ 0.84
- PR-AUC ≈ 0.25 (baseline ≈ 0.05 due to prevalence)
- Strong recall achievable at the cost of precision

Performance evaluation focuses on decision trade-offs rather than raw accuracy.

---

## Cost-Sensitive Threshold Optimization

Instead of using a fixed 0.5 threshold, thresholds were optimized under varying cost assumptions:

- FN:FP = 2
- FN:FP = 5
- FN:FP = 10

This demonstrates how decision boundaries shift depending on operational priorities (e.g., minimizing missed cases vs reducing false positives).

This transforms the model from a classifier into a configurable decision engine.

---

## Streamlit Risk Scoring Prototype

The project includes a lightweight Streamlit application that:

- Accepts user inputs
- Outputs predicted probability
- Assigns risk tier (Low / Moderate / High)
- Allows adjustable classification threshold
- Simulates operational decision behavior

This represents a minimal viable scoring interface suitable for hospital operations or digital health prototyping.

---

## Repository Structure

```
stroke-risk-scoring-engine/
│
├── notebooks/
│   ├── 01_clinical_eda.ipynb
│   ├── 02_modeling.ipynb
│
├── app/
│   ├── app.py
│   ├── model.joblib
│   ├── requirements.txt
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── README.md
```

---

## Running the Streamlit App

From inside the `app/` directory:

```
pip install -r requirements.txt
streamlit run app.py
```

---

## Deployment Considerations

This prototype demonstrates key data product principles:

- Leakage-safe preprocessing
- Embedded transformation logic
- Configurable decision thresholds
- Cost-aware evaluation
- Exportable scoring component

For real-world deployment, additional steps would be required:

- External validation
- Calibration assessment
- Drift monitoring
- Periodic retraining
- Clinical or domain review

---

## Disclaimer

This project is for educational and demonstration purposes only.  
It is not a validated clinical decision tool and should not be used for medical decision-making.

---

## Author

Ignacio Spreafico  
MD | Data & Decision Science
