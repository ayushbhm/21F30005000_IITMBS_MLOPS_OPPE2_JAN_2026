import pandas as pd
import numpy as np
import shap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/data.csv')
print(df.columns.tolist())
print(df.shape)

# Drop sno if present
if 'sno' in df.columns:
    df = df.drop(columns=['sno'])

X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(f"Model accuracy: {model.score(X_test, y_test):.4f}")

# SHAP on heart disease predicted samples only
explainer = shap.TreeExplainer(model)
y_pred = model.predict(X_test)
X_heart = X_test[y_pred == 1]
print(f"\nSamples predicted as heart disease: {len(X_heart)}")

shap_values = explainer.shap_values(X_heart)
# For class 1 (heart disease)
if isinstance(shap_values, list):
    sv = shap_values[1]
else:
    sv = shap_values

mean_abs_shap = pd.Series(np.abs(sv).mean(axis=0), index=X.columns).sort_values()
print("\nFeature importance (mean |SHAP|) - ascending (least to most important):")
print(mean_abs_shap)

# Save bar plot
plt.figure(figsize=(8,6))
mean_abs_shap.plot(kind='barh')
plt.title('Mean |SHAP| for Heart Disease Predicted Samples')
plt.tight_layout()
plt.savefig('shap_importance.png')
print("\nSaved shap_importance.png")

print("\n=== DELIVERABLE 2 PLAIN ENGLISH SUMMARY ===")
bottom3 = mean_abs_shap.head(3).index.tolist()
print(f"The samples predicted to have heart disease are LEAST dependent on: {bottom3}")
print("These features contribute minimally to the model's heart disease predictions.")
