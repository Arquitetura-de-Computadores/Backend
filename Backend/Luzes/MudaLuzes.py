import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Keys import link

caminho = "Luzes"
condicao = {'luz': True}

#(Pach):
def mudaLuz(link, caminho, condicao):
    condicaoLuz = requests.patch(f'{link}/{caminho}/.json', data=json.dumps(condicao))
    
    return condicaoLuz

condicaoLuz = mudaLuz(link, caminho, condicao)
print(mudaLuz(link, caminho, condicao))
print(condicaoLuz.text)

#(Get):
def buscaLuz():
    condicaoLuz = requests.get(f'{link}/.json')
    return condicaoLuz

print(condicaoLuz)
print(condicaoLuz.text)