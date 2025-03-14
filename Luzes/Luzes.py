import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

#(Get):
def buscaLuz():
    caminho = "Luzes/luz"
    condicaoLuz = requests.get(f'{link}{caminho}/.json')
    return condicaoLuz.json()

condicaoLuz = buscaLuz()
