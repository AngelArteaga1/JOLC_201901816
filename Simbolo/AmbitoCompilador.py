from Simbolo.Simbolo import *
from Export import Salida
from Simbolo.SimboloCompilador import SimboloCompilador

class AmbitoCompilador:
    
    def __init__(self, prev, name=''):
        self.prev = prev
        self.name = name
        # NUEVO
        self.size = 0
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        self.funcion = False
        if(prev != None):
            self.size = self.prev.size
            self.breakLbl = self.prev.breakLbl
            self.continueLbl = self.prev.continueLbl
            self.returnLbl = self.prev.returnLbl

        self.variables = {}
        self.functions = {}
        self.structs = {}
        self.referencias = {}

    def saveVar(self, idVar, symType, inHeap, structType = "", auxTipo = None):
        env = self
        esReferencia = self.getReferencia(idVar)
        newSymbol = SimboloCompilador(idVar, symType, self.size, self.prev == None, inHeap, structType, auxTipo)
        if esReferencia:
            ambitoGlobal = self.getGlobal()
            newSymbol.isGlobal = True
            ambitoGlobal.variables[idVar] = newSymbol
        if self.insideFunction():
            while env.funcion != True:
                if idVar in env.variables.keys():
                    newSymbol = env.variables[idVar]
                    newSymbol.tipo = symType
                    newSymbol.inHeap = inHeap
                    newSymbol.structType = structType
                    newSymbol.auxTipo = auxTipo
                    return env.variables[idVar]
                env = env.prev
            if idVar in env.variables.keys():
                newSymbol = env.variables[idVar]
                newSymbol.tipo = symType
                newSymbol.inHeap = inHeap
                newSymbol.structType = structType
                newSymbol.auxTipo = auxTipo
                env.variables[idVar] = newSymbol
            else:
                newSymbol.isGlobal = self.prev == None
                self.variables[idVar] = newSymbol
                self.size += 1
        else:
            while env != None:
                if idVar in env.variables.keys():
                    newSymbol = env.variables[idVar]
                    newSymbol.tipo = symType
                    newSymbol.inHeap = inHeap
                    newSymbol.structType = structType
                    newSymbol.auxTipo = auxTipo
                    return env.variables[idVar]
                env = env.prev
            newSymbol.isGlobal = self.prev == None
            self.variables[idVar] = newSymbol
            self.size += 1
            return self.variables[idVar]

    def saveLocalVar(self, idVar, symType, inHeap, structType = "", auxTipo = None):
        newSymbol = SimboloCompilador(idVar, symType, self.size, self.prev == None, inHeap, structType,auxTipo)
        if not idVar in self.variables.keys():
            newSymbol = self.variables[idVar]
            newSymbol.tipo = symType
            newSymbol.inHeap = inHeap
            newSymbol.structType = structType
            newSymbol.auxTipo = auxTipo
            return self.variables[idVar]
        else:
            self.size += 1
            self.variables[idVar] = newSymbol
            return self.variables[idVar]

    def saveGlobalVar(self, idVar, symType, inHeap, structType = "", auxTipo = None):
        self.referencias[idVar] = None
        envGlobal = self.getGlobal()
        newSymbol = SimboloCompilador(idVar, symType, envGlobal.size, envGlobal.prev == None, inHeap, structType, auxTipo)
        if idVar in envGlobal.variables.keys():
            newSymbol = envGlobal.variables[idVar]
            newSymbol.tipo = symType
            newSymbol.inHeap = inHeap
            newSymbol.structType = structType
            newSymbol.auxTipo = auxTipo
            return envGlobal.variables[idVar]
        else:
            envGlobal.size += 1
            envGlobal.variables[idVar] = newSymbol
            return envGlobal.variables[idVar]


    def saveFunc(self, idFunc, function):
        if idFunc in self.functions.keys():
            print("Función repetida")
        else:
            self.functions[idFunc] = function
    
    def saveStruct(self, idStruct, attr):
        if idStruct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[idStruct] = attr

    def getVar(self, idVar):
        env = self
        while env != None:
            if idVar in env.variables.keys():
                return env.variables[idVar]
            env = env.prev
        return None
    
    def getFunc(self, idFunc):
        env = self
        while env != None:
            if idFunc in env.functions.keys():
                return env.functions[idFunc]
            env = env.prev
        return None
        
    def getStruct(self, idStruct):
        env = self
        while env != None:
            if idStruct in env.structs.keys():
                return env.structs[idStruct]
            end = end.prev
        return None

    def getReferencia(self, id):
        env = self
        while env != None:
            if id in env.referencias.keys():
                return True
            env = env.prev
        return False

    def insideFunction(self):
        env = self
        while env != None:
            if env.funcion:
                return True
            env = env.prev
        return False

    def getGlobal(self):
        env = self
        while env.prev != None:
            env = env.prev
        return env