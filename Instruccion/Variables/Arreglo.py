from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class Arreglo(Instruccion):

    def __init__(self, arreglo, listaIndice, valor, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.arreglo = arreglo
        self.listaIndice = listaIndice
        self.valor = valor
    
    def exec(self, ambito):
        #Ahora la recursividad
        copiaListita = self.listaIndice[:]
        copiaArreglo = self.arreglo
        self.ejecutar(ambito, copiaArreglo , copiaListita)

    def ejecutar(self, ambito, arreglito, listita):
        # Obtenemos el primer indice de la lista
        index = listita.pop(0).exec(ambito)
        variable = arreglito.exec(ambito)
        valor = self.valor.exec(ambito)
        if variable.tipo != Tipo.ARRAY:
            print("Error Semantico: la variable no es de tipo ARRAY, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: la variable no es de tipo ARRAY, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: la variable no es de tipo ARRAY", self.linea, self.columna))
            return Return(0, None)
        elif index.tipo != Tipo.INT:
            print("Error Semantico: el indice de la lista no es de tipo INT64, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el indice de la lista no es de tipo INT64, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el indice de la lista no es de tipo INT64", self.linea, self.columna))
            return Return(0, None)
        elif index.val > len(variable.val) or index.val < 0:
            print("Error Semantico: el indice '" + str(index.val) + "' de la lista no existe, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el indice '" + str(index.val) + "' de la lista no existe, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el indice '" + str(index.val) + "' de la lista no existe", self.linea, self.columna))
            return Return(0, None)
        if len(listita) <= 0:
            variable.val[index.val-1] = valor
        else:
            arreglito = variable.val[index.val-1]
            self.ejecutar(ambito, arreglito, listita)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="ASIGNACION_ARRAY"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreVal = "Nodo" + str(Salida.num)
        Salida.graph += nombreVal + '[label="ARRAY"];\n'
        Salida.graph += nombreLit + '->' + nombreVal + ';\n'
        Salida.num += 1
        self.arreglo.graph(nombreVal)
        nombreLista = "Nodo" + str(Salida.num)
        Salida.graph += nombreLista + '[label="LISTA_INDICES"];\n'
        Salida.graph += nombreLit + '->' + nombreLista + ';\n'
        Salida.num += 1
        for indice in self.listaIndice:
            indice.graph(nombreLista)
        nombreigual = "Nodo" + str(Salida.num)
        Salida.graph += nombreigual + '[label="="];\n'
        Salida.graph += nombreLit + '->' + nombreigual + ';\n'
        Salida.num += 1
        self.valor.graph(nombreLit)
