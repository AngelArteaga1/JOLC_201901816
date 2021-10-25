from Abstracto.Expresion import *
from Abstracto.Return import *
from Expresiones.ResultadoTipo import *
from Export import Salida
from Simbolo.Generador import Generador

class Relacional(Expresion):
    
    def __init__(self, left, right, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.left = left
        self.right = right
        self.tipo = tipo

    def exec(self, ambito):
        valLeft = self.left.exec(ambito)
        valRight = self.right.exec(ambito)
        
        resultado = Return(False, Tipo.BOOLEAN)
            
        #Obtenemos el tipo del resultado y si hubo algun error retornamos
        resultado.tipo = getTipo(valLeft.tipo, valRight.tipo, self.tipo, self.linea, self.columna)
        if resultado.tipo == Tipo.NOTHING:
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

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("INICIO EXPRESION RELACIONAL")

        left = self.left.compile(ambito)
        right = None

        result = ReturnCompilador(None, Tipo.BOOLEAN, False)

        if left.tipo != Tipo.BOOLEAN:
            right = self.right.compile(ambito)
            if (left.tipo == Tipo.INT or left.tipo == Tipo.FLOAT) and (right.tipo == Tipo.INT or right.tipo == Tipo.FLOAT):
                self.checkLabels()
                generador.addIf(left.val, right.val, self.getOp(), self.trueLbl)
                generador.addGoto(self.falseLbl)
            elif left.tipo == Tipo.STRING and right.tipo == Tipo.STRING:
                # Únicamente se puede con igualdad o desigualdad
                self.checkLabels()


                if self.tipo == OpRelacional.EQUALSEQUALS:
                    generador.addComment('AQUI EMPIEZA LA COMPARACION DE CADENAS')
                    #Obtenemos la posicion del string uno y la almacenamos en una temporal
                    tempL = generador.addTemp()
                    posL = generador.addTemp()
                    generador.addExp(posL,left.val,'','')
                    #Obtenemos la posicion del string de la derecha
                    tempR = generador.addTemp()
                    posR = generador.addTemp()
                    generador.addExp(posR,right.val,'','')


                    #Generamos el label ciclo
                    ciclo = generador.newLabel()
                    confirmar = generador.newLabel()
                    generador.putLabel(ciclo)

                    #Obtenemos el heap
                    generador.getHeap(tempL, posL)
                    generador.getHeap(tempR, posR)

                    generador.addIf(tempL, tempR, '!=', self.falseLbl)
                    generador.addIf(tempL, '-1', '==', confirmar)
                    
                    #incrementamos
                    generador.addExp(posL, posL, '1', '+')
                    generador.addExp(posR, posR, '1', '+')
                    
                    #Volvemos al ciclo
                    generador.addGoto(ciclo)
                    
                    #Comprobamos si son iguales
                    generador.putLabel(confirmar)
                    generador.addIf(tempL, tempR, '==', self.trueLbl)
                    generador.addGoto(self.falseLbl)
                    generador.addComment('AQUI TERMINA LA COMPARACION DE CADENAS')
                    result.trueLbl = self.trueLbl
                    result.falseLbl = self.falseLbl

                    return result
                elif self.tipo == OpRelacional.DISTINT:
                    generador.addComment('AQUI EMPIEZA LA COMPARACION DE CADENAS')
                    #Obtenemos la posicion del string uno y la almacenamos en una temporal
                    tempL = generador.addTemp()
                    posL = generador.addTemp()
                    generador.addExp(posL,left.val,'','')
                    #Obtenemos la posicion del string de la derecha
                    tempR = generador.addTemp()
                    posR = generador.addTemp()
                    generador.addExp(posR,right.val,'','')


                    #Generamos el label ciclo
                    ciclo = generador.newLabel()
                    confirmar = generador.newLabel()
                    generador.putLabel(ciclo)

                    #Obtenemos el heap
                    generador.getHeap(tempL, posL)
                    generador.getHeap(tempR, posR)

                    generador.addIf(tempL, tempR, '!=', self.trueLbl)
                    generador.addIf(tempL, '-1', '==', confirmar)
                    
                    #incrementamos
                    generador.addExp(posL, posL, '1', '+')
                    generador.addExp(posR, posR, '1', '+')
                    
                    #Volvemos al ciclo
                    generador.addGoto(ciclo)
                    
                    #Comprobamos si son iguales
                    generador.putLabel(confirmar)
                    generador.addIf(tempL, tempR, '==', self.falseLbl)
                    generador.addGoto(self.falseLbl)
                    generador.addComment('AQUI TERMINA LA COMPARACION DE CADENAS')
                    result.trueLbl = self.trueLbl
                    result.falseLbl = self.falseLbl

                    return result
        else:
            gotoRight = generador.newLabel()
            leftTemp = generador.addTemp()

            generador.putLabel(left.trueLbl)
            generador.addExp(leftTemp, '1', '', '')
            generador.addGoto(gotoRight)

            generador.putLabel(left.falseLbl)
            generador.addExp(leftTemp, '0', '', '')

            generador.putLabel(gotoRight)

            right = self.right.compile(ambito)
            if right.tipo != Tipo.BOOLEAN:
                print("Error, no se pueden comparar")
                return ReturnCompilador(None, Tipo.NOTHING, False)
            gotoEnd = generador.newLabel()
            rightTemp = generador.addTemp()

            generador.putLabel(right.trueLbl)
            
            generador.addExp(rightTemp, '1', '', '')
            generador.addGoto(gotoEnd)

            generador.putLabel(right.falseLbl)
            generador.addExp(rightTemp, '0', '', '')

            generador.putLabel(gotoEnd)

            self.checkLabels()
            generador.addIf(leftTemp, rightTemp, self.getOp(), self.trueLbl)
            generador.addGoto(self.falseLbl)

        generador.addComment("FIN DE EXPRESION RELACIONAL")
        generador.addSpace()
        result.trueLbl = self.trueLbl
        result.falseLbl = self.falseLbl

        return result     
    
    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()

    def getOp(self):
        if self.tipo == OpRelacional.GREATER:
            return '>'
        elif self.tipo == OpRelacional.LESS:
            return '<'
        elif self.tipo == OpRelacional.GREATEREQUAL:
            return '>='
        elif self.tipo == OpRelacional.LESSEQUAL:
            return '<='
        elif self.tipo == OpRelacional.EQUALSEQUALS:
            return '=='
        elif self.tipo == OpRelacional.DISTINT:
            return '!='