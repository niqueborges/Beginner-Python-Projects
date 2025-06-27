import os
from dotenv import load_dotenv

# Carrega o .env antes de definir as variáveis
env_file = os.getenv('ENV_FILE', '.env.dev')
load_dotenv(env_file)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecret')
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

def get_config():
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    return DevelopmentConfig()

