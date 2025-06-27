# Refatorado para usar yfinance e .env

import time
import smtplib
import logging
import os
from dotenv import load_dotenv
import yfinance as yf

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configurações
STOCK_SYMBOL = "TSLA"
TARGET_PRICE = 800.0

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(subject, body):
    """Função para enviar alerta por e-mail."""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)
            logging.info("E-mail enviado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")

def get_stock_price():
    """Obtém o preço atual da ação usando yfinance."""
    try:
        stock = yf.Ticker(STOCK_SYMBOL)
        stock_price = stock.history(period="1d")["Close"].iloc[-1]
        return float(stock_price)
    except Exception as e:
        logging.error(f"Erro ao obter preço da ação: {e}")
        return None

def monitor_stock_price():
    """Monitora o preço da ação e envia alerta quando o preço-alvo for atingido."""
    while True:
        stock_price = get_stock_price()
        if stock_price is not None:
            logging.info(f"Preço atual da ação: ${stock_price:.2f}")
            if stock_price >= TARGET_PRICE:
                subject = "Tesla Stock Price Alert"
                body = f"The stock price has reached ${stock_price:.2f}!"
                send_email(subject, body)
                break
        time.sleep(60)

if __name__ == "__main__":
    monitor_stock_price()

        
    
    
    
    


