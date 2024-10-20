# Q2. Write a Python program to read “StudentsPerformance.csv” file. Solvefollowing:
# - To display the shape of dataset.
# - To display the top rows of the dataset with their columns.Note: Download
# dataset from following link :
# (https://www.kaggle.com/spscientist/students-performance-inexams?
# select=StudentsPerformance.csv)

import pandas as pd

# Step 1: Load the dataset
file_path = 'StudentsPerformance.csv'  # Make sure to set the correct path to the file
data = pd.read_csv(file_path)

# Step 2: Display the shape of the dataset
print("Shape of the dataset:", data.shape)

# Step 3: Display the top rows of the dataset
print("\nTop rows of the dataset:")
print(data.head())
