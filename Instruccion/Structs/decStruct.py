from Abstracto.Instruccion import *
from Export import Salida

class decStruct(Instruccion):

    def __init__(self, id, tipo, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.tipo = tipo
    
    def exec(self, ambito):
        struct = ambito.getStruct(self.tipo)
        if struct == None:
            print("""Error Semantico: el struct '""" + self.id + """' no existe, 
            linea: """ + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += """Error Semantico: el struct '""" + self.id + """' no existe, 
            linea: """ + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: el struct '" + self.id + "' no existe", self.linea, self.columna))
            return
        atributos = {}
        for att in struct:
            atributos.update({
                att: 0
            })
        ambito.guardarVarStruct(self.id, atributos, self.tipo, self.linea, self.columna)

    def graph(self, padre):
        return ""

    def compile(self, ambito):
        print("hola")