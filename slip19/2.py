# Q2. Write a python program to implement multiple Linear Regression modelfor a car dataset.
# Dataset can be downloaded from:
# https://www.w3schools.com/python/python_ml_multiple_regression.asp

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the car dataset
url = "https://www.w3schools.com/python/car_data.csv"  # Replace with your local path if needed
car_data = pd.read_csv(url)

# Display the first few rows of the dataset
print("Car Dataset:")
print(car_data.head())

# Define independent variables (features) and dependent variable (target)
X = car_data[['Weight', 'Volume']]  # Example features (Weight, Volume)
y = car_data['CO2']  # Example target (CO2 emission)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model with the training data
model.fit(X_train, y_train)

# Predict using the test data
y_pred = model.predict(X_test)

# Calculate the performance of the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Display the coefficients of the model
print(f"Intercept (b0): {model.intercept_}")
print(f"Coefficients (b1, b2): {model.coef_}")
