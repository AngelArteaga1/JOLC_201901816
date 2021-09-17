from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class Asignar(Instruccion):

    def __init__(self, id, valor, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.valor = valor
    
    def exec(self, ambito):
        # verificamos si es 
        variable = self.id.exec(ambito)
        valor = self.valor.exec(ambito)
        variable.val = valor.val

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="ASIGNACION"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.id.graph(nombreLit)
        nombreigual = "Nodo" + str(Salida.num)
        Salida.graph += nombreigual + '[label="="];\n'
        Salida.graph += nombreLit + '->' + nombreigual + ';\n'
        Salida.num += 1
        self.valor.graph(nombreLit)