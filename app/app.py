import os, sys, json, logging, pickle, pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

FEATURES = ['age','gender','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    for col in df.select_dtypes(include='object').columns:
        df[col] = pd.factorize(df[col])[0]
    df = df[FEATURES]
    pred = int(model.predict(df)[0])
    prob = float(model.predict_proba(df)[0][pred])
    log_entry = {"input": data, "prediction": pred, "probability": prob}
    print(json.dumps(log_entry), flush=True)
    logging.info(json.dumps(log_entry))
    return jsonify({"prediction": pred, "probability": prob})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
