from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and columns
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('model/columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values
        location = request.form['location']
        bedrooms = int(request.form['bedrooms'])
        bedroom_area = float(request.form['bedroom_area'])
        bathrooms = int(request.form['bathrooms'])
        bathroom_area = float(request.form['bathroom_area'])
        toilets = int(request.form['toilets'])
        toilet_area = float(request.form['toilet_area'])

        # Build input dictionary
        input_dict = {
            'Bedrooms': bedrooms,
            'BedroomArea': bedroom_area,
            'Bathrooms': bathrooms,
            'BathroomArea': bathroom_area,
            'Toilets': toilets,
            'ToiletArea': toilet_area,
            f'Location_{location}': 1
        }

        # Fill missing columns
        for col in model_columns:
            if col not in input_dict:
                input_dict[col] = 0

        # Predict
        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]

        return render_template('index.html', result=f"Estimated Price: ₹{prediction:.2f} Lakhs")

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
