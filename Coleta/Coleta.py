import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = f"Coleta/"

def carregar_mapeamento_coleta():
    with open('mapeamento_coleta.json', 'r') as file:
        return json.load(file)

#(Get):
def buscaColeta():
    try:
        response = requests.get(f'{link}{caminho}.json')
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            print(f"Erro: Dados inesperados no coleta: {data}")
            return {}
        
        return data

    except requests.RequestException as e:
        print(f"Erro ao buscar coleta: {e}")
        return {}