from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class AccesoArray(Expresion):

    def __init__(self, id, expresion, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.expresion = expresion

    def exec(self, ambito):
        valor = self.id.exec(ambito)
        index = self.expresion.exec(ambito)
        if not(valor.tipo == Tipo.ARRAY or valor.tipo == Tipo.STRING):
            print("Error Semantico: el valor no es te tipo ARRAY o STRING, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor no es te tipo ARRAY o STRING, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor no es te tipo ARRAY o STRING", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        elif not(index.tipo == Tipo.INT or index.tipo == Tipo.RANGE):
            print("Error Semantico: el indice de la lista no es de tipo INT64 o RANGE, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el indice de la lista no es de tipo INT64 o RANGE, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el indice de la lista no es de tipo INT64 o RANGE", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        #Aqui ya devolvemos el valor
        if index.tipo == Tipo.INT:
            if index.val > len(valor.val) or index.val < 0:
                print("Error Semantico: el indice '" + str(index.val) + "' de la lista no existe, linea: " + str(self.linea) + " columna: " + str(self.columna))
                Salida.salida += "Error Semantico: el indice '" + str(index.val) + "' de la lista no existe, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                Salida.errores.append(Error("Error Semantico: el indice '" + str(index.val) + "' de la lista no existe", self.linea, self.columna))
                return Return("Nothing", Tipo.NOTHING)
            if valor.tipo == Tipo.ARRAY:
                return Return(valor.val[index.val-1].val, valor.val[index.val-1].tipo)
            else: 
                return Return(valor.val[index.val-1], Tipo.STRING)
        else:
            if index.val.minimo.tipo == Tipo.END: index.val.minimo.val = len(valor.val)-1
            if index.val.maximo.tipo == Tipo.END: index.val.maximo.val = len(valor.val)
            if index.val.minimo.tipo == Tipo.BEGIN: index.val.minimo.val = 0
            if index.val.maximo.tipo == Tipo.BEGIN: index.val.maximo.val = 1
            if valor.tipo == Tipo.ARRAY:
                return Return(valor.val[index.val.minimo.val:index.val.maximo.val], Tipo.ARRAY)
            else: 
                return Return(valor.val[index.val.minimo.val:index.val.maximo.val], Tipo.STRING)

    def graph(self, padre):
        nombreAcceso = "Nodo" + str(Salida.num)
        Salida.graph += nombreAcceso + '[label="ACCESO_ARRAY"];\n'
        Salida.graph += padre + '->' + nombreAcceso + ';\n'
        Salida.num += 1
        nombreValor = "Nodo" + str(Salida.num)
        Salida.graph += nombreValor + '[label="VALOR"];\n'
        Salida.graph += nombreAcceso + '->' + nombreValor + ';\n'
        Salida.num += 1
        nombreIndice = "Nodo" + str(Salida.num)
        Salida.graph += nombreIndice + '[label="INDICE"];\n'
        Salida.graph += nombreAcceso + '->' + nombreIndice + ';\n'
        Salida.num += 1
        self.id.graph(nombreValor)
        self.expresion.graph(nombreIndice)
