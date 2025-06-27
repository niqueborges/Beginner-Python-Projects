import os
from dotenv import load_dotenv
from config import get_config

env_file = os.getenv('ENV_FILE', '.env.dev')
print(f"Carregando arquivo de ambiente: {env_file}")

load_dotenv(env_file)

# Agora imprima para ver se foram carregadas
print("Variáveis ambiente após load_dotenv:")
print(f"FLASK_ENV = {os.getenv('FLASK_ENV')}")
print(f"DATABASE_URL = {os.getenv('DATABASE_URL')}")
print(f"DEBUG = {os.getenv('DEBUG')}")
print(f"SECRET_KEY = {os.getenv('SECRET_KEY')}")

config = get_config()

def main():
    print(f"Ambiente do config.py: {os.getenv('FLASK_ENV')}")
    print(f"DEBUG do config.py: {config.DEBUG}")
    print(f"DATABASE_URI do config.py: {config.DATABASE_URI}")
    print(f"SECRET_KEY do config.py: {config.SECRET_KEY}")

if __name__ == "__main__":
    main()
