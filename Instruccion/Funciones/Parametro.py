from Abstracto.Instruccion import *

class Parametro(Instruccion):

    def __init__(self, id, tipo, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.tipo = tipo
    
    def exec(self):
        return self

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="PARAMETRO"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        if self.tipo != None:
            nombreParam = "Nodo" + str(Salida.num)
            Salida.graph += nombreParam + '[label="' + str(self.tipo) + '"];\n'
            Salida.graph += nombreLit + '->' + nombreParam + ';\n'
            Salida.num += 1