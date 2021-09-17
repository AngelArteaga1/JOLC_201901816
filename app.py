from flask import Flask, request, render_template

from Gramatica import grammar
from Export import Salida
from Simbolo.Ambito import *

app = Flask(__name__)

@app.route("/exec", methods=['POST'])
def home():
    try:
        Salida.init()
        input = request.json['input']

        f = open("exec.txt", "w")
        f.write(input)
        f.close()
        
        nuevoAmbito = Ambito(None)
        Salida.ast = grammar.parse(input)
        try:
            for instr in Salida.ast:
                instr.exec(nuevoAmbito)
        except:
            print("Error al ejecutar instrucciones")
            Salida.salida += "Error al ejecutar instrucciones" + "\n"
        
        return { 'msg': Salida.salida, 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/graph", methods=['GET'])
def graph():
    try:
        Salida.init()
        f = open("exec.txt", "r")
        input = f.read()
        
        Salida.ast = grammar.parse(input)
        #Vamos a graficar el inicio
        Salida.graph += "digraph G\n{\n"
        Salida.graph += 'node[shape="box", style=filled fillcolor="#990033", fontcolor=white]'
        nombrePadre = "Nodo" + str(Salida.num)
        Salida.graph += nombrePadre + '[label="RAIZ"];\n'
        Salida.num += 1
        try:
            for instr in Salida.ast:
                instr.graph(nombrePadre)
            Salida.graph += "}"
        except:
            print("Error al generar arbol")
            Salida.graph += "Error al generar arbol" + "\n"
        return { 'msg': Salida.graph, 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

@app.route("/prueba", methods=['GET'])
def home_prueba():
    f = open("dotito.txt", "w")
    f.write("pepe")
    f.close()
    f = open("./dotito.txt", "r")
    input = f.read()
    return input

@app.route("/editor", methods=['GET'])
def home_editor():
    return render_template('editor.html')

@app.route("/tree", methods=['GET'])
def home_tree():
    return render_template('tree.html')

if __name__ == '__main__':
    app.run()