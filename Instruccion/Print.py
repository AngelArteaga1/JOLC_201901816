from Abstracto.Instruccion import *
from Export import Salida

class Print(Instruccion):

    def __init__(self, listaVal, linea, columna, nuevaLinea):
        Instruccion.__init__(self, linea, columna)
        self.listaVal = listaVal
        self.nuevaLinea = nuevaLinea
    
    def exec(self, ambito):
        imprimir = ""
        for val in self.listaVal:   
            valor = val.exec(ambito)
            if valor.tipo == None:
                return
            elif valor.tipo == Tipo.ARRAY:
                imprimir += str(self.arrayToString(valor))
                continue
            elif valor.tipo == Tipo.STRUCT:
                imprimir += str(self.structToString(valor))
                continue
            elif valor.tipo == Tipo.NOTHING:
                imprimir += "Nothing"
                continue
            imprimir += str(valor.val)
        if self.nuevaLinea:
            print(imprimir)
            Salida.salida += imprimir + "\n"
        else:
            print(imprimir, end="")
            Salida.salida += imprimir

    def structToString(self, valor):
        struct = {}
        for item in valor.val:
            if valor.val[item].tipo == Tipo.STRUCT:
                struct[item] = self.structToString(valor.val[item])
                continue
            elif valor.val[item].tipo == Tipo.ARRAY:
                struct[item] = self.arrayToString(valor.val[item])
                continue
            struct[item] = valor.val[item].val
        return struct

    def arrayToString(self, valor):
        array = []
        for item in valor.val:
            if item.tipo == Tipo.ARRAY:
                array.append(self.arrayToString(item))
                continue
            elif item.tipo == Tipo.STRUCT:
                array.append(self.structToString(item))
                continue
            array.append(item.val)
        return array

    def graph(self, padre):
        nombrePrint = "Nodo" + str(Salida.num)
        if self.nuevaLinea: 
            Salida.graph += nombrePrint + '[label="PRINTLN"];\n'
        else:
            Salida.graph += nombrePrint + '[label="PRINT"];\n'
        Salida.graph += padre + '->' + nombrePrint + ';\n'
        Salida.num += 1
        nombreLista = "Nodo" + str(Salida.num)
        Salida.graph += nombreLista + '[label="LISTA_VALORES"];\n'
        Salida.graph += nombrePrint + '->' + nombreLista + ';\n'
        Salida.num += 1
        for val in self.listaVal:
            val.graph(nombreLista)