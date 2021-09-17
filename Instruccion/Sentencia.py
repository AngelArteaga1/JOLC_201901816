from Expresiones.Nativas import trunc
from Abstracto.Instruccion import *
from Abstracto.Return import *
from Simbolo.Ambito import *

class Sentencia(Instruccion):

    def __init__(self, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.instrucciones = instrucciones
        self.funcion = False
    
    def exec(self, ambito):
        if self.funcion:
            ambito.funcion = True
        for instruccion in self.instrucciones:
            ret = instruccion.exec(ambito)
            if ret != None:
                if ret.tipo == Tipo.RETURNST:
                    return ret
                elif ret.tipo == Tipo.CONTINUEST and self.funcion == False:
                    return ret
                elif ret.tipo == Tipo.BREAKST and self.funcion == False:
                    return ret
            elif instruccion == self.instrucciones[-1] and self.funcion:
                return Return(None, Tipo.NOTHING)

    def graph(self, padre):
        for instr in self.instrucciones:
            instr.graph(padre)