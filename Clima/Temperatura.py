import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

#(Get):
def buscaTemperatura():
    caminho = "Clima/temperatura"
    temperatura = requests.get(f'{link}{caminho}/.json')

    #Formata o temperatura para json
    return temperatura.json()

temperatura = buscaTemperatura()
