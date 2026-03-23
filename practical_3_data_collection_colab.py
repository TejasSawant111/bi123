# Practical 3: Data Collection from CSV (Google Colab)
# Aim: Data Collection from a CSV file using pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Read csv file
data = pd.read_csv("file.csv")
print(data.head())

print("First 5 rows:")
print(data.head())

print("\nSummary Statistics:")
print(data.describe())

print("\nInfo:")
print(data.info())

# Histogram
plt.figure(figsize=(8, 6))
sns.histplot(data[data.columns[1]], bins=20, kde=True)
plt.title("Histogram")
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=data.columns[0], y=data.columns[1], data=data)
plt.show()
