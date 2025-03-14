from flask import Flask, jsonify
from flask_cors import CORS
from Keys import link
from Clima.Temperatura import buscaTemperatura
from Clima.Umidade import buscaUmidade
from Luzes.Luzes import buscaLuz
from Trafego.Trafego import buscaTrafego

app = Flask(__name__)
CORS(app)

@app.route('/temperatura', methods=['GET'])
def get_temperatura():
    temperatura = buscaTemperatura()
    
    if temperatura is None:
        return jsonify({'error': 'Temperatura não disponível.'}), 400

    return jsonify({'temperatura': temperatura})

@app.route('/umidade', methods=['GET'])
def get_umidade():
    umidade = buscaUmidade()
    
    if umidade is None:
        return jsonify({'error': 'Umidade não disponível.'}), 400

    return jsonify({'umidade': umidade})

@app.route('/luz', methods=['GET'])
def get_luz():
    luz = buscaLuz()
    
    if luz is None:
        return jsonify({'error': 'Luz não disponível.'}), 400

    return jsonify({'luz': luz})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)