# Q2.Consider the student data set. It can be downloaded from:
# https://drive.google.com/open?id=1oakZCv7g3mlmCSdv9J8kdSaqO 5_6dIOw .
# Write a programme in python to apply simple linear regression and find out mean
# absolute error, mean squared error and root mean squared error.

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the dataset from Google Drive link (localize the download first if needed)
url = "https://drive.google.com/uc?export=download&id=1oakZCv7g3mlmCSdv9J8kdSaqO5_6dIOw"
data = pd.read_csv(url)

# Assuming 'X' is the independent variable and 'Y' is the dependent variable
X = data[['X']]  # Independent variable (reshape if necessary)
Y = data['Y']    # Dependent variable

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Calculate error metrics
mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)

# Print the results
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
