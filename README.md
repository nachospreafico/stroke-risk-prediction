# Stroke Risk Scoring Engine

## Decision-Aware Predictive Modeling Prototype

This project implements a leakage-safe machine learning pipeline for probabilistic stroke risk prediction, with emphasis on **decision-aware threshold selection** rather than raw classification accuracy.

The objective is to demonstrate how predictive models can be translated into operational decisions through structured evaluation and cost-sensitive analysis.

---

## Project Scope

This repository includes:

- Structured exploratory data analysis (EDA)
- Reproducible preprocessing and modeling pipeline
- Class imbalance handling (~19:1 ratio)
- ROC-AUC and Precision–Recall evaluation
- Cost-sensitive threshold optimization
- Exportable scoring component (`model.joblib`)

The focus is on modeling rigor and decision logic rather than UI or deployment tooling.

---

## Modeling Approach

### Preprocessing

- Median imputation for numeric features
- Standard scaling for continuous variables
- One-hot encoding for categorical variables
- Binary passthrough (0/1 indicators)
- Strict train/test separation prior to fitting

All transformations are embedded inside a `scikit-learn` Pipeline to prevent data leakage and ensure reproducibility.

### Model

- Logistic Regression
- `class_weight="balanced"` to address severe class imbalance
- Probabilistic output (risk score)

---

## Performance Summary

Held-out test performance:

- **ROC-AUC ≈ 0.84**
- **PR-AUC ≈ 0.25** (baseline ≈ 0.05 due to prevalence)

Evaluation emphasizes recall–precision trade-offs and operational impact rather than raw accuracy.

---

## Decision-Aware Threshold Optimization

Instead of using the default 0.5 threshold, classification thresholds were optimized under varying false-negative to false-positive cost ratios (e.g., 2:1, 5:1, 10:1).

This demonstrates:

- How operating points shift under different risk tolerances
- The trade-off between missed cases and unnecessary follow-ups
- The importance of separating model probability from decision policy

The model is therefore framed as a **risk scoring engine**, not a fixed classifier.

---

## Key Takeaways

- Probabilistic models require explicit decision rules.
- Threshold selection is a business/operational decision.
- Evaluation under class imbalance requires PR-based metrics.
- Clean preprocessing and pipeline design are critical for reproducibility.

---

## Limitations

- Observational dataset (predictive ≠ causal)
- No external validation dataset
- Limited feature set
- No calibration analysis included in this version

This project is intended as a methodological demonstration, not a clinical decision tool.

---

## Repository Structure

```
stroke-risk-scoring-engine/
│
├── notebooks/
│   ├── 01_clinical_eda.ipynb
│   ├── 02_modeling.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── model.joblib
├── README.md
```

---

## Author

Ignacio Spreafico  
MD | Data & Decision Science
