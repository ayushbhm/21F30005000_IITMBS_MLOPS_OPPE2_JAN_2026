# Deliverable 5: Per-Sample Prediction with Logging & Observability

## Overview
- Generated 100-row synthetic dataset from training distribution
- Sent each row individually to deployed API at http://34.134.212.183/predict
- Each prediction logged with: timestamp, input features, prediction, probability
- Observability demonstrated via GCP Cloud Logging

## GCP Cloud Logging Query
resource.type=k8s_container
resource.labels.cluster_name=heart-disease-cluster
textPayload=~"prediction"

## Sample Log Entry Confirmed in GCP Cloud Logging
2026-05-03T09:14:05Z  {"input": {"age": 55, "gender": 1, "cp": 3, "trestbps": 130, "chol": 250, "fbs": 0, "restecg": 1, "thalach": 150, "exang": 0, "oldpeak": 1.5, "slope": 2, "ca": 0, "thal": 2}, "prediction": 0, "probability": 0.94}

## Conclusion
All 100 predictions successfully logged to GCP Cloud Logging via GKE stdout capture.
