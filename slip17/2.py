# Q2. Write a python programme to implement multiple linear regression modelfor stock market
# data frame as follows:
# Stock_Market = {'Year':
# [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2
# 016,20,16,2016,2016,2016,2016,2016,2016,2016,2016,2016],
# 'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
# 'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1
# .75,1.75,1.75,1.75,1.75,1.75],
# 'Unemployment_Rate':
# [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5
# .9,6.2,6.2,6.1],
# 'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,
# 965,943,958,971,949,884,866,876,822,704,719] }
# And draw a graph of stock market price verses interest rate


import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Creating the stock market data frame
Stock_Market = {
    'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
    'Month': [12,11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
    'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
    'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
    'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(Stock_Market)

# Define the independent variables (Interest Rate and Unemployment Rate)
X = df[['Interest_Rate', 'Unemployment_Rate']]

# Define the dependent variable (Stock Index Price)
y = df['Stock_Index_Price']

# Create the linear regression model
model = LinearRegression()

# Fit the model with the data
model.fit(X, y)

# Print the coefficients and intercept
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predicting stock index price based on the model
predicted_stock_index_price = model.predict(X)
print("Predicted Stock Index Price:", predicted_stock_index_price)

# Plot the graph of Stock Index Price vs. Interest Rate
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='blue', label='Actual Stock Price')
plt.plot(df['Interest_Rate'], predicted_stock_index_price, color='red', label='Predicted Stock Price')
plt.xlabel('Interest Rate')
plt.ylabel('Stock Index Price')
plt.title('Stock Index Price vs Interest Rate')
plt.legend()
plt.show()
