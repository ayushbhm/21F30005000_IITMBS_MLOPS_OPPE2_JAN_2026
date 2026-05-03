import pickle, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/data.csv')
if 'sno' in df.columns: df = df.drop(columns=['sno'])
for col in df.select_dtypes(include='object').columns:
    df[col] = pd.factorize(df[col])[0]

X = df.drop(columns=['target'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.4f}")

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Saved model.pkl")
