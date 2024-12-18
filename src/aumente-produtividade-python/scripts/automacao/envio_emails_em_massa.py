import win32com.cliente as win32
import pandas as pd

# Lendo os dados de venda de um arquivo CSV
sales_data = pd.read_csv("sales.csv")

# Processando os dados de vendas
total_sales = sales_data["sales"].sum()
average_sales = sales_data["sales"].mean()
max_sales = sales_data["sales"].max()
min_sales = sales_data["sales"].min()

# Criando o relatório de vendas
report = "Total Sales: $" + str(total_sales) + "\n"
report += "Average Sales: $" + str(average_sales) + "\n"
report += "Maximum Sales: $" + str(max_sales) + "\n"
report += "Minimum Sales: $" + str(min_sales)