from Abstracto.Instruccion import *
from Abstracto.Return import *
from Export import Salida

class Declaracion(Instruccion):

    def __init__(self, id, val, tipo, tipoDeclaracion , linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.val = val
        self.tipo = tipo
        self.tipoDeclaracion = tipoDeclaracion
    
    def exec(self, ambito):
        if self.val == None and self.tipoDeclaracion == TipoDeclaracion.GLOBAL:
            ambito.guardarVarGlobal(self.id, None, None)
            return
        valor = self.val.exec(ambito)
        if valor.tipo == Tipo.STRUCT:
            #Validamos si tiene tipo
            if self.tipo == None: 
                ambito.guardarVarStruct(self.id, valor.val, valor.auxTipo, self.linea, self.columna)
            else:
                if isinstance(self.tipo, str):
                    if valor.auxTipo == self.tipo:
                        ambito.guardarVarStruct(self.id, valor.val, valor.auxTipo, self.linea, self.columna)
                    else:
                        Salida.salida += "Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.auxTipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                        Salida.errores.append(Error("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.auxTipo) + "' y  no de tipo '" + str(self.tipo) + "'", self.linea, self.columna))
                        print("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.auxTipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                else:
                    print("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                    Salida.salida += "Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                    Salida.errores.append(Error("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "'", self.linea, self.columna))
        else:
            if self.tipoDeclaracion == TipoDeclaracion.DEFAULT:
                if self.tipo == None:
                    ambito.guardarVar(self.id, valor.val, valor.tipo, self.linea, self.columna)
                else:
                    if isinstance(self.tipo, str):
                        print("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                        Salida.salida += "Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                        Salida.errores.append(Error("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "'", self.linea, self.columna))
                    elif self.tipo == valor.tipo:
                        ambito.guardarVar(self.id, valor.val, valor.tipo, self.linea, self.columna)
                    else:
                        print("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                        Salida.salida += "Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                        Salida.errores.append(Error("Error Semantico: la variable '" + self.id + "' es de tipo '" + str(valor.tipo) + "' y  no de tipo '" + str(self.tipo) + "'", self.linea, self.columna))
            elif self.tipoDeclaracion == TipoDeclaracion.LOCAL:
                ambito.guardarVarLocal(self.id, valor.val, valor.tipo, self.linea, self.columna)
            else:
                ambito.guardarVarGlobal(self.id, valor.val, valor.tipo, self.linea, self.columna)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="ASIGNACION/DECLARACION"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        if self.tipoDeclaracion == TipoDeclaracion.LOCAL:
            nombreLocal = "Nodo" + str(Salida.num)
            Salida.graph += nombreLocal + '[label="LOCAL"];\n'
            Salida.graph += nombreLit + '->' + nombreLocal + ';\n'
            Salida.num += 1
        elif self.tipoDeclaracion == TipoDeclaracion.GLOBAL:
            nombreGlobal = "Nodo" + str(Salida.num)
            Salida.graph += nombreGlobal + '[label="GLOBAL"];\n'
            Salida.graph += nombreLit + '->' + nombreGlobal + ';\n'
            Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        nombreigual = "Nodo" + str(Salida.num)
        Salida.graph += nombreigual + '[label="="];\n'
        Salida.graph += nombreLit + '->' + nombreigual + ';\n'
        Salida.num += 1
        if self.val != None:
            self.val.graph(nombreLit)
        if self.tipo != None:
            nombreTipo = "Nodo" + str(Salida.num)
            Salida.graph += nombreTipo + '[label=":' + str(self.tipo) + '"];\n'
            Salida.graph += nombreLit + '->' + nombreTipo + ';\n'
            Salida.num += 1