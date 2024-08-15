import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com/sport/football/premier-league/table'
headers = []
page = requests.get(url)

# Check if the page was fetched correctly
if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")

    # Inspect the HTML to find the correct class name
    table = soup.find("table")

    # If table is None, print an error message
    if table is None:
        print("Error: Could not find the table. Please check the class name or the HTML structure.")
    else:
        # Get headers
        for i in table.find_all('th'):
            title = i.text
            headers.append(title)

        league_table = pd.DataFrame(columns=headers)

        # Get rows
        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            length = len(league_table)
            league_table.loc[length] = row

        print(league_table)
else:
    print(f"Error: Unable to fetch the page. Status code: {page.status_code}")
