from flask import Flask, jsonify
from flask_cors import CORS
from Keys import link
from Clima.Temperatura import buscaTemperatura
from Clima.Umidade import buscaUmidade
from Luzes.Luzes import buscaLuz
from Trafego.Trafego import buscaTrafego, carregar_mapeamento_ruas
from Coleta.Coleta import buscaColeta, carregar_mapeamento_coleta

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

@app.route('/trafego', methods=['GET'])
def get_trafego():
    trafego = buscaTrafego()
    
    if not trafego:
        return jsonify({'error': 'Tráfego não disponível.'}), 400

    mapeamento_ruas = carregar_mapeamento_ruas()

    ruas_formatadas = []
    for chave_rua, dados_rua in trafego.items():
        if 'id' not in dados_rua:
            print(f"Erro: ID ausente na rua {chave_rua}")
            continue

        rua_id = str(dados_rua['id'])
        rua_info = mapeamento_ruas.get(rua_id)

        if rua_info:
            ruas_formatadas.append({
                "label": f"{rua_info['rua']}, {rua_info['bairro']}",
                "status": dados_rua['status']
            })
        else:
            print(f"ID {rua_id} não encontrado no mapeamento.")
            ruas_formatadas.append({
                "label": "Rua desconhecida",
                "status": dados_rua['status']
            })

    return jsonify({'trafego': ruas_formatadas})

@app.route('/coleta', methods=['GET'])
def get_coleta():
    coletas = buscaColeta()
    
    if not coletas:
        return jsonify({'error': 'Coleta não disponível.'}), 400

    mapeamento_coletas = carregar_mapeamento_coleta()

    coletas_formatadas = []
    for chave_coleta, dados_coleta in coletas.items():
        if 'id' not in dados_coleta:
            print(f"Erro: ID ausente na coleta {chave_coleta}")
            continue

        coleta_id = str(dados_coleta['id'])
        coleta_info = mapeamento_coletas.get(coleta_id)

        if coleta_info:
            coletas_formatadas.append({
                "label": f"{coleta_info['rua']}, {coleta_info['bairro']}",
                "status": dados_coleta['status'],
                "peso": dados_coleta['peso']
            })
        else:
            print(f"ID {coleta_id} não encontrado no mapeamento.")
            coletas_formatadas.append({
                "label": "Coleta desconhecida",
                "status": dados_coleta['status'],
                "peso": dados_coleta['peso']
            })

    return jsonify({'coletas': coletas_formatadas})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)