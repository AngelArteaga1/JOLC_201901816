from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida
from Simbolo.Generador import Generador

class ReturnST(Expresion):

    def __init__(self, expresion, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expresion = expresion
    
    def exec(self, ambito):
        try:
            value = self.expresion.exec(ambito)
            return Return(value, Tipo.RETURNST)
        except:
            print("Error en Return")
            Salida.salida += "Error en Return, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error en Return", self.linea, self.columna))

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="RETURN"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.expresion.graph(nombreLit)

    def compile(self, ambito):
        genAux = Generador()
        generador = genAux.getInstance()
        if(ambito.returnLbl == ''):
            print("Return fuera de funcion")
            generador.addError("Error Semantico: return fuera de funcion, linea: " + str(self.linea) + " columna: " + str(self.columna))
            return

        value = self.expresion.compile(ambito)
        if(value.tipo == Tipo.NOTHING):
            generador.setStack('P', '0')
            generador.addGoto(ambito.returnLbl)
            return
        if(value.tipo == Tipo.BOOLEAN):
            tempLbl = generador.newLabel()
            
            generador.putLabel(value.trueLbl)
            generador.setStack('P', '1')
            generador.addGoto(tempLbl)

            generador.putLabel(value.falseLbl)
            generador.setStack('P', '0')

            generador.putLabel(tempLbl)
        else:
            generador.setStack('P', value.val)
        generador.addGoto(ambito.returnLbl)