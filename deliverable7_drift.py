import pandas as pd, numpy as np
from scipy import stats

df = pd.read_csv('data/data.csv')
if 'sno' in df.columns: df = df.drop(columns=['sno'])
for col in df.select_dtypes(include='object').columns:
    df[col] = pd.factorize(df[col])[0]

train = df.drop(columns=['target'])

np.random.seed(42)
synth = pd.DataFrame({col: np.random.choice(df[col].dropna().values, 100) for col in train.columns})
synth.to_csv('data/synthetic_100.csv', index=False)

print("=== KS Drift Test ===")
results = []
for col in train.columns:
    t = train[col].dropna().values
    s = synth[col].dropna().values
    stat, p = stats.ks_2samp(t, s)
    drift = "DRIFT" if p < 0.05 else "OK"
    results.append((col, round(stat,4), round(p,4), drift))
    print(f"{col:12s} KS={stat:.4f} p={p:.4f} {drift}")

drifted = [r[0] for r in results if r[3]=="DRIFT"]
print(f"\nDrifted features: {drifted if drifted else 'None - No significant drift detected'}")
