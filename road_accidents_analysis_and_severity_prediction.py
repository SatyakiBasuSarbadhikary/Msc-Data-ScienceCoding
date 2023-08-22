# -*- coding: utf-8 -*-
"""road-accidents-analysis-and-severity-prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ATgOYgSX8YWghtJtJzzWUCajCCZKg24v
"""

import pandas as pd

import pandas as pd
import numpy as np

# Load the CSV file into a pandas DataFrame
#from google.colab import drive
#drive.mount('/content/drive')
data_file_path = "/content/drive/MyDrive/dft-road-casualty-statistics-casualty-provisional-mid-year-unvalidated-2022 (1).csv"
df = pd.read_csv(data_file_path)

# Display the first few rows of the DataFrame
df.head()

# Shape of the dataset
shape = df.shape

# Data types of the columns
data_types = df.dtypes

# Check for missing values
missing_values = df.isnull().sum()

# Descriptive statistics of the numerical columns
descriptive_stats = df.describe()

# Count of unique values for each column
unique_counts = df.nunique()

shape, data_types, missing_values, descriptive_stats, unique_counts

import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of accident severities
plt.figure(figsize=(8, 6))
sns.countplot(x='casualty_severity', data=df)
plt.title('Distribution of Accident Severities')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.show()

# Plot the relationship between casualty severity and age band
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_severity', y='age_of_casualty', data=df)
plt.title('Casualty Severity by Age of Casualty')
plt.xlabel('Casualty Severity')
plt.ylabel('Age of Casualty')
plt.show()

# Plot the relationship between casualty severity and gender
plt.figure(figsize=(8, 6))
sns.countplot(x='casualty_severity', hue='sex_of_casualty', data=df)
plt.title('Casualty Severity by Gender')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.legend(title='Sex of Casualty', labels=['Unknown', 'Male', 'Female'])
plt.show()

# Plot the relationship between casualty severity and casualty class
plt.figure(figsize=(8, 6))
sns.countplot(x='casualty_severity', hue='casualty_class', data=df)
plt.title('Casualty Severity by Casualty Class')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.legend(title='Casualty Class', labels=['Driver', 'Passenger', 'Pedestrian'])
plt.show()

# Plot the relationship between casualty severity and casualty's home area type
plt.figure(figsize=(8, 6))
sns.countplot(x='casualty_severity', hue='casualty_home_area_type', data=df)
plt.title('Casualty Severity by Home Area Type')
plt.xlabel('Casualty Severity')
plt.ylabel('Count')
plt.legend(title='Home Area Type', labels=['Unknown', 'Urban', 'Semi-Urban', 'Rural'])
plt.show()

# Plot the relationship between casualty severity and the IMD decile
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_severity', y='casualty_imd_decile', data=df)
plt.title('Casualty Severity by IMD Decile')
plt.xlabel('Casualty Severity')
plt.ylabel('IMD Decile')
plt.show()

