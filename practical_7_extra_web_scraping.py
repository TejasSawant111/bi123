# Practical 7 Extra: Web Scraping
# Aim: Data Collection from Web

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read and Load Data from the Web

# Define the URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all the quotes and their authors
quotes = []
authors = []

for quote in soup.find_all('span', class_='text'):
    quotes.append(quote.get_text())

for author in soup.find_all('small', class_='author'):
    authors.append(author.get_text())

# Create a DataFrame from the extracted data
data_df = pd.DataFrame({'Quote': quotes, 'Author': authors})
print(data_df)
