from flask import Flask, request, jsonify
from flask_cors import CORS

import Interprete.Gramatica as Gm
import json

from Figura import Figura

#import pyserial
import serial
import time

app = Flask(__name__)
CORS(app)  # Habilitar CORS para la aplicación Flask

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
    
    fig = figuras(matriz_recibido)
    
    for f in fig:
        temp = f.binario()
        sendserial(temp)

    return jsonify({'mensaje': 'Graficación terminada'})

def figuras(matriz_recibido):
    nfilas = 3
    ncolumnas = 3
    pointer = 0
    figuras = []

    for filas in range(1,nfilas+1):
        for columnas in range(1,ncolumnas+1):
            fmatriz = int(matriz_recibido[pointer]['pos']['fila'])
            cmatriz = int(matriz_recibido[pointer]['pos']['columna'])
            if fmatriz == filas and cmatriz == columnas:
                color = matriz_recibido[pointer]['color']
                figura = matriz_recibido[pointer]['figura']
                figuras.append(Figura(color=color, forma=figura, vacio=False))
                pointer = controlpointer(len(matriz_recibido), pointer)
            else:
                figuras.append(Figura(color=None, forma=None, vacio=True))

    return figuras

def controlpointer(limite, contador):
    if contador < limite - 1:
        return contador + 1
    return contador


def sendserial(cmd):
    ser = serial.Serial('COM5', 9600)
    time.sleep(10)  # Espera a que se establezca la conexión serial
    try:       
        ser.write(cmd.encode())
        print(cmd)
    finally:
        ser.close()


if __name__ == '__main__':
    # Ejecutar la aplicación Flask
    app.run(debug=True, port=4000)