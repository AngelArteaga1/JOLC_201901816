from Abstracto.Expresion import *
from Abstracto.Return import *
from Export import Salida
from Simbolo.Generador import Generador

class Acceso(Expresion):

    def __init__(self, id, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id

    def exec(self, ambito):
        valor = ambito.getVar(self.id)
        if valor == None:
            print("Error Semantico: la variable '" + str(self.id) + "' no existe, linea: " + str(self.linea) + " columna: " + str(self.columna))
            Salida.salida += "Error Semantico: la variable '" + str(self.id) + "' no existe, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
            Salida.errores.append(Error("Error Semantico: la variable '" + str(self.id) + "' no existe", self.linea, self.columna))
            return Return("Nothing", Tipo.NOTHING)
        elif valor.tipo == Tipo.STRUCT:
            return Return(valor.atributos, valor.tipo, valor.objeto)
        return Return(valor.val, valor.tipo)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="' + str(self.id) + '"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1

    def compile(self, environment):
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("Compilacion de Acceso")
        
        var = environment.getVar(self.id)
        if(var == None):
            print("Error, no existe la variable")
            return ReturnCompilador(None, Tipo.NOTHING, False)

        # Temporal para guardar variable
        temp = generador.addTemp()

        # Obtencion de posicion de la variable
        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generador.addTemp()
            generador.addExp(tempPos, 'P', var.pos, "+")
        generador.getStack(temp, tempPos)

        if var.tipo != Tipo.BOOLEAN:
            generador.addComment("Fin compilacion acceso")
            generador.addSpace()
            return Return(temp, var.tipo, True)
        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()
        
        generador.addIf(temp, '1', '==', self.trueLbl)
        generador.addGoto(self.falseLbl)

        generador.addComment("Fin compilacion acceso")
        generador.addSpace()

        ret = Return(None, Tipo.BOOLEAN, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret