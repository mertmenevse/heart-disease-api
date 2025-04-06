#START

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('heart_disease_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # JSON verisini al
    data = request.get_json()
    
    # Özellikleri numpy dizisine çevir
    features = np.array(data['features']).reshape(1, -1)
    
    # Tahmin yap
    prediction = model.predict(features)
    
    # Sonucu JSON olarak döndür
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)