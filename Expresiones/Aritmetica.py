from Abstracto.Expresion import *
from Abstracto.Return import *
from Expresiones.ResultadoTipo import *
from Export import Salida
from Simbolo.Generador import Generador

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

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        leftValue = self.left.compile(ambito)
        rightValue = self.right.compile(ambito)

        temp = generador.addTemp()
        op = ''
        resultadoTipo = getTipo(leftValue.tipo, rightValue.tipo, self.tipo, self.linea, self.columna)
        if resultadoTipo == Tipo.NOTHING:
            ReturnCompilador('0', resultadoTipo, False)
        if(self.tipo == OpAritmetico.PLUS):
            op = '+'
        elif(self.tipo == OpAritmetico.MINUS):
            op = '-'
        elif(self.tipo == OpAritmetico.TIMES):
            if leftValue.tipo == Tipo.STRING and rightValue.tipo == Tipo.STRING:
                generador.fConcatenar()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, leftValue.val)
                
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, rightValue.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('concatenar')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, resultadoTipo, True)
            else:
                op = '*'
        elif(self.tipo == OpAritmetico.DIV):
            op = '/'
            errorLbl = generador.newLabel()
            returnLbl = generador.newLabel()
            tempR = generador.addTemp()
            generador.addExp(tempR,rightValue.val,'','')
            generador.addIf(tempR,'0','==',errorLbl)
            generador.addExp(temp, leftValue.val, tempR, op)
            generador.addGoto(returnLbl)
            
            generador.putLabel(errorLbl)
            generador.addExp(temp,'0','','')
            generador.addError("Error Semantico: No es posible dividir entre 0, linea: " + str(self.linea) + " columna: " + str(self.columna))
            
            generador.putLabel(returnLbl)
            return ReturnCompilador(temp, resultadoTipo, True)
            
        elif(self.tipo == OpAritmetico.MOD):
            if not generador.math:
                generador.addMath()
            generador.addExpMod(temp, leftValue.val, rightValue.val)
            return ReturnCompilador(temp, resultadoTipo, True)
        if (self.tipo == OpAritmetico.POW):
            if leftValue.tipo == Tipo.STRING and rightValue.tipo == Tipo.INT:
                generador.fPotenciaStringLeft()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, leftValue.val)
                
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, rightValue.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('potenciaLeft')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, resultadoTipo, True)
            else:
                generador.fPotencia()
                paramTemp = generador.addTemp()

                generador.addExp(paramTemp, 'P', ambito.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, leftValue.val)
                
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, rightValue.val)
                
                generador.newEnv(ambito.size)
                generador.callFun('potencia')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(ambito.size)

                return ReturnCompilador(temp, resultadoTipo, True)
        else:
            generador.addExp(temp, leftValue.val, rightValue.val, op)
            return ReturnCompilador(temp, resultadoTipo, True)