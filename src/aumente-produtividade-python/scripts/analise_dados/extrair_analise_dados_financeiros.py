import yfinance as yf
import pandas as pd

# Baixando os dados históricos da ação
ticker = "AAPL"
data = yf.download(ticker, period="1y")

# Convertendo os índices para datas
data.index = pd.to_datetime(data.index)

# Calculando os retornos diários
data["Daily Return"] = data["Adj Close"].pct_change()

# Calculando estatísticas
average_daily_return = data["Daily Return"].mean()
maximum_daily_return = data["Daily Return"].max()
minimum_daily_return = data["Daily Return"].min()

print("Average Daily Return:", average_daily_return)
print("Maximum Daily Return:", maximum_daily_return)
print("Minimum Daily Return:", minimum_daily_return)

# Salvando os dados em CSV
data.to_csv("daily_stock_prices.csv", index=True)

                    