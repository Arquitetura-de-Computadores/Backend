import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = f"Trafego/"

def carregar_mapeamento_ruas():
    with open('mapeamento_ruas.json', 'r') as file:
        return json.load(file)

#(Get):
def buscaTrafego():
    try:
        response = requests.get(f'{link}{caminho}.json')
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            print(f"Erro: Dados inesperados no tráfego: {data}")
            return {}
        
        return data

    except requests.RequestException as e:
        print(f"Erro ao buscar tráfego: {e}")
        return {}
