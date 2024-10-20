# Q2. Write a Python program build Decision Tree Classifier forshows.csvfrom pandas and
# predict class label for show starring a 40 years old American comedian, with 10
# years of experience, and a comedy ranking of 7? Create a csv file as shown in
# https://www.w3schools.com/python/python_ml_decision_tree.asp

# First, create a CSV file named shows.csv with the following content:
Age,Nationality,Experience,Comedy_Ranking,Class
30,American,5,8,Hit
45,American,15,9,Hit
38,British,10,6,Miss
28,Canadian,3,5,Miss
40,American,10,7,Hit
35,American,8,6,Hit

##############################

# Now, use the following Python code to build the Decision Tree Classifier:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('shows.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
data['Nationality'] = label_encoder.fit_transform(data['Nationality'])
data['Class'] = label_encoder.fit_transform(data['Class'])

# Split features and target variable
X = data[['Age', 'Nationality', 'Experience', 'Comedy_Ranking']]
y = data['Class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Predicting the class for a 40-year-old American comedian
new_show = [[40, label_encoder.transform(['American'])[0], 10, 7]]
predicted_class = classifier.predict(new_show)

# Decode the predicted class back to original labels
predicted_label = label_encoder.inverse_transform(predicted_class)
print(f"The predicted class for the show is: {predicted_label[0]}")
