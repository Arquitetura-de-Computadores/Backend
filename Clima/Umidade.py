import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

#(Get):
def buscaUmidade():
    caminho = "Clima/umidade"
    umidade = requests.get(f'{link}{caminho}/.json')
    return umidade.json()

umidade = buscaUmidade()
