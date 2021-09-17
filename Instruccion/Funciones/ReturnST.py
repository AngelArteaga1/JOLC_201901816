from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class ReturnST(Expresion):

    def __init__(self, expresion, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expresion = expresion
    
    def exec(self, ambito):
        try:
            value = self.expresion.exec(ambito)
            return Return(value, Tipo.RETURNST)
        except:
            print("Error en Return")
            Salida.salida += "Error en Return, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error en Return", self.linea, self.columna))

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="RETURN"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.expresion.graph(nombreLit)