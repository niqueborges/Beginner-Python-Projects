import win32com.client as win32
import pandas as pd
from dotenv import load_dotenv
import os

# Carregando variáveis de ambiente
load_dotenv()

# Função principal
def main():
    # Lendo os dados de venda de um arquivo CSV
    sales_data = pd.read_csv("sales.csv")

    # Processando os dados de vendas
    total_sales = sales_data["sales"].sum()
    average_sales = sales_data["sales"].mean()
    max_sales = sales_data["sales"].max()
    min_sales = sales_data["sales"].min()

    # Criando o relatório de vendas
    report = (
        f"Total Sales: ${total_sales:.2f}\n"
        f"Average Sales: ${average_sales:.2f}\n"
        f"Maximum Sales: ${max_sales:.2f}\n"
        f"Minimum Sales: ${min_sales:.2f}"
    )

    # Recuperando o e-mail do destinatário do arquivo .env
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    # Enviando email
    send_email(recipient_email, "Daily Sales Report", report, "sales.csv")

# Função para envio de e-mail
def send_email(recipient, subject, body, attachment):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 indica um e-mail padrão
    mail.To = recipient
    mail.Subject = subject
    mail.Body = body
    mail.Attachments.Add(attachment)
    mail.Send()

if __name__ == "__main__":
    main()
