import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = "Clima/umidade"

#(Get):
def buscaUmidade():
    umidade = requests.get(f'{link}{caminho}/.json')
    return umidade

umidade = buscaUmidade()
print(umidade)
print(umidade.text)