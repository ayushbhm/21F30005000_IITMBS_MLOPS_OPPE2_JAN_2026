# Deliverable 5: Per-Sample Prediction with Logging

- Generated 100-row synthetic dataset (data/synthetic_100.csv)
- Sent each row individually to deployed API: http://34.134.212.183/predict
- Each prediction logged with timestamp, input features, prediction, probability
- App logs visible in GCP Cloud Logging (stdout → GKE → Cloud Logging automatically)
- Results saved to predictions_log.csv
