from Abstracto.Expresion import *
from Abstracto.Return import *
from Expresiones.ResultadoTipo import *
from Export import Salida

class Aritmetica(Expresion):
    
    def __init__(self, left, right, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.left = left
        self.right = right
        self.tipo = tipo
    
    def exec(self, ambito):
        valLeft = self.left.exec(ambito)
        valRight = self.right.exec(ambito)

        resultado = Return(0, Tipo.INT)

        #Obtenemos el tipo del resultado y si hubo algun error retornamos
        resultado.tipo = getTipo(valLeft.tipo, valRight.tipo, self.tipo, self.linea, self.columna)
        if resultado.tipo == Tipo.NOTHING:
            return resultado
        
        if self.tipo == OpAritmetico.PLUS:
            resultado.val = valLeft.val + valRight.val
        elif self.tipo == OpAritmetico.MINUS:
            resultado.val = valLeft.val - valRight.val
        elif self.tipo == OpAritmetico.TIMES:
            if valLeft.tipo == Tipo.STRING and valRight.tipo == Tipo.STRING:
                resultado.val = valLeft.val + valRight.val
            else:
                resultado.val = valLeft.val * valRight.val
        elif self.tipo == OpAritmetico.DIV:
            resultado.val = valLeft.val / valRight.val
        elif self.tipo == OpAritmetico.MOD:
            resultado.val = valLeft.val % valRight.val
        elif self.tipo == OpAritmetico.POW:
            if(valLeft.tipo == Tipo.STRING and valRight.tipo == Tipo.INT):
                result = ""
                for i in range(valRight.val):
                    result += valLeft.val
                resultado.val = result
            else:
                resultado.val = pow(valLeft.val, valRight.val)
        
        return resultado
    

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        if self.tipo == OpAritmetico.PLUS:
            Salida.graph += nombreLit + '[label="+"];\n'
        if self.tipo == OpAritmetico.MINUS:
            Salida.graph += nombreLit + '[label="-"];\n'
        if self.tipo == OpAritmetico.TIMES:
            Salida.graph += nombreLit + '[label="*"];\n'
        if self.tipo == OpAritmetico.DIV:
            Salida.graph += nombreLit + '[label="/"];\n'
        if self.tipo == OpAritmetico.MOD:
            Salida.graph += nombreLit + '[label="%"];\n'
        if self.tipo == OpAritmetico.POW:
            Salida.graph += nombreLit + '[label="^"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.left.graph(nombreLit)
        self.right.graph(nombreLit)