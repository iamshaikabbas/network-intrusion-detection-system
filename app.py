from flask import Flask, request, jsonify
import joblib
import pandas as pd
from realtime_engine import add_packet, get_features

app = Flask(__name__)

rf_model = joblib.load("models/rf_model.pkl")
iso_model = joblib.load("models/iso_model.pkl")

feature_names = list(rf_model.feature_names_in_)

latest_result = {"prediction": "Normal", "rate": 0}

@app.route('/')
def home():
    return "DDoS Detection Running"

@app.route('/predict', methods=['POST'])
def predict():
    global latest_result

    data = request.json
    features = data["features"]

    size = features[0]
    ttl = features[1]

    # 🔹 Update buffer
    add_packet(size, ttl)
    window = get_features()

    if window is None:
        return jsonify({"prediction": "Collecting..."})

    df = pd.DataFrame([features], columns=feature_names)

    ml = rf_model.predict(df)[0]
    anomaly = iso_model.predict(df)[0]

    rule = window["rate"] > 10 or size > 1500

    if rule or anomaly == -1 or ml == 1:
        result = "Attack"
    else:
        result = "Normal"

    latest_result = {
        "prediction": result,
        "rate": window["rate"]
    }

    return jsonify(latest_result)

@app.route('/status', methods=['GET'])
def status():
    return jsonify(latest_result)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)