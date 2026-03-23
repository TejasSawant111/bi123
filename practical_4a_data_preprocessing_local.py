# Practical 4A: Data Preprocessing (Local Python)
# Aim: Data cleaning and preprocessing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load your dataset from the CSV file
file_path = r'C:\Users\khana\OneDrive\Desktop\Sana\IT\TY IT\BI\NEw Practical\weather_game.csv'

# Read the CSV file with a different encoding (Latin-1)
data = pd.read_csv(file_path, encoding='ISO-8859-1')

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

# Fill missing values
data['Temperature'].fillna(data['Temperature'].mean(), inplace=True)
data['Outlook'] = data['Outlook'].astype('category').cat.codes
data['Wind'] = data['Wind'].map({'weak': 0, 'strong': 1})
data['Play'] = data['Play'].map({'no': 0, 'yes': 1})

print("\n\nAfter Cleaning\n\n")
print("First 5 rows of the dataset:")
print(data.head())
