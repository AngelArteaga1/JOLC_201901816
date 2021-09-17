from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class Acceso(Expresion):

    def __init__(self, id, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id

    def exec(self, ambito):
        valor = ambito.getVar(self.id)
        if valor == None:
            print("Error Semantico: la variable '" + str(self.id) + "' no existe, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: la variable '" + str(self.id) + "' no existe, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: la variable '" + str(self.id) + "' no existe", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        elif valor.tipo == Tipo.STRUCT:
            return Return(valor.atributos, valor.tipo, valor.objeto)
        return Return(valor.val, valor.tipo)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="' + str(self.id) + '"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1