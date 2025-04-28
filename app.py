# app.py
from flask import Flask, request, jsonify
import joblib
import json

# Configuration
API_TOKEN = "mon_super_token_secret"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # Limite : 1 Mo max par requête pour éviter DoS

# Charger le modèle et le vectorizer
model = joblib.load('waf_model_optimized.pkl')
vectorizer = joblib.load('waf_vectorizer.pkl')

def build_request_text(request_dict):
    headers = ' '.join([f"{k}:{v}" for k, v in request_dict.get("headers", {}).items()])
    body = json.dumps(request_dict.get("body", {}))
    request_text = ' '.join([
        request_dict.get("method", ""),
        request_dict.get("url", ""),
        headers,
        body
    ])
    return request_text

def predict_request(request_dict):
    request_text = build_request_text(request_dict)
    X_input = vectorizer.transform([request_text])
    prob = model.predict_proba(X_input)[0, 1]
    prediction = 1 if prob > 0.86 else 0
    label = "Attack" if prediction == 1 else "Normal"
    return label, float(prob)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Bienvenue sur l'API AI Firewall 🚀</h1><p>Utilisez l'endpoint /predict pour faire des prédictions.</p>"


@app.route('/predict', methods=['POST'])
def predict():
    # ✅ Vérifier que le header Authorization contient le bon token
    auth_header = request.headers.get('Authorization')
    if auth_header != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    if not request.is_json:
        return jsonify({"error": "Request must be JSON."}), 400

    request_data = request.get_json()
    try:
        prediction, probability = predict_request(request_data)
        return jsonify({
            "prediction": prediction,
            "probability": probability
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
