# Heart Disease Prediction - MLOps Pipeline

End-to-end MLOps pipeline that takes a heart disease classification model from a Jupyter notebook to a production-grade, containerized, auto-scaling API on Google Kubernetes Engine.

---

## What This Project Does

A Random Forest model predicts heart disease from 14 clinical features. This project wraps that model in a Flask API, containerizes it with Docker, deploys it on GKE with autoscaling, and adds explainability, fairness testing, live logging, stress testing, and drift detection.

---

## Project Structure

    .github/workflows/ci-cd.yml   - Automated CI/CD pipeline via GitHub Actions
    app/app.py                    - Flask prediction API
    app/Dockerfile                - Container definition
    app/requirements.txt          - Python dependencies
    app/model.pkl                 - Trained model (RandomForest, 86.89% accuracy)
    app/train_save_model.py       - Script to retrain and save the model
    k8s/deployment.yaml           - Kubernetes deployment, service, and autoscaler
    data/data.csv                 - Original heart disease dataset (303 rows)
    data/synthetic_100.csv        - 100-row synthetic data for prediction and drift testing

---

## Deliverable Files

### Model Explainability (SHAP)

- **deliverable2_shap.py** - Trains RandomForest, runs SHAP TreeExplainer only on samples predicted as heart disease positive
- **deliverable2_explainability.md** - Plain English findings: fbs, trestbps, and restecg are the least influential features
- **shap_importance.png** - Bar chart of mean absolute SHAP values per feature

### Fairness Testing (Fairlearn)

- **deliverable3_fairness.md** - MetricFrame results by age group. Key finding: patients under 40 have a 50% false negative rate; selection rate disparity across groups is 0.317
- **fairness_by_age.png** - Accuracy and selection rate visualized across age groups

### API Deployment on GKE

- **app/app.py** - Flask app with /health and /predict endpoints. Every prediction is logged to stdout with full input, output, and timestamp
- **app/Dockerfile** - Builds a python:3.10-slim container served by gunicorn on port 8080
- **k8s/deployment.yaml** - Kubernetes Deployment, LoadBalancer Service, and HorizontalPodAutoscaler with a maximum of 3 pods scaling at 60% CPU
- **.github/workflows/ci-cd.yml** - On every push to master: authenticates to GCP via Workload Identity Federation, builds and pushes Docker image to Artifact Registry, then deploys to GKE

### Per-Sample Prediction and Observability

- **deliverable5_logging.py** - Sends all 100 synthetic rows individually to the live API and records each response
- **predictions_log.csv** - Full output log with timestamp, input features, prediction, and probability for all 100 samples
- **deliverable5_cloud_logging_proof.md** - Confirms prediction logs are visible in GCP Cloud Logging via kubectl stdout capture

### Stress Testing (wrk)

- **wrk_post.lua** - Lua script that defines the POST request body for wrk benchmarking
- **deliverable6_stress_test.md** - Results at 2000 concurrent connections: 37.84 req/s, average latency 5.77s, 394 timeouts. Analysis of throughput and latency distribution included

### Input Drift Detection

- **deliverable7_drift.py** - Runs Kolmogorov-Smirnov test comparing training data distribution against the 100-row synthetic prediction dataset for all 13 features
- **deliverable7_drift.md** - Results: no significant drift detected in any feature (all p-values above 0.05)

---

## Infrastructure Summary

- GKE Cluster: heart-disease-cluster, us-central1-a, e2-medium, 2 nodes
- Docker Image Registry: Artifact Registry (us-central1)
- Authentication: Workload Identity Federation, no service account keys stored
- API Live At: http://34.134.212.183
