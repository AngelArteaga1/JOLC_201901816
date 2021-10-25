from Gramatica.grammar import parse
from Simbolo.AmbitoCompilador import *
from Export import Salida
from Simbolo.Generador import Generador

Salida.init()
ambitoGlobal = AmbitoCompilador(None, "Global")
f = open("./input.jl", "r")
input = f.read()
Salida.ast = parse(input)

genAux = Generador()
genAux.clean()
generador = genAux.getInstance()

for instr in Salida.ast:
    instr.compile(ambitoGlobal)
f = open("compilado.go", "w")
f.write(generador.getCodigo())
f.close()

print("Se compilo la solucion correctamente :)")

'''for instr in Salida.ast:
    returnST = instr.exec(ambitoGlobal)
    if returnST != None:
        if returnST.tipo == Tipo.RETURNST:
            print("""Error Semantico: el return esta afuera de una funcion, 
            linea: """ + str(instr.linea) + " columna: " + str(instr.columna))
'''