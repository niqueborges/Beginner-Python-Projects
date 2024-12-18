import win32com.cliente as win32
import pandas as pd

# Lendo os dados de venda de um arquivo CSV
sales_data = pd.read_csv("sales.csv")

# Processando os dados de vendas
total_sales = sales_data["sales"].sum()
average_sales = sales_data["sales"].mean()
max_sales = sales_data["sales"].max()
min_sales = sales_data["sales"].min()