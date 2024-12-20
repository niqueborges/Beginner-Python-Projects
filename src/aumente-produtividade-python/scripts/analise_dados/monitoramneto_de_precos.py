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

# Função para enviar alerta por e-mail

def send_email(subject, body):
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_addres, email_password)
    message = f"Subject: {subject}\n\n{body}"
    smtp.sendmail(email_addres, to_email, message)
    smtp.quit()
    


