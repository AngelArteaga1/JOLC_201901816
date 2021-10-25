from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class Break(Instruccion):

    def __init__(self, linea, columna):
        Instruccion.__init__(self, linea, columna)
    
    def exec(self, ambito):
        return Return(None, Tipo.BREAKST)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="BREAK"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1

    def compile(self, ambito):
        print("hola")