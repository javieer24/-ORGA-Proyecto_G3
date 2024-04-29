from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import Interprete.Gramatica as Gm
import json
import os

#import pyserial

app = Flask(__name__)
CORS(app)  # Habilitar CORS para la aplicación Flask

# Ruta para servir los archivos estáticos del frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path == "":
        return send_from_directory('../Frontend', 'Page.html')
    elif os.path.exists(os.path.join('../Frontend', path)):
        return send_from_directory('../Frontend', path)
    else:
        return send_from_directory('../Frontend', 'Page.html')

@app.route('/plotterserial/analizar', methods=['POST'])
def analizar():

    datos = request.json
    codigo_recibido = datos.get('texto', '')

    if codigo_recibido == '':
        return jsonify({'error': 'No se recibió código'})

    parse = Gm.parse(codigo_recibido)
    
    if not parse:
        return jsonify({
            'mensaje': 'Error en el análisis',
            'impresiones': []
        })
    
    sentencias = []
    for sent in parse:
        sentencias.append(json.dumps(sent.to_dict()))

    try:
        return jsonify({
            'mensaje': 'Análisis terminado',
            'impresiones': sentencias
        })

    except Exception as e:
        print(e)
        return jsonify({
            'mensaje': 'Error en el análisis',
            'impresiones': []
        })

@app.route('/plotterserial/graficar', methods=['POST'])
def graficar():

    datos = request.json
    matriz_recibido = datos.get('matriz', '')

    if not matriz_recibido:
        return jsonify({'error': 'No se recibió matriz'})
    

    for item in matriz_recibido:
        fila = item['pos']['fila']
        columna = item['pos']['columna']
        color = item['color']
        figura = item['figura']
        print(f"Fila: {fila}, Columna: {columna}, Color: {color}, Figura: {figura}")
        print("")

        # TODO: Implementar logica impresora con pyserial


    return jsonify({'mensaje': 'Graficación terminada'})

if __name__ == '__main__':

    # Ejecutar la aplicación Flask
    app.run(debug=True, port=4000)