# Plot the distribution of casualty types
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_type', data=df)
plt.title('Distribution of Casualty Types')
plt.xlabel('Casualty Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Plot the relationship between casualty severity and casualty type
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_severity', y='casualty_type', data=df)
plt.title('Casualty Severity by Casualty Type')
plt.xlabel('Casualty Severity')
plt.ylabel('Casualty Type')
plt.show()

import numpy as np

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
plt.figure(figsize=(15, 12))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

plt.title('Correlation Matrix Heatmap')
plt.show()

# Count the number of records with negative ages
negative_age_count = df[df['age_of_casualty'] < 0].shape[0]

# Count the number of records with undefined gender values
undefined_gender_count = df[(df['sex_of_casualty'] == -1) | (df['sex_of_casualty'] == 9)].shape[0]

negative_age_count, undefined_gender_count

# Exclude records with negative ages or undefined gender values
df_clean = df[(df['age_of_casualty'] >= 0) & ((df['sex_of_casualty'] == 1) | (df['sex_of_casualty'] == 2))]

# Verify that the records have been removed
negative_age_count_clean = df_clean[df_clean['age_of_casualty'] < 0].shape[0]
undefined_gender_count_clean = df_clean[(df_clean['sex_of_casualty'] == -1) | (df_clean['sex_of_casualty'] == 9)].shape[0]

negative_age_count_clean, undefined_gender_count_clean, df_clean.shape

# Plot the distribution of accidents across age bands
plt.figure(figsize=(10, 8))
sns.countplot(x='age_band_of_casualty', data=df_clean)
plt.title('Distribution of Accidents by Age Band of Casualty')
plt.xlabel('Age Band of Casualty')
plt.ylabel('Count')
plt.show()

# Plot the distribution of accidents by gender
plt.figure(figsize=(8, 6))
sns.countplot(x='sex_of_casualty', data=df_clean)
plt.title('Distribution of Accidents by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks([0, 1], ['Male', 'Female'])
plt.show()

# Plot the distribution of accidents by casualty's home area type
plt.figure(figsize=(8, 6))
sns.countplot(x='casualty_home_area_type', data=df_clean)
plt.title('Distribution of Accidents by Casualty Home Area Type')
plt.xlabel('Home Area Type')
plt.ylabel('Count')
plt.xticks([0, 1, 2], ['Urban', 'Semi-Urban', 'Rural'])
plt.show()

# Plot the relationship between home area type and casualty severity
plt.figure(figsize=(8, 6))
sns.boxplot(x='casualty_home_area_type', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Home Area Type')
plt.xlabel('Home Area Type')
plt.ylabel('Casualty Severity')
plt.xticks([0, 1, 2], ['Urban', 'Semi-Urban', 'Rural'])
plt.show()

# Plot the relationship between gender and casualty severity
plt.figure(figsize=(8, 6))
sns.boxplot(x='sex_of_casualty', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Gender')
plt.xlabel('Gender')
plt.ylabel('Casualty Severity')
plt.xticks([0, 1], ['Male', 'Female'])
plt.show()

# Plot the relationship between age band and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='age_band_of_casualty', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Age Band')
plt.xlabel('Age Band')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of pedestrian location values
plt.figure(figsize=(10, 8))
sns.countplot(x='pedestrian_location', data=df_clean)
plt.title('Distribution of Pedestrian Location Values')
plt.xlabel('Pedestrian Location')
plt.ylabel('Count')
plt.show()

# Plot the distribution of pedestrian movement values
plt.figure(figsize=(10, 8))
sns.countplot(x='pedestrian_movement', data=df_clean)
plt.title('Distribution of Pedestrian Movement Values')
plt.xlabel('Pedestrian Movement')
plt.ylabel('Count')
plt.show()

# Plot the relationship between pedestrian location and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='pedestrian_location', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Pedestrian Location')
plt.xlabel('Pedestrian Location')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the relationship between pedestrian movement and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='pedestrian_movement', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Pedestrian Movement')
plt.xlabel('Pedestrian Movement')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of accidents by year
plt.figure(figsize=(10, 8))
sns.countplot(x='accident_year', data=df_clean)
plt.title('Distribution of Accidents by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Calculate the average casualty severity by year
average_severity_by_year = df_clean.groupby('accident_year')['casualty_severity'].mean()

# Plot the average casualty severity by year
plt.figure(figsize=(10, 8))
sns.lineplot(x=average_severity_by_year.index, y=average_severity_by_year.values)
plt.title('Average Casualty Severity by Year')
plt.xlabel('Year')
plt.ylabel('Average Casualty Severity')
plt.show()

# Display the first few values of the 'accident_index' column
df_clean['accident_index'].head()

# Plot the distribution of vehicle reference values
plt.figure(figsize=(10, 8))
sns.countplot(x='vehicle_reference', data=df_clean)
plt.title('Distribution of Vehicle Reference Values')
plt.xlabel('Vehicle Reference')
plt.ylabel('Count')
plt.show()

# Plot the relationship between vehicle reference and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='vehicle_reference', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Vehicle Reference')
plt.xlabel('Vehicle Reference')
plt.ylabel('Casualty Severity')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


# Select the columns to include in the model
columns_to_include = ['casualty_class', 'sex_of_casualty', 'age_band_of_casualty',
                      'casualty_home_area_type', 'vehicle_reference', 'accident_year',
                      'casualty_severity']

# Create a new DataFrame with only the selected columns
df_model = df_clean[columns_to_include]

# One-hot encode the categorical variables
encoder = OneHotEncoder(sparse=False, drop='first')
encoded_features = encoder.fit_transform(df_model.drop(columns='casualty_severity'))

# Check the version of sklearn and use the appropriate method to get feature names
from sklearn import __version__ as sklearn_version
from packaging import version

if version.parse(sklearn_version) >= version.parse('1.0'):
    # For sklearn version 1.0 and above, use 'get_feature_names_out' method
    feature_names = encoder.get_feature_names_out(input_features=df_model.drop(columns='casualty_severity').columns)
else:
    # For older versions of sklearn, use 'get_feature_names' method
    feature_names = encoder.get_feature_names(input_features=df_model.drop(columns='casualty_severity').columns)

# Create a DataFrame with the encoded features
df_encoded = pd.DataFrame(encoded_features, columns=feature_names)

# Add the target variable to the DataFrame
df_encoded['casualty_severity'] = df_model['casualty_severity'].values

# Split the data into a training set and a test set
train, test = train_test_split(df_encoded, test_size=0.2, random_state=42)

# Fit a decision tree model to the training data
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(train.drop(columns='casualty_severity'), train['casualty_severity'])

# Evaluate the model on the test data
predictions = model.predict(test.drop(columns='casualty_severity'))
mse = mean_squared_error(test['casualty_severity'], predictions)

mse

# Extract feature importances from the model
feature_importances = model.feature_importances_

# Create a DataFrame of features and their importances
importances_df = pd.DataFrame({
    'feature': train.drop(columns='casualty_severity').columns,
    'importance': feature_importances
})

# Sort the DataFrame by importance
importances_df = importances_df.sort_values(by='importance', ascending=False)

importances_df.head(10)

# Plot the distribution of Casualty_IMD_Decile values
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_imd_decile', data=df_clean)
plt.title('Distribution of Casualty IMD Decile Values')
plt.xlabel('Casualty IMD Decile')
plt.ylabel('Count')
plt.show()

# Plot the relationship between Casualty_IMD_Decile and Casualty_Severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_imd_decile', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by IMD Decile')
plt.xlabel('Casualty IMD Decile')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of casualty type values
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_type', data=df_clean)
plt.title('Distribution of Casualty Type Values')
plt.xlabel('Casualty Type')
plt.ylabel('Count')
plt.show()

# Plot the relationship between casualty type and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_type', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Casualty Type')
plt.xlabel('Casualty Type')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of pedestrian road maintenance worker values
plt.figure(figsize=(10, 8))
sns.countplot(x='pedestrian_road_maintenance_worker', data=df_clean)
plt.title('Distribution of Pedestrian Road Maintenance Worker Values')
plt.xlabel('Pedestrian Road Maintenance Worker')
plt.ylabel('Count')
plt.show()

# Plot the relationship between pedestrian road maintenance worker and casualty severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='pedestrian_road_maintenance_worker', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Pedestrian Road Maintenance Worker')
plt.xlabel('Pedestrian Road Maintenance Worker')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of Casualty_Home_Area_Type values
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_home_area_type', data=df_clean)
plt.title('Distribution of Casualty Home Area Type Values')
plt.xlabel('Casualty Home Area Type')
plt.ylabel('Count')
plt.show()

# Plot the relationship between Casualty_Home_Area_Type and Casualty_Severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_home_area_type', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Home Area Type')
plt.xlabel('Casualty Home Area Type')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of Age_of_Casualty values
plt.figure(figsize=(10, 8))
sns.histplot(df_clean['age_of_casualty'], bins=20, kde=True)
plt.title('Distribution of Age of Casualty')
plt.xlabel('Age of Casualty')
plt.ylabel('Count')
plt.show()

# Plot the relationship between Age_of_Casualty and Casualty_Severity
plt.figure(figsize=(10, 8))
sns.scatterplot(x='age_of_casualty', y='casualty_severity', data=df_clean, alpha=0.5)
plt.title('Casualty Severity by Age of Casualty')
plt.xlabel('Age of Casualty')
plt.ylabel('Casualty Severity')
plt.show()

# Create a new variable that combines Age_Band_of_Casualty and Casualty_Type
df_clean['age_band_and_type'] = df_clean['age_band_of_casualty'].astype(str) + '_' + df_clean['casualty_type'].astype(str)

# Plot the distribution of the new variable
plt.figure(figsize=(20, 8))
sns.countplot(x='age_band_and_type', data=df_clean, order=df_clean['age_band_and_type'].value_counts().index)
plt.title('Distribution of Age Band and Casualty Type Combinations')
plt.xlabel('Age Band and Casualty Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Select the top 10 most common age_band_and_type values
top_10 = df_clean['age_band_and_type'].value_counts().index[:10]

# Filter the DataFrame to include only the top 10 values
df_top_10 = df_clean[df_clean['age_band_and_type'].isin(top_10)]

# Plot the relationship between age_band_and_type and casualty_severity for the top 10 values
plt.figure(figsize=(10, 8))
sns.boxplot(x='age_band_and_type', y='casualty_severity', data=df_top_10)
plt.title('Casualty Severity by Age Band and Casualty Type')
plt.xlabel('Age Band and Casualty Type')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of Accident_Year values
plt.figure(figsize=(10, 8))
sns.countplot(x='accident_year', data=df_clean)
plt.title('Distribution of Accident Year')
plt.xlabel('Accident Year')
plt.ylabel('Count')
plt.show()

# Calculate the average Casualty_Severity for each Accident_Year
avg_severity_by_year = df_clean.groupby('accident_year')['casualty_severity'].mean().reset_index()

# Plot the average Casualty_Severity over time
plt.figure(figsize=(10, 8))
sns.lineplot(x='accident_year', y='casualty_severity', data=avg_severity_by_year)
plt.title('Average Casualty Severity by Year')
plt.xlabel('Accident Year')
plt.ylabel('Average Casualty Severity')
plt.show()

# Plot the distribution of the top 20 Vehicle_Reference values
plt.figure(figsize=(10, 8))
sns.countplot(x='vehicle_reference', data=df_clean, order=df_clean['vehicle_reference'].value_counts().iloc[:20].index)
plt.title('Distribution of Top 20 Vehicle Reference Values')
plt.xlabel('Vehicle Reference')
plt.ylabel('Count')
plt.show()

# Select the top 20 most common Vehicle_Reference values
top_20 = df_clean['vehicle_reference'].value_counts().index[:20]

# Filter the DataFrame to include only the top 20 values
df_top_20 = df_clean[df_clean['vehicle_reference'].isin(top_20)]

# Plot the relationship between Vehicle_Reference and Casualty_Severity for the top 20 values
plt.figure(figsize=(12, 8))
sns.boxplot(x='vehicle_reference', y='casualty_severity', data=df_top_20)
plt.title('Casualty Severity by Vehicle Reference')
plt.xlabel('Vehicle Reference')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of Status values
plt.figure(figsize=(10, 8))
sns.countplot(x='status', data=df_clean)
plt.title('Distribution of Status Values')
plt.xlabel('Status')
plt.ylabel('Count')
plt.show()

# Plot the relationship between Status and Casualty_Severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='status', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by Status')
plt.xlabel('Status')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of the top 20 Accident_Reference values
plt.figure(figsize=(10, 8))
sns.countplot(x='accident_reference', data=df_clean, order=df_clean['accident_reference'].value_counts().iloc[:20].index)
plt.title('Distribution of Top 20 Accident Reference Values')
plt.xlabel('Accident Reference')
plt.ylabel('Count')
plt.show()

# Select the top 20 most common Accident_Reference values
top_20_refs = df_clean['accident_reference'].value_counts().index[:20]

# Filter the DataFrame to include only the top 20 values
df_top_20_refs = df_clean[df_clean['accident_reference'].isin(top_20_refs)]

# Plot the relationship between Accident_Reference and Casualty_Severity for the top 20 values
plt.figure(figsize=(12, 8))
sns.boxplot(x='accident_reference', y='casualty_severity', data=df_top_20_refs)
plt.title('Casualty Severity by Accident Reference')
plt.xlabel('Accident Reference')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of Casualty_IMD_Decile values
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_imd_decile', data=df_clean)
plt.title('Distribution of Casualty IMD Decile Values')
plt.xlabel('Casualty IMD Decile')
plt.ylabel('Count')
plt.show()

# Plot the relationship between Casualty_IMD_Decile and Casualty_Severity
plt.figure(figsize=(10, 8))
sns.boxplot(x='casualty_imd_decile', y='casualty_severity', data=df_clean)
plt.title('Casualty Severity by IMD Decile')
plt.xlabel('Casualty IMD Decile')
plt.ylabel('Casualty Severity')
plt.show()

# Plot the distribution of the top 20 LSOA_of_Casualty values
plt.figure(figsize=(10, 8))
sns.countplot(x='lsoa_of_casualty', data=df_clean, order=df_clean['lsoa_of_casualty'].value_counts().iloc[:20].index)
plt.title('Distribution of Top 20 LSOA of Casualty Values')
plt.xlabel('LSOA of Casualty')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Select the top 20 most common LSOA_of_Casualty values
top_20_lsoas = df_clean['lsoa_of_casualty'].value_counts().index[:20]

# Filter the DataFrame to include only the top 20 values
df_top_20_lsoas = df_clean[df_clean['lsoa_of_casualty'].isin(top_20_lsoas)]

# Plot the relationship between LSOA_of_Casualty and Casualty_Severity for the top 20 values
plt.figure(figsize=(12, 8))
sns.boxplot(x='lsoa_of_casualty', y='casualty_severity', data=df_top_20_lsoas)
plt.title('Casualty Severity by LSOA of Casualty')
plt.xlabel('LSOA of Casualty')
plt.ylabel('Casualty Severity')
plt.xticks(rotation=90)
plt.show()

# Plot the distribution of the top 20 Casualty_Reference values
plt.figure(figsize=(10, 8))
sns.countplot(x='casualty_reference', data=df_clean, order=df_clean['casualty_reference'].value_counts().iloc[:20].index)
plt.title('Distribution of Top 20 Casualty Reference Values')
plt.xlabel('Casualty Reference')
plt.ylabel('Count')
plt.show()

# Select the top 20 most common Casualty_Reference values
top_20_cas_refs = df_clean['casualty_reference'].value_counts().index[:20]

# Filter the DataFrame to include only the top 20 values
df_top_20_cas_refs = df_clean[df_clean['casualty_reference'].isin(top_20_cas_refs)]

# Plot the relationship between Casualty_Reference and Casualty_Severity for the top 20 values
plt.figure(figsize=(12, 8))
sns.boxplot(x='casualty_reference', y='casualty_severity', data=df_top_20_cas_refs)
plt.title('Casualty Severity by Casualty Reference')
plt.xlabel('Casualty Reference')
plt.ylabel('Casualty Severity')
plt.show()

# Calculate the correlation matrix for numeric variables
corr_matrix = df_clean.corr()

# Plot the correlation matrix as a heatmap for better visualization
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Matrix of Numeric Variables')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Separate the features (X) and the target variable (y)
X = df_encoded.drop(columns='casualty_severity')
y = df_encoded['casualty_severity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
rf.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = rf.predict(X_test)

# Calculate the root mean squared error (RMSE) and the R-squared value (R^2)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

rmse, r2

# Get the feature importances
importances = rf.feature_importances_

# Convert the importances into a DataFrame
importances_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
})

# Sort the DataFrame by importance
importances_df = importances_df.sort_values(by='Importance', ascending=False)

# Display the top 10 most important features
importances_df.head(10)

from sklearn.ensemble import GradientBoostingRegressor

# Create a Gradient Boosting Regressor
gb = GradientBoostingRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
gb.fit(X_train, y_train)

# Make predictions on the testing data
y_pred_gb = gb.predict(X_test)

# Calculate the root mean squared error (RMSE) and the R-squared value (R^2)
rmse_gb = np.sqrt(mean_squared_error(y_test, y_pred_gb))
r2_gb = r2_score(y_test, y_pred_gb)

rmse_gb, r2_gb

# Get the feature importances
importances_gb = gb.feature_importances_

# Convert the importances into a DataFrame
importances_df_gb = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances_gb
})

# Sort the DataFrame by importance
importances_df_gb = importances_df_gb.sort_values(by='Importance', ascending=False)

# Display the top 10 most important features
importances_df_gb.head(10)

# Create the interaction term
df_encoded['age_sex_interaction'] = df_encoded['age_band_of_casualty_11'] * df_encoded['sex_of_casualty_2']

# Separate the features (X) and the target variable (y) again
X = df_encoded.drop(columns='casualty_severity')
y = df_encoded['casualty_severity']

# Split the data into training and testing sets again
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gradient Boosting Regressor
gb_interaction = GradientBoostingRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
gb_interaction.fit(X_train, y_train)

# Make predictions on the testing data
y_pred_gb_interaction = gb_interaction.predict(X_test)

# Calculate the root mean squared error (RMSE) and the R-squared value (R^2)
rmse_gb_interaction = np.sqrt(mean_squared_error(y_test, y_pred_gb_interaction))
r2_gb_interaction = r2_score(y_test, y_pred_gb_interaction)

rmse_gb_interaction, r2_gb_interaction

# Get the feature importances
importances_gb_interaction = gb_interaction.feature_importances_

# Convert the importances into a DataFrame
importances_df_gb_interaction = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances_gb_interaction
})

# Sort the DataFrame by importance
importances_df_gb_interaction = importances_df_gb_interaction.sort_values(by='Importance', ascending=False)

# Display the top 10 most important features
importances_df_gb_interaction.head(10)

# List of parameter combinations to try
param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [100, 200, 300]
}

# Initialize a DataFrame to store the results
results = pd.DataFrame(columns=['Learning Rate', 'Number of Estimators', 'RMSE', 'R²'])

# For each combination of parameters
for learning_rate in param_grid['learning_rate']:
    for n_estimators in param_grid['n_estimators']:

        # Create a Gradient Boosting Regressor with these parameters
        gb_tuned = GradientBoostingRegressor(learning_rate=learning_rate, n_estimators=n_estimators, random_state=42)

        # Fit the model on the training data
        gb_tuned.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred_gb_tuned = gb_tuned.predict(X_test)

        # Calculate the root mean squared error (RMSE) and the R-squared value (R^2)
        rmse_gb_tuned = np.sqrt(mean_squared_error(y_test, y_pred_gb_tuned))
        r2_gb_tuned = r2_score(y_test, y_pred_gb_tuned)

        # Store the results in the DataFrame
        results = results.append({
            'Learning Rate': learning_rate,
            'Number of Estimators': n_estimators,
            'RMSE': rmse_gb_tuned,
            'R²': r2_gb_tuned
        }, ignore_index=True)

results