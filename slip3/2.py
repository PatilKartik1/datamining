# Q2. Consider the following observations/data. And apply simple linear regression and find
# out estimated coefficients b0 and b1.( use numpypackage)
# x=[0,1,2,3,4,5,6,7,8,9,11,13]
# y = ([1, 3, 2, 5, 7, 8, 8, 9, 10, 12,16, 18]

import numpy as np

# Data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12, 16, 18])

# Calculate the coefficients using numpy
n = len(x)
b1 = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b0 = (np.sum(y) - b1 * np.sum(x)) / n

print(f"Estimated coefficients:")
print(f"b0 (Intercept): {b0}")
print(f"b1 (Slope): {b1}")
