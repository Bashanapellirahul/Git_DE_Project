import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldfootball.net/top_scorer/eng-premier-league/'
headers = []
page = requests.get(url)

# Check if the page was fetched correctly
if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the table with the class name 'standard_tabelle'
    table = soup.find("table", class_="standard_tabelle")

    # If table is None, print an error message
    if table is None:
        print("Error: Could not find the table. Please check the class name or the HTML structure.")
    else:
        # Get headers
        header_row = table.find('tr')
        if header_row:
            for i in header_row.find_all(['th', 'td']):
                title = i.text.strip()
                headers.append(title)
                print(title)

        if not headers:
            print("Error: No headers found. Please check the table structure.")
        else:
            print(f"Headers found: {headers}")
            league_table = pd.DataFrame(columns=headers)

            # Get rows
            for j in table.find_all('tr')[1:]:
                row_data = j.find_all('td')
                row = [i.text.strip() for i in row_data]
                if len(row) == len(headers):
                    length = len(league_table)
                    league_table.loc[length] = row
                else:
                    print(f"Skipping row with mismatched columns: {row}")

            print(league_table)
else:
    print(f"Error: Unable to fetch the page. Status code: {page.status_code}")
