from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class For(Instruccion):

    def __init__(self, id, expresion, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.expresion = expresion
        self.instrucciones = instrucciones
    
    def exec(self, ambito):
        valor = self.expresion.exec(ambito)
        nuevoAmbito = Ambito(ambito, "For")
        if valor.tipo == Tipo.RANGE:
            rango = range(valor.val.minimo.val, valor.val.maximo.val+1)
            for i in rango:
                nuevoAmbito.guardarVar(self.id, i, Tipo.INT, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        elif valor.tipo == Tipo.ARRAY:
            for i in valor.val:
                nuevoAmbito.guardarVar(self.id, i.val, i.tipo, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        elif valor.tipo == Tipo.STRING:
            for i in valor.val:
                nuevoAmbito.guardarVar(self.id, i, Tipo.STRING, self.linea, self.columna)
                item = self.instrucciones.exec(nuevoAmbito)
                if item != None:
                    if item.tipo == Tipo.BREAKST:
                        break
                    elif item.tipo == Tipo.CONTINUEST:
                        continue
                    else:
                        return item
        else:
            print("Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo) + ", linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo) + ", linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor del for no es iterable porque es de tipo " + str(valor.tipo), self.linea, self.columna))
            return

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="FOR"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        self.expresion.graph(nombreLit)
        nombreInstr = "Nodo" + str(Salida.num)
        Salida.graph += nombreInstr + '[label="INSTRUCCIONES"];\n'
        Salida.graph += nombreLit + '->' + nombreInstr + ';\n'
        Salida.num += 1
        self.instrucciones.graph(nombreInstr)