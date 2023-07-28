# -*- coding: utf-8 -*-
"""Diabets_ML_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Gx6NoWQDqkDMIvi_4j8o3Vs6KBL_qBz
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
import io
from google.colab import files
uploaded=files.upload()
data = pd.read_csv(io.BytesIO(uploaded["diabetes.csv"]))

# Separate the features (X) and the target variable (y)
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.linear_model import LogisticRegression

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model as a pickle file
import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
    import pickle
import time
import json
from flask import Flask, request, jsonify

# Load the trained model from the pickle file
with open('/content/model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.get_json()

    # Convert the input dictionary to a DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Make prediction using the loaded model
    prediction = model.predict(input_df)[0]

    # Map the prediction to 'Diabetic' or 'Non-Diabetic'
    result = 'Diabetic' if prediction == 1 else 'Non-Diabetic'

    # Prepare the output data
    output_data = {
        'input_parameters': input_data,
        'predicted_value': result
    }

    # Generate the output file name with timestamp
    current_timestamp = int(time.time())
    output_file_name = f'Prediction_{current_timestamp}.txt'
    output_file_path = f'/content/output/{output_file_name}'  # Assuming output directory exists

    # Save the output data to the output file
    with open(output_file_path, 'w') as output_file:
        json.dump(output_data, output_file)

    # Return the prediction result as the API response
    return jsonify(result)

if __name__ == '__main__':
    app.run()

"""This code snippet demonstrates how to build a machine learning model for diabetes prediction and create an API using Python-Flask to serve the model. The steps involved are as follows:

Import the necessary libraries: We import pandas for data manipulation, train_test_split from sklearn.model_selection for splitting the dataset, LogisticRegression from sklearn.ensemble for building the machine learning model, pickle for saving the trained model, and Flask for creating the API.

Load the dataset: We read the dataset from a CSV file called 'diabetes.csv' using pandas.

Split the dataset: We split the dataset into independent variables (X) and the dependent variable (y).

Split the data into training and testing sets: We split the data into training and testing sets using the train_test_split function.

Train the machine learning model: We create an instance of the RandomForestClassifier and fit it to the training data.

Save the trained model: We save the trained model as a pickle file called 'model.pkl'.

Create the Flask app: We create a Flask app.

Load the trained model in the API logic: We define a route '/predict' that accepts POST requests. Inside the route, we get the input data from the user, use the loaded model to predict the values based on the input dictionary, save the result in a file in the "output" directory, and return the predicted value as a JSON response.

Run the Flask app: We run the Flask app.

By following these steps, you can build a machine learning model for diabetes prediction and create an API to serve the model.

Postman input :
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
"""

#!mkdir -p /content/output #to create output directory.Run this code before executing the main code
