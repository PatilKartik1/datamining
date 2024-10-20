# Q2. Consider the following observations/data. And apply simple linear regression and find out
# estimated coefficients b1 and b1 Also analyse theperformance of the model
# (Use sklearn package)
# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([7,14,15,18,19,21,26,23])

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data points
x = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)  # reshaping for sklearn
y = np.array([7, 14, 15, 18, 19, 21, 26, 23])

# Creating the model and fitting the data
model = LinearRegression()
model.fit(x, y)

# Estimated coefficients
b0 = model.intercept_  # Intercept
b1 = model.coef_[0]    # Slope

# Print the coefficients
print(f"Estimated intercept (b0): {b0}")
print(f"Estimated slope (b1): {b1}")

# Model performance (R-squared)
r_squared = model.score(x, y)
print(f"R-squared: {r_squared}")

# Plotting the regression line
plt.scatter(x, y, color='blue')  # scatter plot of actual data
plt.plot(x, model.predict(x), color='red')  # regression line
plt.title('Simple Linear Regression')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
