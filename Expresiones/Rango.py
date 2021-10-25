from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class Rango(Expresion):

    def __init__(self, minimo, maximo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.minimo = minimo
        self.maximo = maximo

    def exec(self, ambito):
        min = self.minimo.exec(ambito)
        max = self.maximo.exec(ambito)
        if not(min.tipo == Tipo.INT or max.tipo == Tipo.INT
        or min.tipo == Tipo.BEGIN or max.tipo == Tipo.END):
            print("Error Semantico: el valor del rango no es te tipo INT64, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor del rango no es te tipo INT64, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor del rango no es te tipo INT64", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        elif min.tipo == Tipo.END and max.tipo == Tipo.BEGIN:
            print("Error Semantico: el valor minimo del rango es mayor que el maximo, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor minimo del rango es mayor que el maximo, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor minimo del rango es mayor que el maximo", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        elif (min.val > max.val and min.tipo != Tipo.BEGIN
        and min.tipo != Tipo.END and max.tipo != Tipo.BEGIN 
        and min.tipo != Tipo.END):
            print("Error Semantico: el valor minimo del rango es mayor que el maximo, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor minimo del rango es mayor que el maximo, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor minimo del rango es mayor que el maximo", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        else:
            return Return(Rango(min, max, self.linea, self.columna ), Tipo.RANGE)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label=":"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.minimo.graph(nombreLit)
        self.maximo.graph(nombreLit)

    def compile(self, ambito):
        print("hola")