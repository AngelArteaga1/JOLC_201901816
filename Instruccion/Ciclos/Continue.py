from Abstracto.Instruccion import *
from Abstracto.Return import *
from Simbolo.Generador import Generador

class Continue(Instruccion):

    def __init__(self, linea, columna):
        Instruccion.__init__(self, linea, columna)
    
    def exec(self, ambito):
        return Return(None, Tipo.CONTINUEST)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="CONTINUE"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        if ambito.continueLbl == '':
            generador.addError("Error Semantico: continue fuera de funcion, linea: " + str(self.linea) + " columna: " + str(self.columna))
            return

        generador.addGoto(ambito.continueLbl)