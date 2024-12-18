import requests
import pandas as pd
from bs4 import BeautifulSoup

#Extrair dados de um site
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table", {"data-test": "historical-prices"})
                        