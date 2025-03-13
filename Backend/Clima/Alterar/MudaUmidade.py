import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from Keys import link

caminho = "Clima/umidade"
umidade = {'umidade': '35'}

#(Pach):
def mudaTemperatura(link, caminho, graus):
    temperatura = requests.patch(f'{link}/{caminho}/.json', data=json.dumps(graus))
    
    return temperatura

temperatura = mudaTemperatura(link, caminho, graus)

print(temperatura)
print(temperatura.text)