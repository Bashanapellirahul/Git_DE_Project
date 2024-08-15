import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com/sport/football/premier-league/table'
#the page link we want to extract from
headers = []
#a list that stores our header names
page = requests.get(url)
#makes a request to the webpage and returns the html content
soup = BeautifulSoup(page.text, "html.parser")
#we can use this to clean and sort through the html content toget what we need
table= soup.find("table")
#find the contents in this part of the html content with that class_name
#we use _class because the class is a keyword in python
for i in table.find_all('th'):
#finds all the html tags th which holds the header details
 title = i.text
#gets the text content and appends it to the headers list
 headers.append(title)
league_table = pd.DataFrame(columns = headers)
#creates a dataframe with the headers
for j in table.find_all('tr')[1:]:
#finds all the content with tr tag in the table
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(league_table)
 league_table.loc[length] = row
#gets them by row and saves to the league_table dataframe
print(league_table)


