from Simbolo.Simbolo import *
from Export import Salida

class Ambito:
    
    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = {}
        self.referencias = {}
        self.funciones = {}
        self.structs = {}
        self.tipoStructs = {}
        self.mutableStruct = {}
        self.funcion = False
    
    def guardarVar(self, id, val, tipoVar):
        env = self
        nuevoSimbolo = Simbolo(val, id, tipoVar)
        esReferencia = self.getReferencia(id)
        if esReferencia:
            ambitoGlobal = self.getGlobal()
            ambitoGlobal.variables[id] = nuevoSimbolo
        if self.insideFunction():
            while env.funcion != True:
                if id in env.variables.keys():
                    env.variables[id] = nuevoSimbolo
                    return
                env = env.anterior
            if id in env.variables.keys():
                env.variables[id] = nuevoSimbolo
            else:
                self.variables[id] = nuevoSimbolo
        else:
            while env != None:
                if id in env.variables.keys():
                    env.variables[id] = nuevoSimbolo
                    return
                env = env.anterior
            self.variables[id] = nuevoSimbolo

    def guardarVarLocal(self, id, val, tipoVar):
        nuevoSimbolo = Simbolo(val, id, tipoVar)
        self.variables[id] = nuevoSimbolo

    def guardarVarGlobal(self, id, val, tipoVar):
        self.referencias[id] = None
        if val == None: return
        envGlobal = self.getGlobal()
        nuevoSimbolo = Simbolo(val, id, tipoVar)
        envGlobal.variables[id] = nuevoSimbolo

    def guardarFunc(self, id, funcion, linea, columna):
        if id in self.funciones.keys():
            print("Error Semantico: la funcion '" + id + "' ya existe, linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: la funcion '" + id + "' ya existe, linea: " + str(linea) + " columna: " + str(columna) + "\n"
        else:
            self.funciones[id] = funcion

    def guardarVarStruct(self, id, atributo, tipo):
        env = self
        nuevoSimbolo = Simbolo(None, id, Tipo.STRUCT, tipo)
        nuevoSimbolo.atributos = atributo
        while env != None:
            if id in env.variables.keys():
                env.variables[id] = nuevoSimbolo
                return
            env = env.anterior
        self.variables[id] = nuevoSimbolo

    def guardarStruct(self, id, atributo, tipoAtributo, esInmutable, linea, columna):
        if id in self.structs.keys():
            print("Error Semantico: el struct '" + id + "' ya existe, linea: " + str(linea) + " columna: " + str(columna))
            Salida.salida += "Error Semantico: el struct '" + id + "' ya existe, linea: " + str(linea) + " columna: " + str(columna) + "\n"
        else:
            self.structs[id] = atributo
            self.tipoStructs[id] = tipoAtributo
            self.mutableStruct[id] = esInmutable

    def getVar(self, idVar):
        env = self
        while env != None:
            if idVar in env.variables.keys():
                return env.variables[idVar]
            env = env.anterior
        return None

    def getFunc(self, id):
        env = self
        while env != None:
            if id in env.funciones.keys():
                return env.funciones[id]
            env = env.anterior
        return None

    def getStruct(self, id):
        env = self
        while env != None:
            if id in env.structs.keys():
                return env.structs[id]
            env = env.anterior
        return None

    def getTipoStruct(self, id):
        env = self
        while env != None:
            if id in env.tipoStructs.keys():
                return env.tipoStructs[id]
            env = env.anterior
        return None

    def getMutableStruct(self, id):
        env = self
        while env != None:
            if id in env.mutableStruct.keys():
                return env.mutableStruct[id]
            env = env.anterior
        return None

    def getReferencia(self, id):
        env = self
        while env != None:
            if id in env.referencias.keys():
                return True
            env = env.anterior
        return False

    def insideFunction(self):
        env = self
        while env != None:
            if env.funcion:
                return True
            env = env.anterior
        return False

    def getGlobal(self):
        env = self
        while env.anterior != None:
            env = env.anterior
        return env