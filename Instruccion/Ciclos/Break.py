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
        if ambito.breakLbl == '':
            print("Break fuera de ciclo")
            return
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addGoto(ambito.breakLbl)