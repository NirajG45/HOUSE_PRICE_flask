from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        age = int(request.form['age'])

        features = np.array([[area, bedrooms, age]])
        prediction = model.predict(features)[0]

        return render_template('index.html', result=f"Estimated Price: ₹{prediction:.2f} Lakhs")

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

# Optional API endpoint
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    features = np.array([[data['area'], data['bedrooms'], data['age']]])
    prediction = model.predict(features)[0]
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=True)
