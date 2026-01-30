import joblib
import pandas as pd

model = joblib.load("models/energy_model.pkl")
metrics = joblib.load("models/metrics.pkl")

def predict_energy(hour, temperature, humidity, appliance_load, occupancy):
    df = pd.DataFrame([[
        hour, temperature, humidity, appliance_load, occupancy
    ]], columns=[
        'hour', 'temperature', 'humidity', 'appliance_load', 'occupancy'
    ])

    return round(model.predict(df)[0], 2), metrics