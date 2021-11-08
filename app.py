from flask import Flask, request, render_template
import json

from Gramatica import grammar
from Export import Salida
from Simbolo.Ambito import *
from Simbolo.AmbitoCompilador import AmbitoCompilador
from Simbolo.Generador import Generador

app = Flask(__name__)

@app.route("/exec", methods=['POST'])
def home():
    try:
        Salida.init()
        input = request.json['input']

        f = open("exec.txt", "w")
        f.write(input)
        f.close()
        
        nuevoAmbito = Ambito(None, "Global")
        Salida.ast = grammar.parse(input)
        try:
            for instr in Salida.ast:
                instr.exec(nuevoAmbito)
        except:
            print("Error al ejecutar instrucciones")
            Salida.salida += "Error al ejecutar instrucciones" + "\n"
            Salida.errores.append(Error("Error al ejecutar instrucciones", 0, 0))
        
        return { 'msg': Salida.salida, 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/compile", methods=['POST'])
def compile():
    try:
        Salida.init()
        input = request.json['input']

        f = open("exec.txt", "w")
        f.write(input)
        f.close()

        genAux = Generador()
        genAux.clean()
        generador = genAux.getInstance()
        
        nuevoAmbito = AmbitoCompilador(None, "Global")
        Salida.ast = grammar.parse(input)
        try:
            for instr in Salida.ast:
                instr.compile(nuevoAmbito)
        except:
            print("Error al compilar instrucciones")
            Salida.errores.append(Error("Error al ejecutar instrucciones", 0, 0))
        
        return { 'msg': generador.getCodigo(), 'code': 200 }
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

@app.route("/getErrors", methods=['GET'])
def errors():
    try:
        Salida.init()
        f = open("exec.txt", "r")
        input = f.read()
        
        Salida.ast = grammar.parse(input)
        
        nuevoAmbito = Ambito(None, "Global")
        Salida.ast = grammar.parse(input)
        try:
            for instr in Salida.ast:
                instr.exec(nuevoAmbito)
        except:
            print("Error al ejecutar instrucciones")
            Salida.salida += "Error al ejecutar instrucciones" + "\n"
            Salida.errores.append(Error("Error al ejecutar instrucciones", 0, 0))
        # Pasamos la lista a diccionario
        listita = []
        for i in Salida.errores:
            obj = {}
            obj["descripcion"] = i.descripcion
            obj["linea"] = i.linea
            obj["columna"] = i.columna
            listita.append(obj)
        return { 'msg': json.dumps(listita), 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/getSimbols", methods=['GET'])
def simbols():
    try:
        Salida.init()
        f = open("exec.txt", "r")
        input = f.read()
        
        Salida.ast = grammar.parse(input)
        
        nuevoAmbito = Ambito(None, "Global")
        Salida.ast = grammar.parse(input)
        try:
            for instr in Salida.ast:
                instr.exec(nuevoAmbito)
        except:
            print("Error al ejecutar instrucciones")
            Salida.salida += "Error al ejecutar instrucciones" + "\n"
            Salida.errores.append(Error("Error al ejecutar instrucciones", 0, 0))
        # Pasamos la lista a diccionario
        listita = []
        for i in Salida.simbolos:
            obj = {}
            obj["nombre"] = str(i.id)
            obj["tipo"] = str(i.tipo)
            obj["ambito"] = str(i.nombreAmbito)
            obj["linea"] = i.linea
            obj["columna"] = i.columa
            listita.append(obj)
        print(listita)
        return { 'msg': json.dumps(listita), 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

@app.route("/editor", methods=['GET'])
def home_editor():
    return render_template('editor.html')

@app.route("/tree", methods=['GET'])
def home_tree():
    return render_template('tree.html')

@app.route("/errors", methods=['GET'])
def home_errors():
    return render_template('errors.html')

@app.route("/simbols", methods=['GET'])
def home_simbols():
    return render_template('simbols.html')

if __name__ == '__main__':
    app.run()