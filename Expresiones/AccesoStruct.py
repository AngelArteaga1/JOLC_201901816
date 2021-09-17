from Abstracto.Expresion import *
from Export import Salida

class AccesoStruct(Expresion):

    def __init__(self, id, atributo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.atributo = atributo
    
    def exec(self, ambito):
        var = self.id.exec(ambito)
        #Verificamos si el valor es de tipo struct
        if var.tipo != Tipo.STRUCT:
            print("Error Semantico: el valor no es de tipo struct, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el valor no es de tipo struct, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el valor no es de tipo struct", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        #Verificamos si existe el parametro
        if self.atributo in var.val:
            #Esto ya trae un Return
            return var.val[self.atributo]
        else:
            print("Error Semantico: no existe el atributo '" + str(self.atributo) + "' del struct '" + str(var.auxTipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: no existe el atributo '" + str(self.atributo) + "' del struct '" + str(var.auxTipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: no existe el atributo '" + str(self.atributo) + "' del struct '" + str(var.auxTipo) + "'", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="ACCESO_STRUCT"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.id.graph(nombreLit)
        nombreAtr = "Nodo" + str(Salida.num)
        Salida.graph += nombreAtr + '[label=".' + str(self.atributo) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreAtr + ';\n'
        Salida.num += 1