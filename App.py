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

@app.route('/umidade', methods=['POST'])
def postUmidade():

    #Faz uma requisição qualquer
    umidade = request.get_json()
    umidade = buscaUmidade()

    if umidade is None:
        print("Umidade não fornecida.")
        return jsonify({'error': 'Umidade não disponível.'}), 400

    print("Umidade retornada:", umidade)
    return jsonify({'umidade': umidade})

@app.route('/luz', methods=['POST'])
def postLuz():

    #Faz uma requisição qualquer
    luz = request.get_json()
    luz = buscaLuz()

    if luz is None:
        print("Luz não fornecida.")
        return jsonify({'error': 'Luz não disponível.'}), 400

    print("Luz retornada:", luz)
    return jsonify({'luz': luz})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)