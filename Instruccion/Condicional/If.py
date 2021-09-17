from Abstracto.Instruccion import *
from Abstracto.Return import Tipo
from Export import Salida

class If(Instruccion):

    def __init__(self, condicion, instrucciones, linea, columna, elseSt = None):
        Instruccion.__init__(self, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.elseSt = elseSt
    
    def exec(self, ambito):
        cond = self.condicion.exec(ambito)
        if cond.tipo != Tipo.BOOLEAN:
            print("Error Semantico: la condicion del if no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: la condicion del if no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: la condicion del if no es de tipo BOOL", self.linea, self.columna))
            return
        if cond.val:
            return self.instrucciones.exec(ambito)
        elif self.elseSt != None:
            return self.elseSt.exec(ambito)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="IF"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreCond = "Nodo" + str(Salida.num)
        Salida.graph += nombreCond + '[label="CONDICION"];\n'
        Salida.graph += nombreLit + '->' + nombreCond + ';\n'
        Salida.num += 1
        self.condicion.graph(nombreCond)
        nombreInstr = "Nodo" + str(Salida.num)
        Salida.graph += nombreInstr + '[label="INSTRUCCIONES"];\n'
        Salida.graph += nombreLit + '->' + nombreInstr + ';\n'
        Salida.num += 1
        self.instrucciones.graph(nombreInstr)
        if self.elseSt != None:
            nombreElse = "Nodo" + str(Salida.num)
            Salida.graph += nombreElse + '[label="ELSE"];\n'
            Salida.graph += nombreLit + '->' + nombreElse + ';\n'
            Salida.num += 1
            self.elseSt.graph(nombreElse)