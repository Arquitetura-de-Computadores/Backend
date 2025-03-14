import sys
import os
import requests
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from Keys import link

caminho = "Clima"
umidade = {'umidade': 12}

#(Pach):
def mudaTemperatura(link, caminho, umidade):
    temperatura = requests.patch(f'{link}/{caminho}/.json', data=json.dumps(umidade))
    
    return temperatura

temperatura = mudaTemperatura(link, caminho, umidade)

print(temperatura)
print(temperatura.text)