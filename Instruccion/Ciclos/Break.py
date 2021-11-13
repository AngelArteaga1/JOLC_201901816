from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida
from Simbolo.Generador import Generador

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
        genAux = Generador()
        generador = genAux.getInstance()
        if ambito.breakLbl == '':
            generador.addError("Error Semantico: break fuera de funcion, linea: " + str(self.linea) + " columna: " + str(self.columna))
            return

        generador.addGoto(ambito.breakLbl)