from Abstracto.Expresion import *
from Abstracto.Return import *
from Expresiones.ResultadoTipo import *
from Export import Salida

class Relacional(Expresion):
    
    def __init__(self, left, right, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.left = left
        self.right = right
        self.tipo = tipo

    def exec(self, ambito):
        valLeft = self.left.exec(ambito)
        valRight = self.right.exec(ambito)

        #Si hubo algun error antes
        if valLeft.tipo == None or valRight.tipo == None:
            return Return(0, None)

        
        resultado = Return(False, Tipo.BOOLEAN)
            
        #Obtenemos el tipo del resultado y si hubo algun error retornamos
        resultado.tipo = getTipo(valLeft.tipo, valRight.tipo, self.tipo, self.linea, self.columna)
        if resultado.tipo == None:
            return resultado

        if self.tipo == OpRelacional.GREATER:
            resultado.val = valLeft.val > valRight.val
        elif self.tipo == OpRelacional.LESS:
            resultado.val = valLeft.val < valRight.val
        elif self.tipo == OpRelacional.GREATEREQUAL:
            resultado.val = valLeft.val >= valRight.val
        elif self.tipo == OpRelacional.LESSEQUAL:
            resultado.val = valLeft.val <= valRight.val
        elif self.tipo == OpRelacional.EQUALSEQUALS:
            resultado.val = valLeft.val == valRight.val
        elif self.tipo == OpRelacional.DISTINT:
            resultado.val = valLeft.val != valRight.val
        
        return resultado

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        if self.tipo == OpRelacional.GREATER:
            Salida.graph += nombreLit + '[label=">"];\n'
        if self.tipo == OpRelacional.LESS:
            Salida.graph += nombreLit + '[label="<"];\n'
        if self.tipo == OpRelacional.GREATEREQUAL:
            Salida.graph += nombreLit + '[label=">="];\n'
        if self.tipo == OpRelacional.LESSEQUAL:
            Salida.graph += nombreLit + '[label=">="];\n'
        if self.tipo == OpRelacional.EQUALSEQUALS:
            Salida.graph += nombreLit + '[label="=="];\n'
        if self.tipo == OpRelacional.DISTINT:
            Salida.graph += nombreLit + '[label="!="];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.left.graph(nombreLit)
        self.right.graph(nombreLit)