import os
import win32com.client as win64
import pandas as pd
from dotenv import load_dotenv

# Carregando variáveis de ambiente
load_dotenv()

# Caminho para o arquivo CSV
csv_path = "src/aumente-produtividade-python/scripts/automacao/sales.csv"

# Função principal
def main():
    # Verifica se o arquivo CSV existe, se não, cria um vazio
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as f:
            f.write("sales\n")  # Escreve um cabeçalho básico

    # Lendo os dados de venda do arquivo CSV
    sales_data = pd.read_csv(csv_path)

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

    # Enviando e-mail
    send_email(recipient_email, "Daily Sales Report", report, "sales.csv")

# Função para envio de e-mail
def send_email(recipient, subject, body, attachment):
    try:
        outlook = win64.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)  # 0 indica um e-mail padrão
        mail.To = recipient
        mail.Subject = subject
        mail.Body = body
        mail.Attachments.Add(attachment)
        mail.Send()
    except Exception as e:
        print(f"Erro ao tentar enviar o email: {e}")

if __name__ == "__main__":
    main()
