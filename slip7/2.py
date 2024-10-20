# Q2. Consider the following observations/data. And apply simple linear regression and find out
# estimated coefficients b1 and b1 Also analyse theperformance of the model
# (Use sklearn package)
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([7,14,15,18,19,21,26,23])

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Define the data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # Reshaping for sklearn
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Create a LinearRegression model
model = LinearRegression()

# Fit the model
model.fit(x, y)

# Get the coefficients
b0 = model.intercept_  # Intercept
b1 = model.coef_[0]    # Slope

# Predict y values
y_pred = model.predict(x)

# Performance metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Results
print(f"Estimated coefficients:\nb0 (intercept): {b0}\nb1 (slope): {b1}")
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
