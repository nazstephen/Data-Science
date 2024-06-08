import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the data from website
URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')

# Create a list to store the column names
heading_table = []
for row in soup.find_all('th'):  
    heading_table.append(row.text)

# Create a list to store the data
content = []
for row in soup.find_all('tr'):
    if not row.find_all('th'):
        content.append([element.text for element in row.find_all('td')])

# Create DataFrame
weather_records = pd.DataFrame(content, columns = heading_table)
print(weather_records)