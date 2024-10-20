# Q2. Write a python program to implement multiple Linear Regression modelfor a car dataset.
# Dataset can be downloaded from:
# https://www.w3schools.com/python/python_ml_multiple_regression.asp

# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Step 2: Load the dataset
url = "https://www.w3schools.com/python/pandas/data/cardata.csv"  # Adjust URL if necessary
data = pd.read_csv(url)

# Step 3: Display the first few rows of the dataset
print(data.head())

# Step 4: Define the features and the target variable
# Assuming 'price' is the target variable and other columns are features
X = data[['age', 'mileage', 'hp']]  # Example features
y = data['price']  # Target variable

# Step 5: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Create a linear regression model
model = LinearRegression()

# Step 7: Fit the model to the training data
model.fit(X_train, y_train)

# Step 8: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 9: Evaluate the model
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred, squared=False))

# Step 10: Print the coefficients
print('Coefficients:', model.coef_)
