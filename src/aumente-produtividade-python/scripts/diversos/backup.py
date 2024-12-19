import pandas as pd
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import requests
import schedule
import time

def backup_and_upload():
    # Carregando os dados de um arquivo excel no Pandas dataframe
    file_path = "sales_data.xlsx"
    df = pd.read_excel(file_path)
    
    # Salvar backup dos dados em uma pasta local
    backup_folder = Path("backups")
    backup_folder.mkdir(exist_ok=True)
