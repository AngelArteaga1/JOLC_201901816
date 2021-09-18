from Gramatica.grammar import parse
from Simbolo.Ambito import *
from Export import Salida

Salida.init()
ambitoGlobal = Ambito(None, "Global")
f = open("./input.jl", "r")
input = f.read()
Salida.ast = parse(input)

for instr in Salida.ast:
    returnST = instr.exec(ambitoGlobal)
    if returnST != None:
        if returnST.tipo == Tipo.RETURNST:
            print("""Error Semantico: el return esta afuera de una funcion, 
            linea: """ + str(instr.linea) + " columna: " + str(instr.columna))

'''#Vamos a graficar el inicio
Salida.graph += "digraph G\n{\n"
Salida.graph += 'node[shape="box"];\n'
nombrePadre = "Nodo" + str(Salida.num)
Salida.graph += nombrePadre + '[label="RAIZ"];\n'
Salida.num += 1
for instr in Salida.ast:
    instr.graph(nombrePadre)
Salida.graph += "}"

f = open("dotito.txt", "w")
f.write(Salida.graph)
f.close()'''