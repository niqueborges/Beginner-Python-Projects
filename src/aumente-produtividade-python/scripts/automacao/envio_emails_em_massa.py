import os
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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

    # Recuperando informações do .env
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    # Enviando e-mail
    send_email(sender_email, sender_password, recipient_email, "Daily Sales Report", report, csv_path)

# Função para envio de e-mail
def send_email(sender, password, recipient, subject, body, attachment_path):
    try:
        # Configurando o e-mail
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject

        # Adicionando corpo do e-mail
        msg.attach(MIMEText(body, "plain"))

        # Adicionando anexo
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(attachment_path)}",
        )
        msg.attach(part)

        # Conectando ao servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Ativando encriptação TLS
            server.login(sender, password)
            server.send_message(msg)

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

if __name__ == "__main__":
    main()
