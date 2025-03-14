import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

sensor = 2
rua = sensor
caminho = f"Trafego/rua{rua}"

#(Get):
def buscaTrafego():
    trafego = requests.get(f'{link}{caminho}/.json')
    return trafego

trafego = buscaTrafego()
print(trafego)
print(trafego.text)