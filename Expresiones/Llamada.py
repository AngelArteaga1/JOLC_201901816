from Instruccion.Funciones.Parametro import Parametro
from Abstracto.Expresion import *
from Simbolo.Ambito import *
from Expresiones.Nativas import *
from Export import Salida

class Llamada(Expresion):

    def __init__(self, id, parametros, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.id = id
        self.parametros = parametros
    
    def exec(self, ambito):
        funcion = ambito.getFunc(self.id)
        if funcion != None:
            nuevoAmbito = Ambito(ambito.getGlobal(), self.id)
            nuevoAmbito.funcion = True
            for i in range(len(self.parametros)):
                parametro = self.parametros[i].exec(ambito)
                #Verificamos si es el mismo len de los parametros
                if len(funcion.parametros) != len(self.parametros):
                    print("Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(self.linea) + " columna: " + str(self.columna))
                    Salida.salida += "Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos, linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                    Salida.errores.append(Error("Error Semantico: la llamada a la funcion '" + str(self.id) + "' no tiene la cantidad de parametros correctos", self.linea, self.columna))
                    return Return("Nothing", Tipo.NOTHING)
                #Ahora verificamos si los parametros son como sus tipos
                if funcion.parametros[i].tipo != None:
                    if parametro.tipo == Tipo.STRUCT:
                        if funcion.parametros[i].tipo != parametro.auxTipo:
                            print("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "'", self.linea, self.columna))
                            return Return("Nothing", Tipo.NOTHING)
                    else:
                        if funcion.parametros[i].tipo != parametro.tipo:
                            print("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el parametro no es de tipo '" + str(funcion.parametros[i].tipo) + "'", self.linea, self.columna))
                            return Return("Nothing", Tipo.NOTHING)
                #verificamos si es una struct
                if parametro.tipo == Tipo.STRUCT:
                    nuevoAmbito.guardarVarStruct(funcion.parametros[i].id, parametro.val, parametro.auxTipo, self.linea, self.columna)
                else:
                    nuevoAmbito.guardarVar(funcion.parametros[i].id, parametro.val, parametro.tipo, self.linea, self.columna)
            funcion.instrucciones.funcion = True
            returnST = funcion.instrucciones.exec(nuevoAmbito)
            if returnST != None:
                if returnST.tipo == Tipo.RETURNST:
                    return returnST.val
                else:
                    return returnST
        elif self.id == "log10":
            return log10(self, ambito)
        elif self.id == "log":
            return log(self, ambito)
        elif self.id == "sin":
            return sin(self, ambito)
        elif self.id == "cos":
            return cos(self, ambito)
        elif self.id == "tan":
            return tan(self, ambito)
        elif self.id == "sqrt":
            return sqrt(self, ambito)
        elif self.id == "parse":
            return parse(self, ambito)
        elif self.id == "trunc":
            return trunc(self, ambito)
        elif self.id == "float":
            return Float(self, ambito)
        elif self.id == "string":
            return string(self, ambito)
        elif self.id == "typeof":
            return typeof(self, ambito)
        elif self.id == "push!":
            return push(self, ambito)
        elif self.id == "pop!":
            return Pop(self, ambito)
        elif self.id == "length":
            return length(self, ambito)
        elif self.id == "uppercase":
            return uppercase(self, ambito)
        elif self.id == "lowercase":
            return lowercase(self, ambito)
        #Ahora verificamos si es una struct
        struct = ambito.getStruct(self.id)
        tipoStruct = ambito.getTipoStruct(self.id)
        if struct != None:
            atributos = {}
            for i in range(len(self.parametros)):
                valor = self.parametros[i].exec(ambito)
                if tipoStruct[i] != None:
                    if valor.tipo == Tipo.STRUCT:
                        if tipoStruct[i] == valor.auxTipo:
                            atributos.update({
                                struct[i] : Return(valor.val, valor.tipo, valor.auxTipo)
                            })
                        else:
                            print("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
                            Salida.errores.append(Error("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "'", self.linea, self.columna))
                            atributos.update({
                                struct[i] : Return("Nothing", Tipo.NOTHING)
                            })
                    else:
                        if tipoStruct[i] == valor.tipo:
                            atributos.update({
                                struct[i] : Return(valor.val, valor.tipo, self.id)
                            })
                        else:
                            print("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
                            Salida.salida += "Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n" 
                            Salida.errores.append(Error("Error Semantico: el atributo " + str(i+1) + " de '" + str(self.id) + "' es de tipo '" + str(valor.tipo) + "' y no de tipo '" + str(tipoStruct[i]) + "'", self.linea, self.columna))
                            atributos.update({
                                struct[i] : Return("Nothing", Tipo.NOTHING)
                            })
                else:
                    atributos.update({
                        struct[i] : Return(valor.val, valor.tipo, self.id)
                    })
            return Return(atributos, Tipo.STRUCT, self.id)
        print("Error Semantico: no existe la funcion o el struct '" + str(self.id) + "', linea: " + str(self.linea) + " columna: " + str(self.columna))
        Salida.salida += "Error Semantico: no existe la funcion o el struct '" + str(self.id) + "', linea: " + str(self.linea) + " columna: " + str(self.columna) + "\n"
        Salida.errores.append(Error("Error Semantico: no existe la funcion o el struct '" + str(self.id) + "'", self.linea, self.columna))
        return Return("Nothing", Tipo.NOTHING)

    def graph(self, padre):
        nombreLit = "Nodo" + str(Salida.num)
        Salida.graph += nombreLit + '[label="LLAMADA/STRUCT"];\n'
        Salida.graph += padre + '->' + nombreLit + ';\n'
        Salida.num += 1
        nombreFuncion = "Nodo" + str(Salida.num)
        Salida.graph += nombreFuncion + '[label="' + self.id + '"];\n'
        Salida.graph += nombreLit + '->' + nombreFuncion + ';\n'
        Salida.num += 1
        if len(self.parametros) > 0:
            nombreLista = "Nodo" + str(Salida.num)
            Salida.graph += nombreLista + '[label="LISTA_PARAMETROS"];\n'
            Salida.graph += nombreLit + '->' + nombreLista + ';\n'
            Salida.num += 1
            for param in self.parametros:
                if isinstance(param, Tipo):
                    nombreTipo = "Nodo" + str(Salida.num)
                    Salida.graph += nombreTipo + '[label="' + str(param) + '"];\n'
                    Salida.graph += nombreLista + '->' + nombreTipo + ';\n'
                    Salida.num += 1
                else:
                    param.graph(nombreLista)