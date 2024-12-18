import requests
import pandas as pd
from bs4 import BeautifulSoup

# Extrair dados de um site
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table", {"data-test": "historical-prices"})
                        
# Extrair dados de uma tabela
data = []
table_body = table.find("tbody")
rows =table_body.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    cols = [ele.text.strip()for ele in cols]
    data.append([ele for ele in cols if ele])

# Converter o dado para o pandas dataframe
df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

                    