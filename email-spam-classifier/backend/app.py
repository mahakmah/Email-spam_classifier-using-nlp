from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend (different port) to access backend

# Load saved model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return "Spam Classifier Backend is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    message = data.get('email', '')
    
    if not message.strip():
        return jsonify({'result': 'No input provided'}), 400
    
    # Vectorize and predict
    vect_msg = vectorizer.transform([message])
    prediction = model.predict(vect_msg)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
