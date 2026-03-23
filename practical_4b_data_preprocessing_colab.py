# Practical 4B: Data Preprocessing (Google Colab)
# Aim: Data cleaning and preprocessing using Google Colab

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
data = pd.read_csv(file_name, encoding='ISO-8859-1')

# Data Exploration

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Define a list of numerical columns
numerical_columns = ['Temperature', 'Humidity']

# Summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(data[numerical_columns].describe())

# Handling Missing Values

# Check for missing values in the numerical columns
missing_values = data[numerical_columns].isnull().sum()
print("\nMissing values in the numerical columns:")
print(missing_values)

data['Temperature'].fillna(data['Temperature'].mean(), inplace=True)
data['Outlook'] = data['Outlook'].astype('category').cat.codes
data['Wind'] = data['Wind'].map({'weak': 0, 'strong': 1})
data['Play'] = data['Play'].map({'no': 0, 'yes': 1})

# Data Exploration

# Display the first few rows of the dataset
print("\n\nAfter Cleaning\n\n")
print("First 5 rows of the dataset:")
print(data.head())

# Define a list of numerical columns
numerical_columns = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play']

# Summary statistics of the dataset
print("\nSummary statistics of the dataset after cleaning:")
print(data[numerical_columns].describe())

# Handling Missing Values

# Check for missing values in the numerical columns
missing_values = data[numerical_columns].isnull().sum()
print("\nMissing values in the numerical columns after cleaning:")
print(missing_values)
