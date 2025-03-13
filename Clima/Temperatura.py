import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = "Clima/temperatura"

#(Get):
def buscaTemperatura():
    temperatura = requests.get(f'{link}{caminho}/.json')
    return temperatura

temperatura = buscaTemperatura()
print(temperatura)
print(temperatura.text)