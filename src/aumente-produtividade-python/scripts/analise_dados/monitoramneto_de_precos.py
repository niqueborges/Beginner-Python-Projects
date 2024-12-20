import time
import smtplib
import requests

# URL do preço das ações da Tesla
url = "https://finance.yahoo.com./quote/TSLA/"

# Preço-alvo para monitorar
target_price = 800

# Detalhes da conta de e-mail
email_addres = "sender@example.com"
email_password = "password"
to_email = "receiver@example.com"

