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
    backup_file_path = backup_folder / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    shutil.copy(file_path, backup_file_path)
    
    # Upload do arquivo de backup em uma pasta do sharepoint
    sharepoint_url = "https://<company_name>.sharepoint.com/sites/site_name>/Shared%20Documents/backups"
    file_name = backup_file_path.name
    with open(backup_file_path, "rb") as f:
        requests.put(f"{sharepoint_url}/{file_name}", data=f)
        
    # Agendar o backup para rodar em uma data e horários específicos
    schedule.every().monday.at("09:00").do(backup_and_upload)
    schedule.every().wednesday.at("09:00").do(backup_and_upload)
    schedule.every().friday.at("09:00").do(backup_and_upload)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    
