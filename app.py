from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')  # Load trained model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sqft = float(request.form['GrLivArea'])
        beds = int(request.form['BedroomAbvGr'])
        baths = int(request.form['FullBath'])

        features = np.array([[sqft, beds, baths]])
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction_text=f"Predicted House Price: ${prediction:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
