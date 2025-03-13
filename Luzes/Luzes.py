import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = "Luzes"
condicao = {'luz': True}

#(Get):
def buscaLuz():
    condicaoLuz = requests.get(f'{link}{caminho}/.json')
    return condicaoLuz

condicaoLuz = buscaLuz()

print(condicaoLuz)
print(condicaoLuz.text)