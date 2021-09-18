from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class While(Instruccion):

    def __init__(self, condicion, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
    
    def exec(self, ambito):
        cond = self.condicion.exec(ambito)
        if cond.tipo != Tipo.BOOLEAN:
            print("Error Semantico: la condicion del while no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: la condicion del while no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: la condicion del while no es de tipo BOOL", self.linea, self.columna))
            return
        nuevoAmbito = Ambito(ambito, "For")
        while cond.val:
            item = self.instrucciones.exec(nuevoAmbito)
            if item != None:
                if item.tipo == Tipo.BREAKST:
                    break
                elif item.tipo == Tipo.CONTINUEST:
                    continue
                else:
                    return item
            cond = self.condicion.exec(nuevoAmbito)
            if cond.tipo != Tipo.BOOLEAN:
                print("Error Semantico: la condicion del while no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna))
                Salida.salida += "Error Semantico: la condicion del while no es de tipo BOOL, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                Salida.errores.append(Error("Error Semantico: la condicion del while no es de tipo BOOL", self.linea, self.columna))
                return

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="WHILE"];\n'
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