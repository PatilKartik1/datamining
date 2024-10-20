# Q2. Write a Python Programme to read the dataset (“Iris.csv”). dataset download from
# (https://archive.ics.uci.edu/ml/datasets/iris) and apply Apriori algorithm.

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the dataset
data = pd.read_csv('Iris.csv')

# Step 2: Preprocess the data
# Convert the species to categorical values
data['Species'] = data['Species'].astype('category').cat.codes

# Step 3: Create a binary matrix
# Binarize the data for the Apriori algorithm
basket = pd.get_dummies(data, columns=['Species'], prefix='', prefix_sep='')

# Step 4: Apply Apriori algorithm
frequent_itemsets = apriori(basket, min_support=0.1, use_colnames=True)

# Step 5: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Display results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)
