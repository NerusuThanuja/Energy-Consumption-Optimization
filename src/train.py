import sys, os, numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import load_and_preprocess
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_percentage_error
import joblib

data = load_and_preprocess("data/household_power_consumption.txt")

data['hour'] = data.index.hour
data['temperature'] = 20 + np.random.randn(len(data)) * 4
data['humidity'] = 55 + np.random.randn(len(data)) * 12
data['appliance_load'] = np.random.uniform(0.5, 3.5, len(data))
data['occupancy'] = np.random.randint(1, 6, len(data))

X = data[['hour', 'temperature', 'humidity', 'appliance_load', 'occupancy']]
y = data['energy']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

metrics = {
    "r2": round(r2_score(y_test, y_pred), 3),
    "mape": round(mean_absolute_percentage_error(y_test, y_pred), 3),
    "feature_importance": dict(zip(X.columns, model.feature_importances_.round(3)))
}

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/energy_model.pkl")
joblib.dump(metrics, "models/metrics.pkl")

print("✅ Model trained successfully")