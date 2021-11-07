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
        if ambito.continueLbl == '':
            print("Continue fuera de ciclo")
            return
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addGoto(ambito.continueLbl)