def detect_anomaly(actual, predicted):
    if abs(actual - predicted) > 1.8:
        return "⚠️ Anomaly detected: sudden energy spike"
    return "Normal usage"