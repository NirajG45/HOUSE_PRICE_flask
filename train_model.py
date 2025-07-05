import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset (can be extended)
data = {
    'Location': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai'],
    'Bedrooms': [2, 3, 3, 4, 5],
    'BedroomArea': [300, 450, 500, 600, 750],
    'Bathrooms': [1, 2, 2, 3, 3],
    'BathroomArea': [100, 150, 180, 200, 240],
    'Toilets': [1, 2, 2, 2, 3],
    'ToiletArea': [80, 100, 120, 130, 150],
    'Price': [50, 80, 95, 120, 160]
}

df = pd.DataFrame(data)

# One-hot encode location
df = pd.get_dummies(df, columns=['Location'])

# Features and labels
X = df.drop('Price', axis=1)
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and columns
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/columns.pkl', 'wb') as f:
    pickle.dump(X.columns.tolist(), f)

print("✅ Model trained and saved.")
