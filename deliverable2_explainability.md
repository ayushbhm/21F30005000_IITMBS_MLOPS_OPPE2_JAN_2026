# Deliverable 2: Model Explainability (SHAP)

## Method
Used SHAP TreeExplainer on a RandomForestClassifier (accuracy: 86.89%) to analyze which features the model relies on least when predicting heart disease (target=1).

## SHAP Feature Importance (ascending) for Heart Disease Predicted Samples

| Feature   | Mean |SHAP| |
|-----------|--------------|
| fbs       | 0.0053       |
| trestbps  | 0.0101       |
| restecg   | 0.0156       |
| chol      | 0.0170       |
| age       | 0.0206       |
| gender    | 0.0243       |
| thalach   | 0.0394       |
| slope     | 0.0430       |
| exang     | 0.0752       |
| oldpeak   | 0.0865       |
| thal      | 0.0867       |
| ca        | 0.0954       |
| cp        | 0.0977       |

## Plain English Summary

The samples predicted to have heart disease are **least dependent on**:
1. **fbs (Fasting Blood Sugar)** – Whether blood sugar exceeds 120 mg/dl barely influences the prediction.
2. **trestbps (Resting Blood Pressure)** – The patient's resting blood pressure contributes very little.
3. **restecg (Resting ECG Results)** – The resting electrocardiographic reading has minimal impact.

In contrast, the model relies most heavily on chest pain type (cp), number of major vessels (ca), thal, and oldpeak to flag heart disease.
