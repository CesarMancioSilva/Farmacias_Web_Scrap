import requests
import json
import os
import pandas as pd
from datetime import datetime
from scripts.categories import GetCategories
from scripts.farmacias import getFarmacias
from scripts.transform import transform_save_csv
from scripts.consolidate import GatherFiles
from dotenv import load_dotenv


all_csv_path=[]
def ExecuteScrapper():
    farmacias = getFarmacias()
    api_key = os.getenv("URL_PAGE_PART")
    for farmacia in farmacias:
        url_categories = GetCategories(farmacia)
        for category in url_categories:
            try:
                url_get = f"{api_key}/{farmacia['id']}/catalog-category/{url_categories[category]}?items_page=1&items_size=20000"
                
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36','Accept': 'application/json',}
                
                response = requests.get(url_get, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    items = data['data']['categoryMenu']['itens'] 

                    farmacia_folder = farmacia['name']
                    if not os.path.exists(farmacia_folder):
                        os.makedirs(farmacia_folder)
                    
                    csv_filename = f"{category}.csv"
                    csv_path = os.path.join(farmacia_folder, csv_filename)
                    
                    transform_save_csv(csv_path,items,category,farmacia['name'])
                    all_csv_path.append(csv_path)
                else:
                    print(f"Erro na requisição. Status: {response.status_code}")
                    print("Resposta:", response.text)
                    
            except requests.exceptions.RequestException as e:
                print(f"Erro na requisição: {e}")
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar JSON: {e}")
            except KeyError as e:
                print(f"Campo não encontrado no JSON: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    load_dotenv()
    ExecuteScrapper()
    GatherFiles(all_csv_path)
