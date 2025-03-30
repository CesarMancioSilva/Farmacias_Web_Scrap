import requests
import json
import os

def GetCategories(farmacia):
    url_categories = os.getenv("URL_FARMACIA")
    try:

        url_category = f"{url_categories}/{farmacia['id']}/taxonomies"
        
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
        }
        # Fazendo a requisição GET
        response = requests.get(url_category, headers=headers)
            
        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Convertendo a resposta para JSON
            data = response.json()
            for element in data['data']['categories']:
                url_categories[element['name']]=element['id']
        else:
            print(f"Erro na requisição. Código de status: {response.status_code}")
            print("Resposta:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")

    return url_categories
        
