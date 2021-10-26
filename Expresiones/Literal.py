from Abstracto.Expresion import *
from Abstracto.Return import *
from Simbolo.Generador import Generador 
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

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        if(self.tipo == Tipo.INT or self.tipo == Tipo.FLOAT):
            return ReturnCompilador(str(self.val), self.tipo, False)
        elif self.tipo == Tipo.CHAR:
            return ReturnCompilador(str(ord(self.val[0])), self.tipo, False)
        elif self.tipo == Tipo.BOOLEAN:
            if self.trueLbl == '':
                self.trueLbl = generador.newLabel()
            if self.falseLbl == '':
                self.falseLbl = generador.newLabel()
            
            if(self.val):
                generador.addGoto(self.trueLbl)
                generador.addComment("GOTO PARA EVITAR ERROR DE GO")
                generador.addGoto(self.falseLbl)
            else:
                generador.addGoto(self.falseLbl)
                generador.addComment("GOTO PARA EVITAR ERROR DE GO")
                generador.addGoto(self.trueLbl)
            
            ret = ReturnCompilador(self.val, self.tipo, False)
            ret.trueLbl = self.trueLbl
            ret.falseLbl = self.falseLbl

            return ret
        elif self.tipo == Tipo.STRING:
            retTemp = generador.addTemp()
            generador.addExp(retTemp, 'H', '', '')

            for char in str(self.val):
                generador.setHeap('H', ord(char))   # heap[H] = NUM;
                generador.nextHeap()                # H = H + 1;

            generador.setHeap('H', '-1')            # FIN DE CADENA
            generador.nextHeap()

            return ReturnCompilador(retTemp, Tipo.STRING, True)
        elif self.tipo == Tipo.NOTHING:
            return ReturnCompilador('', Tipo.NOTHING, False)
        else:
            print('Por hacer')