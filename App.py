import requests
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for
from Keys import link

app = Flask(__name__)

@app.route('/temperatura', methods=['POST'])
def temperatura():
    if request.method == 'POST':
        data = request.get_json()
        print("Dados recebidos:", data)

        if not isinstance(data, dict):
            return jsonify({'error': 'Formato de dados inválido. Esperado um objeto JSON.'}), 400

        
    return jsonify({'error': 'Método não permitido.'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)