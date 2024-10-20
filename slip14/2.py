# Q2. Write a Python Programme to apply Apriori algorithm on Groceries dataset. Dataset
# can be downloaded from
# (https://github.com/amankharwal/Websitedata/blob/master/Groceries
# _dataset.csv).
# Also display support and confidence for each rule.

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the dataset
url = 'https://github.com/amankharwal/Websitedata/raw/master/Groceries_dataset.csv'
data = pd.read_csv(url)

# Data preprocessing
# The dataset might be in a transactional format, so we need to transform it
# Create a basket for each transaction
basket = (data.groupby(['Invoice', 'Item'])['Item']
          .count().unstack().reset_index().fillna(0)
          .set_index('Invoice'))

# Convert the values to 1 (purchase) or 0 (no purchase)
def encode_units(x):
    return 1 if x > 0 else 0

basket_encoded = basket.applymap(encode_units)

# Apply the Apriori algorithm
frequent_itemsets = apriori(basket_encoded, min_support=0.01, use_colnames=True)

# Generate the rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Display the support and confidence for each rule
print("Rules with Support and Confidence:")
for index, row in rules.iterrows():
    print(f"Rule: {row['antecedents']} -> {row['consequents']}, Support: {row['support']:.4f}, Confidence: {row['confidence']:.4f}")
