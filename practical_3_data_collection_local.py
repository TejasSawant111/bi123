# Practical 3: Data Collection from CSV (Local Python IDE)
# Aim: Data Collection from a CSV file using pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read csv file (give correct path of your file)
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
plt.xlabel(data.columns[1])
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=data.columns[0], y=data.columns[1])
plt.title("Boxplot")
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.show()
