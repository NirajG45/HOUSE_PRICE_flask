# 🏠 House Price Prediction Web App - Using Flask and Linear Regression

## 🔍 Project Description

This is a **Machine Learning-powered web application** developed using **Python's Flask framework** that predicts the **house price** based on three key features:

- `GrLivArea` (Above Ground Living Area in square feet)
- `BedroomAbvGr` (Number of bedrooms above ground)
- `FullBath` (Number of full bathrooms)

The web app uses a **Linear Regression model**, trained on real housing data and saved using **Joblib**. Users enter house details via a simple web form, and the app displays the predicted price instantly.

---

## 💡 Key Features

- 🔗 **End-to-End ML Integration**: Complete flow from training to prediction.
- 📦 **Pre-trained Linear Regression Model**: Provides fast and reliable predictions.
- 🎨 **User-Friendly Interface**: Clean and responsive HTML/CSS frontend.
- 🌐 **Flask Backend**: Handles data routing and prediction logic.
- 📈 **Accurate Predictions**: Based on real-world housing features.
- 💬 **Live Result Display**: Output shown dynamically on the same page.

---

## 🧠 Technologies Used

| Technology         | Purpose                          |
|--------------------|----------------------------------|
| Python             | Core programming language        |
| Flask              | Web application framework        |
| Pandas, NumPy      | Data processing & array handling |
| Scikit-learn       | Model training (Linear Regression) |
| Joblib             | Model serialization              |
| HTML, CSS          | Frontend UI & styling            |

---

## ⚙️ How It Works

### 1. Model Training (`train_model.py`)
- Loads a dataset (e.g., CSV with house features).
- Trains a Linear Regression model on:
  - `GrLivArea`
  - `BedroomAbvGr`
  - `FullBath`
- Saves the trained model to `model.pkl` using `joblib`.

### 2. Web Application (`app.py`)
- Loads `model.pkl` during initialization.
- Defines Flask routes:
  - `/`: Loads input form (HTML page).
  - `/predict`: Accepts POST data, predicts price, and returns output.

### 3. Frontend Page (`templates/index.html`)
- Simple and responsive HTML form.
- Collects input data from users.
- Displays prediction output or errors dynamically.

---

## 📌 Example Use Case

A user wants to estimate the selling price of a house with:

- `1800 sq ft` area  
- `3 bedrooms`  
- `2 full bathrooms`  

After submitting the form, the app returns:

**`Predicted House Price: $245,000.00`**

---

## ✅ Ideal For

- Beginners learning Flask & ML deployment
- Educational demonstrations of machine learning pipelines
- College mini/major project submission
- Quick ML model deployment examples

---

## 🚀 How to Run This Project Locally

```bash
# 1. Clone the repo or download the files
git clone <your-repo-url>

# 2. Navigate into the folder
cd HousePriceFlaskApp

# 3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the Flask app
python app.py
