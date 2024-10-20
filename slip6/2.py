# Q2. Write a python program to implement hierarchical Agglomerative clusteringalgorithm.
# (Download Customer.csv dataset from github.com).

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the dataset
url = 'https://github.com/path/to/Customer.csv'  # Update with actual GitHub URL
data = pd.read_csv(url)

# Preview the dataset
print("Data Preview:")
print(data.head())

# Assuming 'Annual Income' and 'Spending Score' are the features for clustering
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Create a linkage matrix for dendrogram
Z = linkage(X, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

# Fit Agglomerative Clustering
n_clusters = 5  # Number of clusters
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters)
data['Cluster'] = agg_clustering.fit_predict(X)

# Visualize the clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=data, palette='viridis')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
