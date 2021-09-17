from Abstracto.Instruccion import *
from Export import Salida

class AccesoAsignacion(Instruccion):

    def __init__(self, acceso, expresion, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.acceso = acceso
        self.expresion = expresion

    def exec(self, ambito):
        ente = self.acceso.exec(ambito)
        valor = self.expresion.exec(ambito)
        #Verificamos si el ente es de tipo struct
        if self.acceso.id.exec(ambito).tipo == Tipo.NOTHING:
            return
        #Verificamos si el struct es mutable o no
        nombreStruct = ente.auxTipo
        inmutable = ambito.getMutableStruct(nombreStruct)
        if inmutable:
            print("Error Semantico: el struct '" + nombreStruct+ "' no es mutable, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: el struct '" + nombreStruct+ "' no es mutable, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            return
        #Verificamos si el valor del parametro tiene el tipo correcto
        atributos = ambito.getStruct(nombreStruct)
        tipoAtributos = ambito.getTipoStruct(nombreStruct)
        for i in range(len(atributos)):
            if atributos[i] == self.acceso.atributo:
                if tipoAtributos[i] != None and valor.tipo != tipoAtributos[i]:
                    print("Error Semantico: el atributo '" + self.acceso.atributo + "' no es de tipo '" + str(tipoAtributos[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                    Salida.salida += "Error Semantico: el atributo '" + self.acceso.atributo + "' no es de tipo '" + str(tipoAtributos[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                    return
        ente.auxTipo = valor.auxTipo
        ente.tipo = valor.tipo
        ente.val = valor.val

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="ASIGNACION_STRUCT"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        self.acceso.graph(nombreLit)
        nombreigual = "Nodo" + str(Salida.num)
        Salida.graph += nombreigual + '[label="="];\n'
        Salida.graph += nombreLit + '->' + nombreigual + ';\n'
        Salida.num += 1
        self.expresion.graph(nombreLit)