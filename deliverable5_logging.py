import pandas as pd, numpy as np, requests, json, datetime

synth = pd.read_csv('data/synthetic_100.csv')
API_URL = "http://API_IP/predict"  # replace after cluster ready

results = []
for i, row in synth.iterrows():
    payload = row.to_dict()
    try:
        r = requests.post(API_URL, json=payload, timeout=5)
        result = r.json()
    except Exception as e:
        result = {"error": str(e)}
    log = {"timestamp": datetime.datetime.utcnow().isoformat(), "sample_id": i,
           "input": payload, **result}
    results.append(log)
    print(json.dumps(log))

pd.DataFrame(results).to_csv('predictions_log.csv', index=False)
print(f"\nDone. Logged {len(results)} predictions.")
