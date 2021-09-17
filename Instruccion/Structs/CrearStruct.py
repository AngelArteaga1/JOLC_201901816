from Abstracto.Instruccion import *

class CrearStruct(Instruccion):

    def __init__(self, id, atributo, esInmutable, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.atributo = atributo
        self.esInmutable = esInmutable
    
    def exec(self, ambito):
        atributos = []
        tipoAtributos = []
        for att in self.atributo:
            atributos.append(att.id)
            tipoAtributos.append(att.tipo)
        ambito.guardarStruct(self.id, atributos, tipoAtributos, self.esInmutable, self.linea, self.columna)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="DEC_STRUCT"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreId = "Nodo" + str(Salida.num)
        Salida.graph += nombreId + '[label="' + str(self.id) + '"];\n'
        Salida.graph += nombreLit + '->' + nombreId + ';\n'
        Salida.num += 1
        if not self.esInmutable:
            nombreMut = "Nodo" + str(Salida.num)
            Salida.graph += nombreMut + '[label="MUTABLE"];\n'
            Salida.graph += nombreLit + '->' + nombreMut + ';\n'
            Salida.num += 1
        if len(self.atributo) > 0:
            nombreParams = "Nodo" + str(Salida.num)
            Salida.graph += nombreParams + '[label="LISTA_ATRIBUTOS"];\n'
            Salida.graph += nombreLit + '->' + nombreParams + ';\n'
            Salida.num += 1
            for param in self.atributo:
                param.graph(nombreParams)