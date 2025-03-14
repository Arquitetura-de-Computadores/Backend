import requests
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from Keys import link
from Clima.Temperatura import buscaTemperatura
from Clima.Umidade import buscaUmidade
from Luzes.Luzes import buscaLuz
from Trafego.Trafego import buscaTrafego

app = Flask(__name__)
CORS(app)

@app.route('/temperatura', methods=['POST'])
def postTemperatura():

    #Faz uma requisição qualquer
    temperatura = request.get_json()
    temperatura = buscaTemperatura()

    if temperatura is None:
        print("Temperatura não fornecida.")
        return jsonify({'error': 'Temperatura não disponível.'}), 400

    print("Temperatura retornada:", temperatura)
    return jsonify({'temperatura': temperatura})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)