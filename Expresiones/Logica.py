from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida

class Logica(Expresion):
    
    def __init__(self, left, right, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.left = left
        self.right = right
        self.tipo = tipo

    def exec(self, ambito):
        valLeft = self.left.exec(ambito)
        valRight = self.right.exec(ambito)

        #Verificamos si ambos tipos son booleanos
        if valLeft.tipo != Tipo.BOOLEAN or valRight.tipo != Tipo.BOOLEAN:
            print("Error Semantico: No es posible realizar la operacion logica entre '" + str(valLeft.tipo) + "' y '" + str(valRight.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: No es posible realizar la operacion logica entre '" + str(valLeft.tipo) + "' y '" + str(valRight.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: No es posible realizar la operacion logica entre '" + str(valLeft.tipo) + "' y '" + str(valRight.tipo) + "'", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)

        resultado = Return(False, Tipo.BOOLEAN)
        if self.tipo == OpLogica.AND:
            resultado.val = valLeft.val and valRight.val
        if self.tipo == OpLogica.OR:
            resultado.val = valLeft.val or valRight.val
        if self.tipo == OpLogica.NOT:
            resultado.val = not valLeft.val
        
        return resultado

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        if self.tipo == OpLogica.AND:
            Salida.graph += nombreLit + '[label="&&"];\n'
        if self.tipo == OpLogica.OR:
            Salida.graph += nombreLit + '[label="||"];\n'
        if self.tipo == OpLogica.NOT:
            Salida.graph += nombreLit + '[label="!"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.left.graph(nombreLit)
        if self.tipo != OpLogica.NOT: self.right.graph(nombreLit)