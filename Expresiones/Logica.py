from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida
from Simbolo.Generador import Generador

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

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("INICIO EXPRESION LOGICA")

        self.checkLabels()
        lblAndOr = ''

        if self.tipo == OpLogica.AND:
            lblAndOr = self.left.trueLbl = generador.newLabel()
            self.right.trueLbl = self.trueLbl
            self.left.falseLbl = self.right.falseLbl = self.falseLbl
        elif self.tipo == OpLogica.OR:
            self.left.trueLbl = self.right.trueLbl = self.trueLbl
            lblAndOr = self.left.falseLbl = generador.newLabel()
            self.right.falseLbl = self.falseLbl
        else:
            self.left.falseLbl = self.trueLbl
            self.left.trueLbl = self.falseLbl

        left = self.left.compile(ambito)
        if self.tipo != OpLogica.NOT:
            if left.tipo != Tipo.BOOLEAN:
                print("No se puede utilizar en expresion booleana")
                return
            generador.putLabel(lblAndOr)

            right = self.right.compile(ambito)
            if right.tipo != Tipo.BOOLEAN:
                print("No se puede utilizar en expresion booleana")
                return
        generador.addComment("FINALIZO EXPRESION LOGICA")
        generador.addSpace()
        ret = ReturnCompilador(None, Tipo.BOOLEAN, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret
    
    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()