# Q2. Write a python program to implement k-means algorithm to build prediction model (Use
# Credit Card Dataset CC GENERAL.csv Download from kaggle.com)

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('CC GENERAL.csv')

# Display the first few rows of the dataset
print(data.head())

# Preprocess the data: Drop non-numeric columns and handle missing values
data = data.drop(columns=['CUST_ID'])  # Drop the customer ID column
data.fillna(data.mean(), inplace=True)  # Fill missing values with column means

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Find the optimal number of clusters using the Elbow method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Fit the K-means model with the optimal number of clusters (e.g., 5)
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(data_scaled)

# Add the cluster labels to the original dataset
data['Cluster'] = kmeans.labels_

# Display the cluster centroids
print("Cluster Centers:\n", scaler.inverse_transform(kmeans.cluster_centers_))

# Analyze the clustering results
print(data.groupby('Cluster').mean())
