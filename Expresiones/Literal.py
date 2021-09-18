from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class Literal(Expresion):

    def __init__(self, val, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.val = val
        self.tipo = tipo
    
    def exec(self, ambito):
        if self.tipo == Tipo.ARRAY:
            arreglito = self.val[:]
            for i in range(len(arreglito)):
                arreglito[i] = arreglito[i].exec(ambito)
            return Return(arreglito, self.tipo)

        return Return(self.val, self.tipo)

    def graph(self, padre):
        if self.tipo == Tipo.ARRAY:
            nombreLista = "Nodo" + str(Salida.num)
            Salida.graph += nombreLista + '[label="LISTA_VALORES"];\n'
            Salida.graph += padre + '->' + nombreLista + ';\n'
            Salida.num += 1
            for valor in self.val:
                valor.graph(nombreLista)
        elif self.tipo == Tipo.STRING or self.tipo == Tipo.CHAR:
            nombreLit = "Nodo" + str(Salida.num)
            Salida.graph += nombreLit + '[label="\'' + str(self.val) + '\'"];\n'
            Salida.graph += padre + '->' + nombreLit + ';\n'
            Salida.num += 1
        else:
            nombreLit = "Nodo" + str(Salida.num)
            Salida.graph += nombreLit + '[label="' + str(self.val) + '"];\n'
            Salida.graph += padre + '->' + nombreLit + ';\n'
            Salida.num += 1

