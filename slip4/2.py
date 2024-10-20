# Q2. Consider following dataset
# weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunn
# y','Overcast','Overcast','Rainy']
# temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
# play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No'].
# Use Naïve Bayes algorithm to predict [0: Overcast, 2: Mild]tuple belongs to which class
# whether to play the sports or not.

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Step 1: Prepare the dataset
weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 
           'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']
temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 
        'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 
        'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Create a DataFrame
data = pd.DataFrame({
    'Weather': weather,
    'Temperature': temp,
    'Play': play
})

# Step 2: Encode categorical variables
label_encoder = LabelEncoder()
data['Weather'] = label_encoder.fit_transform(data['Weather'])
data['Temperature'] = label_encoder.fit_transform(data['Temperature'])
data['Play'] = label_encoder.fit_transform(data['Play'])

# Step 3: Prepare the features and labels
X = data[['Weather', 'Temperature']]
y = data['Play']

# Step 4: Train the Naive Bayes model
model = GaussianNB()
model.fit(X, y)

# Step 5: Make predictions for the input (Overcast, Mild)
input_data = np.array([[label_encoder.transform(['Overcast'])[0], 
                         label_encoder.transform(['Mild'])[0]]])
prediction = model.predict(input_data)

# Convert numerical prediction back to the original class labels
predicted_class = label_encoder.inverse_transform(prediction)

# Output the prediction
print(f"Predicted class for the input (Overcast, Mild): {predicted_class[0]}")
