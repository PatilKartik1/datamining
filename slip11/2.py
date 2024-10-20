# Q2. Write a python program to implement hierarchical clustering algorithm.(Download
# Wholesale customers data dataset from github.com).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Step 1: Load the dataset
url = 'https://raw.githubusercontent.com/path/to/wholesale-customers-data.csv'  # Replace with actual path
data = pd.read_csv(url)

# Step 2: Preprocessing (if needed)
# Assuming the dataset has numeric values for clustering
data = data.select_dtypes(include=[np.number])

# Step 3: Perform hierarchical clustering
linked = linkage(data, method='ward')

# Step 4: Create a dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, 
           orientation='top', 
           labels=data.index, 
           distance_sort='descending', 
           show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Index')
plt.ylabel('Distance')
plt.show()

# Step 5: Create clusters
# Define the number of clusters
num_clusters = 4
clusters = fcluster(linked, num_clusters, criterion='maxclust')

# Add cluster information to the original data
data['Cluster'] = clusters

# Display the first few rows of the dataset with clusters
print(data.head())
