# requests will download the files, bs4 is to parse through the website

import requests
from bs4 import BeautifulSoup

# fetching the url to turn it into soup

url = 'http://www.ico.org/new_historical.asp?section=Statistics'
filetype = '.xlsx'

html = requests.get(url, timeout=5)

s = BeautifulSoup(html.content, 'html.parser')

# parsing through and printing all links on the website

for link in s.find_all('a'):
    excel_link = link.get('href')
    if filetype in excel_link:
        print(excel_link)
        with open(link.text, 'wb') as file:
            response = requests.get(url + excel_link, timeout=5)
            file.write(response.content)